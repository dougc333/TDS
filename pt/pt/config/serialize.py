#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
import sys
from enum import Enum
from typing import Dict, List, Tuple, Union

from .component import Registry
from .config_adapter import upgrade_to_latest
from .pytext_config import PyTextConfig


class ConfigParseError(Exception):
    pass


class UnionTypeError(ConfigParseError):
    pass


class EnumTypeError(ConfigParseError):
    pass


class MissingValueError(ConfigParseError):
    pass


class IncorrectTypeError(Exception):
    pass


def _canonical_typename(cls):
    print("cls:", cls)
    sys.exit(1)
    if cls.__name__.endswith(".Config"):
        return cls.__name__[: -len(".Config")]
    return cls.__name__


def _extend_tuple_type(cls, value):
    sub_cls_list = list(cls.__args__)
    if len(sub_cls_list) != len(value):
        if len(sub_cls_list) != 2 or sub_cls_list[1] is not Ellipsis:
            raise ConfigParseError(
                f"{len(value)} values found which is more than number of types in tuple {cls}"
            )
        del sub_cls_list[1]
        sub_cls_list.extend(
            (cls.__args__[0],) * (len(value) - len(sub_cls_list)))
    return sub_cls_list


def _union_from_json(subclasses, json_obj):
    print("union_from_json")
    if type(json_obj) is not dict:
        raise IncorrectTypeError(
            f"incorrect Union value {json_obj} for union {subclasses}"
        )
    type_name = list(json_obj)[0]
    print("union_from_json type_name:", type_name)
    for subclass in subclasses:
        print("union_from_json processing subclass:", subclass)
        if type(None) != subclass and (
            type_name.lower() == _canonical_typename(subclass).lower()
        ):
            return _value_from_json(subclass, json_obj[type_name])
    raise UnionTypeError(
        f"no suitable type found for {type_name} in union {subclasses}"
    )


def _is_optional(cls):
    return _get_class_type(cls) == Union and type(None) in cls.__args__


def _enum_from_json(enum_cls, json_obj):
    for e in enum_cls:
        if e.value == json_obj:
            return e
    raise EnumTypeError(f"invalid enum value {json_obj} for {enum_cls}")


def _value_from_json(cls, value):
    print("_value_from_json:", value)
    print("_value_from_json cls:", cls)
    cls_type = _get_class_type(cls)
    print("_value_from_json cls_type:", cls_type)
    print("type cls_type:", type(cls_type))
    if value is None:
        return value
    # Unions must be first because Union explicitly doesn't
    # support __subclasscheck__.
    # optional with more than 2 classes is treated as Union
    elif _is_optional(cls) and len(cls.__args__) == 2:
        sub_cls = cls.__args__[0] if type(None) != cls.__args__[
            0] else cls.__args__[1]
        return _value_from_json(sub_cls, value)
    # nested config
    elif hasattr(cls, "_fields"):
        print("from json has _fields")
        return config_from_json(cls, value)
    elif cls_type == Union:
        print("cls_type is union")
        #print("union shit:", _union_from_json(cls.__args__, value))
        return _union_from_json(cls.__args__, value)
    elif issubclass(cls_type, Enum):
        print("is subclass")
        return _enum_from_json(cls, value)
    elif issubclass(cls_type, List):
        print("is subclass")
        sub_cls = cls.__args__[0]
        return [_value_from_json(sub_cls, v) for v in value]
    elif issubclass(cls_type, Tuple):
        print("tuple bullshit")
        return tuple(
            _value_from_json(c, v)
            for c, v in zip(_extend_tuple_type(cls, value), value)
        )
    elif issubclass(cls_type, Dict):
        print("more subclass shit")
        sub_cls = cls.__args__[1]
        return {key: _value_from_json(sub_cls, v) for key, v in value.items()}
    # built in types
    print("value from json cls(value):", cls(value))
    return cls(value)


def _try_component_config_from_json(cls, value):
    if type(value) is dict and len(value) == 1:
        options = Registry.subconfigs(cls)
        type_name = list(value)[0]
        for option in options:
            if type_name.lower() == _canonical_typename(option).lower():
                return _value_from_json(option, value[type_name])
    return None


def pytext_config_from_json(json_obj, ignore_fields=(), auto_upgrade=True):
    print("pytext_config_from_json in serialize.py")
    if auto_upgrade:
        print("auto_upgrade in pytext_config_from_json")
        json_obj = upgrade_to_latest(json_obj)
        print("json_obj in autoupgrade:", json_obj)
    print("pytext_config_from_json calling config_from_json")
    foo = config_from_json(PyTextConfig, json_obj, ignore_fields)
    print("type foo:", type(foo))
    print("foo:", foo)
    return foo


def config_from_json(cls, json_obj, ignore_fields=()):
    print("serialize.py config_from_json")
    print("cls:", cls)
    print("are u safe? cls_annotations:", cls.__annotations__.items())
    print("json_obj:", json_obj)
    print("222222222222")
    if getattr(cls, "__EXPANSIBLE__", False):
        print("getattr false")
        component_config = _try_component_config_from_json(cls, json_obj)
        if component_config:
            return component_config
    parsed_dict = {}
    if not hasattr(cls, "_fields"):
        raise IncorrectTypeError(f"{cls} is not a valid config class")
    unknown_fields = set(json_obj) - {f[0]
                                      for f in cls.__annotations__.items()}
    print("unknown_fields:", unknown_fields)
    if unknown_fields:
        cls_name = getattr(cls, "__name__", cls)
        cls_fields = {f[0] for f in cls.__annotations__.items()}
        raise ConfigParseError(
            f"Unknown fields for class {cls_name} with fields {cls_fields} \
            detected in config json: {unknown_fields}"
        )
    print("cls_annotations:", cls.__annotations__)
    for field, f_cls in cls.__annotations__.items():
        value = None
        is_optional = _is_optional(f_cls)
        print("is_optional:", _is_optional)
        print("f_cls:", f_cls)
        print("field:", field)
        if field not in json_obj:
            print("field not in json_obj")
            if field in cls._field_defaults:
                # if using default value, no conversion is needed
                value = cls._field_defaults.get(field)
                print("value:", value)
        else:
            print("else....")
            try:
                print("calling _value_from_json")
                value = _value_from_json(f_cls, json_obj[field])
                print("value2:", type(value))
            except ConfigParseError:
                raise
            except Exception as e:
                raise ConfigParseError(
                    f"failed to parse {field} to {f_cls} with json payload \
                    {json_obj[field]}"
                ) from e
        # validate value
        print("validate value")
        if value is None and not is_optional:
            cls_name = getattr(cls, "__name__", cls)
            print("cls_name:", cls_name)
            raise MissingValueError(
                f"missing value for {field} in class {cls_name} with json {json_obj}"
            )
        parsed_dict[field] = value
        print("parsed_dict:", parsed_dict)
    return cls(**parsed_dict)


def _value_to_json(cls, value):
    cls_type = _get_class_type(cls)
    assert _is_optional(cls) or value is not None
    if value is None:
        return value
    # optional with more than 2 classes is treated as Union
    elif _is_optional(cls) and len(cls.__args__) == 2:
        sub_cls = cls.__args__[0] if type(None) != cls.__args__[
            0] else cls.__args__[1]
        return _value_to_json(sub_cls, value)
    elif cls_type == Union or getattr(cls, "__EXPANSIBLE__", False):
        real_cls = type(value)
        if hasattr(real_cls, "_fields"):
            value = config_to_json(real_cls, value)
        return {_canonical_typename(real_cls): value}
    # nested config
    elif hasattr(cls, "_fields"):
        return config_to_json(cls, value)
    elif issubclass(cls_type, Enum):
        return value.value
    elif issubclass(cls_type, List):
        sub_cls = cls.__args__[0]
        return [_value_to_json(sub_cls, v) for v in value]
    elif issubclass(cls_type, Tuple):
        return tuple(
            _value_to_json(c, v) for c, v in zip(_extend_tuple_type(cls, value), value)
        )
    elif issubclass(cls_type, Dict):
        sub_cls = cls.__args__[1]
        return {key: _value_to_json(sub_cls, v) for key, v in value.items()}
    print("v3:", value)
    return value


def config_to_json(cls, config_obj):
    json_result = {}
    if not hasattr(cls, "_fields"):
        raise IncorrectTypeError(f"{cls} is not a valid config class")
    for field, f_cls in cls.__annotations__.items():
        value = getattr(config_obj, field)
        json_result[field] = _value_to_json(f_cls, value)
    return json_result


def _get_class_type(cls):
    """
    type(cls) has an inconsistent behavior between 3.6 and 3.7 because of
    changes in the typing module. We therefore rely on __origin__, present only
    in classes from typing to extract the origin of the class for comparison,
    otherwise default to the type sent directly
    :param cls: class to infer
    :return: class or in the case of classes from typing module, the real type
    (Union, List) of the created object
    """
    return cls.__origin__ if hasattr(cls, "__origin__") else cls


def parse_config(config_json):
    """
    Parse PyTextConfig object from parameter string or parameter file
    """
    print("serialize.py in parse_config")
    print("config_json type", type(config_json))
    print(config_json)
    print("+++++++")
    if "config" in config_json:
        print("config is in config_json")
        config_json = config_json["config"]
    return pytext_config_from_json(config_json)

# test metaclass
from collections import OrderedDict
from typing import Any, List, Optional, Union


class ConfigBaseMeta(type):
    def annotations_and_defaults(cls):
        #print("ConfigBaseMeta annotations_and_defaults")
        annotations = OrderedDict()
        defaults = {}
        for base in reversed(cls.__bases__):
            if base is ConfigBase:
                continue
            annotations.update(getattr(base, "__annotations__", {}))
            defaults.update(getattr(base, "_field_defaults", {}))
        annotations.update(vars(cls).get("__annotations__", {}))
        defaults.update({k: getattr(cls, k)
                         for k in annotations if hasattr(cls, k)})
        return annotations, defaults

    @property
    def __annotations__(cls):
        annotations, _ = cls.annotations_and_defaults()
        return annotations
    
    _field_types = __annotations__


    @property
    def _fields(cls):
        return cls.__annotations__.keys()

    @property
    def _field_defaults(cls):
        _, defaults = cls.annotations_and_defaults()
        return defaults


class ConfigBase(metaclass=ConfigBaseMeta):
    def items(self):
        return self._asdict().items()

    def _asdict(self):
        return {k: getattr(self, k) for k in type(self).__annotations__}

	def __init__(self, **kwargs):
        """Configs can be constructed by specifying values by keyword.
        If a keyword is supplied that isn't in the config, or if a config requires
        a value that isn't specified and doesn't have a default, a TypeError will be
        raised."""
        #print("ConfigBase init")
        specified = kwargs.keys() | type(self)._field_defaults.keys()
        required = type(self).__annotations__.keys()
        # Unspecified fields have no default and weren't provided by the caller
        unspecified_fields = required - specified
        if unspecified_fields:
            raise TypeError(
                f"Failed to specify {unspecified_fields} for {type(self)}")

        # Overspecified fields are fields that were provided but that the config
        # doesn't know what to do with, ie. was never specified anywhere.
        overspecified_fields = specified - required
        if overspecified_fields:
            raise TypeError(
                f"Specified non-existent fields {overspecified_fields} for {type(self)}"
            )

        vars(self).update(kwargs)

  	def __str__(self):
        lines = [self.__class__.__name__ + ":"]
        for key, val in vars(self).items():
            lines += f"{key}: {val}".split("\n")
        return "\n    ".join(lines)


class PlaceHolder:
    pass

class TestConfig(ConfigBase):
    # Snapshot of a trained model to test
    load_snapshot_path: str
    # Test data path
    test_path: str = "test.tsv"
    #: Field names for the TSV. If this is not set, the first line of each file
    #: will be assumed to be a header containing the field names.
    field_names: Optional[List[str]] = None
    use_cuda_if_available: bool = True
    # Whether to use TensorBoard
    use_tensorboard: bool = True
    # Output path where metric reporter writes to.
    test_out_path: str = ""


t=TestConfig()
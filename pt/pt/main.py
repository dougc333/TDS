
import click
import json
import sys
from pt.config.serialize import (
    config_to_json,
    parse_config,
    pytext_config_from_json,
)


class Attrs:
    def __repr__(self):
        return f"Attrs({', '.join(f'{k}={v}' for k, v in vars(self).items())})"


@click.group()
@click.option("--include", multiple=True)
@click.option("--config-file", default="")
@click.option("--config-json", default="")
@click.option(
    "--config-module", default="", help="python module that contains the config object"
)
@click.pass_context
def main(context, config_file, config_json, config_module, include):
    print("main main main main main main is here do you see me")
    print("context:",context)
    print("config_file:",config_file)
    print("config_json:",config_json)
    print("config_module:",config_module)
    print("include:",include)

    for path in include or []:
        print("add_include path:",path)
        add_include(path)

    context.obj = Attrs()
    print("context.obj from Attrs:",context.obj)

    def load_config():
        # Cache the config object so it can be accessed multiple times
        print("main load_config cache? ")
        if not hasattr(context.obj, "config"):
            print("no attrs")
            if config_module:
                print("main load_config config_module True")
                context.obj.config = import_module(config_module).config
            else:
                if config_file:
                    print("config file exists")
                    with open(config_file) as file:
                        config = json.load(file)
                elif config_json:
                    print("config_json")
                    config = json.loads(config_json)
                else:
                    click.echo("No config file specified, reading from stdin")
                    config = json.load(sys.stdin)
                context.obj.config = parse_config(config)
                print("context.obj.config",config.obj.config)
        return context.obj.config

    context.obj.load_config = load_config


@main.command()
@click.pass_context
def train(context):
    print("pt context object", context)
    config = context.obj.load_config()
    print("pt have config object")
    print("\n===pt training...")
    metric_channels = []
    if config.use_tensorboard:
        print("\npt comment out usetensorboard")
        # metric_channels.append(TensorBoardChannel())
    try:
        if config.distributed_world_size == 1:
            print("\n===train_model")
            train_model(config, metric_channels=metric_channels)
        else:
            print("\n===train_model_distributed")
            train_model_distributed(config, metric_channels)
        print("\n=== Starting testing...")
        test_model_from_snapshot_path(
            config.save_snapshot_path,
            config.use_cuda_if_available,
            test_path=None,
            metric_channels=metric_channels,
        )
    finally:
        for mc in metric_channels:
            mc.close()


if __name__ == '__main__':
    main()

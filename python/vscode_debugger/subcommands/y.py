#this is a test program to test click subcommands and debugger interaction
#import pdb
import click


class Foo:
  def __init__(self):
    print('init running')
    self.name="Foo"
    self.val = 1
    self.str = "Foo string"



@click.group()
@click.option("--config-file", default="train_cnn.json")
@click.option("--config-json", default="")
@click.option(
    "--config-module", default="", help="python module that contains the config object"
)
@click.pass_context
def main(context, config_file, config_json, config_module):
  #pdb.set_trace() use debugger to view context, config_file, config_json, config_module, include
  print("main")
  f = Foo()

@main.command()
@click.option("--a_option", default="")
def train(a_option):
  print("train subcommand a_option:",a_option)
  

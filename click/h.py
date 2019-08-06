
import click

@click.command()
def hello():
  click.echo("click says he")

@click.group()
def cli():
  pass

@cli.command()
def db():
  click.echo('db')

cli.add_command(db)

if '__name__'  == '__main__':
  hello()
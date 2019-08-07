#click group and argument examples. an argument is for file IO
import click

@click.group()
def cli():
  click.echo('cli high level function')

@cli.command()
@click.option('--st', default='string st', type=str)
@click.option('--repeat', default=3, type=int)
def foo(st,repeat):
	click.echo('function foo option s is %s:' % st)
	for x in range(repeat):
		click.echo(x)
	


@ckick option()
import click

@click.command()
@click.option('--st', default='default st')
def cli(st):
	click.echo("h2 program parameter st is:%st" % st) 


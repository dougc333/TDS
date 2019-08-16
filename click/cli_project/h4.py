import click

@click.command()
@click.option('--string', type=str, default = 'default string')
@click.argument('out',type=click.File('w'),required=False)
def cli(string,out):
	click.echo('string %s' % string) 
	click.echo(out)

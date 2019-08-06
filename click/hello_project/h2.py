import click

@click.command()
@click.option('--s',type='string', default="default string in option")
def cli(s,repeat):
	print("s:",s) 
	click.echo("hello world w.click")
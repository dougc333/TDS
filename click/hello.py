
import click

@click.command()
@click.option('--s',type='string', default="default string in option")
@click.option('--repeat', default=1, type=int, help='repeat')
@click.argument('out',type=click.File('w'),default='-',required=False)
def cli(s,repeat,out):
	print("s:",s) #cant replace w/click.echo as in video
	click.echo("hello world w.click")
	#click.echo(out)
	for x in range(repeat):
		print(x)
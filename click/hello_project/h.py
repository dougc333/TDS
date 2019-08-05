
import click

@click.command()
@click.option('--s',type='string', default="default string in option")
@click.option('--repeat', default=1, type=int, help='repeat')
def cli():
	print("s:",s) #cant replace w/click.echo as in video
	click.echo("hello world w.click")
	for x in range(repeat):
		print(x)

print("end")
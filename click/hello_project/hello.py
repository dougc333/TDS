import click

@click.command()
@click.option('--string', type=str,default='asdfasdf')
@click.option('--repeat', type=int, default=1)
#I am divided whether this is good. Once p2 is EOL what is the point? 
#and I prefer the better features of fstrings anyway
def cli(string,repeat):
	click.echo("s:%s" %string) #have to use python2 syntax for click.echo. 
	print("s:",string)
	click.echo("this is echo")
	print(type(repeat))
	print('repeat',repeat)
	click.echo("repeat:%d"%repeat) #have to use python2 syntax for click.echo. 
	for x in range(repeat):
		click.echo(x)
	for x in range(repeat,-1,-1):
		print(x)
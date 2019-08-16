import click

@click.group()
def cli():
	pass



#I am divided whether this is good. Once p2 is EOL what is the point? 
#and I prefer the better features of fstrings anyway
@cli.command()
@click.option('--string', type=str,default='asdfasdf')
@click.option('--repeat', type=int, default=1)
@click.argument('out',type=click.File('w'), default='-',required=False)
def hi(string,repeat,out):
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
	click.echo(out)
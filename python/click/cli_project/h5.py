import click

class Config(object):
	def __init(self):
		self.verbose=False

pass_config = click.make_pass_decorator(Config,ensure=True)

@click.group()
@click.option('--verbose', is_flag=True)
@pass_config
def cli(config,verbose):
	config.verbose = verbose
	click.echo('cli verbose')	

@cli.command()
@click.option('--string', default='default string option')
@click.option('--repeat',default=4)
@pass_config
def foo(config,string,repeat):
	click.echo('foo string %s' % string)
	if config.verbose:
		click.echo('verbose in foo function where the verbose state \
		has been transferred to foo from cli using the pass_config decorator')
	for x in range(repeat):
		click.echo(x)

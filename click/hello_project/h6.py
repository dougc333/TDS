import click


class Config(object):
	def __init__(self):
		self.verbose=False
		
pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option('--home-directory', type=click.Path())
@click.option('--verbose',is_flag=True)
@pass_config
def cli(config,verbose,home_directory):
	click.echo('cli')
	config.verbose = verbose
	if home_directory is None:
		home_directory = os.getcwd()
		#home_directory = '.'
	config.home_directory = home_directory

pass_config = click.make_pass_decorator(Config,ensure=True)


@cli.command()
@click.option('--string', default='default_string')
@click.option('--repeat', default=3)
@pass_config
def foo(config,string, repeat):
	if config.verbose:
		click.echo('config verbose')
	click.echo("home directory is:%s " % config.home_directory)
	for x in range(repeat):
		click.echo(x)
	

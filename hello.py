import click

@click.command()
@click.argument('name')

def hello():
    """
    Example script
    see: http://click.pocoo.org/5/setuptools/
    """
    click.echo('Hello '+name+'!')

if __name__ == '__main__':
	hello()

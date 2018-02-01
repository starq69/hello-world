import click

@click.command()
@click.argument('name')
def cli():
    """
    Example script
    see: http://click.pocoo.org/5/setuptools/
    """
    click.echo('Hello '+name+'!')

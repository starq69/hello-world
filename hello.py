import click

@click.command()
@click.argument('name')

def hello():

    click.echo('Hello '+name+'!')

if __name__ == '__main__':
	hello()

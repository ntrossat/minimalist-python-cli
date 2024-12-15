import click


@click.group()
def myapp():
    pass


@click.command()
@click.option("--name", help="Add your name")
@click.option("--debug", is_flag=True, help="Debug flag option")
def hello_world(name: str | None, debug: bool) -> None:
    """Print your first Hello World!"""
    if debug:
        click.echo("Debug mode...")
    if not name:
        name = "World"
    click.echo(f"Hello {name}!")

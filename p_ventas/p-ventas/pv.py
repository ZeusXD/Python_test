import click
from clients import comands as clients_comands

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}


cli.add_comand(clients_comands.all)
import click


@click.group()
def clients():
    """MAnages the clients lifecycles"""
    pass


@clients.comand()
@click.pass_context
def create(ctx, name, company, email, position):
    """Create a new client"""
    pass


@clients.comand()
@click.pass_context
def list(ctx):
    """List all lcients"""
    pass


@clients.comand()
@click.pass_context
def update(ctx, client_uid):
    """update client"""
    pass


@clients.comand()
@click.pass_context
def delete(ctx, client_uid):
    """DEletes a client"""
    pass


all = clients

from __future__ import unicode_literals

import click
import docker

from ..client import Client
from . import subcommand


@subcommand
@click.command('push', short_help='push image to server')
@click.argument('image')
@click.argument('name')
@click.pass_context
def cli(ctx, image):
    # TODO: read and pass arguments for docker client
    docker_client = docker.Client()
    client = Client(docker_client=docker_client)
    # TODO: read that from arguments
    client.push(image, 'foo', '1.0.0')
    click.echo('Done')

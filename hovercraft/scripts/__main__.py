from __future__ import unicode_literals
import sys
import logging

import click
import venusian

import hovercraft
from hovercraft import scripts


LOG_MAPPING = {
    'd': logging.DEBUG,
    'debug': logging.DEBUG,
    'i': logging.INFO,
    'info': logging.INFO,
    'w': logging.WARNING,
    'warn': logging.WARNING,
    'e': logging.ERROR,
    'err': logging.ERROR,
    'error': logging.ERROR,
}


class MasterCLI(click.MultiCommand):

    def __init__(self, *args, **kwargs):
        super(MasterCLI, self).__init__(*args, **kwargs)
        self.subcommands = self._scan_subcommands()

    def _scan_subcommands(self):
        subcommands = {}
        scanner = venusian.Scanner(subcommands=subcommands)
        scanner.scan(scripts, categories=('subcommands', ))
        return subcommands

    def list_commands(self, ctx):
        command_names = self.subcommands.keys()
        command_names.sort()
        return command_names

    def get_command(self, ctx, name):
        if name not in self.subcommands:
            return
        return self.subcommands[name]


@click.command(cls=MasterCLI, invoke_without_command=True)
@click.option(
    '-l', '--log-level',
    type=click.Choice(LOG_MAPPING.keys()),
    help='log LEVEL',
    default='info',
)
@click.option(
    '-v', '--version',
    is_flag=True,
    help='print hovercraft version',
)
@click.pass_context
def cli(ctx, log_level, version):
    click.echo('Log level: {}'.format(log_level), err=True)

    root = logging.getLogger('')
    root.setLevel(level=LOG_MAPPING[log_level])
    
    ctx.obj['log_level'] = log_level

    if version:
        click.echo(hovercraft.__version__)
        return
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help(), err=True)
        sys.exit(-1)


def main():
    cli(obj={})

if __name__ == '__main__':
    main()

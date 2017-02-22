from __future__ import absolute_import

import sys

import click

from raincoat.raincoat import Raincoat

__version__ = "0.6.0"

CONTEXT_SETTINGS = {'help_option_names': ['-h', '--help']}

@click.option('--path', default=".", help='Path to analyze (default is "." )')
def main(path):
@click.command(context_settings=CONTEXT_SETTINGS)
    """
    Analyze your code to find outdated copy-pasted snippets.
    "Raincoat has you covered when your code is not DRY."

    Full documentation at http://raincoat.readthedocs.io/en/latest/
    """
    raincoat = Raincoat()

    errors = list(raincoat.raincoat(path=path))
    for error, match in errors:
        click.echo(match)
        click.echo(error)
        click.echo()

    sys.exit(int(bool(errors)))

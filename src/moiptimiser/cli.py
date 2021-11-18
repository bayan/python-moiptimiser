"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mmoiptimiser` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``moiptimiser.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``moiptimiser.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import click

from moiptimiser.impl import *

@click.command(help='FILEPATH points to a multi-objective linear programming file using the LP format')
@click.argument('filepath')
def main(filepath):
    moiptimiser = Tamby2020MOIPtimiser.from_lp_file(filepath)
    nds = moiptimiser.find_non_dominated_objective_vectors()
    for nd in nds:
        click.echo(repr(nd))
    click.echo(f"{len(nds)} non dominated vectors found")

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

class MoipAlgorithmClass(click.ParamType):
    name = "Algorithm"

    TAMBY2020_TWO_STAGE = 'tamby2020-two-stage'
    TAMBY2020_DIRECT = 'tamby2020-direct'
    OZLEN2014 = 'ozlen2014'

    lookup = {
        TAMBY2020_TWO_STAGE: Tamby2020TwoStageMOIPtimiser,
        TAMBY2020_DIRECT: Tamby2020DirectMOIPtimiser,
        OZLEN2014: Ozlen2014MOIPtimiser
    }

    valid_options = tuple(lookup.keys())

    def convert(self, value, param, ctx):
        if value not in self.valid_options:
            self.fail(
                f"'{value}' is not one of the valid multi-objective integer programming algorithm that have been implemented. " +
                f"Please select one of the following valid options: {self.valid_options}.",
                param,
                ctx,
            )
        return self.lookup[value]

@click.command(help='FILEPATH points to a multi-objective linear programming file using the LP format')
@click.argument('filepath')
@click.option('-a','--algorithm', default=MoipAlgorithmClass.TAMBY2020_TWO_STAGE,
              help=f"Selected algorithm. Valid options are {MoipAlgorithmClass.valid_options}",
              type=MoipAlgorithmClass())
def main(filepath, algorithm):
    moiptimiser = algorithm.from_lp_file(filepath)
    nds = moiptimiser.find_non_dominated_objective_vectors()
    for nd in nds:
        click.echo(repr(nd))
    click.echo(f"Non-dominated vectors found: {len(nds)}")
    click.echo(f"Solver calls: {moiptimiser.num_solver_calls}")

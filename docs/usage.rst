=====
Usage
=====

To use moiptimiser in your python code::

  from moiptimiser.impl import MOIPtimiser
  moiptimiser = MOIPtimiser.from_lp_file('/path/to/mutli-objective.lp')
  non_dominated_vectors = moiptimiser.find_non_dominated_objective_vectors()

Alternatively, you can use the command line tool to process a file and print out the non-dominated vectors that are found::

  python -mmoiptimiser /path/to/mutli-objective.lp


Or if installed correctly, you should also be able to perform the last command like this::

  moiptimiser /path/to/mutli-objective.lp

========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-moiptimiser/badge/?style=flat
    :target: https://readthedocs.org/projects/python-moiptimiser
    :alt: Documentation Status

.. |version| image:: https://img.shields.io/pypi/v/moiptimiser.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/moiptimiser

.. |wheel| image:: https://img.shields.io/pypi/wheel/moiptimiser.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/moiptimiser

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/moiptimiser.svg
    :alt: Supported versions
    :target: https://pypi.org/project/moiptimiser

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/moiptimiser.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/moiptimiser

.. |commits-since| image:: https://img.shields.io/github/commits-since/bayan/python-moiptimiser/v0.0.2.svg
    :alt: Commits since latest release
    :target: https://github.com/bayan/python-moiptimiser/compare/v0.0.2...master



.. end-badges

Multi-Objective Integer Programming with Gurobi and Python

The optimisation software from `Gurobi <https://www.gurobi.com/>`_ now supports `multi-objective programming <https://www.gurobi.com/documentation/9.0/refman/multiple_objectives.html>`_.

Since there are multiple objectives, there may be many solutions, each of which may optimise the objectives with a different set of priorities. Finding all such solutions can be algorithmically costly, so Gurobi's solver only returns a single result.

However, due to the importance of such functionality, much research has been invested into finding better algorithms that can efficiently find all solutions.

This python package extends Gurobi's multi-objective functionality by using the algorithm developed by (Ozlen et al., 2014). It provides a module that can be used in python programs, as well as a command line tool that can read `multi-objective LP <https://www.gurobi.com/documentation/9.0/refman/lp_format.html>`_ files.



* Free software: MIT license

Installation
============

::

    pip install moiptimiser

You can also install the in-development version with::

    pip install https://github.com/bayan/python-moiptimiser/archive/master.zip


Documentation
=============


https://python-moiptimiser.readthedocs.io/


Development
===========

To run the all tests run::

    tox


References
==========

Ozlen, M., Burton, B.A., MacRae, C.A.G., 2014. Multi-Objective Integer Programming: An Improved Recursive Algorithm. J Optim Theory Appl 160, 470–482. https://doi.org/10.1007/s10957-013-0364-y

===========================
!!! UNDER CONSTRUCTION !!!!
===========================

This code is currently under development. First working version expected soon, so watch this space...







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

.. |commits-since| image:: https://img.shields.io/github/commits-since/bayan/python-moiptimiser/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/bayan/python-moiptimiser/compare/v0.0.0...master



.. end-badges

Multi-Objective Integer Programming with Gurobi and Python

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

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

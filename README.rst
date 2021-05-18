Clean Auckland GTFS
*******************
.. image:: https://travis-ci.org/mrcagney/clean_auckland_gtfs.svg?branch=master
    :target: https://travis-ci.org/mrcagney/clean_auckland_gtfs

Some Python 3.8+ tools for cleaning Auckland Transport GTFS feeds.
Such feeds can be found on `Transit Feeds here <transitfeeds.com/p/auckland-transport/124>`_, for example.

Cleaning involves

- Dropping school routes
- Aggregating GTFS routes by route short name, so that GTFS routes match public-facing routes. Auckland does not have 2000 routes!
- Dropping stops with no stop times, trips with no stop times, shapes with no trips, routes with no trips, and services with no trips, in that order.


Installation
============
``poetry add clean_auckland_gtfs``


Usage
=====
Use as a library.
See the Jupyter notebook at ``notebooks/examples.ipynb`` for inspiration.


Notes
=====
- Development status is Alpha
- This project uses semantic versioning


Authors
=======
- Alex Raichev, 2016-12-08


Changes
=======

0.5.0, 2021-05-18
-----------------
- Upgraded to Python 3.9 and updated dependencies.
- Modularized a bit more.
- Updated school strings to search for.


0.4.4, 2020-05-08
-----------------
- Updated dependencies.


0.4.3, 2020-02-12
-----------------
- Updated dependencies.


0.4.2, 2019-10-31
-----------------
- Updated requirements.
- Made dropping school routes optional in function ``clean``.


0.4.1, 2019-05-27
-----------------
- Updated requirements.


0.4.0, 2019-04-08
-----------------
- Removed "Stanmore Bay To Long Bay" and "Long Bay To Stanmore Bay" routes.
- Removed accidental Tornado dependency.
- Published to PyPI.


0.3.0, 2019-03-04
-----------------
- Switched to Poetry.
- Updated school route search.


0.2.0, 2017-10-17
-----------------
- Dropped zombie stops, trips, etc. in ``main.clean`` function


0.1.0, 2016-06-07
-----------------
- Updated requirements
- Added some tests


0.0.0, 2016-12-08
-----------------
- First release
Clean Auckland GTFS
********************
Some Python 3.5+ tools for cleaning Auckland Transport GTFS feeds.
Such feeds can be found on `Transit Feeds here <transitfeeds.com/p/auckland-transport/124>`_, for example.

Cleaning involves

- Dropping school routes
- Aggregating GTFS routes by route short name, so that GTFS routes match public-facing routes. Auckland does not have 2500 transit routes!
- Dropping stops with no stop times, trips with no stop times, shapes with no trips, routes with no trips, and services with no trips, in that order.


Installation
=============
``pip install -U git+https://github.com/araichev/clean_auckland_gtfs``


Usage
======
Use as a library.


Notes
======
- Development status is Alpha
- This project uses semantic versioning


Authors
========
- Alex Raichev, 2016-12-08



History
========

0.2.0, 2017-10-17
-------------------
- Dropped zombie stops, trips, etc. in ``main.clean`` function


0.1.0, 2016-06-07
-------------------
- Updated requirements
- Added some tests


0.0.0, 2016-12-08
------------------
- First release
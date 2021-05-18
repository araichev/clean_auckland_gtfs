import gtfs_kit as gk
import pandas as pd

from .context import clean_auckland_gtfs, DATA_DIR
from clean_auckland_gtfs import *


feed = gk.read_feed(DATA_DIR/'raw_auckland_gtfs_20210519.zip', dist_units='km')

def test_find_school_routes():
    sr = find_school_routes(feed)
    assert isinstance(sr, pd.DataFrame)

    # Should drop some routes
    assert sr.shape[0] > 0

    sr = find_school_routes(feed, school_max_ntrips=0)

    # Should drop no routes
    assert sr.empty

def test_drop_school_routes():
    n = feed.routes.shape[0]
    feed1 = drop_school_routes(feed)

    # Should drop some routes
    k = feed1.routes.shape[0]
    assert k < n

    feed1 = drop_school_routes(feed, school_max_ntrips=0)

    # Should drop no routes
    assert feed1 == feed

def test_clean():
    n = feed.routes.shape[0]
    feed1 = clean(feed)

    # Should drop some routes
    k = feed1.routes.shape[0]
    assert k < n

    # Route short names should be unique
    j = feed1.routes.route_short_name.nunique()
    assert j == k

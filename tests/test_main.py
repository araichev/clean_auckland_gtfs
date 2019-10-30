import gtfs_kit as gk

from .context import clean_auckland_gtfs, DATA_DIR
from clean_auckland_gtfs import *


feed = gk.read_gtfs(DATA_DIR/'raw_auckland_gtfs_20190221.zip', dist_units='km')

def test_drop_school_routes():
    n = feed.routes.shape[0]
    feed1 = drop_school_routes(feed)

    # Should drop some routes
    k = feed1.routes.shape[0]
    assert k < n

def test_clean():
    n = feed.routes.shape[0]
    feed1 = clean(feed)

    # Should drop some routes
    k = feed1.routes.shape[0]
    assert k < n

    # Route short names should be unique
    j = feed1.routes.route_short_name.nunique()
    assert j == k

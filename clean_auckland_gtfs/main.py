from __future__ import annotations
import gtfs_kit as gk
import pandas as pd


SCHOOL_STRINGS = [
    "college",
    "intermediate",
    "grammar",
    "primary",
    "high",
    "school",
    "sch",
    "boys",
    "girls",
] + [
    "Rosmini",
    "St Marks",
    "Clendon to Manurewa and Greenmeadows",
    "Sacred Heart",
    "St Josephs",
    "Ponsonby Int",
    "Long Bay To Stanmore Bay",
    "Stanmore Bay To Long Bay",
    "Sancta Maria",
    "Our Lady Star Of The Sea",
    "St Ignatius",
    "St Thomas",
    "Baradine",
]

def find_school_routes(
    feed: gk.Feed,
    school_max_ntrips:int=4,
    school_strings:list[str]=SCHOOL_STRINGS,
) -> pd.DataFrame:
    """
    Given a GTFSTK Feed object, find all routes that appear to be school routes, and
    return the resulting GTFS DataFrame of routes.

    The school route criteria, all of which must be satisfied, are:

    - the route is a bus
    - the route has at most ``school_max_ntrips`` trips
    - the route long name contains at least one of the strings in ``school_strings``

    If an empty list of school strings is given, then ignore the route long name
    criterion.
    """
    # Route is a bus
    school_routes = (
        feed.routes
        .loc[lambda x: x.route_type == 3]
    )

    # Route has at most school_max_ntrips
    t = feed.trips.groupby("route_id").count().reset_index()
    rids = t.loc[lambda x: x.trip_id <= school_max_ntrips, "route_id"]
    school_routes = school_routes.loc[lambda x: x.route_id.isin(rids)]

    # Route long name contains school-like word
    if school_strings:
        condition = False
        for s in school_strings:
            condition |= school_routes["route_long_name"].str.contains(s, case=False)

        school_routes = school_routes.loc[condition]

    return school_routes.copy()

def drop_school_routes(
    feed: gk.Feed,
    school_max_ntrips:int=4,
    school_strings:list[str]=SCHOOL_STRINGS,
) -> gk.Feed:
    """
    Given a GTFSTK Feed object, drop all routes that appear to be school routes,
    along with their associated trips, stop times, etc.,
    and return the resulting new feed.

    The school route criteria, all of which must be satisfied, are:

    - the route is a bus
    - the route has at most ``school_max_ntrips`` trips
    - the route long name contains at least one of the strings in ``school_strings``

    If an empty list of school strings is given, then ignore the route long name
    criterion.
    """
    school_routes = find_school_routes(feed, school_max_ntrips, school_strings)

    # Subset feed non-school routes
    feed.routes = feed.routes.loc[lambda x: ~x.route_id.isin(school_routes.route_id)].copy()

    # Subset to non-school trips
    rids = feed.routes.route_id
    feed.trips = feed.trips.loc[lambda x: x.route_id.isin(rids)].copy()

    # Subset to non-school stop times
    st = feed.stop_times
    feed.stop_times = st.loc[lambda x: x.trip_id.isin(feed.trips.trip_id)].copy()

    return feed


def clean(
    feed: gk.Feed,
    school_max_ntrips:int=4,
    school_strings:list[str]=SCHOOL_STRINGS,
    *,
    keep_school_routes:bool=False
) -> gk.Feed:
    """
    Given a GTFSTK object representing an Auckland GTFS feed,
    do the following in order.

    1. Optionally drop its school routes via the function
       :func:`drop_school_routes` and its associated parameters
    2. Aggregate the routes by route short name
    3. Drop zombie stops, trips, etc. via ``gtfs_kit.drop_zombies
    4. Clean the stop codes by adding leading zeros where necessary

    Then return the resulting feed.
    """
    if not keep_school_routes:
        feed = drop_school_routes(feed, school_max_ntrips, school_strings)

    feed = gk.aggregate_routes(feed)
    feed = gk.drop_zombies(feed)

    # Add leading zeros to stop codes
    def clean_stop_code(x):
        n = len(x)
        if n < 4:
            x = "0"*(4 - n) + x
        return x

    if "stop_code" in feed.stops.columns:
      s = feed.stops
      s["stop_code"] = s["stop_code"].map(clean_stop_code)
      feed.stops = s

    return feed

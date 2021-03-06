#!/usr/bin/env python
"""
Note: As of late March 2020, Venmo started putting out fake data to their
public web API. The fake data consists of twenty or so transactions with
generic user names and messages.
"""
import requests

from venmo_scraper.constants import DEFAULT_OUTPUT_DIR, URL_API
from venmo_scraper.utils import create_dir, dump_data


def get_data():
    """Return JSON of response from GET request of endpoint."""
    r = requests.get(URL_API, headers={'user-agent': 'transactions'})
    data = r.json()['data']

    return data


def get_public_feed(output_dir):
    """Call Venmo public API and dump response to disk."""
    create_dir(output_dir)
    data = get_data()
    dump_data(data, output_dir)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Get Venmo's public feed")
    parser.add_argument('-o', '--output_dir',
                        default=DEFAULT_OUTPUT_DIR,
                        action='store',
                        help="specify Venmo data output directory")
    args = parser.parse_args()

    get_public_feed(args.output_dir)

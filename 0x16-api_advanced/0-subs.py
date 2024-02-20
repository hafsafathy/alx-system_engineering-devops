#!/usr/bin/python3
"""
 queries the Reddit API and returns the number of subscribers
"""

from json import loads
import requests


def number_of_subscribers(subreddit):
    """If not a valid subreddit, return 0."""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)'}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs

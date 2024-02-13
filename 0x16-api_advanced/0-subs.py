#!/usr/bin/python3
"""
 queries the Reddit API and returns the number of subscribers
"""

from json import loads
from requests import get


def number_of_subscribers(subreddit):
    """If not a valid subreddit, return 0."""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Custom-User-Agent'}
    response = get(url, headers=headers)
    reddits = response.json()

    try:
        subscribers = reddits.get('data').get('subscribers')
        return int(subscribers)
    except:
        return 0

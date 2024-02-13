#!/usr/bin/python3
"""Contains recurse function"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursively retrieves the titles of all hot articles for a given subreddit."""
    if hot_list is None:
        hot_list = []

    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = "https://www.reddit.com/r/{subreddit}/hot.json".format(subreddit)
    headers = { "User-Agent": "0x16-api_advanced:project:\
                 v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {'limit': 100}

    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])

        for child in children:
            post = child.get('data', {})
            title = post.get('title')
            hot_list.append(title)

        after = data.get('after')
        if after:
            recurse(subreddit, hot_list, after)

    elif response.status_code == 404:
        return None
    return hot_list

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
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Custom-User-Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        # Extract the number of subscribers from the JSON response
        data = response.json().get('data', {})
        subscribers = data.get('subscribers', 0)
        return subscribers
    else:
        # Return 0 for invalid subreddits or other errors
        return 0


#!/usr/bin/python3
'''Function that queries the redditAPI'''
import requests


def number_of_subscribers(subreddit):
    '''
        queries the number of subscribers for a given a subreddit
    '''
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return
    payload_data = response.json().get("data")
    return payload_data.get("subscribers")

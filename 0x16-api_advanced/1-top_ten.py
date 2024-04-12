#!/usr/bin/python3
'''Lists the first hot ten posts of a given subreddit'''
import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API
    for the hot 10 posts on a subreddit
    """
    req = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)

#!/usr/bin/python3
"""1. Top Ten1"""


def top_ten(subreddit):
    """function that queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given
    subreddit."""
    import requests

    subscribers = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                               .format(subreddit),
                               headers={"User-Agent": "My-User-Agent"},
                               allow_redirects=False)
    if subscribers.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in subscribers.json().get("data").get("children")]

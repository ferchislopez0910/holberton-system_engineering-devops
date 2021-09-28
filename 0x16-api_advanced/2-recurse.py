#!/usr/bin/python3
"""2. Recurse it!"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """unction that queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit """

    import requests

    subscribers = requests.get("https://www.reddit.com/r/{}/hot.json".format(
                            subreddit),
                            params={"count": count, "after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if subscribers.status_code >= 400:
        return None

    hot_l = hot_list + [child.get("data").get("title")
                        for child in subscribers.json()
                        .get("data")
                        .get("children")]

    info = subscribers.json()
    if not info.get("data").get("after"):
        return hot_l

    return recurse(subreddit, hot_l, info.get("data").get("count"),
                   info.get("data").get("after"))

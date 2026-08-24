import requests


def select_api(api):
    dom = f"htpps://{api}"
    return dom


def github_url(api, username):
    dm = select_api(api)
    if dm == "htpps://api.github.com":
        endp = get_username(username)
        url = dm + endp

    return url


def get_username(username):
    endpoint = f"/users/{username}"
    return endpoint


def get_github_actions(action):
    if not action in ["repos, followers, following, gists"]:
        raise Exception("Action unknown")
    else:
        act = f"/{action}"
    return
import requests

def get_url(api):
    dm = select_api(api)
    if dm == "https://api.github.com":
        endp = get_username()
        endp = endp + get_github_actions()
        url = dm + endp

    return url


def select_api(api):
    dom = f"https://{api}"
    return dom


def get_username():
    username = input("What is the username? ")
    endpoint = f"/users/{username}"
    return endpoint


def get_github_actions():
    action = input("What is the action? ")
    if not action in ["repos", "followers", "following", "gists", ""]:
        raise Exception("Action unknown")
    else:
        act = f"/{action}"
    return act


def get_request():
    url = get_url("api.github.com")
    r = requests.get(url)
    r.raise_for_status
    return r.json()
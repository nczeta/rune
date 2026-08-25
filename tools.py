import requests

def get_github_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        error = {"error": "invalid username"}
        return error
    dic = {}
    for repo in r.json():
        dic[repo["name"]] = repo["html_url"]
    
    return dic


def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    try:
        r = requests.get(url)
        r.raise_for_status
    except requests.exceptions.HTTPError:
        error = "error: invalid username"
        return error

    return r.json()


def get_github_followers(username):
    url = f"https://api.github.com/users/{username}/followers"
    try:
        r = requests.get(url)
        r.raise_for_status
    except requests.exceptions.HTTPError:
        error = "error: invalid username"
        return error

    return r.json()


def get_github_following(username):
    url = f"https://api.github.com/users/{username}/following"
    try:
        r = requests.get(url)
        r.raise_for_status
    except requests.exceptions.HTTPError:
        error = "error: invalid username"
        return error

    return r.json()
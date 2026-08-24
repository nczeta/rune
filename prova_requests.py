import requests

r = requests.get('https://api.github.com/users/nczeta/repos')
repos = r.json()


for repo in repos:
    print(repo["html_url"])

def get_username(username):
    endpoint = f"/users/{username}"
    return endpoint

def github_actions(action):
    end = f"/{action}"
    return end

def assemble_url(endp, api):
    url = api + endp
    return url
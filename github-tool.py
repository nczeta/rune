import requests

url_api = "api.github.com"

def main():
    user = input("Insert username: ")

    print_repos(user)    


def get_url(username):
    url = f"https://{url_api}/users/{username}/repos"
    return url


def get_request(username):
    url = get_url(username)
    try:
        r = requests.get(url)
        status = r.raise_for_status()
    except requests.exceptions.HTTPError:
        dic = {"error": "invalid username"}
        return dic
    return r.json()


def print_repos(user):
    r = get_request(user)

    for repo in r:
        print(repo["name"])
        print(repo["html_url"])

main()
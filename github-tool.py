import requests

url_api = "api.github.com"

def main():
    user = input("Insert username: ")
    r = get_request(user)
    data = get_repos(r)
    
    print(data)    


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


def get_repos(r):
    dic = {}

    for repo in r:
        dic[repo["name"]] = repo["html_url"]

    return dic

main()
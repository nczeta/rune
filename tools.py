import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

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


def web_search(query):
    url = "https://api.tavily.com/search"

    data = {
        "api_key": os.getenv("TAVILY_API_KEY"),
        "query": query
    }

    responses = requests.post(
        url,
        json=data
    )
    responses = responses.json()["results"]

    results = []
    for response in responses:
        result = {
            "url": response['url'],
            "content": response['content']
        }
        results.append(result)

    return results


def web_fetch(web_page):
    try:
        r = requests.get(web_page)
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        error = "error: invalid webpage"
        return error

    soup = BeautifulSoup(r.text, "html.parser")
    for tag in soup(['script', 'style']):
        tag.decompose()

    txt = soup.get_text(separator=" ", strip=True)
    print(txt)

web_fetch("https://www.google.com/")
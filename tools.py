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


def web_fetch(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        error = "error: invalid webpage"
        return error

    soup = BeautifulSoup(r.text, "html.parser")

    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()

    content = soup.find("article")

    if content is None:
        content = soup.find("main")

    if content is None:
        content = soup.find("body")

    if content is None:
        return "Error: could not extract webpage content"

    txt = soup.get_text(separator=" ", strip=True)
    return txt


def search_places(query):
    url = "https://places.googleapis.com/v1/places:searchText"
    header = {
        "X-Goog-Api-Key": os.getenv("MAPS_API_KEY"),
        "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.rating"
    }
    body = {
        "textQuery": query
    }
    try:
        response = requests.post(
            url,
            headers=header,
            json=body
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        error = "error: invalid place"
        return error

    return response.json()


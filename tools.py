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
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        error = "error: invalid username"
        return error

    return r.json()


def get_github_followers(username):
    url = f"https://api.github.com/users/{username}/followers"
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        error = "error: invalid username"
        return error

    return r.json()


def get_github_following(username):
    url = f"https://api.github.com/users/{username}/following"
    try:
        r = requests.get(url)
        r.raise_for_status()
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

    results = []

    for place in response.json()['places']:
        results.append(
            {
                "name": place['displayName']['text'],
                "address": place['formattedAddress'],
                "rating": place['rating']
            }
        )

    return results


def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    try:
        response = requests.get(
            url,
            params={
                "name": city,
                "count": 1,
                "language": "it",
                "format": "json"
            }
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError:
            error = "error: invalid city"
            return error

    datas = response.json()['results'][0]
    latitude = datas['latitude']
    longitude = datas['longitude']

    return latitude, longitude


def get_forecast(query):
    latitude, longitude = get_coordinates(query)
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,weather_code",
        "timezone": "auto"
    }
    try:
        response = requests.get(
            url,
            params=params
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError:
            error = "error: couldn't get the forecast"
            return error

    data = response.json()

    current = data["current"]
    daily = data["daily"]

    forecast = {
        "current": {
            "time": current["time"],
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "apparent_temperature": current["apparent_temperature"],
            "precipitation": current["precipitation"],
            "weather_code": current["weather_code"],
            "wind_speed": current["wind_speed_10m"]
        },
        "daily": []
    }

    for i in range(len(daily["time"])):
        forecast["daily"].append({
            "date": daily["time"][i],
            "temperature_max": daily["temperature_2m_max"][i],
            "temperature_min": daily["temperature_2m_min"][i],
            "precipitation": daily["precipitation_sum"][i],
            "weather_code": daily["weather_code"][i]
        })

    return forecast
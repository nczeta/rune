from tools import *

tools_des = [
    {
        "type": "function",
        "function": {
            "name": "get_github_repos",
            "description": "Get the public repos from a provided GitHub user",
            "parameters": {
                "type": "object",
                "properties": {
                    "username": {
                        "type": "string",
                        "description": "The GitHub username"
                    }
                },
                "required": ["username"]
            }
        }
    },
    {
            "type": "function",
            "function": {
                "name": "get_github_user",
                "description": "Get public information about a GitHub user, profile details and account dates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "The GitHub username"
                        }
                    },
                    "required": ["username"]
                }
            }
    },
    {
                "type": "function",
                "function": {
                    "name": "get_github_following",
                    "description": "Get the users followed by a provided GitHub user",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "username": {
                                "type": "string",
                                "description": "The GitHub username"
                            }
                        },
                        "required": ["username"]
                    }
                }
    },
    {
                "type": "function",
                "function": {
                    "name": "get_github_followers",
                    "description": "Get the users who follow a provided GitHub user",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "username": {
                                "type": "string",
                                "description": "The GitHub username"
                            }
                        },
                        "required": ["username"]
                    }
                }
    },
    {
                "type": "function",
                "function": {
                    "name": "web_search",
                    "description": "Search the web for information using a search query. Returns a list of relevant web pages with their URLs and a short content snippet.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "The search query to use to find relevant information on the web."
                            }
                        },
                        "required": ["query"]
                    }
                }
    },
    {
                "type": "function",
                "function": {
                    "name": "web_fetch",
                    "description": "Fetch and extract the readable text content from a specific web page.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "url": {
                                "type": "string",
                                "description": "The URL of the web page to fetch and read."
                            }
                        },
                        "required": ["url"]
                    }
                }
    },
    {
        "type": "function",
        "function": {
            "name": "search_places",
            "description": "Search for places and locations using Google Places.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The place, business, or location to search for."
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
    "type": "function",
    "function": {
        "name": "get_forecast",
        "description": "Get the current weather and forecast for a specified location.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                        "type": "string",
                        "description": "The city or location for which to get the weather forecast."
                    }
                },
                "required": ["query"]
            }
        }
    }
]

tool_functions = {
    "get_github_repos": get_github_repos,
    "get_github_user": get_github_user,
    "get_github_following": get_github_following,
    "get_github_followers": get_github_followers,
    "web_search": web_search,
    "web_fetch": web_fetch,
    "search_places": search_places,
    "get_forecast": get_forecast
}
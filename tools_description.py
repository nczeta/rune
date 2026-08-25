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
                "description": "Get public information about a GitHub user, including their followers, following, profile details, and account dates.",
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
    }
]

tool_functions = {
    "get_github_repos": get_github_repos,
    "get_github_user": get_github_user
}
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
    }
]

tool_functions = {
    "get_github_repos": get_github_repos
}
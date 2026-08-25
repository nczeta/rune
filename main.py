from groq import Groq
from tools_description import tools_des
from tools import *
from dotenv import load_dotenv
import json

load_dotenv()

def main():
    client = Groq()

    messages = []

    while True:
        user_message = input("User: ")
        messages.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        response = get_response(messages, client)
        print("Assistant:", response)
        arguments = json.loads(response.tool_calls[0].function.arguments)
        print(get_github_repos(arguments["username"]))

        messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

def get_response(messages, client):
    response = client.chat.completions.create (
            model="openai/gpt-oss-120b",
            messages=messages,
            tools = tools_des
        )
    return response.choices[0].message#.content


main()
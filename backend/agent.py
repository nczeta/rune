from groq import Groq
from tools.description import *
from tools.tools import *
from dotenv import load_dotenv
import json

load_dotenv()
messages = []

def run_rune(user, messages):
    client = Groq()

    messages.append(
        {
            "role": "user",
            "content": user
        }
    )

    while True:
        response = get_response(messages, client)
        if not response.tool_calls:
            messages.append(
                {
                    "role": "assistant",
                    "content": response.content
                }
            )
            return response.content, messages
        else:
            messages.append(
                {
                    "role": "assistant",
                    "content": response.content,
                    "tool_calls": [
                        {
                            "id": response.tool_calls[0].id,
                            "type": "function",
                            "function": {
                                "name": response.tool_calls[0].function.name,
                                "arguments": response.tool_calls[0].function.arguments
                            }
                        }
                    ]
                }
            )
            
            arguments = json.loads(response.tool_calls[0].function.arguments)
            name = response.tool_calls[0].function.name
            function = tool_functions[name]
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": response.tool_calls[0].id,
                    "content": json.dumps(function(**arguments))
                }
            )
                
            
            


def get_response(messages, client):
    response = client.chat.completions.create (
            model="openai/gpt-oss-120b",
            messages=messages,
            tools = tools_des
        )
    return response.choices[0].message

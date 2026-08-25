from groq import Groq
from tools_description import *
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
        
        if response.tool_calls:
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
            response = get_response(messages, client)    
        
        print(response.content)
        messages.append(
            {
                "role": "assistant",
                "content": response.content
            }
        )

def get_response(messages, client):
    response = client.chat.completions.create (
            model="openai/gpt-oss-120b",
            messages=messages,
            tools = tools_des
        )
    return response.choices[0].message


main()
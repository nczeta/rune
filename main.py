from groq import Groq
from tools_description import tools_des
from dotenv import load_dotenv

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
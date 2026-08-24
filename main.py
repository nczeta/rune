from groq import Groq

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

        messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

def get_response(messages, client):
    response = client.chat.completions.create (
            model="openai/gpt-oss-120b",
            messages=messages
        )
    return response.choices[0].message.content


main()
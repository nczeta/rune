from groq import Groq

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

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages
    )
    print(response.choices[0].message.content)
    
    messages.append(
        {
            "role": "assistant",
            "content": response.choices[0].message.content
        }
    )




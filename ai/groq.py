import os
from groq import Groq


def ask_groq(prompt):

    client = Groq(
        api_key=os.environ["GROQ_API_KEY"]
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile"
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

import os
from groq import Groq


def ask_groq(prompt, mode="research"):

    client = Groq(
        api_key=os.environ["GROQ_API_KEY"]
    )

    if mode == "fast":
        model = "openai/gpt-oss-20b"
    else:
        model = "openai/gpt-oss-120b"


    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

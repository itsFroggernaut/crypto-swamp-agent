import os
import time
from google import genai


def ask_gemini(prompt):

    client = genai.Client(
        api_key=os.environ["GEMINI_API_KEY"]
    )

    for attempt in range(3):

        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            print(
                f"Gemini attempt {attempt+1} failed:"
            )

            print(e)

            time.sleep(5)

    return "Gemini unavailable after 3 retries."

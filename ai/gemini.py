import os
import google.generativeai as genai


def ask_gemini(prompt):

    genai.configure(
        api_key=os.environ["GEMINI_API_KEY"]
    )

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    response = model.generate_content(
        prompt
    )

    return response.text

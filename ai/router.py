from ai.gemini import ask_gemini
from ai.groq import ask_groq


def ask_ai(prompt, mode="research"):

    if mode == "research":
        return ask_gemini(prompt)

    elif mode == "fast":
        return ask_groq(prompt)

    else:
        return "Unknown AI mode"

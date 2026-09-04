from ai.gemini import ask_gemini
from ai.groq import ask_groq


def ask_ai(prompt, mode="research"):

    if mode == "research":

        result = ask_gemini(prompt)

        if "unavailable" in result.lower():
            return ask_groq(prompt, "research")

        return result


    elif mode == "fast":

        return ask_groq(prompt, "fast")


    else:
        return "Unknown mode"

import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)


def ask_ai(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return f"Sorry, an error occurred: {e}"


if __name__ == "__main__":
    while True:
        question = input("You: ")

        if question.lower() == "exit":
            break

        print("\nJarvis:", ask_ai(question))
import os
from google import genai
from dotenv import load_dotenv



load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)

chat = client.chats.create(model="gemini-3.5-flash")


def ask_ai(prompt: str):

    try:
        response = chat.send_message(prompt)
        return response.text

    except Exception as e:
        return f"Sorry, an error occurred: {e}"
    
    
def new_chat():
    global chat

    chat = client.chats.create(
        model="gemini-2.5-flash"
    )


if __name__ == "__main__":
    while True:
        question = input("You: ")

        if question.lower() == "exit":
            break

        print("\nJarvis:", ask_ai(question))
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
        # Instruct the model on desired output length based on your query
        system_instruction = (
            " Provide a concise, short summary response."
            if "in detail" not in prompt.lower()
            else " Provide a detailed, comprehensive response."
        )

        full_prompt = f"{prompt}\n\n[Instruction: {system_instruction}]"

        response = chat.send_message(full_prompt)
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
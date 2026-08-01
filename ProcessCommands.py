
import webbrowser
import pywhatkit
import time
from news import get_top_news
from Speak import speak


def processCommand(command):
    print(command)
    
    if "open google" in command.lower():
        webbrowser.open("https://www.google.com")
    
    elif "open" in command.lower() or "play" in command.lower():
        pywhatkit.playonyt(command)
    elif "news" in command.lower():
        headlines = get_top_news()

        if not headlines:
            speak("Sorry, I was unable to fetch the news at the moment.")
        else:
            speak("Here are today's top headlines.")
            print("Here are today's top headlines.")

            for i, headline in enumerate(headlines[:5], start=1):
                headline = headline.replace("- BBC News", "").strip()

                print(f"{i}. {headline}")

                speak(f"Headline {i}")

                speak(headline)
                time.sleep(0.3)

            speak("That's all for today's news.")
            print("That's all for today's news.")
            
    elif "search" in command.lower() or ".com" in command.lower():
            webbrowser.open(f"https://www.google.com/search?q={command.lower()}")
            
if __name__=="__main__":
    Running=True
    while Running:
        
        command=input("Enter your Command: ")
        if "bye" in command.lower():
            Running=False
            continue
        processCommand(command)
        
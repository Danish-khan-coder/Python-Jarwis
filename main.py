from news import get_top_news
import speech_recognition as sr
import requests
import webbrowser
import pyttsx3
import pywhatkit
import time


r = sr.Recognizer()





def speak(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        engine.setProperty("rate", 170)#Speaking rate of speaker
    except Exception as e:
        print("Speech Error:", e)
    
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
        
        
    
    
if __name__ == "__main__":
    speak(". Initallizing Jarwis ........")
    running=True
    while running: 
        
        
        print("Recognizing ....")
        try:
            with sr.Microphone() as source:
                print("Listning .....  ")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source ,timeout =5,phrase_time_limit=2)
            
            word = r.recognize_google(audio)
            
            if "jarvis" in word.lower():
                speak("I'm listening.")
                active = True

                while active:
                    with sr.Microphone() as source:
                        print("Listening for command...")

                        r.adjust_for_ambient_noise(source, duration=0.5)

                        audio = r.listen(source,timeout=10,phrase_time_limit=5)

                        command = r.recognize_google(audio, language="en-IN").lower()

                        print(command)
                        processCommand(command)
                
                        if "sleep" in command:
                            speak("Going to sleep.")
                            active = False
                            break
                
            elif "shutdown" in word.lower():
                speak(" Shutting down")
                print("Shutting down......")
                
                running = False
            else:
                print("Sleeping......")
                
                          
        except sr.WaitTimeoutError:
            print("No speech detected.")

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")

        except sr.RequestError as e:
            print("Speech recognition service error:", e)
        
        except requests.exceptions.RequestException as e:
            print(f"Could not connect to the news service: {e}")
            speak("Sorry, I couldn't connect to the news service.")
            
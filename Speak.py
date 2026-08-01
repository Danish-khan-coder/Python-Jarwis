import pyttsx3

def speak(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 170)

        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Speech Error:", e)
if __name__ =="__main__":
    speak("Hello Danish How are you")
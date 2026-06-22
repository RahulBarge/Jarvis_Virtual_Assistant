import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.stop()
    engine.say(text)
    engine.runAndWait()

from llm import ai_res
from text_to_speak import speak
import requests
import webbrowser
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("news_api")



def processcomm(c):
    print(c)
    if "open google" in c.lower():
        print(" Opening Google")
        webbrowser.open("http://google.com")
    elif "open linkedin" in c.lower():
        print(" Opening linkedin")
        webbrowser.open("http://linkedin.com")
    elif "open instagram" in c.lower():
        print(" Opening instagram")
        webbrowser.open("http://instagram.com")
    elif "news" in c.lower():
        url = f"http://api.mediastack.com/v1/news?access_key={API_KEY}&countries=in&languages=en&limit=5"

        response = requests.get(url)
        data = response.json()

        speak("Here are the latest headlines")

        for article in data["data"]:
            title = article["title"]
            print(title)
            speak(title)
    else:
        # Integerate LLM 
        # commands handel by AI
        output = ai_res(c)
        speak(output) 
        
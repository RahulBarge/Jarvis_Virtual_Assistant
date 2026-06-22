import speech_recognition as sr
import webbrowser
import pyttsx3
import sounddevice as sd
import numpy as np
import requests
from listener import listen
import llm
from text_to_speak import speak
from command import processcomm
import news
# from google import genai
# from dotenv import load_dotenv
# import os

# load_dotenv()

# # Initialize text-to-speech engine


# def speak(text):
#     engine = pyttsx3.init()
#     engine.stop()
#     engine.say(text)
#     engine.runAndWait()

# API_KEY = os.getenv("news_api")
# api_key = os.getenv("Google_api")
# client = genai.Client(api_key = api_key)

# def ai_res(que):
#      response = client.models.generate_content_stream(
#         model="gemini-3.5-flash",
#         contents=que
#     )
#      answer = ""

#      for chunk in response:
#             if chunk.text:
#                 print(chunk.text, end="", flush=True)
#                 answer += chunk.text

#      return answer


# def processcomm(c):
#     print(c)
#     if "open google" in c.lower():
#         print(" Opening Google")
#         webbrowser.open("http://google.com")
#     elif "open linkedin" in c.lower():
#         print(" Opening linkedin")
#         webbrowser.open("http://linkedin.com")
#     elif "open instagram" in c.lower():
#         print(" Openin166g instagram")
#         webbrowser.open("http://instagram.com")
#     elif "news" in c.lower():
#         url = f"http://api.mediastack.com/v1/news?access_key={API_KEY}&countries=in&languages=en&limit=5"

#         response = requests.get(url)
#         data = response.json()

#         speak("Here are the latest headlines")

#         for article in data["data"]:
#             title = article["title"]
#             print(title)
#             speak(title)
#     else:
#         # Integerate LLM 
#         # commands handel by AI
#         output = ai_res(c)
#         speak(output) 
        


    

if __name__ == "__main__":
    speak("Hello Rahul ...")
    speak("How canI help I you ")
    
    # # Audio settings
    # sample_rate = 16000  # Sphinx and Google work best with 16000Hz
    # duration = 3     # How many seconds to listen for each command

    while True:
        r = sr.Recognizer()
        print("\nListening....!")
       
        
        # 3. Recognize speech using Google api
        try:
            # # 1. Record audio using sounddevice instead of sr.Microphone()
            # # This records 5 seconds of audio from your default mic
            #  raw_audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
            #  sd.wait()  # Wait until the recording finishes

            # # 2. Convert the raw sounddevice array into a format SpeechRecognition understands
            #  audio_bytes = raw_audio.tobytes()
            #  audio_data = sr.AudioData(audio_bytes, sample_rate, 2)  # 2 means 16-bit audio
             command = listen()
             print("Processing audio...")
            #  command = r.recognize_google(audio_data)
             print(command)

             if(command.lower() == "hi jarvis"):
                  speak(" Yes boss ")
                 #  Listen for command
                  print("jarvis active..")
                #   raw_audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
                #   sd.wait()  # Wait until the recording finishes

                #  # 2. Convert the raw sounddevice array into a format SpeechRecognition understands
                #   audio_bytes = raw_audio.tobytes()
                #   audio_data = sr.AudioData(audio_bytes, sample_rate, 2)  # 2 means 16-bit audio
                #   command = r.recognize_google(audio_data)
                  command = listen()
                  print(command)

                  processcomm(command)

             
        except Exception as e:
            print("Error; {0}".format(e))
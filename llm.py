from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("Google_api")
client = genai.Client(api_key = api_key)
def ai_res(que):
     response = client.models.generate_content_stream(
        model="gemini-3.5-flash",
        contents=que
    )
     answer = ""

     for chunk in response:
            if chunk.text:
                print(chunk.text, end="", flush=True)
                answer += chunk.text

     return answer
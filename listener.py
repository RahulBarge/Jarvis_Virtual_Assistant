import sounddevice as sd
import speech_recognition as sr


# Audio settings
sample_rate = 16000  # Sphinx and Google work best with 16000Hz
duration = 3     # How many seconds to listen for each command
r = sr.Recognizer()
    # 3. Recognize speech using Google api
def listen():
            # 1. Record audio using sounddevice instead of sr.Microphone()
            # This records 5 seconds of audio from your default mic
             raw_audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
             sd.wait()  # Wait until the recording finishes

            # 2. Convert the raw sounddevice array into a format SpeechRecognition understands
             audio_bytes = raw_audio.tobytes()
             audio_data = sr.AudioData(audio_bytes, sample_rate, 2)  # 2 means 16-bit audio
             command = r.recognize_google(audio_data)
             return command            

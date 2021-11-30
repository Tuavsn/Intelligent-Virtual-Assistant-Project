import pyttsx3
import speech_recognition
ear=speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("say something :)")
    audio = ear.listen(mic)
try:
    you = ear.recognize_google(audio)
except:
    you = "what"
engine=pyttsx3.init()
engine.say(you)
engine.runAndWait()
import pyttsx3
import speech_recognition
ear=speech_recognition.Recognizer()
engine=pyttsx3.init()
while True:
    with speech_recognition.Microphone() as mic:
        print("say something :)")
        audio = ear.listen(mic)
    try:
        you = ear.recognize_google(audio)
    except:
        robot = "what"
    if you=="hello":
        robot="hello sir"
    elif you=="goodbye":
        robot="goodbye Tuan"
        engine.say(robot)
        engine.runAndWait()
        break
    engine.say(robot)
    engine.runAndWait()
    
    '''
    công thức tính 1 giá trị ngẫu nhiên :
    ngẫu_nhiên = 15
    ngẫu_nhiên = (ngẫu_nhiên * 8 + 4) % 11
  
    '''

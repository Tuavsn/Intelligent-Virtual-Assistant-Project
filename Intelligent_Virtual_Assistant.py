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
    làm Game đi làm Game tốt cho sức khỏe đặc biệt là người già trẻ nhỏ
    '''

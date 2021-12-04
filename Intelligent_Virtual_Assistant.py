#-----------IMPORTANT!!!! => YÊU CẦU:   -----------------#
# MỞ TERMINAL =>    pip install pywin32
#                   pip install pyttsx3
#                   pip install speechrecognition
#                   pip install pipwin
#                   pipwin install pyaudio

#---------------------------//------------------------------#
#-----------------IMPORT THƯ VIỆN--------------------#
import pyttsx3                                  # THƯ VIỆN NÓI
from gtts import gTTS
from playsound import playsound
import os
import time
import speech_recognition                       # THƯ VIỆN NHẬN DIỆN GIỌNG NÓI
from datetime import date, datetime             # THƯ VIỆN NGÀY THÁNG
#----------------ASSISTANT MACHINE-------------------#
# KHỞI TẠO
ai_brain = ' '
ai_ear = speech_recognition.Recognizer()        
ai_mouth = pyttsx3.init()              
voice=ai_mouth.getProperty('voices')
ai_mouth.setProperty('voice',voice[1].id)       # Thiết lập giọng nữ cho AI ( voice[0]: giọng nam )
#------------------ASSISTANT FUNCTION------------------#
def ai_listen_in_Vietnamese():
    with speech_recognition.Microphone() as mic:                                 
        print("AI: AI đang nghe")
        audio = ai_ear.record(mic, duration=3)      # Ai lắng nghe giọng nói của bạn qua microphone rồi lưu vào biến audio
        print("AI: .....")
    try:
        your_query=ai_ear.recognize_google(audio,language='vi-VN')    #Ai nhận diện giọng nói của bạn thông qua biến audio
    except:
        speak_v('Oops!, Tôi không thể nghe được yêu cầu của bạn, bạn có thể nói lại được không?')
        your_query=''
    return your_query

def speak_v(audio):
    tts = gTTS(text=audio, lang='vi',slow=False)
    filename = 'voice.mp3'
    tts.save(filename)
    print(audio)
    playsound(filename)
    os.remove(filename)

def speak(audio):
    print('AI: '+audio)
    ai_mouth.say(audio)
    ai_mouth.runAndWait()

def gio():
    h = str(datetime.now().hour)
    p = str(datetime.now().minute)
    Time='bây giờ là '+h+' giờ '+p+' phút'
    speak_v(Time)

def time():
    Time = datetime.now().strftime('%I:%M:%p')
    speak(Time)

def welcome():
    hour=datetime.now().hour
    if hour >=1 and hour < 6:
        speak_v('Xin chào')
        speak_v("Tôi có thể giúp gì được cho bạn") 
    elif hour >= 6 and hour < 12:
        speak_v('Chào buổi sáng')
        speak_v("Tôi có thể giúp gì được cho bạn") 
    elif hour >= 12 and hour < 18:
        speak_v('Chào bạn')
        speak_v("Tôi có thể giúp gì được cho bạn") 
    elif hour >= 18 and hour < 24:
        speak_v('Chào buổi tối')
        speak_v("Tôi có thể giúp gì được cho bạn") 
#------------------MAIN()-----------------------------#
if __name__ == '__main__':
    start_button=str(input())
    if start_button=="start":                         # XỬ LÝ TIẾNG VIỆT
            welcome()
            while True:
                query = ai_listen_in_Vietnamese().lower()
                if 'chào' in query:
                    speak_v('Chào bạn')
                elif 'bây giờ là mấy giờ' in query:
                    gio()
                elif 'tạm biệt' in query:
                    speak_v('Tạm biệt bạn')
                    break
                if 'hello' in query:
                    speak('Hello sir')
                elif 'time' in query:
                    time()
                elif 'goodbye' in query:
                    speak('Goodbye sir')
                    break 



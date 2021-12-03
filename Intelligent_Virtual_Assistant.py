#-----------IMPORTANT!!!! => YÊU CẦU:   -----------------#
# MỞ TERMINAL =>    pip install pywin32
#                   pip install pyttsx3
#                   pip install speechrecognition
#                   pip install pipwin
#                   pipwin install pyaudio

#---------------------------//------------------------------#
#-----------------IMPORT THƯ VIỆN--------------------#
import pyttsx3                                  # THƯ VIỆN NÓI
import speech_recognition                       # THƯ VIỆN NHẬN DIỆN GIỌNG NÓI
from datetime import date, datetime             # THƯ VIỆN NGÀY THÁNG
#----------------ASSISTANT MACHINE-------------------#
# KHỞI TẠO
ai_brain = ' '
ai_ear = speech_recognition.Recognizer()        
ai_mouth = pyttsx3.init()              
voice=ai_mouth.getProperty('voices')
ai_mouth.setProperty('voice',voice[1].id)       # Thiết lập giọng nữ cho AI ( voice[0]: giọng nam )
#------------------ASSISTANT METHOD------------------#
def start_ai():
    with speech_recognition.Microphone() as mic:
        print("Hello sir :\"> ")                    
        print("How can I help you?")                
        ai_ear.adjust_for_ambient_noise(mic)        # Giảm tiếng ồn cho microphone
        audio = ai_ear.record(mic, duration=3)      # Ai lắng nghe giọng nói của bạn qua microphone rồi lưu vào biến audio
        print("\nAi: ...")
    try:
        your_input = ai_ear.recognize_google(audio, language='vi-VN')    #Ai nhận diện giọng nói của bạn thông qua biến audio
    except:
        print('Oops!, Something wrong :"<, you can type your input here:\n')
        your_input=str(input("Your input: "))
    return your_input
#------------------MAIN()-----------------------------#
if __name__ == '__main__':
    start_button=str(input())
    if start_button=="start":
        start_ai()

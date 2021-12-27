#-----------IMPORTANT!!!! => YÊU CẦU:   -----------------#
# MỞ TERMINAL =>    pip install pywin32
#                   pip install pyttsx3
#                   pip install speechrecognition
#                   pip install pipwin
#                   pipwin install pyaudio
#                   pip install gTTS
#                   pip install playsound
#---------------------------//------------------------------#
#-----------------IMPORT THƯ VIỆN--------------------#
from math import e
import runpy
import pyttsx3                                  # THƯ VIỆN NÓI
from gtts import gTTS
from playsound import playsound                 # THƯ VIỆN CHẠY NHẠC
import os                                       # THƯ VIỆN MỞ ĐÓNG FILE
from time import sleep
import speech_recognition                       # THƯ VIỆN NHẬN DIỆN GIỌNG NÓI
from datetime import date, datetime             # THƯ VIỆN NGÀY THÁNG
import webbrowser                               # THƯ VIỆN BROWSER
#----------------ASSISTANT MACHINE-------------------#
# KHỞI TẠO
ai_ear = speech_recognition.Recognizer()        
ai_mouth = pyttsx3.init()              
voice=ai_mouth.getProperty('voices')
ai_mouth.setProperty('voice',voice[1].id)                             # Thiết lập giọng nữ cho AI ( voice[0]: giọng nam )
#------------------ASSISTANT FUNCTION------------------#

def ai_listen():
    with speech_recognition.Microphone() as mic:                                 
        print("AI: AI đang nghe")
        ai_ear.dynamic_energy_threshold = 3000
        audio = ai_ear.record(mic,duration=3)                                    # Ai lắng nghe giọng nói của bạn qua microphone rồi lưu vào biến audio
        print("AI: .....")
    try:
        your_query=ai_ear.recognize_google(audio, language='vi-VN')    #Ai nhận diện giọng nói của bạn thông qua biến audio
    except:
        speak_v('xin lỗi tôi không nghe được bạn nói')
        your_query=''
    return your_query.lower()

def ai_wake():
    while True:
        with speech_recognition.Microphone() as mic:
            ai_ear.dynamic_energy_threshold = 4000
            audio = ai_ear.record(mic, duration=5)
        try:
            speech_as_text = ai_ear.recognize_google(audio)
            if "assistant" or "hey assistant" in speech_as_text:
                speak_v("tôi có thể giúp gì cho bạn")
                break
            else:
                pass
        except speech_recognition.WaitTimeoutError:
            pass
        except speech_recognition.UnknownValueError:
            pass
        except speech_recognition.RequestError:
            print("Network error.")

def speak_v(audio):
    tts = gTTS(text=audio, lang='vi',slow=False)
    filename = 'voice.mp3'
    tts.save(filename)
    print('AI: '+audio)
    playsound(filename)
    os.remove(filename)

def speak(audio):
    print('AI: '+audio)
    ai_mouth.say(audio)
    ai_mouth.runAndWait()

def ngay():
    day = str(date.today().day)
    month = str(date.today().month)
    year = str(date.today().year)
    today = 'hôm nay là ngày '+day+' tháng '+month+' năm '+year
    speak_v(today)

def gio():
    h = str(datetime.now().hour)
    p = str(datetime.now().minute)
    Time='bây giờ là '+h+' giờ '+p+' phút'
    speak_v(Time)

def day():
    today = date.today().strftime('today is %d, %b %Y')
    speak(today)

def time():
    Time = datetime.now().strftime('%I:%M:%p')
    speak(Time)

def youtube_search():
    speak_v('Bạn muốn xem gì?')
    while True:
        search_for = ai_listen()
        if search_for:
            domain = search_for
            break
    url = 'https://www.youtube.com/results?search_query='+domain
    webbrowser.open(url)
    speak_v("Bạn đang tìm kiếm video trên Youtube.")

def open_website():
    speak_v('nhập website mà bạn muốn truy cập')
    website = str(input('nhập website bạn muốn truy cập: https://www.'))
    domain = website
    url = 'https://www.' + domain
    webbrowser.open(url)
    speak_v("Trang web bạn yêu cầu đã được mở.")

def google_search():
    speak_v('Bạn muốn tìm kiếm gì trên google')
    while True:
        search_for = ai_listen()
        if search_for:
            domain = search_for
            break
    speak_v('Đang trả về kết quả tìm kiếm')
    url="https://www.google.com/search?q="+domain
    webbrowser.open(url) 

# def play_game():
#     import importturtle
#     importturtle.thread.stop()

def welcome():
    hour=datetime.now().hour
    if hour >=1 and hour < 6:
        speak_v('Xin chào')
        speak_v('bạn vẫn còn thức sao')
        speak_v("Hãy gọi tôi khi bạn cần") 
    elif hour >= 6 and hour < 12:
        speak_v('Chào buổi sáng')
        speak_v("Hãy gọi tôi khi bạn cần")
    elif hour >= 12 and hour < 18:
        speak_v('Chào bạn')
        speak_v("Hãy gọi tôi khi bạn cần") 
    elif hour >= 18 and hour < 24:
        speak_v('Chào buổi tối')
        speak_v("Hãy gọi tôi khi bạn cần")
    print('------------------------------------------------')
    print("Gọi tôi bằng lệnh: Assistant hoặc Hey Assistant")
    print('--------------//---------------')
    print('''Một số chức năng cơ bản:
        1. Thông báo ngày, giờ.
        2. Tìm kiếm trên youtube, google.
        3. Truy cập website.
        4. Trò chơi rắn săn mồi.
    ''')
    print('--------------//---------------')

#------------------MAIN()-----------------------------#
if __name__ == '__main__':                                 
    welcome()
    while True:
        ai_wake()
        query = ai_listen()
        if 'chào' in query:
            speak_v('Chào bạn')
        elif 'hello' in query:
            speak('Hello sir')
        elif 'hôm nay là ngày' in query:
            ngay()
        elif 'bây giờ là mấy giờ' in query:
            gio()
        elif 'what is today' in query:
            day()
        elif 'time' in query:
            time()
        elif 'youtube' in query:
            youtube_search()
        elif 'website' in query:
            open_website()
        elif 'google' in query:
            google_search()
        elif 'à thế à' in query:
            speak_v('À thế làm sao mà à')
        elif 'tạm biệt' in query:
            speak_v('Tạm biệt bạn')
            exit()
        elif 'goodbye' in query:
            speak('Goodbye sir')
            exit()

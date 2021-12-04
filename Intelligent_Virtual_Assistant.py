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
from playsound import playsound                 # THƯ VIỆN CHẠY NHẠC
import os                                       # THƯ VIỆN MỞ ĐÓNG FILE
import time
import speech_recognition                       # THƯ VIỆN NHẬN DIỆN GIỌNG NÓI
from datetime import date, datetime             # THƯ VIỆN NGÀY THÁNG
import webbrowser                               # THƯ VIỆN BROWSER
#----------------ASSISTANT MACHINE-------------------#
# KHỞI TẠO
ai_brain = ' '
ai_ear = speech_recognition.Recognizer()        
ai_mouth = pyttsx3.init()              
voice=ai_mouth.getProperty('voices')
ai_mouth.setProperty('voice',voice[1].id)                             # Thiết lập giọng nữ cho AI ( voice[0]: giọng nam )
#------------------ASSISTANT FUNCTION------------------#
def ai_listen():
    with speech_recognition.Microphone() as mic:                                 
        print("AI: AI đang nghe")
        audio = ai_ear.listen(mic)                                    # Ai lắng nghe giọng nói của bạn qua microphone rồi lưu vào biến audio
        print("AI: .....")
    try:
        your_query=ai_ear.recognize_google(audio,language='vi-VN')    #Ai nhận diện giọng nói của bạn thông qua biến audio
    except:
        speak_v('Oops!, bạn có thể nói lại được không?')
        your_query=''
    return your_query

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
        if result:
            domain = search_for
            break
    url = 'https://www.youtube.com/results?search_query='+domain
    webbrowser.open(url)
    speak_v("Bạn đang tìm kiếm video trên Youtube.")

def open_website():
    speak_v('nhập website mà bạn muốn truy cập')
    website = str(input('nhập website bạn muốn truy cập (phải thêm .com or ...): '))
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
    speak('Đang trả về kết quả tìm kiếm')
    url="https://www.google.com/search?q="+domain
    webbrowser.open(url)

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
    if start_button=="start":                                   
            welcome()
            while True:
                query = ai_listen().lower()
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
                    break
                elif 'goodbye' in query:
                    speak('Goodbye sir')
                    break



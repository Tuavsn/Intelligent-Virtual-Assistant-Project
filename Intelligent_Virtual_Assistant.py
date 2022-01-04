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
from pynput.keyboard import Key, Controller
import subprocess 
import requests                  
from gtts import gTTS                           # THƯ VIỆN NÓI
from playsound import playsound                 # THƯ VIỆN CHẠY NHẠC
import os                                       # THƯ VIỆN MỞ ĐÓNG FILE
from time import sleep
import speech_recognition                       # THƯ VIỆN NHẬN DIỆN GIỌNG NÓI
from datetime import date, datetime             # THƯ VIỆN NGÀY THÁNG
import webbrowser                               # THƯ VIỆN BROWSER
#----------------ASSISTANT MACHINE-------------------#
# KHỞI TẠO
ai_ear = speech_recognition.Recognizer() 
wake_up_keywords = [ ("assistant"), ("wake up"), ("tôi cần hỗ trợ"), ("trợ lý ảo") ]   
#------------------ASSISTANT FUNCTION------------------#
def ai_wake():
    while True:
        with speech_recognition.Microphone() as mic:
            ai_ear.dynamic_energy_threshold = 4000
            audio = ai_ear.record(mic, duration=4)
        try:
            speech_as_text = ai_ear.recognize_google(audio, language='vi-VN').lower()
            if  speech_as_text in wake_up_keywords:
                speak_v("Tôi có thể giúp gì cho bạn")
                break
            else:
                pass
        except speech_recognition.WaitTimeoutError:
            pass
        except speech_recognition.UnknownValueError:
            pass
        except speech_recognition.RequestError:
            print("Network error.")

def ai_listen():
    with speech_recognition.Microphone() as mic:                                 
        print("Assistant: Tôi đang nghe")
        ai_ear.dynamic_energy_threshold = 4000
        audio = ai_ear.record(mic,duration=4)                                   
        print("Assistant: .....")
    try:
        your_query=ai_ear.recognize_google(audio, language='vi-VN')  
    except:
        your_query=''
    return your_query.lower()

def speak_v(audio):
    tts = gTTS(text=audio, lang='vi',slow=False)
    filename = 'voice.mp3'
    tts.save(filename)
    print('AI: '+audio)
    playsound(filename)
    os.remove(filename)

def speak(audio):
    tts = gTTS(text=audio, lang='en',slow=False)
    filename = 'voice.mp3'
    tts.save(filename)
    print('AI: '+audio)
    playsound(filename)
    os.remove(filename)

def open_app(app_name):
    try: 
        subprocess.Popen('C:\\Windows\\System32\\'+app_name[5:]+'.exe')
    except: 
        pass

def switchTab():
    Controller().press(Key.ctrl)
    Controller().press(Key.tab)
    Controller().release(Key.tab)
    Controller().release(Key.ctrl)

def closeTab():
    Controller().press(Key.ctrl)
    Controller().press('w')
    Controller().release('w')
    Controller().release(Key.ctrl)

def newTab():
    Controller().press(Key.ctrl)
    Controller().press('n')
    Controller().release('n')
    Controller().release(Key.ctrl)

def close_window():
    Controller().press(Key.alt_l)
    Controller().press(Key.f4)
    Controller().release(Key.f4)
    Controller().release(Key.alt_l)

def minimizeWindow():
    Controller().press(Key.cmd)
    Controller().press(Key.down)
    Controller().release(Key.down)
    Controller().release(Key.cmd)

def maximizeWindow():
    Controller().press(Key.cmd)
    Controller().press(Key.up)
    Controller().release(Key.up)
    Controller().release(Key.cmd)

def ngay():
    day = str(date.today().day)
    month = str(date.today().month)
    year = str(date.today().year)
    today = 'Hôm nay là ngày '+day+' tháng '+month+' năm '+year
    speak_v(today)

def gio():
    h = str(datetime.now().hour)
    p = str(datetime.now().minute)
    Time='Bây giờ là '+h+' giờ '+p+' phút'
    speak_v(Time)

def day():
    today = date.today().strftime('today is %d, %b %Y')
    speak(today)

def time():
    Time = datetime.now().strftime('%I:%M:%p')
    speak(Time)

def open_google_chrome():
    url='https://www.google.com'
    webbrowser.open(url)

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
    speak_v('Nhập website mà bạn muốn truy cập')
    website = str(input('Nhập website bạn muốn truy cập: https://www.'))
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

def open_facebook():
    url='https://www.facebook.com'
    webbrowser.open(url)
    speak_v("đã truy cập facebook")

def open_instagram():
    url='https://www.instagram.com/'  
    webbrowser.open(url) 
    speak_v("đã truy cập instagram")

def thoi_tiet():
    api_address='http://api.openweathermap.org/data/2.5/weather?q=bienhoa&appid=cee343d33e41970dd63c44b39c8620ab'
    json_data = requests.get(api_address).json()
    format_add = json_data['main']
    speak_v("Nhiệt độ trung bình là {0} Độ C, Nhiệt độ thấp nhất là {1} Độ C, Nhiệt độ cao nhất là {2} Độ C".format(
        json_data['weather'][0]['main'],int(format_add['temp_min']-273),int(format_add['temp_max']-273)))

def weather():
    api_address='http://api.openweathermap.org/data/2.5/weather?q=bienhoa&appid=cee343d33e41970dd63c44b39c8620ab'
    json_data = requests.get(api_address).json()
    format_add = json_data['main']
    speak("Average temperature is {0} Celsius, Min temperature is {1} Celsius, Max temperature is {2} Celsius".format(
        json_data['weather'][0]['main'],int(format_add['temp_min']-273),int(format_add['temp_max']-273)))

# def play_game():
#     import importturtle
#     importturtle.thread.stop()

def welcome():
    hour=datetime.now().hour
    if hour >=1 and hour < 6:
        speak_v('Xin chào')
        speak_v('Bạn vẫn còn thức sao')
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
    print("Gọi tôi bằng những lệnh sau: 'Wake up', 'Assistant', 'Tôi cần hỗ trợ', 'Trợ lý ảo'")
    print('--------------//---------------')
    print('''Một số chức năng cơ bản:
        1. Thông báo ngày, giờ.
        2. Tìm kiếm trên youtube, google.
        3. Truy cập website, google chrome.
        4. Phóng lớn, thu nhỏ và đóng cửa sổ window.
        5. Đóng, chuyển và mở tab mới.
        6. Tuy cập facebook, instagram.
        7. thông báo thời tiết
        8. Mở Pain, Calculator (Nếu máy của bạn có đường dẫn C->windows->system32)
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
        # elif 'thông tin của bạn':
        #     assistant_information_v()
        # elif 'your information':
        #     assistant_information()
        elif 'paint' in query:
            open_app('mspaint')
            speak('Paint was opened')
        elif 'calculator' in query:
            open_app('calc')
            speak('Calculator was opened')
        elif 'đóng cửa sổ' in query:
            close_window()
        elif 'thu nhỏ cửa sổ' in query:
            minimizeWindow()
        elif 'phóng to cửa sổ' in query:
            maximizeWindow()
        elif 'close window' in query:
            close_window()
        elif 'minimize window' in query:
            minimizeWindow()
        elif 'maximize window' in query:
            maximizeWindow()
        elif 'đóng tab' in query:
            closeTab()
        elif 'tab mới' in query:
            newTab()
        elif 'chuyển tab' in query:
            switchTab()
        elif 'close tab' in query:
            closeTab()
        elif 'new tab' in query:
            newTab()
        elif 'switch tab' in query:
            switchTab()
        elif 'hôm nay là ngày' in query:
            ngay()
        elif 'bây giờ là mấy giờ' in query:
            gio()
        elif 'what is today' in query:
            day()
        elif 'time' in query:
            time()
        elif 'google chrome' in query:
            open_google_chrome()
        elif 'youtube' in query:
            youtube_search()
        elif 'google' in query:
            google_search()
        elif 'facebook' in query:
            open_facebook()
        elif 'instagram' in query:
            open_instagram()
        elif 'website' in query:
            open_website()
        elif 'à thế à' in query:
            speak_v('À thế làm sao mà à')
        elif 'thời tiết' in query:
            thoi_tiet()
        elif 'weather' in query:
            weather()
        elif 'you are so intelligent' in query:
            speak('Haha thank you very much, I love it')
        elif 'you are so beautiful' in query:
            speak('Yeah, I know')
        elif 'tạm biệt' in query:
            speak_v('Tạm biệt bạn')
            speak_v('Chúc bạn có một ngày may mắn và thành công')
            break
        elif 'see you later' in query:
            speak('Goodbye sir')
            speak('Have a great day')
            break
        else:
            speak_v('xin lỗi tôi không nghe được bạn nói')

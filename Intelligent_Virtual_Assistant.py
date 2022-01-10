#-----------------IMPORT THƯ VIỆN--------------------#     
from re import S
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
        speak('Xin lỗi, tôi không thể nghe được bạn nói')
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
# ---------------------------------//-----------------------------------//----------------
def clear_screen():
    os.system('cls')

def open_calculator():
    try: 
        subprocess.Popen('C:\\Windows\\System32\\'+'calc'+'.exe')
    except: 
        print('có vẻ devC không nằm trong chỉ mục C:\Program Files (x86)\Dev-Cpp\ ')

def open_devC():
    try: 
        subprocess.Popen('C:\\Program Files (x86)\\Dev-Cpp\\'+'devcpp'+'.exe')
    except: 
        print('có vẻ devC không nằm trong chỉ mục C:\Program Files (x86)\ ')

def open_google_chrome():
    try: 
        subprocess.Popen('C:\\Program Files\\Google\\Chrome\\Application\\'+'chrome'+'.exe')
    except: 
        print('có vẻ Chrome không nằm trong chỉ mục C:\Program Files\Google\Chrome\Application ')

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
    Controller().press('t')
    Controller().release('t')
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
    weather = json_data['weather'][0]['main']
    if weather == 'Clouds':
        weather = 'nhiều mây'
    elif weather == 'Rainy':
        weather = 'có mưa'
    speak_v("Trời thì {0} và nhiệt độ hôm nay là {1} độ C".format(
        weather,int(format_add['temp']-273)))

def weather():
    api_address='http://api.openweathermap.org/data/2.5/weather?q=bienhoa&appid=cee343d33e41970dd63c44b39c8620ab'
    json_data = requests.get(api_address).json()
    format_add = json_data['main']
    speak("It's {0} and the temperature is {1} Celcious".format(
        json_data['weather'][0]['main'],int(format_add['temp']-273)))

def play_game():
    import importturtle
    importturtle.thread.stop()

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

def func_list():
    print('--------------//---------------')
    print('''Một số chức năng cơ bản:
        1. Thông báo ngày, giờ.
        2. Tìm kiếm trên youtube, google.
        3. Truy cập website, google chrome.
        4. Phóng lớn, thu nhỏ và đóng cửa sổ window.
        5. Đóng, chuyển và mở tab mới.
        6. Tuy cập facebook, instagram.
        7. thông báo thời tiết.
        8. Mở devC (lệnh: 'lập trình' hoặc 'programming'), mở máy tính (Calculator).
        9. Trò chơi.
        *Gọi lệnh 'xóa màn hình' hoặc 'clear' để xóa màn hình cmd.
    ''')
    print('--------------//---------------')

#------------------MAIN()-----------------------------#
if __name__ == '__main__':                                 
    welcome()
    while True:
        ai_wake()
        func_list()
        query = ai_listen()
        if 'chào' in query:
            speak_v('Chào bạn')
        elif 'hello' in query:
            speak('Hello Sir')
        elif 'chào buổi sáng' in query:
            speak_v('Chào bạn')
        elif 'chào buổi tối' in query:
            speak_v('Chào bạn')
        elif 'good morning' in query:
            speak('Good morning Sir')
        elif 'good afternoon' in query:
            speak('Good afternoon Sir')
        elif 'good evening' in query:
            speak('Good evening Sir')
        elif 'tên của bạn' in query:
            speak_v('Tôi vẫn chưa có tên, bạn có thể gọi tôi là trợ lý ảo')
        elif 'your name' in query:
            speak("I don't have a name, you can call me Assistant")
        elif 'máy tính' in query:
            open_calculator()
            speak_v('máy tính đã được mở')
        elif 'calculator' in query:
            open_calculator()
            speak('Calculator was opened')
        elif 'lập trình' in query:
            open_devC()
            speak('devC was opened')
        elif 'programming' in query:
            open_devC()
            speak('devC was opened')
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
        elif 'trò chơi' in query:
            play_game()
        elif 'game' in query:
            play_game()
        elif 'à thế à' in query:
            speak_v('À thế làm sao mà à')
        elif 'thời tiết' in query:
            thoi_tiet()
        elif 'weather' in query:
            weather()
        elif 'xóa màn hình' in query:
            clear_screen()
            func_list()
        elif 'clear' in query:
            clear_screen()
            func_list()
        elif 'you are so intelligent' in query:
            speak('Haha thank you very much, I love it')
        elif 'you are so beautiful' in query:
            speak('Yeah, I know')
        elif 'chức năng' in query:
            func_list()
        elif 'help' in query:
            func_list()
        elif 'thank you' in query:
            speak('You are welcome')
        elif 'tạm biệt' in query:
            speak_v('Tạm biệt bạn')
            speak_v('Chúc bạn có một ngày may mắn và thành công')
            break
        elif 'see you later' in query:
            speak('Goodbye sir')
            speak('Have a great day')
            break
        else:
            speak_v('Tôi vẫn chưa có chức năng này')

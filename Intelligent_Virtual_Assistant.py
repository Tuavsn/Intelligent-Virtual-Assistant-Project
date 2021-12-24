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
'''
import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game @TokyoEdTech")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
'''

#-----------IMPORTANT!!!! => YÊU CẦU:   -----------------#
# MỞ TERMINAL =>    pip install pywin32
#                   pip install pyttsx3
#                   pip install speechrecognition
#                   pip install pipwin
#                   pipwin install pyaudio

#---------------------------//------------------------------#
import pyttsx3  #THƯ VIỆN NÓI
import speech_recognition #THƯ VIỆN NHẬN DIỆN GIỌNG NÓI

ear=speech_recognition.Recognizer()
engine=pyttsx3.init() #TẠO OBJECT ENGINE
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)
while True:
    with speech_recognition.Microphone() as mic:
        print("say something :)")
        audio = ear.listen(mic)
    try:
        you = ear.recognize_google(audio)
    except speech_recognition.UnknownValueError:
        robot = "what"
    if "goodbye" in you:
        robot="goodbye Tuan"
        engine.say(robot)
        print(robot)
        engine.runAndWait()
        break
    elif "hello" in you:
        print("""                                                                                       
        @@@    @@@
        @@@    @@@   @@@
        @@@@@&@@@@   @@@
        @@@    @@@   @@@                @
        @@@    @@@   @@@       &@@@@@@@%@
                            @@@@@@ @@@@  @ @ @
                            %@@@@@ @@ @@  @@@@
                            @@&@@@@@@@@@@@@@
                            @@@@@@@@@@@@@@@@                   
                    @    @@@ @@@@@ @@@ @@@ @   @             
                    @@  @@@@ @@&@@ @@@ @@@ @@ @@             
                    @@     @@ @@@&@ @@@ @@@      @@           
                            @@ @@@@@ @@@ @@@                  
                @@        @@ @@@@@ @@@ @@@        @@@        
                    @@@ @@@@@@@@@@@@@@@@&@  @ @@@           
                        @@ @@@@@@@@@@@@@@@@  @                
                                &%       &                      
                                @@       @                      
                            @@@      @@@&                  
                            @@@@@@@  @@@@@@@                   
                """)
        robot="hello sir"
    print(robot)
    engine.say(robot)
    engine.runAndWait()

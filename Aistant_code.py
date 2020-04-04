import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

i=0
emails ={"Rajat": "rajatreigns@gmail.com","Vaibhav": "vniranjan26@gmail.com","Rishabh": "rishabhgupta4999@gmail.com"}
z="Not Found"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Edith my friend. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aiprojectdemo26@gmail.com', 'Ai@k18sp')
    server.sendmail('aiprojectdemo26@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("youtube is opeing............")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("google is opeing............")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("stack overflow is opeing............")

        elif 'open u m s' in query:
            webbrowser.open("ums.lpu.in/lpuums/")   
            speak("university management system is opeing............")


        elif 'play music' in query:
            music_dir = 'D:\Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[i]))
            i=i+1
            speak("opeing music directory......")

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\Program Files\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'stop' in query:
            speak('stop in 3   2    1...')
            break
        
        elif 'send a email' in query:
            try:
                speak("To whom you want to send email ?")
                try:
                    per = takeCommand()
                    to = emails.get(per,z)
                    if (to==z):
                        speak("I did't have addresss of ")
                        speak(per)
                        speak("in our data base")
                    else :
                        speak("What should I say?")
                        content = takeCommand()    
                        sendEmail(to, content)
                        speak("Email has been sent!")
                        print("Email has been sent!")
                    
                except Exception as e:
                    print(e)
                    
            except Exception as e:
                print(e)
                speak("Sorry my friend vaibhav. I am not able to send this email")
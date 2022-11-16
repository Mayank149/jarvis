# importing libraries
from ast import Pass
import datetime
import pyttsx3
import random
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# setting the voice of the engine
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

# defining speak function to convert texts into speech by AI
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Making a function to wish the user as soon as it runs
def wishMe():
    hour = int(datetime.datetime.now().hour) # taking the current time in 24 hours format from api
    n = random.randint(1,3)
    
    if hour<12:
        speak("Good Morning Mayank sir!")
        print("Good Morning Mayank sir!")

        if n ==3:
            speak("Hope you had a Fantastic Morning")
            print("Hope you had a Fantastic Morning")


    elif hour<16:
        speak("Good afternoon Mayank sir!")
        print("Good afternoon Mayank sir!")

        if n ==3:
            speak("Hope you are still full of energy for the rest of your day")
            print("Hope you are still full of energy for the rest of your day")

    else:
        speak("Good evening Mayank sir!")
        print("Good evening Mayank sir!")

        if n ==3:
            speak("I just hope you are not feeling sleepy already.")
            print("I just hope you are not feeling sleepy already.")

def intro():

    intro = random.randint(1,5) # Picking a random intro for fun :P

    if intro == 4:
        speak("i am jarvis, how may i help you today")
        print("i am jarvis, how may i help you today")
    elif intro == 5:
        speak("I am your butler, want some tea and biscuits?")
        print("I am your butler, want some tea and biscuits?")

def takeCommand():
    #takes microphone input from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # listing for user audio with user mic as source
        print("Listning......")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language="en-in") # converting user audio to text by google engine
        print(f"user said: {query}")

    except Exception as e:
        # Print error if the listning fails
        # print(e)
        print("I didn't get it. Can you please repeat")
        speak("I didn't get it. Can you please repeat")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    intro()
    while True:
        query = takeCommand().lower() # converting query to lowercase
        # Logics of responding to user commands by taking them from query
        
        if 'wikipedia' in query: # program to search anything from wikipedia
            print("searching Wiki.....")
            speak("searching Wiki.....")

            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wekipedia")
            print(results)
            speak(results)
            
        #greeting the user if he says hello, hi    
        elif 'hello' in query:
            print("Hello there. Glad to meet you")
            speak("Hello there. Glad to meet you")
        
        elif 'hi' in query:
            print("Hello there. Glad to meet you")
            speak("Hello there. Glad to meet you")

        # responding if user asks how are you
        elif 'how are you' in query:
            print("Great, Thanks for asking")
            speak("Great, Thanks for asking")
        
        # Programs to open websites in browser
        elif 'open youtube' in query: # program to open youtube
            print("Opening youtube in browser......")
            speak("Opening youtube in browser......")
            webbrowser.open("youtube.com")
            break
        elif 'open google' in query: # program to open google
            print("Opening google in browser......")
            speak("Opening google in browser......")
            webbrowser.open("google.com")
            break
        elif 'open amazon' in query: # program to open amazon
            print("Opening amazon in browser......")
            speak("Opening amazon in browser......")
            webbrowser.open("amazon.in")
            break
        elif 'open flipkart' in query: # program to open flipcart
            print("Opening flipkart in browser......")
            speak("Opening flipkart in browser......")
            webbrowser.open("flipkart.com")
            break
        elif 'open hotstar' in query: # program to open hotstar
            print("Opening hotstar in browser......")
            speak("Opening hotstar in browser......")
            webbrowser.open("hotstar.com")
            break
        elif 'open instagram' in query: # program to open instagram
            print("Opening instagram in browser......")
            speak("Opening instagram in browser......")
            webbrowser.open("instagram.com")
            break
        
        #playing music
        elif 'play music' in query:
           
            print("playing some beats.....")
            speak("playing some beats.....")
            music_dir = "C:\\Users\\Admin\\Music"
            songs = os.listdir(music_dir)
            #print(songs)
            limit = len(songs)-1
            n = random.randint(1,limit)
            os.startfile(os.path.join(music_dir,songs[n]))
            break

        elif 'open file explorer' in query:
            print("opening File Explorer")
            speak("opening File Explorer")
            os.startfile("Explorer")
            break

        
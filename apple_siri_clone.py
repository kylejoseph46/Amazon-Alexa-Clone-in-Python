#Includes
import pyttsx3
import speech_recognition as sr
import wikipedia
import random
import time
import os


#Setting up Voice and Listening 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def command():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening... waiting for voice")
            audio = r.listen(source)
            try:
                command = r.recognize_google(audio)
                print(f"kyle:{command}")
                return command
                break
            except:
                print("Try Again")


while True:
    #uses command as voice input
    command = command().lower()  

    if 'kyle' in command:
        speak("How can I help you?")
    elif 'how old are you' in command:
        selection = ['I am ageless', 'You will never find out']
        speak(random.choice(selection))
    elif 'I love you' in command:
        speak('I dont know what you mean I cant experience emotion')


    ### Play music
    elif 'play music' in command:
        music_directory = 'C:\\Users\kylej\Music'  # Insert your own music directory.
        songs = os.listdir(music_directory)
        song = random.randint(0, len(songs)-1)
        print(songs[song])
        speak(f"playing{songs[song]}")
        os.startfile(os.path.join(music_directory, songs[0]))


    ### Ask the time
    elif 'what is the time' in command:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        speak("It's" + current_time)


    ### Ask who a person is (Only works for one word inputs)
    elif 'who is' in command:
        command = command.replace('who is', "")
        speak(wikipedia.summary(command, 2))


    ###Leave program
    elif "bye kyle" in command:
        speak("See you later ! ")
        break
    else:
        speak("What are you saying?")

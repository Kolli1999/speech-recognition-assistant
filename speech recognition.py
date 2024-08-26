import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk

listening = sr.Recognizer()
engine = pt.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def hear():
    cmd = ""  # Initialize cmd to an empty string
    try:
        with sr.Microphone() as mic:
            print('Listening....')
            voice = listening.listen(mic)
            cmd = listening.recognize_google(voice)
            cmd = cmd.lower()
            if 'kolli' in cmd:
                cmd = cmd.replace('kolli', '')
                print(cmd)
    except Exception as e:
        print("Sorry, I didn't catch that:", str(e))
    return cmd

def run():
    cmd = hear()
    print(cmd)
    if 'play' in cmd:
        song = cmd.replace('play', '')
        speak('Playing ' + song)
        pk.playonyt(song)

run()

import speech_recognition as sr
import pyttsx3

#obtain audio from the microphone
r=sr.Recognizer()
listener =r
cn_engine = pyttsx3.init()
cn_engine.setProperty('voice', 'zh')
cn_engine.say('你好, 我是你的助理 Vicky, 有甚麼我可以協助你嗎? 請先回答您要詢問english 或是chinese 問題')
cn_engine.runAndWait()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def take_command():
    try:
        with sr.Microphone() as source:
            print("Please wait. Calibrating microphone...")
            #listen for 5 seconds and create the ambient noise energy level
            r.adjust_for_ambient_noise(source, duration=1)
            print("Say something!")
            audio=r.listen(source)
            command = r.recognize_google(audio, language="zh-TW")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("No response from Google Speech Recognition service: {0}".format(e))
    return command

def talk(text):
    #engine.say('You are saying')
    engine.say(text)
    engine.runAndWait()


def run_command():
    command = take_command()
    command = command.lower()
    print(command)
    if 'english' in command:
        engine.say('Your question is?')
        voice = listener.listen(sr.Microphone())
        command = listener.recognize_google(voice)

        if 'play' in command:
            song = command.replace('play','')
            talk('playing'+ song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('Current time is' + time)
        elif 'who is' in command:
            person = command.replace('who is','')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'how are you' in command:
            talk('sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am not!  I am in a relationship with wifi')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        else:
            talk('I am sorry, can you say again?')
    elif 'chinese' in command:
        cn_engine.say('我目前只聽得懂英文問題')
        cn_engine.runAndWait()

while True:
    run_command()

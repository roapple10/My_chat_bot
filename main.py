from MyLibrary import *
from AI_Chatbot_complete import *



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)

todo_list = ['Go Shopping', 'Clean Room', 'Record Video']


def create_note():
    global listener

    engine.say('What do you want to write onto your note?')
    engine.runAndWait()
    print("I am listening")
    done = False

    while not done:
        try:
            with sr.Microphone() as source:
                #listen your voice
                note = rec(source)
                talk('Choose a filename!')
                # engine.runAndWait()
                filename = rec(source)

            with open(filename, 'w') as f:
                f.write(note)
                done = True
                talk(f"I successfully created the note {filename}")
                # engine.runAndWait()
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            talk("I did not understand you! Please try again!")
            # engine.runAndWait()
        except sr.RequestError as e:
            print("No response from Google Speech Recognition service: {0}".format(e))

def add_todo():
    global listener

    talk('What do you want to add?')
    # engine.runAndWait()
    print("I am listening")

    done = False

    while not done:
        try:
            with sr.Microphone() as source:
                item = rec(source)
                todo_list.append(item)
                done = True
                talk(f"I added {item} to the to do list!")
                # engine.runAndWait()

        except sr.UnknownValueError:
            listener = sr.Recognizer()
            talk("I did not understand you! Please try again!")
            # engine.runAndWait()
        except sr.RequestError as e:
            print("No response from Google Speech Recognition service: {0}".format(e))

def show_todos():
    talk("The items on your to do list are the following")
    for item in todo_list:
        engine.say(item)
    engine.runAndWait()

def hello():
    ans = reply('Hi')
    talk(ans)
    print("I am listening")

def bye():
    bye = reply('bye')
    talk(bye)
    #sys.exit(0)

def talk(text):
    # engine.say('You are saying')
    engine.say(text)
    engine.runAndWait()

def rec(source):
    listener.adjust_for_ambient_noise(source, duration=0.2)
    voice = listener.listen(source)
    note = listener.recognize_google(voice)
    note = note.lower()
    return note

def take_command():
    try:
        with sr.Microphone() as source:
            command = message
            print(command)
            if 'play' in command:
                song = command.replace('play', '')
                talk('playing' + song)
                pywhatkit.playonyt(song)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print(time)
                talk('Current time is' + time)
            elif 'who is' in command:
                person = command.replace('who is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            elif 'single' in command:
                talk('I am not!  I am in a relationship with wifi')
            elif 'joke' in command:
                talk(pyjokes.get_joke())
    except sr.UnknownValueError:
        recognizer = sr.Recognizer()
        engine.say("I did not understand you! Please try again!")
        engine.runAndWait()
    except sr.RequestError as e:
        print("No response from Google Speech Recognition service: {0}".format(e))


# while True:
#    run_command()

# mappings = {'greeting': some_function}
# assistant = GenericAssistant('intents.json', intent_methods=mappings)
# assistant.train_model()
# assistant.request("How are you")


mappings = {"greeting": hello,
            "create_note": create_note,
            "add_todo": add_todo,
            "show_todos": show_todos,
            "goodbye": bye,
            "more_work": take_command}

assistant = GenericAssistant('intents.json', intent_methods=mappings)
#assistant.train_model()
#assistant.save_model()
assistant.load_model()
while True:
    try:
        with sr.Microphone() as source:
            print("I am listening")
            message = rec(source)
            #message = "Bye"
            #print(message)
            assistant.request(message)
    except sr.UnknownValueError:
        recognizer = sr.Recognizer()

# internal modules
import datetime

# external packages
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia as wiki

listener = sr.Recognizer()
engine = pyttsx3.init()

# !-- if voice must be woman voice use code below --!
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[1].id)

# !-- changing voice rate of kali --!
engine.setProperty("rate", 132)

isRunning = True  # global execution key

emptyCount = 1  # how many times command can be empty


# !-- functions start
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print("Listening ...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
    except:
        pass
    return command


def commandCutter(text, cuttingWord):
    newText = text.replace(cuttingWord, "").strip()
    return newText


def run_cyber():
    global emptyCount
    if emptyCount == 3:
        talk("Sir, you can stop my execution by saying Cyber Exit. Otherwise I'm gonna do it by myself for the next "
             "time!")
    elif emptyCount == 4:
        talk("I think you don't want to tell something. But I give you one more chance")
        global isRunning
        isRunning = False

    command = take_command()
    if command != '':
        if "cyber" in command:
            print("Cyber got command")
            emptyCount = 0
            command = commandCutter(command, "cyber")
            print(f"Command => {command}")
            if "time" in command:
                time = datetime.datetime.now().strftime("%I:%M %p")
                talk(f"Sir, current time is {time} now")
                print("Executed process => telling about current time")
                print(f"Current time is {time}")
            elif "play" in command:
                song = commandCutter(command, "play")
                talk(f"I'm opening {song} for you boss. Enjoy!")
                print(f"Executed process => playing {song} music on youtube ...")
                pywhatkit.playonyt(song)
            elif "search for" and "on google" in command:
                searchingStuff = commandCutter(command, "search for")
                searchingStuff = commandCutter(searchingStuff, "on google")
                talk(f"I'm looking for {searchingStuff} on google")
                print(f"Executed process => searching for {searchingStuff} on google ...")
                pywhatkit.search(searchingStuff)
            elif "search for" and "on wikipedia" in command:
                searchingStuff = commandCutter(command, "search for")
                searchingStuff = commandCutter(searchingStuff, "on wikipedia")
                talk(f"I'm looking for {searchingStuff} on wikipedia")
                print(f"Executed process => searching for {searchingStuff} on wikipedia ...")
                info = wiki.summary(searchingStuff, 2)
                print(f"Info : {info}")
                talk(
                    f"Here is the info about {searchingStuff} that I found for you : {info}. That's the brief info about "
                    f"your searching")
            elif "exit" in command:
                isRunning = False
            else:
                talk("Please sir repeat again. I can't understand")
    else:
        emptyCount += 1


# functions end --!

# !-- greeting --!
greeting_msg = "Cyber here sir. Just tell me what should I do"
talk(greeting_msg)

while isRunning:
    run_cyber()

talk("Sir I'm glad to serve you something. Hope you enjoy. Have a good day")

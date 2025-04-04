import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change index if needed
engine.say("Hi Sudhanshu, Kaise ho bhai?")
engine.runAndWait()
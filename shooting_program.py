#!/usr/bin/python3

import pyttsx3
import engineio
import time

engineio = pyttsx3.init()
def speak(text):
    engineio.say(text)
    engineio.runAndWait()
voices = engineio.getProperty('voices')
engineio.setProperty('voice',"english-north")
engineio.setProperty('gender',"male")

speak("Athletes to the line")
time.sleep(120)
speak("Five minutes preparation and sighting time ")
time.sleep(1)
speak("Start")
time.sleep(4*60 + 30)
speak("30 seconds")
time.sleep(30) # Maybe should be slightly less due to time to say "30 seconds"
speak("Stop, Unload")
speak("Insert safety flag, and turn heads and face spectators") # Check!
time.sleep(60)
speak("For the first competition series, load")
time.sleep(5)
speak("Start")
timep.sleep(250)
speak("Stop")
time.sleep(20)
speak("For the next competition series, load")
time.sleep(5)
speak("Start")
timep.sleep(250)
speak("Stop")
time.sleep(20)
for i in range (1,13+1):
    speak("For the next competition shot, load")
    time.sleep(5)
    speak("Start")
    timep.sleep(250)
    speak("Stop")
    time.sleep(20)
speak("For the next competition shot, load")
time.sleep(5)
speak("Start")
timep.sleep(250)
speak("Stop, Unload")
speak("Results are final")


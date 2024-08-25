from flask import Flask, request, jsonify
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui

app = Flask(__name__)
engine = pyttsx3.init()

def speak(audio) -> None:
    engine.say(audio)
    engine.runAndWait()

def get_time() -> str:
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    return f"The current time is {Time}"

def get_date() -> str:
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    return f"The current date is {day}/{month}/{year}"

@app.route('/command', methods=['POST'])
def command():
    data = request.get_json()
    command = data['command'].lower()
    response = ""

    if "time" in command:
        response = get_time()
    elif "date" in command:
        response = get_date()
    elif "who are you" in command:
        response = "I'm JARVIS created by Mr. Kishan and I'm a desktop voice assistant."
        speak(response)
    elif "how are you" in command:
        response = "I'm fine sir, What about you?"
        speak(response)
    elif "open youtube" in command:
        wb.open("youtube.com")
        response = "Opening YouTube"
    elif "open google" in command:
        wb.open("google.com")
        response = "Opening Google"
    elif "play music" in command:
        song_dir = os.path.expanduser("~\\Music")
        songs = os.listdir(song_dir)
        song = random.choice(songs)
        os.startfile(os.path.join(song_dir, song))
        response = f"Playing {song}"
    else:
        response = "Command not recognized"

    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)

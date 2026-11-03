import speech_recognition as sr # as is used to use something with sn alternative name like speech recognition as sr
import webbrowser
import pyttsx3 # text to speech
import musiclibrary
import requests
from openai import OpenAI # remove when doesent work
from gtts import gTTS # remove when doesent work
import pygame
import os 

# pip install pocketsphinx

recognizer = sr.Recognizer()# gives speech recognition functionality
engine = pyttsx3.init() # this will initiallize the pyttsx3
newsapi = "3731cbf358ec44988ceb7d3f35c92e17"
 
def speak_say(text):  
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')


    # Initialize Pygame mixer
    pygame.mixer.init()

# Load the MP3 file
    pygame.mixer.music.load("temp.mp3")

# Play the MP3 file
    pygame.mixer.music.play()

# Keep the program running to allow the music to play
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")


def ai(command):
    client = OpenAI(
api_key = "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",
# pip install openai
 )

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
    {"role": "system", "content": "You are my assistant, named Kako Give short responses"},
    {"role": "user", "content": command}
  ] 
  ) 

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
    
            # Fetch the articles
            articles = data.get('articles', [])
    
            # Print the top headlines
            for i, article in enumerate(articles, start=1):
                speak(f"{i}. {article['title']}")

    else:
        output = ai(c)
        speak(output)

if __name__ == "__main__":
    speak("Hello! My name is Kako")
    while True:
        #Listen for the wake word "Jarvis"
        #obtain the audio from the microphone
        r = sr.Recognizer()
        

        print("Recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "kako"):
                speak("Yeah Buddy")
        # listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))




        
                

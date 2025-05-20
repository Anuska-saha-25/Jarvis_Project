import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "ab4048538eab4e0196c63abc1f2e8f49"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def aiprocess(command):
    client = OpenAI(api_key="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",
    )
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like alexa and google."},
        {
            "role": "user",
            "content": command
        }
    ]
    )

    return completion.choices[0].message.content
    
def processcommand(c):
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
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for article in articles:
                speak(article['title'])
    else:
        #let openai handle the request
        output = aiprocess(c)
        speak(output)
        
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        #listen for the wake word "jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        # recognize speech using Sphinx
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio =r.listen(source, timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("ya")
                #listen for command
                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio =r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processcommand(command)
        except Exception as e:
            print("Sphinx error; {0}".format(e))
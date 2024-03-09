import speech_recognition as sr
import pyttsx3 as pyt
import pywhatkit 
import datetime
import wikipedia
import requests

listener = sr.Recognizer()
engine = pyt.init()
voices = engine.getProperty('voices')
Jake = engine.say("hello there.I'm Jake.How can I help?")

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower
            command = command.replace('jake', '')
        
        if 'jake' in command:
            talk(command)
        else:
            print('')
        
    except:
        pass
   
def run_jake1():
    command = get_command
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('the current time is'+ time)
    
    elif "wikipedia" 'history' 'tell me about' in command:
        person = command.replace('wikipedia,history of,tell me about', "")
        info = wikipedia.summary(person,3)
        talk(info)

    elif 'weather' in command:
        command = command.replace('weather', '')
        city = command 
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        API_KEY = '8841be9a1c7492b92c5244bb326e9673' 
        URL = BASE_URL + "appid=" +API_KEY +"&q=" + city
        response = requests.get(URL).json()
        if response['cod'] == '404':
            print("No City Found!! \nTry Again")
        else:
           weather =  temp_kelvin = response['main']['temp']
        talk(weather)

    else:
        print("Can you please repeat what you just said")
        print("it seems I'm unable to carry outt your command./n sorry")
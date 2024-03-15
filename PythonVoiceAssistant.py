import speech_recognition as sr
import pyttsx3
import datetime
import requests
import webbrowser
import os

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak out the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet the user
def greet():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    if hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
        
# Function to take voice input
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Sorry, the service is down.")
        return ""
    
def get_weather_forecast(city):
    api_key = "7006d7d1e17b00fdde11c48019b271f1"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"The weather in {city} is {weather_description} with a temperature of {temperature}°C."
    else:
        return "Unable to fetch weather data."
    
if __name__ == "__main__":
    greet()
    speak("How can I assist you today?")
    while True:
        command = take_command()
        if "weather" in command:
            speak("Which city's weather would you like to know?")
            city = take_command()
            result = get_weather_forecast(city)
            speak(result)
        elif "open youtube" in command:
            webbrowser.open("https://www.youtube.com")
        elif "open google" in command:
            webbrowser.open("https://www.google.com")
        elif "play music" in command:
            music_dir = "D:\Bgms"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that command.")
            


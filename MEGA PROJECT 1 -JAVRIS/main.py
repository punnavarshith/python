import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init()
driver = None  # Global driver variable
NEWS_API_KEY = 'a362962dede34078a24ff04f8d8db96b'  # Replace with your News API key
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=' + NEWS_API_KEY

def speak(text):
    engine.say(text)
    engine.runAndWait()

def fetch_news_titles():
    try:
        response = requests.get(NEWS_API_URL)
        response.raise_for_status()
        news_data = response.json()
        articles = news_data['articles']
        titles = [article['title'] for article in articles]
        return titles
    except Exception as e:
        print(f"An error occurred while fetching news: {e}")
        return []

def process_command(c):
    global driver
    if 'open google' in c.lower():
        webbrowser.open("https://google.com")
    elif 'open youtube' in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif 'open linkedin' in c.lower():
        webbrowser.open("https://www.linkedin.com/feed/")
    elif 'open chat gpt' in c.lower():
        webbrowser.open("https://chatgpt.com/")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
        url = f"https://www.youtube.com/results?search_query={song.replace(' ', '+')}"
        try:
            if driver is None:
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.get(url)
            time.sleep(3)  # Wait for the page to load
            first_video = driver.find_element(By.XPATH, '//*[@id="video-title"]')
            first_video.click()
        except Exception as e:
            print(f"An error occurred: {e}")
    elif 'close browser' in c.lower() and driver is not None:
        driver.quit()
        driver = None
    elif 'news headlines' in c.lower():
        titles = fetch_news_titles()
        for idx, title in enumerate(titles):
            print(f"{idx + 1}. {title}")
            speak(title)
    
        

if __name__ == "__main__":
    speak('Initializing Jarvis...')
    while True:
        # Recognize speech using Google Speech Recognition
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)
            word = recognizer.recognize_google(audio)
            print("You said: " + word)
            
            if word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    
                    if "exit" in command.lower():
                        speak("Goodbye!")
                        break
                    process_command(command)
            if "exit" in word.lower():
                speak("Goodbye!")
                break
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

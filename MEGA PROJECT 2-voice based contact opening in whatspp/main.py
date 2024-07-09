import pyautogui
import speech_recognition as sr
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyttsx3
import requests
import pyperclip
#import ollama

def speak(text):
    engine.say(text)
    engine.runAndWait()
  
def process_command(c):
    global driver
    if 'open whatsapp' in c.lower():
      while True:  
        try:
            speak("whom to do you want to chat with")
            print("whom to do you want to chat with")
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)
            contact_name = recognizer.recognize_google(audio)
            if "exit" in c.lower():
                speak("Goodbye!")
                break
            
            print(f"Selected contact: {contact_name}")
            print("You are trying to chat with: " + contact_name)
            open_whatsapp_and_select_contact(contact_name)
            # Time delay to switch to WhatsApp window
            time.sleep(5)

           
        except sr.UnknownValueError:
                                 print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
                                 print(f"Could not request results from Google Speech Recognition service; {e}")
        
        
        
# Function to open WhatsApp Web and select a contact
def open_whatsapp_and_select_contact(contact_name):
    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Open WhatsApp Web
    driver.get('https://web.whatsapp.com')

    # Wait for the user to scan the QR code
    print("Please scan the QR code to log in to WhatsApp Web.")
    time.sleep(120)  # Adjust the sleep time as needed to give enough time for QR code scanning

    try:
        # Find the search box and enter the contact name
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.click()
        search_box.send_keys(contact_name)
        time.sleep(10)  # Wait for search results to appear
        search_box.send_keys('\ue007')  # Press Enter (using Unicode for Enter key)
                 # Time delay to switch to WhatsApp window
        time.sleep(5)

        # Coordinates of the starting point of text (you need to find this manually)
        start_x, start_y = 791, 136 # Adjust these values

        # Coordinates of the ending point of text (you need to find this manually)
        end_x, end_y = 826, 613 # Adjust these values

        # Move the cursor to the starting point
        pyautogui.moveTo(start_x, start_y, duration=0.5)

        # Click and hold the mouse button to start the drag
        pyautogui.mouseDown()

        # Move the cursor to the ending point while holding the mouse button
        pyautogui.moveTo(end_x, end_y, duration=2)

        # Release the mouse button to finish the drag
        pyautogui.mouseUp()

        # Adding a small delay to ensure the selection is made
        time.sleep(1)

        # Copy the selected text (Ctrl+C)
        pyautogui.hotkey('ctrl', 'c')

        # Wait a short moment for the clipboard to update
        time.sleep(2)

        # Get the text from the clipboard
        selected_text = pyperclip.paste()

        # Print the copied text
        print("Selected Text:", selected_text)
        while True:
            time.sleep(1)  # Keep the script running to keep the browser open
    except Exception as e:
        print(f"An error occurred: {e}")
        driver.quit()

recognizer = sr.Recognizer()
engine = pyttsx3.init()
driver = None  # Global driver variable
# Main function
if __name__ == "__main__":
    # contact_name = input("Enter the name of the contact you want to chat with: ")
    # open_whatsapp_and_select_contact(contact_name)
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

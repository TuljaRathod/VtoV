import speech_recognition as sr
from PIL import Image
import IPython.display as display
import os
import time

def show_sign_image(char, folder="sign_images"):
    char = char.upper()
    if char.isalnum():  # A-Z or 0–9
        img_path = os.path.join(folder, f"{char}.png")
        if os.path.exists(img_path):
            img = Image.open(img_path)
            display.display(img)
            time.sleep(1)
            display.clear_output(wait=True)

def text_to_sign(text):
    for char in text:
        if char.isalnum():
            show_sign_image(char)

def recognize_and_translate():
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("🎙️ Speak (say 'stop' to exit)...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)
                print("📝 You said:", text)

                if "stop" in text.lower():
                    print("👋 Exiting...")
                    break

                text_to_sign(text)

            except sr.UnknownValueError:
                print("❌ Couldn't understand. Try again.")
            except sr.RequestError:
                print("⚠️ Internet problem.")

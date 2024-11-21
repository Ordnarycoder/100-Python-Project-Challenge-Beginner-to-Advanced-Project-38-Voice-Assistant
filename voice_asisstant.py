import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for voice input and convert to text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Sorry, there seems to be an issue with the speech service.")
            return ""

def handle_command(command):
    """Handle the user's voice command."""
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        from datetime import datetime
        now = datetime.now()
        speak(f"The time is {now.strftime('%H:%M')}")
    elif "yusu"  in command:
        speak("My best friend")
    elif "iron man"  in command:
        speak("Sorry, you're not iron man")
    elif "yus"  in command:
        speak("My best friend")
    elif "hassan" in command:
        speak("My second best friend")
    elif "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I didn't understand that command.")

if __name__ == "__main__":
    speak("Hello! I am your voice asistant. What can I do for you?")
    while True:
        user_command = listen()
        handle_command(user_command)

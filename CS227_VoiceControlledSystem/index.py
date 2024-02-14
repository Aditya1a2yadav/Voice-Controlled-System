import speech_recognition as sr
import serial
import time
import serial.tools.list_ports
import pyttsx3
import datetime
import namste
arduino_port = 'COM15'
arduino_baud_rate = 9600

def tts(text, voice_id=None):
    engine = pyttsx3.init()

    # Set system voice if voice_id is specified
    if voice_id:
        voices = engine.getProperty('voices')
        for voice in voices:
            if voice.id == voice_id:
                engine.setProperty('voice', voice.id)
                break

    engine.say(text)
    engine.runAndWait()

# def tts(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

voice_id = "com.apple.speech.synthesis.voice.Alex"
voice_id2 ="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
voice_id3="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

def wishMe():
    hour = int(datetime.datetime.now().hour)
    time.sleep(1)
    if hour>=0 and hour<12:
        tts("Good Morning!")
        
    elif hour>=12 and hour<18:
        tts("Good Afternoon!")
        
    else:
        tts("Good Evening!")
        
    tts("I am Aditya Sir.")

def send_to_arduino(keyword):
    try:
        # Establish serial connection if it doesn't exist
        if 'arduino' not in globals():
            global arduino
            arduino = serial.Serial(arduino_port, arduino_baud_rate, timeout=1)
            time.sleep(2)  # Allow time for Arduino to reset
        
        arduino.write(keyword.encode())
    except Exception as e:
        print(f"Error in sending data to Arduino: {e}")
        return "Error"
    except sr.RequestError as e:
        print(f"Error making the request to Google Speech Recognition: {e}")
        return "Error"

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            keyword = recognizer.recognize_google(audio).lower()
            print("You said:", keyword)
            return keyword
        except sr.UnknownValueError:
            print("Could not understand audio")
            return "Error"
        except sr.RequestError as e:
            print(f"Error making the request to Google Speech Recognition service: {e}")
            return "Error"

if __name__ == "__main__":
    wishMe()
    a="b"
    while True:
        print("Say Hello Arduino to start")
        tts("Say Hello Arduino to start talking with miss Arduino")
        keyword = recognize_speech()
        if "hello" in keyword:
            print("Yes Boss")
            tts("Yes Boss, I am arduino. How can i help you",voice_id3)
            while True:
                keyword = recognize_speech()
                if "light" in keyword:
                    if "1" in keyword or "one" in keyword:
                        if " on " in keyword:
                            tts("Turning on Light of room 1.",voice_id3)
                            send_to_arduino("on led 1")
                        if " off " in keyword:
                            tts("Turning light off.",voice_id3)
                            send_to_arduino("off led 1")
                    if "2" in keyword or "two" in keyword or "to" in keyword:
                        if " on " in keyword:
                            tts("Turning on Light of room 2.",voice_id3)
                            send_to_arduino("on led 2")
                        if " off " in keyword:
                            tts("Turning light off of room nnumber 2.",voice_id3)
                            send_to_arduino("off led 2")
                    if "3" in keyword or "three" in keyword:
                        if " on " in keyword:
                            tts("Turning on Light 3.",voice_id3)
                            send_to_arduino("on led 3")
                        if " off " in keyword:
                            tts("Turning off Light of room 3.",voice_id3)
                            send_to_arduino("off led 3")
                    if "4" in keyword or "four" in keyword or "for" in keyword:
                        if " on " in keyword:
                            tts("Turning on Light 4.",voice_id3)
                            send_to_arduino("on led 4")
                        if " off " in keyword:
                            tts("Turning off Light of room 4.",voice_id3)
                            send_to_arduino("off led 4")
                    if "all" in keyword:
                        if "on" in keyword:
                            tts("Turning all lights on.",voice_id3)
                            send_to_arduino("on all led")
                        if "off" in keyword:
                            tts("Turning off lights of all the rooms.",voice_id3)
                            send_to_arduino("off all led")
                elif "exit" in keyword or "thank" in keyword:
                    print("Exiting")
                    a="a"
                    tts("Its my pleasure sir. Namaste",voice_id3)
                    break
                elif "off" in keyword or "stop" in keyword:
                    if "buzzer" in keyword or "bazaar" in keyword or "bazar" in keyword:
                        print("Turning buzzer off")
                        tts("Turning buzzer off",voice_id3)
                        send_to_arduino("off buzzer")
                else:
                    print("Say Again")
        elif "thank" in keyword or "exit" in keyword:
            print("Thanks Sir")
            tts("Ok sir. Going to sleep. Namaste",voice_id)
            send_to_arduino("Thank")
            namste.namaste()
            break
                    
        else:
            print("Say again")

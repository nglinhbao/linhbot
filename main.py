import win32com.client as wincl
import speech_recognition as sr
from datetime import date
import pyowm

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("...")
        audio = r.listen(source)
    text = ''

    try:
        say = r.recognize_google(audio)
    except:
        say = ''
    you_say = 'You: '

    if 'hi' in say or 'hello' in say:
        you_say += say
        print(you_say)
        text = 'hello boss'

    elif 'you' in say or 'who' in say:
        you_say += say
        print(you_say)
        text = "I'm your assistant, Linh Bot"

    elif 'today' in say or 'day' in say or 'date' in say:
        you_say += say
        print(you_say)
        today = str(date.today())
        text = 'Today is ' + today

    elif 'weather' in say or 'temperature' in say:

        you_say += say
        print(you_say)
        owm = pyowm.OWM(
            '7a253bcb7ca7ddc9a6da4782f78bca87')

        city = 'Ho Chi Minh'
        loc = owm.weather_manager().weather_at_place(city)
        weather = loc.weather

        temp = weather.temperature(unit='celsius')

        if 'maximum' in say and 'temperature' in say:
            i = 0
            for key, val in temp.items():
                i += 1
                if i == 1:
                    continue
                text = f'Max temperature in Ho Chi Minh city is {val} degrees celsius'
                if i == 2:
                    break
        elif 'minimum' in say and 'temperature' in say:
            i = 0
            for key, val in temp.items():
                i += 1
                if i == 1 or i == 2:
                    continue
                text = f'Min temperature in Ho Chi Minh city is {val} degrees celsius'
                if i == 3:
                    break

        elif 'temperature' or 'weather' in say:
            i = 0
            for key, val in temp.items():
                text = f'Temperature in Ho Chi Minh city is {val} degrees celsius'
                if i == 0:
                    break


    elif 'bye' in say or 'end' in say or 'finished' in say:
        you_say += say
        print(you_say)
        text = 'Goodbye'
        print('Linh Bot: ',text)
        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak(text)
        break

    else:
        print(you_say)
        text = "Sorry, I can't hear you"

    print('Linh Bot: ', text)
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(text)






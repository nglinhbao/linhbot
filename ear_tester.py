import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print ('Say Something!')
    audio = r.listen(source)
try:
    say = r.recognize_google(audio, language='en-US')
except:
    say = ''
print('you: ',say)
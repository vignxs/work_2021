# import os
# from gtts import gTTS
# import os
# tts = gTTS(text='Good morning', lang='en')
# tts.save("good.mp3")
# os.system("mpg321 good.mp3")


import pyttsx3

# initialisation
engine = pyttsx3.init()

# testing
engine.say("My first code on text-to-speech")
engine.say("Thank you, Geeksforgeeks")
engine.runAndWait()

#The best library because you dont have to save the text file or open the file to start the speech

'''
pip install pyttsx3
'''

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello world")
engine.runAndWait()

'''
FOR SPEAKING
'''

### IMPORTS ###
import pyttsx3
import os

def speak(args):
	'''
	Speak method to make it easy speaking. It will pass the argument
	when calling. And initializing Jarvan's voice.
	'''

	engine = pyttsx3.init()

	os.system('cls')

	engine.say(args)

	print(args)

	engine.runAndWait()

def shadow_speaker(args):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')

	engine.say(args)

	engine.runAndWait()
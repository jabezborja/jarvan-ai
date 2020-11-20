
### IMPORTS ###
import socket
import os
from VA.speaker import speak
from VA.audio import recordAudio
from VA.date import date
from VA.admin import Admin
from VA.task import countAllTask
from VA.log import log

def isOperation(resp):
	'''
	Check if the user said is an operation then return True
	'''
	operations = ['+', '-', 'x', '*', '/', 'plus', 'minus', 'times', 'divide', 'multiplied']

	for o in operations:
		if o in resp: return True

	return False

def wake(response):
	wakes = ['good morning', 'good afternoon', 'good evening', 'good night', 'hello', 'hi']

	for wake in wakes:
		if wake in response: return True

	return False

def greet(response, conn):
	'''
	If greets then response
	'''

	# For counting tasks

	cursor = conn.cursor()
	try:
		cursor.execute("SELECT * FROM TASKS")
	except Error:
		handleTaskErrors(conn)

	tasks = cursor.fetchall()
	counted = countAllTask(tasks)
	
	if 'good morning' in response:
		loggreet("good morning", "morning")
		speak('Good morning')
		dateNow = date()
		speak(dateNow[0])
		speak(dateNow[1])
		speak("And you have " + str(counted) + " tasks to be done.")
		speak("Have a nice day.")
	if 'good afternoon' in response:
		log("good afternoon", "afternoon")
		speak('Good afternoon.')
	if 'good evening' in response:
		log("good evening", "evening")
		speak('Good evening')
	if 'good night' in response:
		log("good night", "night")
		speak('Good night ')
		speak("Let's talk tommorow ")
	if 'hello' in response:
		log("Hello", "Hello")
		speak('Hi')
	if 'hi' in response:
		log("Hi", 'Hi')
		speak('Hello')

def asking(resp):
	ask_list = ['who is', 'what is', 'where is', 'when is']

	for ask in ask_list:
		if (ask in resp):
			return True

def loggreet(greets, method):
	greets = "Greeted " + greets
	if method == "morning":
		log(greets + " " + "(MID: greet_morning)")
	elif method == "afternoon":
		log(greets + " " + "(MID: greet_afternoon)")
	elif method == "evening":
		log(greets + " " + "(MID: greet_evening)")
	elif method == "night":
		log(greets + " " + "(MID: greet_night)")
	elif method == "Hello":
		log(greets + " " + "(MID: greet_hello)")
	elif method == "Hi":
		log(greets + " " + "(MID: greet_hi)")
	else:
		print("Error logging")
		log("Error Logging (MID: err_log)")



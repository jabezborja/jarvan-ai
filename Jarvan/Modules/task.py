'''
TASKS
'''

### IMPORTS ###
from sqlite3 import Error
from VA.speaker import speak
from VA.audio import recordAudio
from VA.log import log
import os
import sqlite3

def createTask(conn, intCon):
	'''
	Called for creating a new task in the database
	'''

	### LocVars (Local Variables) ###

	try:
		cursor = conn.cursor()

		# If conn is None or closed.

		if not conn: conn = sqlite3.connect('data.db')

		cursor.execute("SELECT * FROM TASKS")

		tasks = cursor.fetchall()

		speak("Okay, I am going to make a task.")

		# Get the ID
		idnum = countAllTask(tasks) + 1

		speak("What's the title of the task?")

		# Get the Title
		title = recordAudio(intCon).lower()

		speak("What's the description?")

		# Get the description
		desc = recordAudio(intCon).lower()

		speak("What's week number?")

		# Get the week number
		week = recordAudio(intCon).lower()

		# Insert to Database
		data_tuple = (int(idnum), title, desc, week)

		sqlite_insert = """INSERT INTO TASKS (id, title, desc, week) VALUES (?, ?, ?, ?)"""

		# Execute and Commit
		cursor.execute(sqlite_insert, data_tuple)
		conn.commit()
		logtask(title, "POST")
	except Error:
		handleTaskErrors()

	speak("Task Inserted successfully!")

def countAllTask(tasks):
	'''
	Count all the task and return with +1
	'''
	count = 0
	for task in tasks:
		count += 1
	return count

def get_task(conn):
	'''
	Get all the task from database
	'''
	if not conn: conn.connect('data.db')

	try:
		cursor = conn.cursor()
		tasks = cursor.fetchall()
		cursor.execute("SELECT * FROM TASKS")

		tasks = cursor.fetchall()
		if countAllTask(tasks) == 0:
			speak("Looks like you haven't commanded me to create a task yet.")
		else:
			speak("Your tasks are...")
			logtask(None, "GET")
			for task in tasks:
				speak("Task number: " + str(task[0]))
				speak("Title: " + task[1])
				speak("Description: " + task[2])
				speak("Week Number: " + str(task[3]))
	except Error:
		handleTaskErrors(conn)

	speak("If you want to insert more task just command me to create.")

def handleTaskErrors(conn):
	cursor = conn.cursor()

	sql_insert = "CREATE TABLE TASKS (ID PRIMARY KEY, TITLE TEXT, DESC TEXT, WEEK INT)"

	cursor.execute(sql_insert)

def logtask(task, method):
	if method == "POST":
		log(f"Added task {task} (MID: task_post)")
	else:
		log("Asked about tasks (MID: task_get)")
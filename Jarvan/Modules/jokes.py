## IMPORTS ##
from sqlite3 import Error
from VA.timer import Timer
from VA.audio import recordAudio
from VA.task import createTask, countAllTask, get_task, handleTaskErrors
from VA.date import date, Okasyon, occation
from VA.checkers import isOperation, wake
from VA.admin import Admin
from VA.speaker import speak, shadow_speaker
import random	
import os
import sqlite3
import socket

def telljokes(conn):
	joke_arr = get_jokes(conn)

	speak(joke_arr[0])
	speak(joke_arr[1])
	
def get_jokes(conn):
	'''
	Joke method. It will return a random string from database
	called jokes
	'''
	if not conn: conn.connect('data.db')

	cursor = conn.cursor()

	null_datas = ['No jokes found', "To insert a joke. Say 'setup', and after that... say 'add jokes', so you can add jokes."]

	try:
		cursor.execute("SELECT * FROM JOKES")
		jokes = cursor.fetchall()

		joke_arr = []
		answers_arr = []
		number_arr = []
		
		count = Admin.jokes.countJokes(jokes)

		#For counting all jokes and returning it as number array for choosing the Joke and the answer at the same time.
		for k in range(count):
			number_arr.append(k)
		
		# If no jokes found then return with null_datas
		if not number_arr:
			return null_datas

		for joke in jokes:
			joke_arr.append(joke[1])
			answers_arr.append(joke[2])
		
		joke_chose = random.choice(number_arr)

		jok = joke_arr[joke_chose]
		ans = answers_arr[joke_chose]

		datas = [jok, ans]
		return datas
	except Error:
		'''
		If jokes table in database returns null and it will create
		new jokes database.
		'''
		handleJokeError(cursor, conn)

	return null_datas

def handleJokeError(cursor, conn):
	try:
		sql_insert = "CREATE TABLE JOKES (ID PRIMARY KEY, JOKE TEXT, ANSWER TEXT)"

		cursor.execute(sql_insert)
		conn.commit()
	except Error:
		raise Error
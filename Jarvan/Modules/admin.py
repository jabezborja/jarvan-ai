from VA.speaker import speak
from VA.audio import recordAudio
import sqlite3
import os

class Admin:
	"""docstring for Admin"""
	def __init__(self, arg):
		super(Admin, self).__init__()
		self.arg = arg

	def admin(self, response, conn, intCon):

		os.system('cls')
		speak("Setup mode activated")
		print("To deactivate, say something that does not familiar in the setup mode or say exit.")
		validate = recordAudio(intCon).lower()

		if('exit' in validate):
			speak("Setup mode deactivated")
			return
		if ('jokes' in validate):
			self.jokes.addjokes(self.jokes, conn, intCon)

	class jokes:
		"""docstring for jokes"""
		def __init__(self, arg):
			super(jokes, self).__init__()
			self.arg = arg

		def countJokes(jokes):
			count = 0
			for joke in jokes:
				count += 1
			return count

		def addjokes(self, conn, intCon):
			speak("Setting up jokes")
			cursor = conn.cursor()

			cursor.execute("SELECT * FROM JOKES")

			jokes = cursor.fetchall()

			sqlite3_insert = "INSERT INTO JOKES (id, joke, answer) VALUES (?, ?, ?)"

			idnum = self.countJokes(jokes) + 1

			speak("What joke is it?")
			
			joke = recordAudio(intCon).lower()

			speak("Okay, what is the answer?")

			answer = recordAudio(intCon).lower()

			speak("Okay I am going to list it down")

			data_tuple = (int(idnum), joke, answer)

			cursor.execute(sqlite3_insert, data_tuple)
			conn.commit()

			speak("Joke added. That was lit.")

			Admin.admin(Admin.admin, "none", conn, intCon)
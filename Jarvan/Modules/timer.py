### IMPORTS ###
import os
import time
from VA.audio import recordAudio
from VA.speaker import speak
import time

class Timer:
	def __init__(self):
		self._start_time = None

	def start(self):
		"""Start a new timer"""
		if self._start_time is not None:
			raise "Timer is running. Use .stop() to stop it"

		self._start_time = time.perf_counter()

	def stop(self):
		"""Stop the timer, and report the elapsed time"""
		if self._start_time is None:
			raise "Timer is not running. Use .start() to start it"

		elapsed_time = time.perf_counter() - self._start_time
		self._start_time = None
		return(f"Elapsed time: {elapsed_time:0.2f} seconds")

def timer(intCon):
	speak("Timer starts... now.")
	os.system('cls')
	print("Say STOP to stop the timer")
	t = Timer()
	t.start()

	stop = recordAudio(intCon)

	if 'stop' in stop:
		elapsed = t.stop()
		speak("Timer stopped!")
		speak(elapsed)
	

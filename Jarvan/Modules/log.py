import os
import sys
import datetime

def log(log):
	dateandtime = datetime.datetime.today()
	logged = None

	with open('log.txt', 'r') as m:
		logged = m.readlines()

	with open('log.txt', 'w') as l:
		l.writelines('['+str(dateandtime)+'] ' + log + '\n')
		for logs in logged:
			l.writelines(logs)
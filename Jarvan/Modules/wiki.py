from VA.speaker import speak
import wikipedia


def guesswho(question):
	speak('Working for it...')
	question = removePrefix(question)
	print(question)

	title = wikipedia.page(question).title
	summary = wikipedia.summary(question)

	speak("Information about " + title)
	speak(summary)

def removePrefix(question):
	if ('jarvan' in question):
		q = question.replace('jarvan', '')
	if ('who is' in question):
		u = q.replace('who is', '')
	if ('what is' in question):
		e = u.replace('what is', '')
	if ('where is' in question):
		r = e.replace('where is', '')

	return r


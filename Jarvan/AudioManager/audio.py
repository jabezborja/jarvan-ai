
### IMPORTS ###
import speech_recognition as sr


class Audio:
    def __init__(self):
        self.data = None

    def recognize(self, connected):
        if connected:
            r = sr.Recognizer()

            with sr.Microphone() as source:
                print("I'm listening...")
                audio = r.listen(source)

            try:
                self.data = r.recognize_google(audio)
            except sr.UnknownValueError:
                print("I cannot understand you clearly.")
            except sr.RequestError as e:
                raise sr.RequestError("Error: No connection", str(e))

            print("You said: " + self.data)
        else:
            self.data = input("Input: ")

        if self.data:
            return self.data
        else:
            print("Test")

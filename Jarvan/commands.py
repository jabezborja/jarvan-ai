import os
import time
import threading
from .Modules import capitals, date, domath
from . import checkers
from .SpeakManager.speaker import speak


class Commands:
    def __init__(self):
        self.speak = speak
        self.datenow = date.Date()
        self.capitals = capitals.Capital()
        self.checkers = checkers.Checkers()
        self.domath = domath.DoMath()
        self.is_load = False

    ## Jarvan Commands ##
    def commands(self, command):
        self.is_load = True
        thread = threading.Thread(target=self.loading)
        thread.start()
        if 'good morning' in command:
            self.is_load = False
            self.goodmorning()
        elif 'date' in command:
            self.is_load = False
            self.date()
        elif 'capital' in command:
            self.capital(command)
        elif self.checkers.is_operation(command):
            self.is_load = False
            self.answer_math(command)
        else:
            print("Test")

    def goodmorning(self):
        self.speak("Oh! Good morning!")

    def date(self):
        datenow = self.datenow.datenow()

        self.speak(datenow)

    def capital(self, command):
        capital = self.capitals.capital(command)

        self.is_load = False

        self.speak(capital)

    def answer_math(self, command):
        answer = self.domath.calculate(command)

        self.speak(answer)

    def loading(self):
        os.system('cls')
        load = self.is_load
        while load:
            l = 'Loading'
            print(l)
            time.sleep(1)
            os.system('cls')
            l += '.'
            print(l)
            time.sleep(1)
            os.system('cls')
            l += '.'
            print(l)
            time.sleep(1)
            os.system('cls')
            l += '.'
            print(l)
            time.sleep(1)
            os.system('cls')

import os
import time
import threading
from .Modules import capitals, date, domath, music
from . import checkers
from .SpeakManager.speaker import speak, shadow_speaker


class Commands:
    def __init__(self):
        self.speak = speak
        self.datenow = date.Date()
        self.capitals = capitals.Capital()
        self.checkers = checkers.Checkers()
        self.domath = domath.DoMath()
        self.music = music.playmusic
        self.is_load = False

    ## Jarvan Commands ##
    def commands(self, command):
        self.is_load = True
        if 'good morning' in command:
            self.is_load = False
            self.goodmorning()
        elif 'date' in command:
            self.is_load = False
            self.date()
        elif 'capital' in command:
            self.capital(command)
        elif 'play' in command:
            self.play_music(command)
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

    def play_music(self, command):
        music = self.music(command)
        speak("Music is done.")

    def answer_math(self, command):
        answer = self.domath.calculate(command)

        self.speak(answer)

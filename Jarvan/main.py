import os
from .AudioManager.audio import Audio
from playsound import playsound
from . import commands

## GLOVARS ##
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))


class Boot:
    def __init__(self, connected):
        self.connected = connected
        self.jarvan_is_sleeping = False
        self.jarvan_is_activated = True
        self.beep = BASE_DIR + fr'\Jarvan\sounds\beep.mp3'
        self.checkers = self.check_wake
        self.audio = Audio()
        self.command = commands.Commands()

    def start(self):
        while self.jarvan_is_activated:
            os.system('cls')
            data = self.audio
            user_input = data.recognize(self.connected).lower()

            self.command.commands(user_input)

    def check_wake(self, word):
        wake_words = ['jarvan', 'hey']

        for words in wake_words:
            if words in word:
                return True

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
        self.jarvan_is_sleeping = True
        self.jarvan_is_activated = False
        self.beep = BASE_DIR + fr'\Jarvan\sounds\beep.mp3'
        self.checkers = self.check_wake
        self.audio = Audio()
        self.command = commands.Commands()

    def start(self):
        print("Jarvan is now sleeping. To wake him up, just said 'Jarvan' or 'Hey'\nHe will play a 'Beep' sound if he is available.\n")

        while self.jarvan_is_sleeping:
            data = self.audio
            user_input = data.recognize(self.connected).lower()

            if (self.check_wake(user_input)):
                playsound(self.beep)
                self.jarvan_is_sleeping = False
                self.jarvan_is_activated = True

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

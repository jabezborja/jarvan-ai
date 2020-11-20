## IMPORTS ##
from Jarvan.SpeakManager.speaker import speak, shadow_speaker
import os
import sys
import datetime
import calendar
import sqlite3
import time
import random
import math
import socket
import time


class StartJarvan:
    def __init__(self):
        self.connected = False
        self.shadow_speaker = shadow_speaker

    def start(self):
        self.connected = self.checkInternet()

        try:
            from Jarvan import main
        except Exception as e:
            os.system('cls')
            print("Cannot find Jarvan, did you mess with it or something?",
                  "\nMore Info: " + str(e))
            quit()

        self.init_cli()

        boot = main.Boot(self.connected)
        boot.start()

    def checkInternet(self, host='8.8.8.8', port=53, timeout=8):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(
                (host, port))
            return True
        except socket.error:
            print("No internet connection detected.")
            return False

    def init_cli(self):
        os.system('title Jarvan 0.10.0')
        os.system('cls')
        print("Jarvan is now initializing, please wait...")
        self.shadow_speaker("Initializing Jarvan...")
        os.system('cls')


start = StartJarvan()
start.start()

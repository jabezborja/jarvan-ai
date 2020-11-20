
## IMPORTS ##
from sqlite3 import Error
import os
import datetime
import calendar
import sqlite3
import random
import math
import socket
import time


class Date:
    def __init__(self):
        self.date = datetime.datetime.now

    def datenow(self):
        now = datetime.datetime.now()
        my_date = datetime.datetime.today()
        weekday = calendar.day_name[my_date.weekday()]
        monthNum = now.month
        dayNum = now.day

        datas = []

        month_names = ['January', 'February', 'March', ' April', 'May', 'June',
                       'July', 'August', 'September', ' October', 'November', 'December']

        ordinalNumbers = ['1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th',
                          '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24rd', '25th', '26th', '27th', '28th', '29th', '30th', '31st']

        if self.occassion_boolean(month_names[monthNum-1], dayNum):
            occ = self.occassion(month_names[monthNum-1], dayNum)
            data = 'Today is ' + weekday + " " + \
                month_names[monthNum - 1] + ' the ' + \
                ordinalNumbers[dayNum - 1] + '. ' + occ
        else:
            data = 'Today is ' + weekday + " " + \
                month_names[monthNum - 1] + ' the ' + \
                ordinalNumbers[dayNum - 1] + '.'

        datas = data + ' ' + self.pasok(weekday)

        return datas

    def pasok(self, weekday):
        if ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday' in weekday):
            data = [f"It's {weekday}, you have modules to be done. Get up, take a shower, meditate, then do your modules, good luck!",
                    f"It's {weekday} looks like, you have modules to be done. You have to get up. Come on! Dont be too lazy",
                    f"It's {weekday} now. Go get up because you have modules! Dont be too lazy huh!",
                    f"It's {weekday} now."]
            pasok_data = random.choice(data)
        elif ('Saturday', 'Sunday' in weekday):
            pasok_data = "It's weekend, just rest and do things you must do."
        return pasok_data

    def occassion(self, month, day):
        m = month
        if m == "January":
            if day == 1:
                return 'Happy new year!'
            if day == 2:
                return 'Yesterday was new year.'
        if m == "February":
            if day == 14:
                return 'Happy valentines day!'
        if m == "June":
            if day == 21:
                return 'Happy birthday!'
        if m == "November":
            if day == 1:
                return 'Happy Holloween!'
            if day == 2:
                return 'Yesterday was Holloween. Peek A Boo! Haha'
        if m == "December":
            if day == 24:
                return "It's christmas eve!"
            if day == 25:
                return "Merry christmas!"
            if day == 31:
                return "Happy new year's eve!"

    def occassion_boolean(self, month, day):
        m = month
        if m == "January":
            if day == 1:
                return True
            if day == 2:
                return True
        if m == "February":
            if day == 14:
                return True
        if m == "June":
            if day == 21:
                return True
        if m == "November":
            if day == 1:
                return True
            if day == 2:
                return True
        if m == "December":
            if day == 24:
                return True
            if day == 25:
                return True
            if day == 31:
                return True
            return False

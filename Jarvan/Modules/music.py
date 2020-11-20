
## IMPORTS ##
import os
import random
import speech_recognition as sr
from threading import Thread
from playsound import playsound
from VA.speaker import speak
from VA.log import log

### MUSIC PATH ###
MUSIC_PATH = r'C:\\Users\\Jabez Borja\\Music\\Musics'

def playmusic(music):
	if ('favorite' in music):
		playFavorite()

	if ('shuffle', 'some music', 'some song' in music):
		playShuffle(music)

def playsong(music, isRepeat):
	speak("Okay, choosing a music from your playlist...")

	os.system('cls')

	if isRepeat:
		musics = randomizeMusic()

		print("Now playing " + musics[0] + "...")
		logmusic(musics[0], "play_musc_shuf_rpt")
		playsound(MUSIC_PATH + fr"\\{musics[0]}")
		print('Music ended')

		playsong(music, isRepeat)

	musics = randomizeMusic()

	print("Now playing " + musics[1] + "...")
	logmusic(musics[0], "playmusc_shuf")
	playsound(MUSIC_PATH + fr"\\{musics[0]}")
	print('Music ended')

def playFavorite():
	speak("Okay")
	os.system('cls')
	print("Now playing EMMAN - Teka Lang")
	logmusic("EMMAN - Teka Lang", "playmusc_fav")
	playsound(MUSIC_PATH + r'\\EMMAN - Teka Lang (Official Lyric Video).mp3')

	return 

def playShuffle(music):
	isRepeat = False

	if ('repeat' in music):
		isRepeat = True

	playsong(music, isRepeat)

def randomizeMusic():
	music_main = shuffleMusic()
	music_label = removeExtras(music_main)
	music_arr = [music_main, music_label]

	return music_arr

def removeExtras(music):
	music_name = os.path.splitext(music)[0]

	return music_name


def shuffleMusic():
	arr = []

	for (dirpath, dirnames, filenames) in os.walk(MUSIC_PATH):
		arr.extend(filenames)

	os.system('cls')
		
	music = random.choice(arr)

	return music

def logmusic(music, methodID):
	log("Played " + music + f" (MID: {methodID})")

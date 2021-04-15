## IMPORTS ##
import os
import random
from playsound import playsound
from ..SpeakManager.speaker import speak

### MUSIC PATH ###
MUSIC_PATH = r'C:\\Users\\Jabez Borja\\Music\\Musics'

# ENTRY POINT #
def playmusic(music):
	if ('favorite' in music):
		music_played = playFavorite()

	if ('shuffle', 'some music', 'some song' in music):
		music_played = playShuffle(music)

	return music_played

def playsong(music, isRepeat):
	speak("Okay, choosing a music from your playlist...")

	if isRepeat:
		musics = randomizeMusic()

		print("Now playing " + musics[0] + "...")
		playsound(MUSIC_PATH + fr"\\{musics[0]}")
		print('Music ended')

		playsong(music, isRepeat)

	musics = randomizeMusic()

	print("Now playing " + musics[1] + "...")
	playsound(MUSIC_PATH + fr"\\{musics[0]}")
	print('Music ended')

def playFavorite():
	speak("Okay")
	print("Now playing EMMAN - Teka Lang")
	playsound(MUSIC_PATH + r'\\EMMAN - Teka Lang (Official Lyric Video).mp3')

def playShuffle(music):
	isRepeat = False

	if ('repeat' in music):
		isRepeat = True

	return playsong(music, isRepeat)

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


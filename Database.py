from FileManager import  data_export, data_import
from msvcrt import getch
import os

# Checking if files exist. else creating them
if not os.path.exists("pref_anime.l"):
	os.system("copy nul pref_anime.l")
if not os.path.exists("black_list.l"):
	os.system("copy nul black_list.l")

# Converting string data from files into a usable form
pref_anime = data_import("dict", "pref_anime.l")  # is dict of format = { 'animeName': 2, ... } 2 = episode number
black_list = data_import("list", "black_list.l")  # is list of form [animeName1, animeName2, .... ]


def in_list(anime_name):
	"""Returns the name of the list which contains the anime name"""
	if anime_name in pref_anime:
		return "pref_list"
	elif anime_name in black_list:
		return "black_list"
	else:
		return False


def increment(anime_name, number):
	pref_anime[anime_name] = number
	data_export(pref_anime, "dict", 'pref_anime.l')

def add_to_list(anime):
	"""Adds the anime to a list (either preference list, black list, or none of the above"""
	print("\nThe anime " + anime.name + " is not in any list")
	print("Which list should it be added to?:")
	print("1.Preference List\n2.Black List\n")

	#input = ''
	#while input != b'1' and input != b'2' and input != b'3':
	input_ = input()

	if input_ == '1':
		pref_anime[anime.name] = anime.episode_no
		data_export(pref_anime, "dict", 'pref_anime.l')

		print("Download now? (y/n):")
		input_ = input()

		if input_ == 'y':
			anime.download()

	elif input_ == '2':
		black_list.append(anime.name)
		data_export(black_list, 'list', 'black_list.l')
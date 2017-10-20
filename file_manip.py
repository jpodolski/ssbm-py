#!/usr/bin/python3

# ========== DOXYGEN ==========
## @file file_manip.py
## @author Jeff Podolski


from match import Match
from PIL import Image, ImageTk
from utilities import *

def gen_char_filename(match, player_index):
	player_string = "player" + str(player_index)
	print ("media/stock/" + str(character_names.index(match.player[player_index].get_char())) + "_" + str(match.player[player_index].get_sub_color()) + ".png")
	return ("media/stock/" + str(character_names.index(match.player[player_index].get_char())) + "_" + str(match.player[player_index].get_sub_color()) + ".png")

def write_stock_icons(match):
	for n in range (1,4):
		stock = Image.open(gen_char_filename(match, n))
		stock.save("OBS/p" + str(n) + "_char.png", "PNG")

def write_player_tags(match):
	for n in range (1,4):
		file = open("OBS/p" + str(n) + "_tag", "w")
		player_string = "player" + str(n)
		player = getattr(match, player_string)
		file.write(player.get_tag())
		file.close()

def write_player_prefixes(match):
	for n in range (1,4):
		file = open("OBS/p" + str(n) + "_prefix", "w")
		player_string = "player" + str(n)
		player = getattr(match, player_string)
		file.write(player.get_prefix())
		file.close()


def write_team_images(match):
	print("placeholder")

def write_shit():
	print("placeholder")

def export_player_append():
	print("placeholder")

def write_team_names():
	print("yo")
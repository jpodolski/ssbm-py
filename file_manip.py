## @file file_manip.py
## @author Jeff Podolski
## @todo
#   - Make this work
#   - Add real functions
#   - Clean and comment everything

# ==============================================================================
"""

FILE_MANIP.PY

Attribution 4.0 International (CC BY 4.0)

All code below is free and open source, intended to better the smash community
You are free to copy, modify, and redistribute this code as long as credit
is given to the original author (Jeff Podolski). Check out the source!

Github Repo: http://github.com/jpodolski/ssbm-py
Sharing License: https://creativecommons.org/licenses/by/4.0/

"""
# ==============================================================================

from match import Match
from PIL import Image, ImageTk
from utilities import *

def gen_char_filename(match, player_index):
	player_string = "player" + str(player_index)
	print ("media/stock/" + str(character_names.index(match.player[player_index].get_char())) + "_" + str(match.player[player_index].get_sub_color()) + ".png")
	return ("media/stock/" + str(character_names.index(match.player[player_index].get_char())) + "_" + str(match.player[player_index].get_sub_color()) + ".png")

def write_stock_icons(match):
	for n in range (0,4):
		stock = Image.open(gen_char_filename(match, n))
		stock.save("OBS/p" + str(n+1) + "_char.png", "PNG")

def write_player_tags(match, tags):
	for n in range (0,4):
		match.player[n].set_tag(tags[n])
		file = open("OBS/p" + str(n+1) + "_tag", "w")
		file.write(match.player[n].get_tag())
		file.close()

def write_player_prefixes(match):
	for n in range (0,4):
		file = open("OBS/p" + str(n+1) + "_prefix", "w")
		file.write(match.player[n].get_prefix())
		file.close()


def write_team_images(match):
	print("placeholder")

def write_shit():
	print("placeholder")

def export_player_append():
	print("placeholder")

def write_team_names():
	print("yo")
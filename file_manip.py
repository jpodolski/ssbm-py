## @file file_manip.py
## @author Jeff Podolski
## @todo
#   - Make this work (DONE)
#   - Add real functions (KIND OF DONE)
#   - Add in pickle, html, json, etc support (UGH)

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
from information import *

import fileinput
def write_html_tags(player_frames):
	for n in range (0,4):
		with open("templates/tag.html", 'r') as in_file :
			filedata = in_file.read()
		filedata = filedata.replace('$PLAYER', player_frames[n].get_tag())
		with open("OBS/p" + str(n+1) + "_tag.html", 'w') as out_file:
			out_file.write(filedata)

def gen_char_filename(char, sub_color):
	return ("media/stock/" + str(char) + "_" + str(sub_color) + ".png")

def write_stock_icons(player_frames):
	for n in range (0,4):
		stock = Image.open(gen_char_filename(player_frames[n].get_char(), player_frames[n].get_sub_color()))
		stock.save("OBS/p" + str(n+1) + "_char.png", "PNG")

def write_player_tags(player_frames):
	for n in range (0,4):
		file = open("OBS/p" + str(n+1) + "_tag.txt", "w")
		file.write(player_frames[n].get_tag())
		file.close()

def write_player_prefixes(match):
	for n in range (0,4):
		file = open("OBS/p" + str(n+1) + "_prefix.txt", "w")
		file.write(match.player[n].get_prefix())
		file.close()

def write_scores(side, score):
	file = open("OBS/score_" + str(side+1) + ".txt", "w")
	file.write(str(score))
	file.close()

def update(player_frames):
	for n in range (0,4):
		write_stock_icons(player_frames)
		write_player_tags(player_frames)
		write_html_tags(player_frames)
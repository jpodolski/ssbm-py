#!/usr/bin/python3

# ========== DOXYGEN ==========
## @file file_manip.py
## @author Jeff Podolski


from match import Match
from PIL import Image, ImageTk
from utilities import *

def gen_char_filename(match, player):
	if(player == 1):
		return ("media/stock/" + str(character_names.index(match.p1.get_char())) + "_" + str(match.p1.get_sub_color()) + ".png")
	if(player == 2):
		return ("media/stock/" + str(character_names.index(match.p2.get_char())) + "_" + str(match.p2.get_sub_color()) + ".png")
	if(player == 3):
		return ("media/stock/" + str(character_names.index(match.p3.get_char())) + "_" + str(match.p3.get_sub_color()) + ".png")
	if(player == 4):
		return ("media/stock/" + str(character_names.index(match.p4.get_char())) + "_" + str(match.p4.get_sub_color()) + ".png")

def write_stock_icons(match):
	stock1 = Image.open(gen_char_filename(match, 1))
	stock1.save("OBS/p1_char.png", "PNG")
	stock2 = Image.open(gen_char_filename(match, 2))
	stock2.save("OBS/p2_char.png", "PNG")
	stock3 = Image.open(gen_char_filename(match, 3))
	stock3.save("OBS/p3_char.png", "PNG")
	stock4 = Image.open(gen_char_filename(match, 4))
	stock4.save("OBS/p4_char.png", "PNG")

def write_team_names():
	print("yo")
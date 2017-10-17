from tkinter import *
from match import Match
from PIL import Image, ImageTk

def gen_char_filename(match, player):
	if(player == 1):
		return ("media/stock/" + str(character_names.index(pA_char.get())) + "_" + str(match.p1.get_sub_color()) + ".png")
	if(player == 2):
		return ("media/stock/" + str(character_names.index(pB_char.get())) + "_" + str(match.p2.get_sub_color()) + ".png")
	if(player == 3):
		return ("media/stock/" + str(character_names.index(pC_char.get())) + "_" + str(match.p3.get_sub_color()) + ".png")
	if(player == 4):
		return ("media/stock/" + str(character_names.index(pD_char.get())) + "_" + str(match.p4.get_sub_color()) + ".png")
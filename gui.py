#!/usr/bin/python3

## @file player.py
## @author Jeff Podolski
## @todo
#   - Add tabs for settings
#   - Fix file write stuff
#   - Fix referencing 

# ==============================================================================
"""

GUI.PY

Attribution 4.0 International (CC BY 4.0)

All code below is free and open source, intended to better the smash community
You are free to copy, modify, and redistribute this code as long as credit
is given to the original author (Jeff Podolski). Check out the source!

Github Repo: http://github.com/jpodolski/ssbm-py
Sharing License: https://creativecommons.org/licenses/by/4.0/

"""
# ==============================================================================

from tkinter import *
import tkinter.ttk as ttk
from file_manip import *
from match import Match 
from PIL import Image, ImageTk
from information import *
import math

top = Tk() #Define top 

nbook = ttk.Notebook(top)
f1 = ttk.Frame(nbook)   # first page, which would get widgets gridded into it
f2 = ttk.Frame(nbook)   # second page
f3 = ttk.Frame(nbook)   # second page
nbook.add(f1, text='Player Info')
nbook.add(f2, text='Settings')
nbook.add(f3, text='Scene Control')

nbook.grid()

current_match = Match()
char = []
port = []
char_icons = []
player_frames = []
images = []
tkimgs = []

def update(match):
	tags = []
	for n in range (0,4):
		tags.append(player_frames[n].tag.get())
	write_stock_icons(match)
	write_player_tags(match, tags)

def update_character(match, player_index=0):
	for player_index in range (0, 4):
		match.player[player_index].set_char(char[player_index].get())
		images[player_index] = Image.open(gen_char_filename(match, player_index))
		tkimgs[player_index] = ImageTk.PhotoImage(images[player_index])
		char_icons[player_index].configure(image = tkimgs[player_index])
		char_icons[player_index].image = tkimgs[player_index]

# ==================================================================
#			PLAYER 1 GUI ELEMENTS
# ==================================================================

def select_char(index, match, player):
	print ("test")

def inc_color(match, player_index, amt):
	match.player[player_index].set_sub_color(current_match.player[player_index].get_sub_color()+amt)
	update_character(match)

for n in range (0, 4):
	char_variable = StringVar(top)
	char.append(char_variable)
	char[n].set("Generic")
	port_variable = StringVar(top)
	port.append(port_variable)
	port[n].set("Player " + str(n+1))
	img = Image.open("media/stock/26_0.png")
	images.append(img)
	tkimg = ImageTk.PhotoImage(images[n])
	tkimgs.append(tkimg)

for n in range (0, 4):
	pframe = ttk.LabelFrame(f1, text = "Player " + str(n+1))
	pframe.grid(column = math.floor(n/2), row = n%2)
	player_frames.append(pframe)

	tag_label = ttk.Label(player_frames[n], text="Tag:")
	tag_label.grid(row = 0, column = 0, sticky = W)

	port_label = ttk.Label(player_frames[n], text="Port:")
	port_label.grid(row = 1, column = 5, sticky = W)

	prefix_label = ttk.Label(player_frames[n], text="Prefix:")
	prefix_label.grid(row = 0, column = 2, columnspan=2, sticky = W)

	tag = ttk.Entry(player_frames[n])
	tag.grid(row = 0, column = 1, columnspan = 1)

	prefix = ttk.Entry(player_frames[n])
	prefix.grid(row = 0, column = 3, columnspan = 4)

	port_dropdown = ttk.OptionMenu(player_frames[n], port[n], command = lambda _: update_character(current_match, n), *ports)
	port_dropdown.grid(row = 1, column = 6, columnspan = 1, sticky = EW)

	char_dropdown = ttk.OptionMenu(player_frames[n], char[n], command = lambda _: update_character(current_match, n), *character_names)
	char_dropdown.grid(row = 1, column = 0, columnspan = 2, sticky = EW)


	char_prevcolor = ttk.Button(player_frames[n], text = "<", width=1)
	char_prevcolor.config(command = lambda i=n: inc_color(current_match, i, -1))
	char_prevcolor.grid(row = 1, column = 2)

	char_icon = ttk.Label(player_frames[n], image = tkimgs[n])
	char_icon.grid(row = 1, column = 3)
	char_icons.append(char_icon)

	char_nextcolor = ttk.Button(player_frames[n], text = ">", width=1)
	char_nextcolor.config(command = lambda i=n: inc_color(current_match, i, 1))
	char_nextcolor.grid(row = 1, column = 4)


update_button = ttk.Button(top, text = "UPDATE", command = lambda: update(current_match))
update_button.grid(row = 10, column = 0)

#C1 = Canvas(top, image = 
top.mainloop()
#top.call('wm', 'attributes', '.', '-topmost', '1') #Keep gui on top.mainloop()

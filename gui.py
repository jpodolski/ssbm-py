#!/usr/bin/python3

# ========== DOXYGEN ==========
## @file gui.py

## @author Jeff Podolski

## @todo testing this
# - This is one item
# - This is another item
# - Testing this thing

from tkinter import *
import tkinter.ttk as ttk
from file_manip import *
from match import Match
from PIL import Image, ImageTk
from information import *
import math

top = Tk()
current_match = Match()

char = []
port = []
char_icons = []
player_frames = []
images = []
tkimgs = []

def update(match):
	for n in range (0,4):
		player_string = "player" + str(n)
		player = getattr(match, player_string)
		player.set_tag(tag[n].get())
		# p1_tag_text.delete('1.0', END)
		# p1_tag_text.insert(INSERT, p1_tag.get())
		write_stock_icons(match)
		write_player_tags(match)


#			 ________   ______    ______   __       __               ______   __    __  ________ 		 __  __ 
#			/        | /      \  /      \ /  \     /  |             /      \ /  |  /  |/        |		/  |/  |
#			$$$$$$$$/ /$$$$$$  |/$$$$$$  |$$  \   /$$ |            /$$$$$$  |$$ |  $$ |$$$$$$$$/ 		$$ |$$ |
#			    /$$/  $$ |  $$ |$$ |  $$ |$$$  \ /$$$ |            $$ |  $$ |$$ |  $$ |   $$ |   		$$ |$$ |
#			   /$$/   $$ |  $$ |$$ |  $$ |$$$$  /$$$$ |            $$ |  $$ |$$ |  $$ |   $$ |   		$$ |$$ |
#			  /$$/    $$ |  $$ |$$ |  $$ |$$ $$ $$/$$ |            $$ |  $$ |$$ |  $$ |   $$ |   		$$/ $$/ 
#			 /$$/____ $$ \__$$ |$$ \__$$ |$$ |$$$/ $$ |            $$ \__$$ |$$ \__$$ |   $$ |   		 __  __ 
#			/$$      |$$    $$/ $$    $$/ $$ | $/  $$ |            $$    $$/ $$    $$/    $$ |   		/  |/  |
#			$$$$$$$$/  $$$$$$/   $$$$$$/  $$/      $$/              $$$$$$/   $$$$$$/     $$/    		$$/ $$/ 

# 	make sure update is a compresensive and accessible function that writes to file

def update_character(match, player_index):
	#TODO: Separate this from color updates
	for player_index in range (0, 4):
		match.player[player_index].set_char(char[player_index].get())
		images[player_index] = Image.open(gen_char_filename(match, player_index))
		tkimgs[player_index] = ImageTk.PhotoImage(images[player_index])
		char_icons[player_index].configure(image = tkimgs[player_index])
		char_icons[player_index].image = tkimgs[player_index]

		# match.player2.set_char(pB_char.get())
		# pB_img = Image.open(gen_char_filename(match, 2))
		# pB_tkimg = ImageTk.PhotoImage(pB_img)
		# pB_char_icon.configure(image = pB_tkimg)
		# pB_char_icon.image = pB_tkimg

# ==================================================================
#			PLAYER 1 GUI ELEMENTS
# ==================================================================

def select_char(index, match, player):
	print ("test")

def inc_color(match, player_index, amt):
	mod_value = 1+char_mod_table[character_names.index(match.player[player_index].get_char())]
	new_color = (match.player[player_index].get_sub_color() + amt) % mod_value 
	match.player[player_index].set_sub_color(new_color)
	images[player_index] = Image.open(gen_char_filename(match, player_index))
	tkimgs[player_index] = ImageTk.PhotoImage(images[player_index])
	char_icons[player_index].configure(image = tkimgs[player_index])
	char_icons[player_index].image = tkimgs[player_index]


# ==================================================================
#			PLAYER 1 GUI ELEMENTS
# ==================================================================



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



"""
for i in range (1,10):
	exec("label" + str(i) + " = Label(top, text = \"LABEL \" + str(i))")
	exec("label" + str(i) + ".grid(row = " + str(i+2) + ", column = 10)")

for i in range (1,10):
	print("a")
	labelstring = 'labelll' + str(i)
#	$str(i) = Label(top, text = labelstring)
#	$i.grid(row = + str(i+2), column = 9)
"""



for n in range (0, 4):
	pframe = LabelFrame(top, text = "Player " + str(n+1))
	pframe.grid(column = math.floor(n/2), row = n%2)
	player_frames.append(pframe)

	tag_label = Label(player_frames[n], text="Tag:")
	tag_label.grid(row = 0, column = 0, sticky = W)

	port_label = Label(player_frames[n], text="Port:")
	port_label.grid(row = 1, column = 5, sticky = W)

	prefix_label = Label(player_frames[n], text="Prefix:")
	prefix_label.grid(row = 0, column = 2, columnspan=2, sticky = W)

	tag = Entry(player_frames[n])#, bd = 1)
	tag.grid(row = 0, column = 1, columnspan = 1)

	prefix = Entry(player_frames[n])#, bd = 1""")
	prefix.grid(row = 0, column = 3, columnspan = 4)

	port_dropdown = OptionMenu(player_frames[n], port[n], command = lambda _: update_character(current_match, n), *ports)
	port_dropdown.grid(row = 1, column = 6, columnspan = 1, sticky = EW)

# p1_tag_text = Text(top, height = 1, width = 1)
# p1_tag_text.grid(row = 0, column = 10)

	char_dropdown = OptionMenu(player_frames[n], char[n], command = lambda _: update_character(current_match, n), *character_names)
	char_dropdown.grid(row = 1, column = 0, columnspan = 2, sticky = EW)


	char_prevcolor = Button(player_frames[n], text = "<")
	char_prevcolor.option_add("belongs_to", n, priority=None)
	char_prevcolor.config(command = lambda: inc_color(current_match, n, -1))
	char_prevcolor.grid(row = 1, column = 2)

	char_icon = Label(player_frames[n], image = tkimgs[n])
	char_icon.grid(row = 1, column = 3)
	char_icons.append(char_icon)

	char_prevcolor = Button(player_frames[n], text = ">")
	char_prevcolor.config(command = lambda: current_match.player[n].set_sub_color(current_match.player[n].get_sub_color()+1))
	char_prevcolor.grid(row = 1, column = 4)


update_button = Button(top, text = "UPDATE", command = lambda: update(current_match))
update_button.grid(row = 10, column = 0)

#C1 = Canvas(top, image = 
top.mainloop()
top.call('wm', 'attributes', '.', '-topmost', '1') #Keep gui on top.mainloop()

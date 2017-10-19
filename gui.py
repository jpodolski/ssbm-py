#!/usr/bin/python3

# ========== DOXYGEN ==========
## @file gui.py

## @author Jeff Podolski

## @todo testing this
# - This is one item
# - This is another item
# - Testing this thing

from tkinter import *
from file_manip import *
from match import Match
from PIL import Image, ImageTk
from information import *

top = Tk()
current_match = Match()

def update(match):
	match.set_tagA(p1_tag.get())
	p1_tag_text.delete('1.0', END)
	p1_tag_text.insert(INSERT, p1_tag.get())
	write_stock_icons(match)


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

def update_characters(match):
	#TODO: Separate this from color updates
	match.player1.set_char(p1_char.get())
	p1_img = Image.open(gen_char_filename(match, 1))
	p1_tkimg = ImageTk.PhotoImage(p1_img)
	p1_char_icon.configure(image = p1_tkimg)
	p1_char_icon.image = p1_tkimg

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


def inc_color(match, player, amt):
	if(player == 1):
		p1_new_color = (match.player1.get_sub_color() + amt)%(1+char_mod_table[(character_names.index(match.player1.get_char()))]) 
		match.player1.set_sub_color( )
		print( (match.player1.get_sub_color() + amt)%(1+char_mod_table[(character_names.index(match.player1.get_char()))]))
		p1_img = Image.open(gen_char_filename(match, 1))
		p1_tkimg = ImageTk.PhotoImage(p1_img)
		p1_char_icon.configure(image = p1_tkimg)
		p1_char_icon.image = p1_tkimg

	if(player == 2):
		match.player2.set_sub_color( (match.player2.get_sub_color() + amt)%(1+char_mod_table[(character_names.index(match.player2.get_char()))]))
		p2_img = Image.open(gen_char_filename(match, 2))
		p2_tkimg = ImageTk.PhotoImage(p2_img)
		p2_char_icon.configure(image = p2_tkimg)
		p2_char_icon.image = p2_tkimg
	if(player == 3):
		match.player3.set_sub_color( (match.player3.get_sub_color() + amt)%(1+char_mod_table[(character_names.index(match.player3.get_char()))]))
		p3_img = Image.open(gen_char_filename(match, 3))
		p3_tkimg = ImageTk.PhotoImage(p3_img)
		p3_char_icon.configure(image = p3_tkimg)
		p3_char_icon.image = p3_tkimg
	if(player == 4):
		match.player4.set_sub_color( (match.player4.get_sub_color() + amt)%(1+char_mod_table[(character_names.index(match.player4.get_char()))]))
		p4_img = Image.open(gen_char_filename(match, 4))
		p4_tkimg = ImageTk.PhotoImage(p4_img)
		p4_char_icon.configure(image = p4_tkimg)
		p4_char_icon.image = p4_tkimg


# ==================================================================
#			PLAYER 1 GUI ELEMENTS
# ==================================================================
p1_char = StringVar(top)
p1_port = StringVar(top)
p1_char = StringVar(top)
p1_char.set("Generic")
p1_port.set("Player 1")
p1_char.set("Generic") # default value

p1_tag_label = Label(top, text="P1 Tag:")
p1_tag_label.grid(row = 0, column = 0, sticky = W)

p1_port_label = Label(top, text="Port:")
p1_port_label.grid(row = 1, column = 5, sticky = W)

p1_prefix_label = Label(top, text="Prefix:")
p1_prefix_label.grid(row = 0, column = 2, columnspan=2, sticky = W)

p1_tag = Entry(top, bd = 1)
p1_tag.grid(row = 0, column = 1, columnspan = 1)

p1_prefix = Entry(top, bd = 1)
p1_prefix.grid(row = 0, column = 3, columnspan = 4)

p1_port_dropdown = OptionMenu(top, p1_port, command = lambda _: update_characters(current_match), *ports)
p1_port_dropdown.grid(row = 1, column = 6, columnspan = 1, sticky = EW)

# p1_tag_text = Text(top, height = 1, width = 1)
# p1_tag_text.grid(row = 0, column = 10)

p1_char_dropdown = OptionMenu(top, p1_char, command = lambda _: update_characters(current_match), *character_names)
p1_char_dropdown.grid(row = 1, column = 0, columnspan = 2, sticky = EW)

p1_char_prevcolor = Button(top, text = "<", command = lambda: inc_color(current_match, 1, -1))
p1_char_prevcolor.grid(row = 1, column = 2)

p1_img = Image.open("media/stock/26_0.png")
p1_tkimg = ImageTk.PhotoImage(p1_img)

p1_char_icon = Label(top, image = p1_tkimg)
p1_char_icon.grid(row = 1, column = 3)

p1_char_nextcolor = Button(top, text = ">", command = lambda: inc_color(current_match, 1, 1))
p1_char_nextcolor.grid(row = 1, column = 4)


update_button = Button(top, text = "UPDATE", command = lambda: update(current_match))
update_button.grid(row = 2, column = 0)

#C1 = Canvas(top, image =)

top.call('wm', 'attributes', '.', '-topmost', '1') #Keep gui on top
top.mainloop()
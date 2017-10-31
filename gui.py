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
from PlayerFrame import *

top = Tk() #Define top 
top.winfo_toplevel().title("miniGIMR")

nbook = ttk.Notebook(top)
f1 = ttk.Frame(nbook, borderwidth = 6)   # first page, which would get widgets gridded into it
f2 = ttk.Frame(nbook)   # second page
f3 = ttk.Frame(nbook)   # third page
nbook.add(f1, text='Player Info')
nbook.add(f2, text='Settings')
nbook.add(f3, text='Scene Control')

nbook.grid()

current_match = Match()
player_frames = []

def update(player_frames):
	for n in range (0,4):
		write_stock_icons(player_frames)
		write_player_tags(player_frames)

for n in range (0, 4):
	pframe_object = PlayerFrame(f1)
	player_frames.append(pframe_object)
	player_frames[n].set_player(n+1)
	player_frames[n].align()
	
update_button = Button(top, text = "UPDATE", command = lambda: update(player_frames))
update_button.grid(row = 10, column = 0)


top.call('wm', 'attributes', '.', '-topmost', '1') #Keep gui on top
top.mainloop()

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
from Dashboard import *
from SceneSwitch import *

top = Tk() #Define top 
top.winfo_toplevel().title("miniGIMR")

nbook = ttk.Notebook(top)
f1 = ttk.Frame(nbook, borderwidth = 6)   # first page, which would get widgets gridded into it
f2 = ttk.Frame(nbook)   # second page
f3 = ttk.Frame(nbook)   # third page
f4 = ttk.Frame(nbook)   # third page
f5 = ttk.Frame(nbook)   # third page
nbook.add(f1, text='Dashboard')
nbook.add(f2, text='Stream Info')
nbook.add(f3, text='HTML Output')
nbook.add(f4, text='Scene Control')
nbook.add(f5, text='Settings')

nbook.grid()

current_match = Match()
dashboard = Dashboard(f1)
scene_swtich = SceneSwitch(f4)


def switch():
	nbook.select(1)
	
switchbutton = ttk.Button(f4, text = "Add/Remove Scenes", command = lambda: switch())
switchbutton.grid()

html_object = ttk.Label(f3, text = "Settings coming soon. For now, just edit ssbm-py/templates/tag.css yourself")
html_object.pack()

top.resizable(0,0)
top.call('wm', 'attributes', '.', '-topmost', '1') #Keep gui on top
top.mainloop()

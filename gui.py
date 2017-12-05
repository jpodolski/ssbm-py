#!/usr/bin/python3

## @file player.py
## @author Jeff Podolski
## @todo
#   - clean it up, make as compact as possible
#   - run through pylint
#   - tkinter -> tk

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


import tkinter.ttk as ttk
from tkinter import *
from PIL import Image, ImageTk
from PlayerFrame import *
from Dashboard import *
from information import *
from file_manip import *

from SceneSwitch import *

top = Tk() #Define top
top.winfo_toplevel().title("miniGIMR")

nbook = ttk.Notebook(top)
frame_1 = ttk.Frame(nbook, borderwidth = 6)   # first page, which would get widgets gridded into it
frame_2 = ttk.Frame(nbook)   # second page
frame_3 = ttk.Frame(nbook)   # third page
frame_4 = ttk.Frame(nbook)   # third page
frame_5 = ttk.Frame(nbook)   # third page
nbook.add(frame_1, text='Dashboard')
nbook.add(frame_2, text='Stream Info')
nbook.add(frame_3, text='HTML Output')
nbook.add(frame_4, text='Scene Control')
nbook.add(frame_5, text='Settings')

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

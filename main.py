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
from classes.player_frame import *
from classes.dashboard import *
from classes.stream_info import *
from information import *
from classes.file_manip import *
from classes.scene_switch import *
from classes.load_window import *
from classes.load_session import *
from classes.settings import *
from classes.main_window import *
#from classes.initialize import *

# start_load_menu()
status = start_load_menu()
if status != 0:
	start_main_window(status)

#!/usr/bin/python3

## @file StreamInfo.py
## @author Jeff Podolski
## @todo
#   - Maybe change file_manip to provide a generic file-writer for txts
#   - Actually program in the functions

# ==============================================================================

"""
STREAMINFO.PY
Attribution 4.0 International (CC BY 4.0)
All code below is free and open source, intended to better the smash community
You are free to copy, modify, and redistribute this code as long as credit
is given to the original author (Jeff Podolski). Check out the source!
Github Repo: http://github.com/jpodolski/ssbm-py
Sharing License: https://creativecommons.org/licenses/by/4.0/
"""

# ==============================================================================

import tkinter.ttk as ttk # pylint: disable=import-error
# from file_manip import *

class StreamInfo(object): # pylint: disable=too-few-public-methods
    """
    A GUI class that contains the notebook frame that controls
    the information about the stream/event
    """

    def __init__(self, parent):
        self.main = ttk.Frame(parent)
        self.main.grid()
        self.scene_group = ttk.Frame(self.main)
        
        self.tournament_label = ttk.Label(self.main, text='Tournament Name')
        self.tournament_label.grid(row=0, column=0)
        self.tournament_text = ttk.Entry(self.main)
        self.tournament_text.grid(row=0, column=1)

        self.bracket_label = ttk.Label(self.main, text='Bracket Link')
        self.bracket_label.grid(row=1, column=0)
        self.bracket_text = ttk.Entry(self.main)
        self.bracket_text.grid(row=1, column=1)

        self.round_label = ttk.Label(self.main, text='Match Round')
        self.round_label.grid(row=2, column=0)
        self.round_text = ttk.Entry(self.main)
        self.round_text.grid(row=2, column=1)

        self.comm1_label = ttk.Label(self.main, text='Commentator 1')
        self.comm1_label.grid(row=3, column=0)
        self.comm1_text = ttk.Entry(self.main)
        self.comm1_text.grid(row=3, column=1)

        self.comm2_label = ttk.Label(self.main, text='Commentator 2')
        self.comm2_label.grid(row=4, column=0)
        self.comm2_text = ttk.Entry(self.main)
        self.comm2_text.grid(row=4, column=1)

        self.custom_label = ttk.Entry(self.main)
        self.custom_label.grid(row=5, column=0)
        self.custom_add = ttk.Button(self.main, text = "Add Custom Field") 
        self.custom_add.grid(row=5, column=1)






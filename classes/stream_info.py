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
        
        self.bracket_label = ttk.Label(self.main, text='Bracket Link')
        self.bracket_label.grid(row=0, column=0)

        """self.
        """

        # self.char_frame_left.grid(column=0, row=0)






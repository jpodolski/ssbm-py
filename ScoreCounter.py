#!/usr/bin/python3

## @file PlayerFrame.py
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


class ScoreCounter:
    """
    A GUI class that contains the components responsible
    for manipulating one score variable
    """

    """ INITIALIZATION """
        
    def __init__(self, parent):
        """ Initialize the GUI elements and private variables. """
        self.__side = 0
        self.__score = 0
        self.score_frame = ttk.Frame(parent)
        self.score_frame.grid()
        self.tag_label = ttk.Label(self.score_frame, text="Placeholder " + str(self.__side + 1), font = ("Helvetica", 24))
        self.tag_label.grid(row = 0, column = 0, sticky = W)

    """ ACCESSORS """

    def get_score(self):
        """ Returns tag as string """
        return(self.__score)

    def get_side(self):
        """ Returns char as int """
        return(self.__side)

    """ INTERNAL FUNCTIONS """

    def inc_score(self, amt):
        """ Adds the value amt to __sub_color and refreshes image. Called by char_nextcolor and char_prevcolor """
        self.__sub_color = (self.__sub_color + amt)%(char_mod_table[self.__char]+1)



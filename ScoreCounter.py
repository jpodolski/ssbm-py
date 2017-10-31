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
        self.score_frame = ttk.LabelFrame(parent, text = "Player" + str(self.__player), relief="sunken", borderwidth=10)
        self.score_frame.grid(row = 0, column = self.__player)
        self.tag_label = ttk.Label(self.score_frame, text="Score")
        self.tag_label.grid(row = 0, column = 0, sticky = W)

    """ ACCESSORS """

    def get_score(self):
        """ Returns tag as string """
        return(self.__score)

    def get_side(self):
        """ Returns char as int """
        return(self.__side)

    def set_side(self, new_player):
        if new_player > 0:
            self.__player = 1

    """ INTERNAL FUNCTIONS """

    def align(self):
        """ Arranges modules inside the frame and sets the appropriate Label text """
        self.pframe.grid(row = math.floor((self.__player-1)/2), column = (self.__player-1)%2)
        self.pframe.config(text = "Player" + str(self.__player))

    def inc_color(self, amt):
        """ Adds the value amt to __sub_color and refreshes image. Called by char_nextcolor and char_prevcolor """
        self.__sub_color = (self.__sub_color + amt)%(char_mod_table[self.__char]+1)
        self.__image = Image.open(gen_char_filename(self.__char, self.__sub_color))
        self.__tkimg = ImageTk.PhotoImage(self.__image)
        self.char_icon.configure(image = self.__tkimg)


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

import tkinter.ttk as ttk
from file_manip import write_scores


class ScoreCounter(object):
    """
    A GUI class that contains the components responsible
    for manipulating one score variable
    """
    def __init__(self, parent):
        """ Initialize the GUI elements and private variables. """
        self.__side = 0
        self.__score = 0
        self.score_frame = ttk.Frame(parent)
        self.score_frame.grid()
        self.score_label = ttk.Label(self.score_frame, text=str(self.__score))
        self.score_label.configure(font=("Helvetica", 48))
        self.inc_button = ttk.Button(self.score_frame, text="+", command=lambda: self.inc_score(1))
        self.dec_button = ttk.Button(self.score_frame, text="-", command=lambda: self.inc_score(-1))
        self.inc_button.configure(width=1)
        self.dec_button.configure(width=1)
        self.score_label.grid(row=1, column=0)
        self.inc_button.grid(row=0, column=0)
        self.dec_button.grid(row=2, column=0)

    def get_side(self):
        """ returns __side """
        return self.__side

    def get_score(self):
        """ returns __score """
        return self.__score

    def set_side(self, side):
        """ Setter for __side """
        self.__side = side

    def inc_score(self, amt):
        """ Adds the value amt to __score, refreshes the label, and writes the score out. """
        self.__score = self.__score+amt
        self.score_label.config(text=str(self.__score))
        write_scores(self.__side, self.__score)

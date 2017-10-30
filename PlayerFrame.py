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


class PlayerFrame:
    """
    A GUI class that contains the components responsible
    for editing one Player item in the InfoTab
    """
        
    #  Initialization
    #  ==============================
    def __init__(self, parent):
        self.__player = 0
        self.__port = 0
        self.__tkport = IntVar()
        self.__tkport.set(0)
        self.__tkchar = StringVar()
        self.__tkchar.set("HELLO")
        self.__char = "Generic"
        self.__sub_color = 0
        self.__image = Image.open("media/stock/26_0.png")
        self.__tkimg = ImageTk.PhotoImage(self.__image)
        self.pframe = LabelFrame(parent, text = "Player" + str(self.__player))
        self.pframe.grid(row = 0, column = self.__player)
        self.tag_label = Label(self.pframe, text="Tag:")
        self.tag_label.grid(row = 0, column = 0, sticky = W)

        self.port_label = Label(self.pframe, text="Port:")
        self.port_label.grid(row = 1, column = 5, sticky = W)

        self.prefix_label = Label(self.pframe, text="Prefix:")
        self.prefix_label.grid(row = 0, column = 2, columnspan=2, sticky = W)

        self.tag = Entry(self.pframe)
        self.tag.grid(row = 0, column = 1, columnspan = 1)

        self.prefix = Entry(self.pframe)
        self.prefix.grid(row = 0, column = 4, columnspan = 3)

        self.port_dropdown = OptionMenu(self.pframe, self.__tkport, command = lambda _: self.select_port(), *ports)
        self.port_dropdown.grid(row = 1, column = 6, columnspan = 1, sticky = EW)

        self.char_dropdown = OptionMenu(self.pframe, self.__tkchar, command = lambda _: self.select_character(self), *character_names)
        self.char_dropdown.grid(row = 1, column = 0, columnspan = 2, sticky = EW)

        self.char_prevcolor = Button(self.pframe, text = "<")
        self.char_prevcolor.config(command = lambda: self.inc_color(-1))
        self.char_prevcolor.grid(row = 1, column = 2)

        self.char_icon = Label(self.pframe, image = self.__tkimg)
        self.char_icon.grid(row = 1, column = 3)

        self.char_nextcolor = Button(self.pframe, text = ">")
        self.char_nextcolor.config(command = lambda: self.inc_color(1))
        self.char_nextcolor.grid(row = 1, column = 4)

    def set_player(self, new_player):
        self.__player = new_player
    def set_port(self, new_port):
        self.__port = new_port
    def set_char(self, new_char):
        self.__char = new_char
    def set_sub_color(self, new_sub_color):
        self.__sub_color = new_sub_color
    def align(self):
        self.pframe.grid(row = math.floor((self.__player-1)/2), column = (self.__player-1)%2)
        self.pframe.config(text = "Player" + str(self.__player))
    def inc_color(self, amt):
        self.__sub_color = (self.__sub_color + amt)%(char_mod_table[character_names.index(self.__char)]+1)
        self.__image = Image.open(gen_char_filename(self.__char, self.__sub_color))
        self.__tkimg = ImageTk.PhotoImage(self.__image)
        self.char_icon.configure(image = self.__tkimg)
    def select_character(self, string):
        self.__char = self.__tkchar.get()
        self.__sub_color = 0
        self.__image = Image.open(gen_char_filename(self.__char, self.__sub_color))
        self.__tkimg = ImageTk.PhotoImage(self.__image)
        self.char_icon.configure(image = self.__tkimg)




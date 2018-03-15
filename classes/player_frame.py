#!/usr/bin/python3

## @file PlayerFrame.py
## @author Jeff Podolski
## @todo
#   - Better documentation
#   - Works fine tbh

# ==============================================================================
"""
PLAYERFRAME.PY

Attribution 4.0 International (CC BY 4.0)
All code below is free and open source, intended to better the smash community
You are free to copy, modify, and redistribute this code as long as credit
is given to the original author (Jeff Podolski). Check out the source!
Github Repo: http://github.com/jpodolski/ssbm-py
Sharing License: https://creativecommons.org/licenses/by/4.0/
"""
# ==============================================================================

from tkinter import * # pylint: disable=import-error
import tkinter.ttk as ttk  # pylint: disable=import-error
from classes.file_manip import gen_char_filename
from classes.match import Match
from PIL import Image, ImageTk
from information import *
# import math

class PlayerFrame(object): # pylint: disable=too-few-public-methods
    """
    A GUI class that contains the components responsible
    for editing one Player item in the InfoTab
    """

    def __init__(self, parent):
        """ Initialize the GUI elements and private variables. """
        self.__player = 0
        self.__port = 0
        self.__tkport = StringVar()
        self.__tkport.set("Player"+str(self.__player))
        self.__tag = StringVar()
        self.__tag.set("Tag")
        self.__prefix = StringVar()
        self.__prefix.set("Prefix")
        self.__tkchar = StringVar()
        self.__tkchar.set("Generic")
        self.__char = 27
        self.__sub_color = 0
        self.__image = Image.open("media/stock/26_0.png")
        self.__tkimg = ImageTk.PhotoImage(self.__image)
        self.pframe = ttk.LabelFrame(parent, relief="sunken", borderwidth=10)
        self.pframe.configure(text="Player"+str(self.__player))
        self.pframe.grid(row=0, column=self.__player)
        self.tag_label = ttk.Label(self.pframe, text="Tag:")
        self.tag_label.grid(row=0, column=0, sticky='W')

        self.port_label = ttk.Label(self.pframe, text="Port:")
        self.port_label.grid(row=1, column=5, sticky='W')

        self.prefix_label = ttk.Label(self.pframe, text="Prefix:")
        self.prefix_label.grid(row=0, column=2, columnspan=2, sticky='W')

        self.tag = ttk.Entry(self.pframe, textvariable=self.__tag)
        self.tag.grid(row=0, column=1, columnspan=1)

        self.prefix = ttk.Entry(self.pframe, textvariable=self.__prefix)
        self.prefix.grid(row=0, column=4, columnspan=3)

        self.port_dropdown = ttk.OptionMenu(self.pframe, self.__tkport, command=lambda _:self.select_port(), *ports)
        self.port_dropdown.grid(row=1, column=6, columnspan=1, sticky='EW')

        self.char_dropdown = ttk.OptionMenu(self.pframe, self.__tkchar, command=lambda _: self.select_character(self), *character_names)
        self.char_dropdown.grid(row=1, column=0, columnspan=2, sticky='EW')

        self.char_prevcolor = ttk.Button(self.pframe, text="<", width=1)
        self.char_prevcolor.config(command=lambda: self.inc_color(-1))
        self.char_prevcolor.grid(row=1, column=2)

        self.char_icon = ttk.Label(self.pframe, image=self.__tkimg)
        self.char_icon.grid(row=1, column=3)

        self.char_nextcolor = ttk.Button(self.pframe, text=">", width=1)
        self.char_nextcolor.config(command=lambda: self.inc_color(1))
        self.char_nextcolor.grid(row=1, column=4)

    def get_tag(self):
        """ Returns tag as StringVar() """
        return self.__tag.get()

    def get_char(self):
        """ Returns char as int """
        return self.__char

    def get_sub_color(self):
        """ Returns sub-color as int (0-N) """
        return self.__sub_color

    def get_port(self):
        """ Returns port as int (1-4) """
        return self.__port

    def get_prefix(self):
        """ Returns prefix as StringVar() """
        return self.__prefix.get()

    def set_player(self, new_player):
        """ sets __player """
        self.__player = new_player

    def set_char(self, new_char):
        """ sets __player """
        self.__char = new_char

    def set_tag(self, new_tag):
        """ sets __tag """
        self.__tag.set(new_tag)

    def set_sub_color(self, new_sub_color):
        """ sets __sub_color """
        self.__sub_color = new_sub_color

    def set_prefix(self, new_prefix):
        """ sets __prefix """
        self.__prefix.set(new_prefix)

    def set_port(self, new_port):
        """ sets __port """
        self.__port = new_port

    def refresh(self):
        self.__image = Image.open(gen_char_filename(self.__char, self.__sub_color))
        self.__tkimg = ImageTk.PhotoImage(self.__image)
        self.char_icon.configure(image = self.__tkimg)
        print(self.__char)
        print(self.__sub_color)

    def align(self):
        """ Arranges modules inside the frame and sets the appropriate Label text """
        # self.pframe.grid(row = math.floor((self.__player-1)/2), column = (self.__player-1)%2)
        self.pframe.config(text="Player"+str(self.__player))

    def inc_color(self, amt):
        """ Adds the value amt to __sub_color and refreshes image. Called by char_nextcolor and char_prevcolor """
        self.__sub_color = (self.__sub_color+amt)%(char_mod_table[self.__char]+1)
        self.__image = Image.open(gen_char_filename(self.__char, self.__sub_color))
        self.__tkimg = ImageTk.PhotoImage(self.__image)
        self.char_icon.configure(image = self.__tkimg)

    def select_character(self, string):
        """ Sets __char to string and resets sub color. Updates image as well """
        self.__char = character_names.index(self.__tkchar.get())
        self.__sub_color = 0
        self.__image = Image.open(gen_char_filename(self.__char, self.__sub_color))
        self.__tkimg = ImageTk.PhotoImage(self.__image)
        self.char_icon.configure(image=self.__tkimg)

    def select_port(self):
        """ Sets __char to string and resets sub color. Updates image as well """
        self.__port = port_dropdown.index(self.__tkchar.get())
        self.__sub_color = 0
        self.__image = Image.open(gen_char_filename(self.__char, self.__sub_color))
        self.__tkimg = ImageTk.PhotoImage(self.__image)
        self.char_icon.configure(image=self.__tkimg)


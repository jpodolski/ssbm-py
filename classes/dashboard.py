#!/usr/bin/python3

## @file Dashboard.py
## @author Jeff Podolski
## @todo
#   - Better documentation

# ==============================================================================
"""
DASHBOARD.PY

Attribution 4.0 International (CC BY 4.0)
All code below is free and open source, intended to better the smash community
You are free to copy, modify, and redistribute this code as long as credit
is given to the original author (Jeff Podolski). Check out the source!
Github Repo: http://github.com/jpodolski/ssbm-py
Sharing License: https://creativecommons.org/licenses/by/4.0/
"""
# ==============================================================================

from tkinter import * # pylint: disable=import-error
import tkinter.ttk as ttk  # pylint: disable=import-errorfrom classes.player_frame import PlayerFrame
from classes.score_counter import ScoreCounter
from classes.file_manip import update
from information import *
from classes.load_session import *
from classes.player_frame import *

class Dashboard(object): # pylint: disable=too-few-public-methods
    """
    A GUI class that contains the components responsible
    for editing one Player item in the InfoTab
    """

    def __init__(self, parent):
        self.player_frames = []
        self.score_frames = []
        self.selected_teams = ["redteam", "greenteam"]
        self.save_name = None
        self.teamA = StringVar()
        self.teamA.set('Red Team') # initial value
        self.teamB = StringVar()
        self.teamB.set('Red Team') # initial value

        """
        Main Frame
        """
        self.main = ttk.Frame(parent)
        self.main.grid()
        self.char_frame_left = ttk.Frame(self.main)
        self.char_frame_left.grid(column=0, row=0)

        self.score_module_frame = ttk.Frame(self.main)
        self.score_module_frame.grid(column=1, row=0)

        self.char_frame_right = ttk.Frame(self.main)
        self.char_frame_right.grid(column=2, row=0)

        self.score_1_frame = ttk.Frame(self.score_module_frame)
        self.score_1 = ScoreCounter(self.score_1_frame)
        self.score_1.set_side(0)
        self.score_1_frame.grid(row=1, column=0)
        self.score_frames.append(self.score_1)

        self.hyphen = ttk.Label(self.score_module_frame, text="-")
        self.hyphen.configure(font=("Helvetica", 48))
        self.hyphen.grid(row=1, column=1)

        self.update_button = ttk.Button(self.score_module_frame, command=lambda: update(self))
        self.update_button.configure(width=10, text="UPDATE")
        self.update_button.grid(row=2, column=0, columnspan=4, rowspan=3, sticky='S')

        self.score_2_frame = ttk.Frame(self.score_module_frame)
        self.score_2 = ScoreCounter(self.score_2_frame)
        self.score_2.set_side(1)
        self.score_2_frame.grid(row=1, column=2)
        self.score_frames.append(self.score_2)

        self.pframe_1 = PlayerFrame(self.char_frame_left)
        self.pframe_1.pframe.grid(row=0)
        self.pframe_1.set_player(1)
        self.pframe_1.align()

        self.pframe_2 = PlayerFrame(self.char_frame_right)
        self.pframe_2.pframe.grid(row=0)
        self.pframe_2.set_player(2)
        self.pframe_2.align()

        self.pframe_3 = PlayerFrame(self.char_frame_left)
        self.pframe_3.pframe.grid(row=1)
        self.pframe_3.set_player(3)
        self.pframe_3.align()

        self.pframe_4 = PlayerFrame(self.char_frame_right)
        self.pframe_4.pframe.grid(row=1)
        self.pframe_4.set_player(4)
        self.pframe_4.align()

        self.player_frames.append(self.pframe_1)
        self.player_frames.append(self.pframe_2)
        self.player_frames.append(self.pframe_3)
        self.player_frames.append(self.pframe_4)

        self.teamA_dropdown = ttk.OptionMenu(self.char_frame_right,
                                             self.teamA,
                                             command=lambda _: self.select_team(),
                                             *team_colors)
        self.teamB_dropdown = ttk.OptionMenu(self.char_frame_left,
                                             self.teamB,
                                             command=lambda _: self.select_team(),
                                             *team_colors)
        self.teamA_dropdown.grid(row = 2)
        self.teamB_dropdown.grid(row = 2)

    def select_team(self):
        self.selected_teams[0] = (self.teamA.get().lower().replace(" ", ""))
        self.selected_teams[1] = (self.teamB.get().lower().replace(" ", ""))




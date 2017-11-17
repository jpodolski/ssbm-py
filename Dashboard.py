from tkinter import *
from PlayerFrame import *
from ScoreCounter import *
from file_manip import *

class Dashboard:
    """
    A GUI class that contains the components responsible
    for editing one Player item in the InfoTab
    """

    """ INITIALIZATION """

    def __init__(self, parent):
        self.player_frames = []
        self.score_frames = []

        self.main = ttk.Frame(parent)
        self.main.grid()
        self.char_frame_left = ttk.Frame(self.main)
        self.char_frame_left.grid(column = 0, row = 0)

        self.score_module_frame = ttk.Frame(self.main)
        self.score_module_frame.grid(column = 1, row = 0)

        self.char_frame_right = ttk.Frame(self.main)
        self.char_frame_right.grid(column = 2, row = 0)

        self.score_1_frame = ttk.Frame(self.score_module_frame)
        self.score_1 = ScoreCounter(self.score_1_frame)
        self.score_1.set_side(0)
        self.score_1_frame.grid(row = 1, column = 0)
        self.score_frames.append(self.score_1)

        self.hyphen = ttk.Label(self.score_module_frame, text = "-", font = ("Helvetica", 48))
        self.hyphen.grid(row = 1, column = 1)

        self.update_button = ttk.Button(self.score_module_frame, width = 10, text = "UPDATE", command = lambda: update(self))
        self.update_button.grid(row = 2, column = 0, columnspan = 4, rowspan = 3, sticky = S)

        self.score_2_frame = ttk.Frame(self.score_module_frame)
        self.score_2 = ScoreCounter(self.score_2_frame)
        self.score_2.set_side(1)
        self.score_2_frame.grid(row = 1, column = 2)
        self.score_frames.append(self.score_2)

        self.pframe_1 = PlayerFrame(self.char_frame_left)
        self.pframe_1.pframe.grid(row = 0)
        self.pframe_1.set_player(1)
        self.pframe_1.align()

        self.pframe_2 = PlayerFrame(self.char_frame_right)
        self.pframe_2.pframe.grid(row = 0)
        self.pframe_2.set_player(2)
        self.pframe_2.align()

        self.pframe_3 = PlayerFrame(self.char_frame_left)
        self.pframe_3.pframe.grid(row = 1)
        self.pframe_3.set_player(3)
        self.pframe_3.align()

        self.pframe_4 = PlayerFrame(self.char_frame_right)
        self.pframe_4.pframe.grid(row = 1)
        self.pframe_4.set_player(4)
        self.pframe_4.align()

        self.player_frames.append(self.pframe_1)
        self.player_frames.append(self.pframe_2)
        self.player_frames.append(self.pframe_3)
        self.player_frames.append(self.pframe_4)


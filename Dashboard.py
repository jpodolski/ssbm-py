from tkinter import *
from PlayerFrame import *
from ScoreCounter import *

class Dashboard:
    """
    A GUI class that contains the components responsible
    for editing one Player item in the InfoTab
    """

    """ INITIALIZATION """
        
    def __init__(self, parent):
        self.main = ttk.Frame(parent)
        self.main.grid()
        self.char_frame_left = ttk.Frame(self.main)
        self.char_frame_left.grid(column = 0, row = 0)

        self.score_module_frame = ttk.Frame(self.main)
        self.score_module_frame.grid(column = 1, row = 0)

        self.char_frame_right = ttk.Frame(self.main)
        self.char_frame_right.grid(column = 2, row = 0)

        self.score_module_object = ScoreCounter(self.score_module_frame)

        self.player_frames = []
        #still gotta repackage these pframes into a list but im too lazy to do that right now

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
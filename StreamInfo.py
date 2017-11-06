from tkinter import *
from PlayerFrame import *
from ScoreCounter import *
from file_manip import *

class StreamInfo:
    """
    A GUI class that contains the components responsible
    for editing one Player item in the InfoTab
    """

    """ INITIALIZATION """
        
    def __init__(self, parent):
        self.main = ttk.Frame(parent)
        self.main.grid()
        self.scene_group = ttk.Frame(self.main)
        self.char_frame_left.grid(column = 0, row = 0)
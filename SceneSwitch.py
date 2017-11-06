from tkinter import *
from PlayerFrame import *
from ScoreCounter import *
from file_manip import *

class SceneSwitch:
    """
    A GUI class for the Scene Switcher tab
    """

    """ INITIALIZATION """
        
    def __init__(self, parent):
        self.main = ttk.Frame(parent)
        self.main.grid()
        self.scene_a = ttk.Button(self.main, text = "Scene A", command = lambda: write_scene("SCENE_A"))
        self.scene_b = ttk.Button(self.main, text = "Scene B", command = lambda: write_scene("SCENE_B"))
        self.scene_c = ttk.Button(self.main, text = "Scene C", command = lambda: write_scene("SCENE_C"))
        self.scene_a.pack()
        self.scene_b.pack()
        self.scene_c.pack()

#!/usr/bin/python3

## @file SceneSwitch.py
## @author Jeff Podolski
## @todo
#   - Basically everything...
#   - Json parser and auto-setup, etc

# ==============================================================================
"""
SCENESWITCH.PY

Attribution 4.0 International (CC BY 4.0)
All code below is free and open source, intended to better the smash community
You are free to copy, modify, and redistribute this code as long as credit
is given to the original author (Jeff Podolski). Check out the source!
Github Repo: http://github.com/jpodolski/ssbm-py
Sharing License: https://creativecommons.org/licenses/by/4.0/
"""
# ==============================================================================

import tkinter.ttk as ttk
from file_manip import write_scene

class SceneSwitch(object):
    """
    A GUI class for the Scene Switcher tab
    """

    def __init__(self, parent):
        self.main = ttk.Frame(parent)
        self.main.grid()
        self.scene_a = ttk.Button(self.main, text="Scene A", command=lambda: write_scene("SCENE_A"))
        self.scene_b = ttk.Button(self.main, text="Scene B", command=lambda: write_scene("SCENE_B"))
        self.scene_c = ttk.Button(self.main, text="Scene C", command=lambda: write_scene("SCENE_C"))
        self.scene_a.pack()
        self.scene_b.pack()
        self.scene_c.pack()

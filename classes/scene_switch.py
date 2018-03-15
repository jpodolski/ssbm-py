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

import tkinter.ttk as ttk # pylint: disable=import-error
from classes.file_manip import write_scene

class SceneSwitch(object): # pylint: disable=too-few-public-methods
    """
    A GUI class for the Scene Switcher tab
    """

    def add_new_scene(argv, display_string, obs_string, main):
        user_scene = ttk.Button(main.main, text=display_string, command=lambda: write_scene(obs_string))
        user_scene.grid(row=3, column=len(main.scenes))
        scene_group = [user_scene, display_string, obs_string]
        main.scenes.append(scene_group)

    def __init__(self, parent):
        self.scenes = []
        self.main = ttk.Frame(parent)
        self.main.grid()


        self.scene_name_label = ttk.Label(text = "Button Name")
        self.scene_name = ttk.Entry(self.main)
        self.scene_name.grid(row=0, column=0)

        self.obs_name_label = ttk.Label(text = "OBS Scene Name")
        self.obs_name = ttk.Entry(self.main)
        self.obs_name.grid(row=0, column=1)

        self.arg1 = self.scene_name.get()
        self.arg2 = self.obs_name.get()
        self.arg_tuple = ()
        self.add_scene_button = ttk.Button(self.main, text="Add scene", command=lambda: self.add_new_scene(self.scene_name.get(), self.obs_name.get(), self))
        self.add_scene_button.grid(row=1, column=0)

    

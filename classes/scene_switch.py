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

import tkinter as tk
import tkinter.ttk as ttk # pylint: disable=import-error
# from classes.file_manip import scene_button_functionality
from math import floor

def scene_button_functionality(self, scene_list, scene_name, delete_mode):
    """ outputs plain text scene name for use with OBS Scene Switcher """
    if (delete_mode):
        with open("obs/text/current_scene.txt", 'w') as out_file:
            out_file.write(scene_name)
    else:
        for i in range(len(scene_list)):
            # print(scene_list[i][2])
            if(scene_name == scene_list[i][2]):
                self.scenes[i][0].destroy()
                self.scenes.pop(i)

def duplicate_scene_check(display_string, obs_string, scene_list):
    for i in range(len(scene_list)):
        if(scene_list[i][1] == display_string):
            print("COLLISION ON DISPLAY NAME " + display_string + " - Cannot add scene")
            return True
        if(scene_list[i][2] == obs_string):
            print("COLLISION ON ID " + obs_string + " - Cannot add scene")
            return True
    return False

class SceneSwitch(object): # pylint: disable=too-few-public-methods
    """
    A GUI class for the Scene Switcher tab
    """


    def self_destruct(self, main):
        self.destroy()

    def __init__(self, parent):
        self.scenes = [] # Please forgive me 
        self.delete_mode = True # This boolean is the inverse of what it should be. Don't touch it
        self.main = ttk.Frame(parent)
        self.main.grid()

        self.style = ttk.Style()
        self.style.configure("BW.TButton", foreground="black")

        """ INSIDE MAIN FRAME """
        self.left_frame = ttk.LabelFrame(self.main,
                                         height=100,
                                         width=30,
                                         text="Scene Switching",
                                         borderwidth=5,
                                         relief="sunken")

        self.left_frame.grid_rowconfigure(index = 1, minsize=100) 
        self.left_frame.grid(row=0, column=0, sticky='n')
        
        """ SPACE DIVIDER """
        self.frame_divider = tk.Canvas(self.main, width=1, height=200)
        self.frame_divider.grid(row=0, column=1, sticky='n')
        self.frame_divider.create_line(5,5,5,500)

        """ FRAME LABEL """
        self.info_pane = ttk.LabelFrame(self.main,
                                        text="Event Information",
                                        borderwidth=5,
                                        relief="sunken")
        self.info_pane.pack_propagate(0)
        self.info_pane.grid(row=0, column=2, sticky='nw')


        """ INSIDE LEFT FRAME """
        self.scene_input_frame = ttk.Frame(self.left_frame, width=180)
        self.scene_input_frame.grid_columnconfigure(index = 0, minsize=100) 
        self.scene_input_frame.grid(row=0, column=0, sticky='nw')

        self.scene_buttons = ttk.Frame(self.left_frame)
        self.scene_buttons.grid(row=1, column=0, sticky='nw')


        """ INSIDE SCENE INPUT FRAME """
        self.scene_input_buttons = ttk.Frame(self.scene_input_frame, width=100)
        self.scene_input_buttons.grid(row=1, column=0)

        self.scene_input_entry = ttk.Frame(self.scene_input_frame, width=100)
        self.scene_input_entry.grid(row=0, column=0)
        self.scene_input_entry.grid_columnconfigure(index = 0, minsize=0) 
        self.scene_input_entry.grid_columnconfigure(index = 1, minsize=0) 


        """ INSIDE SCENE INPUT ENTRY FRAME """
        self.scene_name_label = ttk.Label(self.scene_input_entry, text = "Button Label", width = 15, anchor='w', justify="left")
        self.scene_name = ttk.Entry(self.scene_input_entry, width = 20)
        self.scene_name_label.grid(row=0, column=0, sticky='w')
        self.scene_name.grid(row=0, column=1, sticky='e')

        self.obs_name_label = ttk.Label(self.scene_input_entry, text = "OBS Scene Name", width = 15, anchor='w', justify="left")
        self.obs_name = ttk.Entry(self.scene_input_entry, width = 20)
        self.obs_name_label.grid(row=1, column=0, sticky='w')   
        self.obs_name.grid(row=1, column=1, sticky='e')

        self.arg1 = self.scene_name.get()
        self.arg2 = self.obs_name.get()
        self.arg_tuple = ()

        """ I'm so sorry """
        self.add_scene_button = ttk.Button(self.scene_input_buttons,
                                           text="Add scene",
                                           width=15,
                                           command=lambda: self.add_new_scene(self.scene_name.get(),
                                                                              self.obs_name.get(),
                                                                              self))




        self.remove_scene_button = ttk.Button(self.scene_input_buttons,
                                              text="Remove Scenes",
                                              width=15,
                                              command=lambda: self.toggle_delete_mode(self))
        
        self.warning_label = ttk.Label(self.scene_input_buttons,
                                       text="")

        self.warning_label.grid(row=0, column=0, columnspan=2)
        self.add_scene_button.grid(row=1, column=0, sticky='n')
        self.remove_scene_button.grid(row=1, column=1,sticky='e')

        self.tournament_var = tk.StringVar()
        self.tournament_var.set("Revival of Melee 7")
        self.tournament_label = ttk.Label(self.info_pane, text='Tournament Name')
        self.tournament_label.grid(row=0, column=0, sticky='w')
        self.tournament_text = ttk.Entry(self.info_pane, textvariable = self.tournament_var)
        self.tournament_text.grid(row=0, column=1, sticky='w')

        self.bracket_var = tk.StringVar()
        self.bracket_var.set("smash.gg/my-tournament")
        self.bracket_label = ttk.Label(self.info_pane, text='Bracket Link')
        self.bracket_label.grid(row=1, column=0, sticky='w')
        self.bracket_text = ttk.Entry(self.info_pane, textvariable = self.bracket_var)
        self.bracket_text.grid(row=1, column=1, sticky='w')

        self.round_var = tk.StringVar()
        self.round_var.set("Winner's Finals")
        self.round_label = ttk.Label(self.info_pane, text='Match Round')
        self.round_label.grid(row=2, column=0, sticky='w')
        self.round_text = ttk.Entry(self.info_pane, textvariable = self.round_var)
        self.round_text.grid(row=2, column=1, sticky='w')

        self.comm1_var = tk.StringVar()
        self.comm1_var.set("Prog")
        self.comm1_label = ttk.Label(self.info_pane, text='Commentator 1')
        self.comm1_label.grid(row=3, column=0, sticky='w')
        self.comm1_text = ttk.Entry(self.info_pane, textvariable = self.comm1_var)
        self.comm1_text.grid(row=3, column=1, sticky='w')

        self.comm2_var = tk.StringVar()
        self.comm2_var.set("D1")
        self.comm2_label = ttk.Label(self.info_pane, text='Commentator 2')
        self.comm2_label.grid(row=4, column=0, sticky='w')
        self.comm2_text = ttk.Entry(self.info_pane, textvariable = self.comm2_var)
        self.comm2_text.grid(row=4, column=1, sticky='w')

        self.custom_label = ttk.Entry(self.info_pane)
        self.custom_label.grid(row=5, column=0, sticky='w')
        self.custom_add = ttk.Button(self.info_pane, text = "Add Custom Field") 
        self.custom_add.grid(row=5, column=1, sticky='e')

    def self_destruct(self, main):
        self.destroy()

    def add_new_scene(self, display_string, obs_string, main):
        if len(self.scenes) < 8:
            if not duplicate_scene_check(display_string, obs_string, self.scenes):        
                user_scene = ttk.Button(self.scene_buttons,
                                        text=display_string,
                                        width=15,
                                        style="BW.TButton",
                                        command=lambda: scene_button_functionality(self,
                                                                                   self.scenes,
                                                                                   obs_string,
                                                                                   self.delete_mode))
                user_scene.grid(row=len(self.scenes)%4, column=int(len(main.scenes)/4))
        #            if(len(self.scenes)<4):
        #            user_scene.pack()

                info_pane = [user_scene, display_string, obs_string]
                self.scenes.append(info_pane)
                # print(self.scenes)
                self.warning_label.config(text = "")
            else:
                self.warning_label.config(text = "Cannot add a button with existing ID")
        else:
            self.warning_label.config(text = "Delete existing scenes to add more")

    """ I don't know why this changes all of the buttons, but it does. I'm not touching it """
    def toggle_delete_mode(self, main):
        if (self.delete_mode):
            self.remove_scene_button.configure(text="Stop Deleting")
            self.style.configure("BW.TButton", foreground="red")
            self.delete_mode = False
        else:
            self.remove_scene_button.configure(text="Remove Scenes")
            self.style.configure("BW.TButton", foreground="black")
            self.delete_mode = True


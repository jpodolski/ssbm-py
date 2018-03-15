#!/usr/bin/python3

## @file player.py
## @author Jeff Podolski
## @todo
#   - clean it up, make as compact as possible
#   - run through pylint
#   - tkinter -> tk

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

import tkinter.ttk as ttk
from tkinter import *
from PIL import Image, ImageTk
from classes.player_frame import *
from classes.dashboard import *
from classes.stream_info import *
from information import *
from classes.file_manip import *
from classes.scene_switch import *
from classes.load_window import *
from classes.load_session import *
from classes.settings import *
#from classes.initialize import *

class MainWindow(ttk.Frame):
	def __init__(self, load_file=None):
		self.load_file = load_file
		self.returning = None
		self.root = tkinter.Tk()
		self.root.title("autoGIMR")

		# self.root.overrideredirect(True)

		self.nbook = ttk.Notebook(self.root)
		self.construct_ui()
		if self.load_file[0] == 1:
			import_dashboard(self.dashboard, "saved/"+self.load_file[1])

	def construct_ui(self):
		self.f1 = ttk.Frame(self.nbook, borderwidth = 6)	# first page, which would get widgets gridded into it
		self.f2 = ttk.Frame(self.nbook)   		# second page
		self.f3 = ttk.Frame(self.nbook)   		# third page
		self.f4 = ttk.Frame(self.nbook)   		# fourth page
		self.f5 = ttk.Frame(self.nbook)   		# fifth page
		self.nbook.add(self.f1, text='Dashboard')
		self.nbook.add(self.f2, text='Stream Info')
		self.nbook.add(self.f3, text='HTML Output')
		self.nbook.add(self.f4, text='Scene Control')
		self.nbook.add(self.f5, text='Settings')

		self.nbook.grid()

		self.current_match = Match()
		self.dashboard = Dashboard(self.f1)
		self.dashboard.save_name = self.load_file[1]
		self.stream_info = StreamInfo(self.f2)
		self.scene_swtich = SceneSwitch(self.f4)

		def switch():
			self.nbook.select(1)

		self.switchbutton = ttk.Button(self.f4, text = "Add/Remove Scenes", command = lambda: switch())
		self.switchbutton.grid()

		self.html_object = ttk.Label(self.f3, text = "Settings coming soon. For now, just edit ssbm-py/templates/tag.css yourself")
		self.html_object.pack()

def start_main_window(status):
	menu = MainWindow(status)
	menu.root.mainloop()
	return_value = menu.returning
	menu.root.destroy()
	print(return_value)
	return menu.returning

def start_load_menu():
	menu2 = LoadMenu()
	menu2.root.mainloop()
	return_value2 = menu2.returning
	menu2.root.quit()
	menu2.root.destroy()
	print(return_value2)
	return return_value2

# start_load_menu()
status = start_load_menu()
if status != 0:
	start_main_window(status)

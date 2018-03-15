import tkinter.ttk as ttk
from tkinter import *
from classes.dashboard import *
from classes.load_session import *
from classes.match import *
from classes.stream_info import *
from classes.scene_switch import *
from classes.settings_pane import *

class MainWindow(ttk.Frame):
	def __init__(self, load_file=None):
		self.load_file = load_file
		self.returning = None
		self.root = Tk()
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
		self.nbook.add(self.f2, text='Stream Control')
		self.nbook.add(self.f3, text='HTML Output')
		self.nbook.add(self.f4, text='Settings')

		self.nbook.grid()
		self.nbook.pack_propagate(0)

		self.current_match = Match()
		self.dashboard = Dashboard(self.f1)
		self.dashboard.save_name = self.load_file[1]
		self.scene_swtich = SceneSwitch(self.f2)
		self.stream_info = SettingsPane(self.f4, self.root)

		self.html_object = ttk.Label(self.f3, text = "Settings coming soon. For now, just edit ssbm-py/templates/tag.css yourself")
		self.html_object.pack()

def start_main_window(status):
	menu = MainWindow(status)
	menu.root.mainloop()
	return_value = menu.returning
	menu.root.destroy()
	print(return_value)
	return menu.returning

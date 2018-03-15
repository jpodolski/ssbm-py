import tkinter.ttk as ttk
from tkinter import *
from dashboard import *
from load_session import *

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
		self.nbook.add(self.f2, text='Stream Control')
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

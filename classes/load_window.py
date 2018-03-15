import tkinter
import tkinter.ttk as ttk
from os import listdir
from os.path import join, isfile

class LoadMenu(object):
	def __init__(self, parent=None, returning = 0):
		self.returning = returning
		self.root = tkinter.Tk()
		self.root.title("Load Save")

		#self.returning = returning
		#self.root = tkinter.Toplevel(master=parent)
		#self.root.title("Save Manager")
		#self.root.overrideredirect(True)
		
		""" MAIN FRAME """
		self.frm_1 = ttk.Frame(self.root)
		self.frm_1.pack(ipadx=2, ipady=2)
		
		""" MESSAGE LABEL """
		self.msg = str("Would you like to load from a save file?")
		message = ttk.Label(self.frm_1, text=self.msg)
		message.pack(padx=8, pady=8)

		""" INNER FRAME """
		self.frm_2 = ttk.Frame(self.frm_1)
		self.frm_2.pack(padx=4, pady=4)

		self.files = [f for f in listdir('saved') if isfile(join('saved', f))]
		self.w = tkinter.Listbox(self.frm_2, selectmode = 'SINGLE', height = 5)
		i = 0
		for item in self.files:
			if item != '.DS_Store':
				print(str(item))
				i = i+1
				self.w.insert('end', item)
		self.w.pack()



		""" BUTTON WIDGETS """
		self.btn_1 = ttk.Button(self.frm_2, width=8, text="Load File")
		self.btn_1['command'] = self.b1_action
		self.btn_1.pack(side='left')
		
		self.btn_2 = ttk.Button(self.frm_2, width=8, text="Cancel")
		self.btn_2['command'] = self.b2_action
		self.btn_2.pack(side='left')
		
		self.btn_3 = ttk.Button(self.frm_2, width=8, text="Create New")
		self.btn_3['command'] = self.b3_action
		self.btn_3.pack(side='left')

		self.new_file_name = ttk.Entry(self.frm_2)
		self.new_file_name.pack(side='right')

		self.btn_2.bind('<KeyPress-Return>', func=self.b3_action)

		""" Position the window """

		# self.root.protocol("WM_DELETE_WINDOW", self.close_mod)
		# self.root.deiconify()


	def b1_action(self, event=None):
		selection = self.w.curselection()
		self.returning = [1, self.w.get(selection[0])]
		print("Loading file " + self.w.get(selection[0]) + "...")
		self.root.quit()
	def b2_action(self, event=None):
		self.root.quit()
	def b3_action(self, event=None):
		if(self.new_file_name.get() != ""):
			self.returning = [0, self.new_file_name.get()]
			self.root.quit()
	def nothing(self):
		print("nothing")
	def close_mod(self):
		pass
	def time_out(self):
		print ("TIMEOUT")
	def to_clip(self, event=None):
		self.root.clipboard_clear()
		self.root.clipboard_append(self.msg)
 
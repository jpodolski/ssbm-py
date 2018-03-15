import tkinter
import tkinter.ttk as ttk
from os import listdir
from os.path import join, isfile

class LoadMenu(object):

    def __init__(self):
        root = self.root = tkinter.Tk()
        root.title("Save Manager")
        root.overrideredirect(True)

        """ MAIN FRAME """
        frm_1 = ttk.Frame(root)
        frm_1.pack(ipadx=2, ipady=2)

        """ MESSAGE LABEL """
        self.msg = str("Would you like to load from a save file?")
        message = ttk.Label(frm_1, text=self.msg)
        message.pack(padx=8, pady=8)

        """ INNER FRAME """
        frm_2 = ttk.Frame(frm_1)
        frm_2.pack(padx=4, pady=4)

        """ TEST IMPLEMENTAITON [DOES NOT WORK] """
        mylist = ['1', '2', '3', '4', '5', '6', '7']
        test_var = tkinter.StringVar(frm_2)
        test_var.set(mylist[3])
        test_dropdown = ttk.OptionMenu(frm_2, test_var, *mylist)
        test_dropdown.pack(padx=4, pady=4)
        print(mylist) # Results in ['1', '2', '3', '4', '5', '6', '7']


        """ REAL IMPLEMENTATION [ALSO DOES NOT WORK] """
        ##files = [f for f in listdir('saved') if isfile(join('saved', f))]
        files=['a', 'b', 'c', 'd', 'e', 'f']
        file_var = tkinter.StringVar(frm_2)
        file_var.set(files[3])
        file_dropdown = ttk.OptionMenu(frm_2, file_var, files[1], *files)
        file_dropdown.pack(padx=4, pady=4)
        print(files) # Results in ['DS_Store', 'test1', 'test2', 'test3']

        """ BUTTON FUNCTIONALITY """
        btn_1 = ttk.Button(frm_2, width=8, text="Load File")
        btn_1['command'] = self.b1_action
        btn_1.pack(side='left')

        btn_2 = ttk.Button(frm_2, width=8, text="Cancel")
        btn_2['command'] = self.b2_action
        btn_2.pack(side='left')

        btn_3 = ttk.Button(frm_2, width=8, text="Create New")
        btn_3['command'] = self.b3_action
        btn_3.pack(side='left')

        btn_2.bind('<KeyPress-Return>', func=self.b3_action)

        root.update_idletasks()

        """ Position the window """
        xp = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
        yp = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
        geom = (root.winfo_width(), root.winfo_height(), xp, yp)
        root.geometry('{0}x{1}+{2}+{3}'.format(*geom))

        root.protocol("WM_DELETE_WINDOW", self.close_mod)
        root.deiconify()


    def b1_action(self, event=None):
        print("B1")
    def b2_action(self, event=None):
        self.root.quit()
    def b3_action(self, event=None):
        print("B3")
    def nothing(self):
        print("nothing")
    def close_mod(self):
        pass
    def time_out(self):
        print ("TIMEOUT")
    def to_clip(self, event=None):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.msg)

##def start_load_menu():
menu = LoadMenu()
menu.root.mainloop()
##    menu.root.destroy()
##    return menu.returning
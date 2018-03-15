import tkinter as tk
import tkinter.ttk as ttk

class SettingsPane(object): # pylint: disable=too-few-public-methods
    """
    A GUI class that contains the notebook frame that controls
    the information about the stream/event
    """

    def __init__(self, parent, root=None):
        self.main = ttk.Frame(parent)
        self.main.grid()
        self.root = root
        self.always_on = 0;

        always_on_label = ttk.Label(self.main, text = "Keep window on top")
        always_on_label.grid(row=0, column=0)
        always_on_check = ttk.Checkbutton(self.main, command=lambda: self.testfunction())
        always_on_check.grid(row=0, column=2)

        load_last_label = ttk.Label(self.main, text = "Automatically load last save on startup")
        load_last_label.grid(row=1, column=0)
        load_last_check = ttk.Checkbutton(self.main, command=lambda: self.dummy())
        load_last_check.grid(row=1, column=2)

        auto_update_label = ttk.Label(self.main, text = "Set count updates to OBS automatically")
        auto_update_label.grid(row=2, column=0)
        auto_update_check = ttk.Checkbutton(self.main, command=lambda: self.dummy())
        auto_update_check.grid(row=2, column=2)

        html_align_label = ttk.Label(self.main, text = "HTML Alignment alternates right/left")
        html_align_label.grid(row=3, column=0)
        html_align_check = ttk.Checkbutton(self.main, command=lambda: self.dummy())
        html_align_check.grid(row=3, column=2)

    def testfunction(self):
        if (self.always_on == 0):
            self.root.call('wm', 'attributes', '.', '-topmost', '1')
            self.always_on = 1
        else:
            self.always_on = 0
            self.root.call('wm', 'attributes', '.', '-topmost', '0')

    def dummy(self):
        print("I don't do anything!")

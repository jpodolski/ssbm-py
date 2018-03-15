import tkinter.ttk as ttk
from os import listdir
from os.path import isfile, join

files = [f for f in listdir('../saved') if isfile(join('../saved', f))]

print(files)
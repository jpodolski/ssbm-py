#!/usr/bin/python

from tkinter import *
from match import Match

top = Tk()
current_match = Match()


def update(match):
	match.set_tagA(E1.get())
	T1.delete('1.0', END)
	T1.insert(INSERT, match.playerA)

L1 = Label(top, text="Player A Tag:")
L1.pack(side = LEFT)
E1 = Entry(top, bd = 1)
E1.pack(side = LEFT)
B1 = Button(top, text = "UPDATE", command = lambda: update(current_match))
B1.pack(side = RIGHT)
T1 = Text(top, height = 1)
T1.pack(side = RIGHT)

top.mainloop()

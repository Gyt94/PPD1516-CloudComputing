#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from PIL import Image, ImageTk

class App:

    def __init__(self, master):

        frame = Frame(master, height=768, width=576, cursor="hand2")
        frame.pack()
        img = ImageTk.PhotoImage(file="Logo_cloud.png")
        lab=Label(frame, image=img)
        lab.photo = img
        lab.pack(side=TOP)
        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "hi there, everyone!"

root = Tk()
root.geometry("500x500")
app = App(root)

root.mainloop()
root.destroy() # optional; see description below
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from PIL import Image, ImageTk
import streamingTwitter

class App:

    def __init__(self, master):

        frame = Frame(master, height=1024, width=700, cursor="hand2")
        frame.pack()
        img = ImageTk.PhotoImage(file="Untitled.png")
        lab=Label(frame, image=img)
        lab.photo = img
        lab.pack(side=TOP)
        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.Rss_btn = Button(frame, text="RSS", command=self.rss)
        self.Rss_btn.pack(side=LEFT)
        self.Twit_btn = Button(frame, text="Touiteur", command=self.twit)
        self.Twit_btn.pack(side=RIGHT)
		

    def twit(self):
        mot = "explosion"
        streamingTwitter.main(["-q",mot])
        print "twit is launch"
    def rss(self):
        execfile("azureEventHubRSS.py")
        print "rss is launch"

root = Tk()
root.geometry("700x500")
app = App(root)

root.mainloop()
root.destroy() # optional; see description below
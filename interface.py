#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from PIL import Image, ImageTk
import streamingTwitter
import tkFont

class App:

    def __init__(self, master):
        helv36 = tkFont.Font(family='Helvetica',
         size=15, weight='bold')  # you don't have to use Helvetica or bold, this is just an example
        
        frame = Frame(master, height=500, width=700, cursor="hand2")
        frame.grid(ipady=10)
        img = ImageTk.PhotoImage(file="Untitled.png")
        lab=Label(frame, image=img)
        lab.photo = img
        lab.grid(row=0, columnspan=3)
        self.button = Button(
            frame, text="QUIT", fg="red", width=10 , command=frame.quit, font=helv36
            )
        self.button.grid(row=1,column=0)
        self.Rss_btn = Button(frame, text="RSS", command=self.rss,width=10, bg="orange", fg="white", font=helv36)
        self.Rss_btn.grid(row=1,column=1)
        self.Twit_btn = Button(frame, text="Touiteur", command=self.twit,width=10, bg="blue", fg="white", font=helv36)
        self.Twit_btn.grid(row=1,column=2)
        ztext= Entry(frame, width=20)
        ztext.insert(0, "Saisir URL RSS")
        ztext.grid()
		

    def twit(self):
        mot = "explosion"
        streamingTwitter.main(["-q",mot])
        print "twit is launch"
    def rss(self):
        execfile("azureEventHubRSS.py")
        print "rss is launch"

root = Tk()
root.geometry("900x500")
root.title("PPD CloudComputing")
app = App(root)

root.mainloop()
root.destroy() # optional; see description below
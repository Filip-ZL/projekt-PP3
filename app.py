# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 21:20:21 2019

@author: Filip
"""
import os
import tkinter as tk
from tkinter import *
from main import *
import keyboard

root = tk.Tk()
file_frame = tk.LabelFrame(root, padx=225, pady=200)
file_frame.grid(column=3,row=0,padx=150,pady=25)
label = Functions.labels(file_frame,['File Name','Timestamp','Save'])
root.geometry('900x600')
r_images = [PhotoImage(file="img/rec.png"),
          PhotoImage(file="img/save.png"),
          PhotoImage(file="img/stop_rec.png")]
uitems = {'File' : [['New',lambda: RecordingWin(root,r_images)],
               ['Save',lambda: Functions.test()],
               ['-','Exit',lambda: Functions._quit()]],
          'Tools' : [['Settings',lambda: Functions.test()]]}
a = MenuBar(root,uitems)
#Functions.new_button(k)
def on_closing():
    if tk.messagebox.askokcancel("Quit","Are you sure to quit without save?"):
        n = 0
        while 1:
            try:
                os.remove("temp/Untitled-{}/{}.png".format(RecordingWin.i,n))
            except:
                break
            finally:
                n += 1  
        root.quit()
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()



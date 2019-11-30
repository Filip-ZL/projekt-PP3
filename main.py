# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 00:10:10 2019

@author: Filip
"""
import tkinter as tk
from tkinter import *
import threading
import os
from os.path import isfile, join
import pyautogui
import numpy as np
import keyboard
#import numpy as np
import cv2
from win32api import GetSystemMetrics
#______________________________________________________________________________
# Class for creating upper menu in application
# Input parameters are following:
# master is parent of bar
# items will show if you click on main item
# items's got 3 input parameters which are 'Name of bar','Name' and called function() after click 
# 
# exmple:
# ###### a = MenuBar(win,{'File': [['New',lambda: function],['Exit',quit]]})
# !!!!! USE LAMBDA BEFORE FUNCTION TO PROTECT IT FROM AUTORUNNING !!!!!
# advice: by adding '-' before parameter 'Exit' will add a separator
class MenuBar:
    def __init__(self,master,items=[]):
        MenuBar.master = master
        menu_bar = Menu(master)
        master.config(menu=menu_bar)
        for mitems in items:
            self._menu = Menu(menu_bar, tearoff=0)
            self.names = items[mitems]
            for name in self.names:
                if name[0].find('-') == 0:
                    self._menu.add_separator()
                    self._menu.add_command(label=name[1],command= name[2])
                else:
                    self._menu.add_command(label=name[0],command= name[1])
            menu_bar.add_cascade(label=mitems, menu=self._menu)
#______________________________________________________________________________
# Basic function like             
class Functions(MenuBar):
    @staticmethod
    def test():
        pass
    def _quit():
        try:
            master = MenuBar.master
            master.quit()
            master.destroy()
        except:
            pass
        
    def check_folder():
        if len(os.listdir('temp') ) == 0:
            return False
        else:    
            return True
    def labels(master,items):
        i = 0
        for item in items:
            label = Label(master,text=item)
            label.grid(row=0,column=i)
            master.grid_rowconfigure(0, weight=1)
            master.grid_columnconfigure(0, weight=1)
            i += 1
#______________________________________________________________________________
# Class for monitor screening
class Record:
    def run():
    # display screen resolution, get it from your OS settings
        SCREEN_SIZE = (GetSystemMetrics(0), GetSystemMetrics(1))
        # define the codec
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        # create the video write object
        out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))
        
        while True:
            # make a screenshot
            img = pyautogui.screenshot()
            # convert these pixels to a proper numpy array to work with OpenCV
            frame = np.array(img)
            # convert colors from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # write the frame
            out.write(frame)
        
            if keyboard.is_pressed('ctrl+alt+i') or Record.switch == False:
                break
        # make sure everything is closed when exited
        cv2.destroyAllWindows()
        out.release()

        print("Loop breaked")

    
    def rec():
         thread = threading.Thread(target=Record.run)  
         thread.start()
    def create_video(frame_array,cv2):
        fps = 24
        size = (1024,768)  
        out = cv2.VideoWriter('movie.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
        for im in frame_array:
         # writing to a image array
             out.write(im)
        out.release()
        print('Video saved succesfully')
#______________________________________________________________________________
# Class for child windows
class RecordingWin:
    i = 0
    def __init__(self,master,photo,title="New"):
        RecordingWin.i +=1
        self.master = master
        self.title = title
        self.sub_window = Toplevel(master)
        self.sub_window.title('{}-{}'.format(title, RecordingWin.i))
        self.sub_window.geometry("300x200+200+200")
        self.file_frame = tk.LabelFrame(self.sub_window,text="New recording pannel", padx=30, pady=20)
        self.file_frame.grid(column=3,row=4,padx=1,pady=1)
        self.rec = Button(self.file_frame,image=photo[0], command= self.switchon)
        self.rec.grid(column=0,row=0)
        self.stop_rec = Button(self.file_frame,image=photo[2], command= self.switchoff, state='disabled')
        self.stop_rec.grid(column=1,row=0)
        self.save = Button(self.file_frame,image=photo[1], command= lambda: Record.create_video('./temp/untitled-1/','video.avi'))
        self.save.grid(column=2,row=0)
    def switchon(self):
        global switch
        Record.switch = True
        self.rec.config(state='disabled')
        self.stop_rec.config(state='active')
        Record.rec()    
            
    def switchoff(self):      
        global switch  
        Record.switch = False
        self.label = Label(self.file_frame,text='Stop rec')
        self.label.grid(column=1,row=1)

        
        
        


        



              

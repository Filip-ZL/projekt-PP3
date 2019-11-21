# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 00:10:10 2019

@author: Filip
"""
import tkinter as tk
from tkinter import *
import threading
import time
import pyautogui as pya
import os
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
    def createNpaste(master,photo,command,column,row):
        r_btn= Button(master, command = command)
        r_btn.config(image=photo,width="30",height="30")
        r_btn.grid(column=column,row=row)

class Record:
    switch = True 
    @staticmethod
    def create_n_save(frames):
        i = 0
        for frame in frames:
            frame.save("temp/{}.png".format(i))
            i += 1
        print(RecordingWin.i)    
    def run():
        counter = time.time()
        i = 0
        fps = 24
        mov = []
        while (Record.switch == True):
            start = time.time()
            scr = pya.screenshot()
            mov.append(scr)
            i += 1
            dur = time.time() - start
            slp = abs(dur - 1/fps)
            time.sleep(slp)

        print(i)
        print("Loop breaked")
        Record.create_n_save(mov)    
    
    def rec():  
         thread = threading.Thread(target=Record.run)  
         thread.start()      
    def switchon():    
        global switch
        Record.switch = True     
        Record.rec()    
            
    def switchoff():      
        global switch  
        Record.switch = False
        
class RecordingWin:
    i = 1
    def __init__(self,master, photo, title):
        self.master = master
        self.title = title
        self.sub_window = Toplevel(master)
        self.sub_window.title('{}-{}'.format(title, RecordingWin.i))
        self.sub_window.geometry("320x240+200+200")
        rec = Functions.createNpaste(self.sub_window,photo[0],lambda: Record.switchon(),0,0)
        stop_rec = Functions.createNpaste(self.sub_window,photo[2],lambda: Record.switchoff(),1,0)
        save = Functions.createNpaste(self.sub_window,photo[1],lambda: Functions.test(),2,0)
        RecordingWin.i +=1


              

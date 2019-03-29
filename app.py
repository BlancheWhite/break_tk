#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:58:24 2019

@author: cristi
"""

from tkinter import *
from tkinter import ttk

class Application(ttk.Frame):
    def __init__(self, master):  #initialize the grid and widgets
        ttk.Frame.__init__(self, master)
        self.master = master
        master.title("Break reminder")
        master.geometry("300x150")

        self.time_between = StringVar()
        self.break_duration = StringVar()
        self.postpone = StringVar()
        
        # create label and entry for time between breaks
        self.time_between_entry = ttk.Entry(master, width=7, textvariable=self.time_between)
        self.time_between_entry.grid(column=2, row=1, sticky=(W))
        self.time_between_label = ttk.Label(master, text="Time Between Breaks")
        self.time_between_label.grid(column=1, row=1, sticky=(W))        
        
        # create label and entry for break duration
        self.break_duration_entry = ttk.Entry(master, width=7, textvariable=self.break_duration)
        self.break_duration_entry.grid(column=2, row=2, sticky=(W))
        self.break_duration_label = ttk.Label(master, text="Break Duration")
        self.break_duration_label.grid(column=1, row=2, sticky=(W))
        
        # create label and entry for postpone breaks
        self.postpone_entry = ttk.Entry(master, width=7, textvariable=self.postpone)
        self.postpone_entry.grid(column=2, row=3, sticky=(W))
        self.postpone_label = ttk.Label(master, text="Postpone Time")
        self.postpone_label.grid(column=1, row= 3, sticky=(W))

    def padx(self):
         # a shortcut to configure the padx and pady on every widget
         for child in mainframe.winfo_children(): 
             child.grid_configure(padx=5, pady=5)
# open the app with the cursor in the below entry:   
#time_between_entry.focus()
root = Tk()
test = Application(root) 

root.mainloop()
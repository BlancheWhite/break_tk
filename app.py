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
#        self.frame = ttk.Frame(master)
#        self.frame.grid(row=0, column=0, sticky = W)
        self.master = master
        master.title("Break reminder")
        master.geometry("400x200")
        
        #creating the main label as a title
        self.mainlabel = ttk.Label(master, text="Settings")
        self.mainlabel.grid(column=0, row=0, sticky=(N, S, E, W), padx=3)
        self.mainlabel.config(font=("Times",26))
        
        self.time_between = StringVar()
        self.break_duration = StringVar()
        self.postpone = StringVar()
        
        # create label and spinbox for time between breaks
        self.frame1 = ttk.Frame(master)
        self.frame1.grid(column=2, row=1 , sticky =(N, W, S, E))
        self.time_between_spin = Spinbox(self.frame1, width=4, from_=1.0, to=100.0, textvariable=self.time_between)
        self.time_between_spin.grid(column=3, row=2, sticky=(N, S, E, W), padx=3)
        self.time_between_label = ttk.Label(self.frame1, text="Time Between Breaks")
        self.time_between_label.grid(column=2, row=2, sticky=(N, S, E, W), padx=3)        
        
        # create label and spinbox for break duration
        self.break_duration_spin = Spinbox(self.frame1, width=4, from_=1.0, to=100.0, textvariable=self.break_duration)
        self.break_duration_spin.grid(column=3, row=3, sticky=(N, S, E, W), padx=3)
        self.break_duration_label = ttk.Label(self.frame1, text="Break Duration")
        self.break_duration_label.grid(column=2, row=3, sticky=(N, S, E, W), padx=3)
        
        # create label and spinbox for postpone breaks
        self.postpone_spin = Spinbox(self.frame1, width=4, from_=1.0, to=100.0, textvariable=self.postpone)
        self.postpone_spin.grid(column=3, row=4, sticky=(N, S, E, W), padx=3)
        self.postpone_label = ttk.Label(self.frame1, text="Postpone Time")
        self.postpone_label.grid(column=2, row=4, sticky=(N, S, E, W), padx=3)
        
        
            
        #create the buttons for the 3 type break inside another frame for resizing
        self.frame2 = ttk.Frame(self.frame1, width=300, height=300)
        self.frame2.grid(column=1, row=1 , sticky =(N, W, S, E))
        self.frame2.grid_propagate(0)
        self.lunch = ttk.Button(self.frame2, text="Lunch")  #to be inserted the command
        self.lunch.grid(column=1, row=2, sticky=(N, S, E, W), padx=3)
        self.recreational = ttk.Button(self.frame2, text="Recreational")  #to be inserted the command
        self.recreational.grid(column=1, row=3, sticky=(N, S, E, W), padx=3)
        self.micro = ttk.Button(self.frame2, text="Micro-break")  #to be inserted the command
        self.micro.grid(column=1, row=4, sticky=E, padx=3)
        
#    def padx(self):
#         # a shortcut to configure the padx and pady on every widget
#         for child in mainframe.winfo_children(): 
#             child.grid_configure(padx=5, pady=5)
# open the app with the cursor in the below entry:   
#time_between_entry.focus()
root = Tk()
test = Application(root) 

root.mainloop()
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
import time

window = tk.Tk()
title = title = window.title("Break reminder")
label = tk.Label(window, text = "Today's date").pack()
#creating label for today's date
label1 = tk.Label(window)
label1.pack()
label2 = tk.Label(window)
label2.pack()
   
def todays_date(time1=""):
    date = time.strftime("%Y/%m/%d")
    time2 = time.strftime("%H:%M:%S")
    if time2 != time1: # if time string has changed, update it
        time1 = time2
        label1.config(text=time2 + " " + date)

    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use &gt;200 ms, but display gets jerky
    label1.after(20, todays_date)

todays_date()
#set the measure of the window 
window.geometry("300x300")
window.mainloop()


    


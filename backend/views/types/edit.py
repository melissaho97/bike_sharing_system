#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Oct 11 07:52:21 2019

@author: Melissa
"""

import tkinter as tk

#Assign the value to each style sheet properties
def init_styleSheet():
    styleDict = {}
    styleDict["Title"] = "CMT - Bike"
    styleDict["windowSize"] = "1024x768"
    styleDict["windowWidth"] = 1024
    styleDict["windowHeight"] = 768
    styleDict["leftPadding"] = 20
    styleDict["rightPadding"] = 20
    styleDict["topPadding"] = 150
    styleDict["fontColor"] = "black"
    styleDict["buttonWidth"] = 80
    styleDict["buttonHeight"] = 30
    styleDict["fontColor"] = "black"
    styleDict["TabHeaderFgColor"] = "white"
    styleDict["TabHeaderBgColor"] = "#4B96E9"
    styleDict["Tab_X_Start"] = styleDict["leftPadding"]
    styleDict["Tab_Y_Start"] = 250
    styleDict["TabRowHeight"] = 30
    styleDict["lineSpace"] = 30
    return(styleDict)

def submitButton():
    return

# Initial Style Sheet
styleDict = init_styleSheet()

# Commond - Header
window = tk.Tk()
window.title(styleDict["Title"])
window.geometry(styleDict["windowSize"])

menu_label = tk.Label()
menu_label.place(x = styleDict["leftPadding"], y = styleDict["topPadding"])
menu_label["fg"] = styleDict["fontColor"]

#Common - Set Menu Name in Header
menu_label["text"] = "Add New Bike Type: "

label_1 = tk.Label(text="Type Name:")
label_1.grid(row=0)

e1 = tk.Entry()
e1.grid(row=0, column=1)

label_2 = tk.Label(text="Fixed Price:")
label_2.grid(row=1)

e2 = tk.Entry()
e2.grid(row=1, column=1)

label_3 = tk.Label(text="Add On Price:")
label_3.grid(row=2)

e3 = tk.ComboBox(windows, values=["January", "February", "March","April"])
e3.grid(row=2, column=1)

label_4 = tk.Label(text="Day Price:")
label_4.grid(row=3)

e4 = tk.Entry()
e4.grid(row=3, column=1)

add_button = tk.Button(text = "Confirm", command = submitButton)
add_button.grid(row=4, column=1)
#add_button.place(x = (styleDict["windowWidth"]-((styleDict["rightPadding"] + styleDict["buttonWidth"])*2)), y = (styleDict["topPadding"]+styleDict["lineSpace"]), width = 278, height = 55)

window.mainloop()

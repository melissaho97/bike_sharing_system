#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Oct 11 07:52:21 2019

@author: Melissa
"""

import tkinter

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
    
def addLocaton():
    

#Initial Style Sheet
styleDict = init_styleSheet()

#Common - Header
window = Tk()
window.title(styleDict["Title"])
window.geometry(styleDict["windowSize"])

menu_label = Label()
menu_label.place(x = styleDict["leftPadding"], y = styleDict["topPadding"])
menu_label["fg"] = styleDict["fontColor"]

#Common - Set Menu Name in Header
menu_label["text"] = "Add New Bike Type: "

label_1 = Label(text="Type Name:")
label_1.grid(row=0)

e1 = Entry()
e1.grid(row=0, column=1)

label_2 = Label(text="Fixed Price:")
label_2.grid(row=1)

e2 = Entry()
e2.grid(row=1, column=1)

label_2 = Label(text="Add On Price:")
label_2.grid(row=2)

e2 = Entry()
e2.grid(row=2, column=1)

label_2 = Label(text="Day Price:")
label_2.grid(row=3)

e2 = Entry()
e2.grid(row=3, column=1)

add_button = Button(text = "Confirm", command = addLocation)
add_button.place(x = (styleDict["windowWidth"]-((styleDict["rightPadding"] + styleDict["buttonWidth"])*2)), y = (styleDict["topPadding"]+styleDict["lineSpace"]), width = 278, height = 55)

window.mainloop()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Oct 11 07:52:21 2019

@author: Melissa
"""

from tkinter import *

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
    styleDict["TabCol_0_Width"] = 98
    styleDict["TabCol_1_Width"] = 225
    styleDict["TabCol_2_Width"] = 215
    styleDict["TabCol_3_Width"] = 235
    styleDict["TabCol_4_Width"] = 215
    styleDict["TabRowHeight"] = 30
    styleDict["lineSpace"] = 30
    return(styleDict)

def db_connect():
    return

def db_query():
    return

def addLocation():
    return

def editLocation():
    return

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
menu_label["text"] = "Type Management: "

#Create control of ViewLocation Page
add_button = Button(text = "Add", command = addLocation)
add_button.place(x = (styleDict["windowWidth"]-((styleDict["rightPadding"] + styleDict["buttonWidth"])*2)), y = (styleDict["topPadding"]+styleDict["lineSpace"]), width = styleDict["buttonWidth"], height = styleDict["buttonHeight"])
edit_button = Button(text = "Edit", command = editLocation)
edit_button.place(x = (styleDict["windowWidth"]-(styleDict["rightPadding"] + styleDict["buttonWidth"])), y = (styleDict["topPadding"]+styleDict["lineSpace"]), width = styleDict["buttonWidth"], height = styleDict["buttonHeight"])

tabCol_List = ["ID", "Type Name", "Fixed Price", "Add-On Price", "Day Price"]
sum_col_width = 0

#Create Table Header
for i in range(len(tabCol_List)):
    table_col_name = "table_col_" + str(i)
    table_col_name = Label(text = tabCol_List[i], borderwidth = 1, relief = "solid")
    if i == 0:
        sum_col_width = styleDict["Tab_X_Start"]
    else:
        col_width_name = "TabCol_" + str(i-1) + "_Width"
        sum_col_width = sum_col_width + styleDict[col_width_name]

    x_pos = sum_col_width
    y_pos = styleDict["Tab_Y_Start"]

    table_width_name = "TabCol_"+str(i)+"_Width"
    table_col_name.place(x = x_pos, y = y_pos, width = styleDict[table_width_name], height = styleDict["TabRowHeight"])
    table_col_name["bg"] = styleDict["TabHeaderBgColor"]
    table_col_name["fg"] = styleDict["TabHeaderFgColor"]

#Display Location Data from DB
db_connect()
db_query()

window.mainloop()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 19:21:48 2019

@author: melissa
"""

#import libraries
import tkinter as tk

#import other pages
import Report

def init_styleSheet():
    global styleDict 
    styleDict = {}
    styleDict["Title"] = "CMT - Bike"
    styleDict["windowSize"] = "1024x768"
    styleDict["windowWidth"] = 1024
    styleDict["windowHeight"] = 768
    styleDict["labelLen"] = 15
    styleDict["xPadding"] = 20
    styleDict["yPadding"] = 5
    styleDict["inlinePadding"] = 5
    styleDict["topPadding"] = 150
    styleDict["fontColor"] = "black"
    styleDict["fontType"] = "Arial"
    styleDict["fontSize"] = "18"
    styleDict["fontStyle"] = "bold"
    styleDict["buttonWidth"] = 10
    styleDict["TabHeaderFgColor"] = "white"
    styleDict["TabHeaderBgColor"] = "#4B96E9"
    return(styleDict)

class BackendHomePage(tk.Frame):
    def __init__(self, master):
        
        #Initialize Frame
        tk.Frame.__init__(self, master)

        #Initialize Style Dict
        styleDict = init_styleSheet()
        h_frame = tk.Frame(self, height = styleDict["topPadding"])
        h_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        title = tk.Label(h_frame, text='CMT-Bike (Staff ONLY)', font=("Arial, 30"))
        title.pack(side=tk.LEFT, padx=30, pady=70)

        menu_frame_1 = tk.Frame(self)
        menu_frame_1.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        a = tk.Button(menu_frame_1, text='Report Management', font=("Arial, 25"), width=15, height=4,
                      command=lambda: master.switch_frame(Report.ReportMngPage))

        a.pack(side=tk.LEFT, padx=30, pady=30)
        
        
        #Display Back End Home Page
        #tk.Label(self, text="Backend Home Page", font=(styleDict["fontType"], styleDict["fontSize"], styleDict["fontStyle"])).pack(side="top", fill="x", pady=5)
        #tk.Button(self, text="Go to Report Management Page",
        #          command = lambda: master.switch_frame(Report.ReportMngPage)).pack()
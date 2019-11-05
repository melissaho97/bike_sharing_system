# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:58:50 2019

@author: FlyingPIG
"""
#import libraries
import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
import pymysql
import CMTBikeMng

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

class BackEndHomePage(tk.Frame):
    def __init__(self, master):
        
        #Initialize Frame
        tk.Frame.__init__(self, master)

        #Initialize Style Dict
        styleDict = init_styleSheet()
        
        #Display Back End Home Page
        tk.Label(self, text="BackEnd Home Page", font=(styleDict["fontType"], styleDict["fontSize"], styleDict["fontStyle"])).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go to Bike Management Page",          
                  command = lambda: master.switch_frame(CMTBikeMng.BikeMngPage)).pack()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 13:18:01 2019

@author: pat
"""

#import libraries
import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
import pymysql
import numpy as np
import matplotlib.pyplot as plt
from pandastable import Table, TableModel

#import other pages
import BackEnd
from config import LoginInfo, DBConnect

def init_styleSheet():
    global styleDict 
    styleDict = {}
    styleDict["Title"] = "CMT - Bike"
    styleDict["windowSize"] = "1024x768"
    styleDict["windowWidth"] = 1024
    styleDict["windowHeight"] = 768
    styleDict["labelLen"] = 6
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

    
def popupMsg(msg):
        popup = tk.Tk()
        popup.title(styleDict["Title"])
        msg_label = tk.Label(popup, text = msg)
        msg_label.pack()
        done_button = tk.Button(popup, text="Done", command = popup.destroy)
        done_button.pack()
        popup.mainloop()
        
def chkNumber(character):
    if character.isdigit():
        return True
    else:
        return False
    
def connectDB():
    host = 'localhost'
    user = 'root'
    password = DBConnect.password
    db = DBConnect.db 
    try:
        connection = pymysql.connect(host, user, password, db)
        #print("Connect to DB Success")
    except pymysql.InternalError as e:
        popupMsg(e)
        #print("Connection Error", e)
    return connection

def disconnectDB(connection):
    connection.close()
    

class ReportMngPage(tk.Frame):
    
    def __init__(self, master):
        
        #Initialize Frame
        tk.Frame.__init__(self, master)
        self.pack(fill = tk.BOTH, expand = True)
        
        #Initialize Style Dict
        styleDict = init_styleSheet()
        
        #Set Header Frame
        h_frame = tk.Frame(self, height = styleDict["topPadding"])
        h_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])      
        home_button = tk.Button(h_frame, text = "Home", width = styleDict["buttonWidth"], command = lambda: master.switch_frame(BackEnd.BackEndHomePage), bg = styleDict["TabHeaderBgColor"])
        home_button.pack(side = tk.LEFT)

        #Set Menu Frame
        menu_frame = tk.Frame(self)
        menu_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])

        menu_label = tk.Label(menu_frame, text = "Sales Report: ", font = ('Arial', 18), anchor = tk.W)
        menu_label.pack(side = tk.LEFT)
        
        
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT SUM(Paid_Amount) AS Amount, DATE_FORMAT(Updated_At,'%Y-%m') AS Date
                    FROM `transaction`
                    GROUP BY DATE_FORMAT(Updated_At,'%Y-%m')
					ORDER BY DATE_FORMAT(Updated_At,'%Y-%m');'''
        cursor.execute(query)
        arr_x = []
        arr_y = []
        for row in cursor.fetchall():
            arr_x.append(row[1])
            arr_y.append(row[0])
        disconnectDB(connection)
        
        plt.plot(arr_x, arr_y)
        
        #print(arr_x)
        #print(arr_y)
        
        
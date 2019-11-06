#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:08:40 2019

@author: Melissa
"""
#import libraries
import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
import pymysql
# Provides classic Python interface
from matplotlib import pyplot as plt
# Handle Dates
import matplotlib.dates as mdates  
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

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
    styleDict["TabHeaderFgColor"] = "#FFFFFF"
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
    password = ''
    db = 'cmt-bike' 
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
        h_frame = tk.Frame(self, bg = styleDict["TabHeaderBgColor"], height = styleDict["topPadding"])
        h_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        
        # Select City Name Frame
        city_name_frame = tk.Frame(self)
        city_name_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        city_name_label = tk.Label(city_name_frame, text = "City Name: ", width = styleDict["labelLen"], anchor = tk.W)
        city_name_label.pack(side = tk.LEFT)
        
        #Get City Name from DB
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT City_Name `City Name` FROM city ORDER BY City_Name;'''
        cursor.execute(query)
        city_list = []
        for row in cursor.fetchall():
            city_list.append(row)
        disconnectDB(connection)
        
        self.var_status = tk.StringVar()
        self.var_status.set("Paid")

        self.var_city_name = tk.StringVar()
        city_name_input = ttk.Combobox(city_name_frame, values = city_list, state='readonly', textvariable = self.var_city_name)
        city_name_input.bind("<<ComboboxSelected>>", self.callback)
        city_name_input.insert(0, 'Select City')
        city_name_input.pack(fill = tk.X)
        
        
    def callback(self, event):
        self.setCurrentLocData()
        
    def setCurrentLocData(self):
        print(self.var_city_name.get())
        print(self.var_status.get())
        # Retrieve Data
        connection = connectDB()
        print("Database")
        cursor = connection.cursor()
        print("Cursor")
        cursor.execute('''SELECT DATE_FORMAT(trans.Updated_At,'%%%%Y-%%%%m') AS Date, trans.Status FROM transaction AS trans WHERE trans.Status=%s;''', (self.var_status.get()))
        #query = "SELECT CAST(SUM(trans.`Paid_Amount`) AS CHAR) AS Amount, trans.Status FROM transaction AS trans WHERE trans.Status='%s';"
        
# =============================================================================
#         query='''SELECT CAST(SUM(trans.`Paid_Amount`) AS CHAR) AS Amount, DATE_FORMAT(trans.Updated_At,'%%%%Y-%%%%m') AS Date, 
#                     trans.Origin_ID, trans.Status,
#     				l.ID, l.City_ID, 
#     				c.ID, c.City_Name
#                     FROM transaction AS trans
#     				INNER JOIN location AS l ON trans.Origin_ID=l.ID
#     				INNER JOIN city AS c ON l.City_ID=c.ID
#     				WHERE c.City_Name=%s AND trans.Status=%s
#                     GROUP BY Date, trans.Origin_ID, l.City_ID
#     				ORDER BY Date;'''
# =============================================================================
# =============================================================================
#         query = '''SELECT SUM(trans.Paid_Amount) AS Amount, DATE_FORMAT(trans.Updated_At,'%y-%m') AS Date, 
#                     trans.Origin_ID, trans.Status,
#     				l.ID, l.City_ID, 
#     				c.ID, c.City_Name
#                     FROM transaction AS trans
#     				INNER JOIN location AS l ON trans.Origin_ID=l.ID
#     				INNER JOIN city AS c ON l.City_ID=c.ID
#     				WHERE c.City_Name=%s AND trans.Status=%s
#                     GROUP BY DATE_FORMAT(trans.Updated_At,'%y-%m'), trans.Origin_ID, l.City_ID
#     				ORDER BY DATE_FORMAT(trans.Updated_At,'%y-%m');'''
# =============================================================================
        #query_params = (self.var_city_name.get(),self.var_status.get())
        #print(cursor.execute(query, (self.var_city_name.get(),self.var_status.get())))
        
        # Initialise 2 arrays
        #arr_x = []
        arr_y = []
        
        # Store Data
        for row in cursor.fetchall():
            #arr_x.append(row[1])
            arr_y.append(row[0])
        disconnectDB(connection)
        
        #print(arr_x)
        print(arr_y)
# =============================================================================
#         x = np.array(arr_x)
#         y = np.array(arr_y)
#         
#         # plot the figure within tkinter
#         fig = Figure(figsize=(len(arr_x),len(arr_y)))
#         a = fig.add_subplot(111)
#         a.scatter(y, x, color='red')
#         a.plot(p, range(2 +max(x)),color='blue')
#         a.invert_yaxis()
# 
#         a.set_title ("Estimation Grid", fontsize=16)
#         a.set_ylabel("Y", fontsize=14)
#         a.set_xlabel("X", fontsize=14)
# 
#         canvas = FigureCanvasTkAgg(fig, master=self.window)
#         canvas.get_tk_widget().pack()
#         canvas.draw()
# 
#         
#     def saveImg(self):
#         plt.savefig('my_figure.png')
# =============================================================================
        
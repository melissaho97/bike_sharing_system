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
import array

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
        #city_name_input.insert(0, 'Select City')
        city_name_input.pack(fill = tk.X)
        
        act_button_frame = tk.Frame(self)
        act_button_frame.pack(padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        save_button = tk.Button(act_button_frame, text = "Save", width = styleDict["buttonWidth"], command = self.saveImg)
        save_button.pack(side = tk.RIGHT, fill = tk.X, padx = styleDict["inlinePadding"])
        
        # Initialise 2 arrays
        self.arr_x = []
        self.arr_y = []
        print('Store Database')
        
        # Changing List into NumPy Array
        x = np.array(self.arr_x)
        y = np.array(self.arr_y)
        
        # Plot
        plt.plot(self.arr_x, self.arr_y)
        plt.xlabel("Time")
        plt.ylabel("Sales")
        plt.show()
        
# =============================================================================
#         fig = plt.Figure(figsize=(len(self.arr_x),len(self.arr_y)))
#         a = fig.add_subplot(111)
#         a.plot(x, y, color='red')
#          
#         a.set_title ("Sales Report", fontsize=16)
#         a.set_ylabel("Sales", fontsize=14)
#         a.set_xlabel("Time", fontsize=14)
#          
#         canvas = FigureCanvasTkAgg(fig, master)
#         canvas.get_tk_widget().pack()
#         canvas.draw()
# =============================================================================
        
# =============================================================================
#         Data1 = {
#         'Time': ['US','CA','GER','UK','FR'],
#         'Sales_Amount': [45000,42000,52000,49000,47000]
#        }
#         
#         # Create Pandas to structure the input data
#         df1 = pd.DataFrame(Data1, columns= ['Time', 'Sales_Amount'])
#         df1 = df1[['Time', 'Sales_Amount']].groupby('Time').sum()
#         
#         # Create a figure object
#         # Figure params: figsize(width, height), 
#         figure1 = plt.Figure(figsize=(6,5), dpi=110, facecolor="b")
#         # add_subplot ->> add multiple plots to a figure
#         ax1 = figure1.add_subplot(111)
#         
#         # FigureCanvasTkAgg can then generate a widget for Tkinter to use
#         bar1 = FigureCanvasTkAgg(figure1, master)
#         bar1.get_tk_widget().pack(fill=tk.BOTH)
#         df1.plot(kind='line', legend=True, ax=ax1)
#         
#         #Set Action Buttion Frame
#         act_button_frame = tk.Frame(self)
#         act_button_frame.pack(padx = styleDict["xPadding"], pady = styleDict["yPadding"])
# =============================================================================
        
    def callback(self, event):
        connection = connectDB()
        print("Database")
        cursor = connection.cursor()
        print("Cursor")
        query = '''SELECT CAST(SUM(trans.`Paid_Amount`) AS CHAR) AS Amount, DATE_FORMAT(trans.Updated_At,"%%Y-%%m") AS Date, 
                    trans.Origin_ID, trans.Status,
    				l.ID, l.City_ID, 
    				c.ID, c.City_Name
                    FROM transaction AS trans
    				INNER JOIN location AS l ON trans.Origin_ID=l.ID
    				INNER JOIN city AS c ON l.City_ID=c.ID
    				WHERE c.City_Name=%s AND trans.Status=%s
                    GROUP BY Date, trans.Origin_ID, l.City_ID
    				ORDER BY Date;'''
        query_params = (self.var_city_name.get(), self.var_status.get())
        print(cursor.execute(query, query_params))
        
        # Store Data
        for row in cursor.fetchall():
            arr_x.set.append(row[1])
            arr_y.set.append(row[0])
        disconnectDB(connection)
        
        print(arr_x)
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
# =============================================================================

    def saveImg(self):
        plt.savefig('my_figure.png')
        
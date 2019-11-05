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
import matplotlib.dates as mdates  # Handle Dates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
        query = '''SELECT City_Name `City Name` FROM city;'''
        cursor.execute(query)
        city_list = []
        for row in cursor.fetchall():
            city_list.append(row)
        disconnectDB(connection)
        
        self.var_city_name = StringVar()
        city_name_input = ttk.Combobox(city_name_frame, values = city_list, state='readonly', textvariable = self.var_city_name)
        city_name_input.set('Select City')
        city_name_input.pack(fill = tk.X)
        
        # Import Data from Transaction Table
        
        # X-Axis Label: Months
# =============================================================================
#         x_label = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#         
#         # Y-Axis Label: Total Sales Amount per Month
#         connection = connectDB()
#         cursor = connection.cursor()
#         query = '''SELECT Paid_Amount FROM transaction WHERE Updated_At;'''
#         cursor.execute(query)
#         city_list = []
#         for row in cursor.fetchall():
#             city_list.append(row)
#         disconnectDB(connection)
# =============================================================================
        
        
        Data1 = {
        'Time': ['US','CA','GER','UK','FR'],
        'Sales_Amount': [45000,42000,52000,49000,47000]
       }

        # Create Pandas to structure the input data
        df1 = pd.DataFrame(Data1, columns= ['Time', 'Sales_Amount'])
        df1 = df1[['Time', 'Sales_Amount']].groupby('Time').sum()
        
        # Create a figure object
        # Figure params: figsize(width, height), 
        figure1 = plt.Figure(figsize=(6,5), dpi=110, facecolor="b")
        # add_subplot ->> add multiple plots to a figure
        ax1 = figure1.add_subplot(111)
        
        # FigureCanvasTkAgg can then generate a widget for Tkinter to use
        bar1 = FigureCanvasTkAgg(figure1, master)
        
        bar1.get_tk_widget().pack(fill=tk.BOTH)
        df1.plot(kind='line', legend=True, ax=ax1)
        plt.title(figure1, 'Sales Report')
        
        #Set Action Buttion Frame
        act_button_frame = tk.Frame(self)
        act_button_frame.pack(padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        save_button = tk.Button(act_button_frame, text = "Save", width = styleDict["buttonWidth"], 
                                command = self.saveImg)
        save_button.pack(side = tk.LEFT)
        
    def saveImg(self):
        plt.savefig('my_figure.png')
        
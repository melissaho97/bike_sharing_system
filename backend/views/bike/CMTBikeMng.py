#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:59:32 2019

@author: pat
"""
#import libraries
import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
import pymysql
import pymysql
from pandastable import Table, TableModel

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
    password = '1234'
    db = 'BikeSharedSystem' 
    try:
        connection = pymysql.connect(host, user, password, db)
        #print("Connect to DB Success")
    except pymysql.InternalError as e:
        popupMsg(e)
        #print("Connection Error", e)
    return connection

def disconnectDB(connection):
    connection.close()
    

class BikeMngPage(tk.Frame):
    
    def __init__(self, master):
        
        #Initialize Frame
        tk.Frame.__init__(self, master)
        self.pack(fill = tk.BOTH, expand = True)
        
        #Initialize Style Dict
        styleDict = init_styleSheet()
        
        #Set Header Frame
        h_frame = tk.Frame(self, bg = styleDict["TabHeaderBgColor"], height = styleDict["topPadding"])
        h_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        
        #Set Menu Frame
        menu_frame = tk.Frame(self)
        menu_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])

        menu_label = tk.Label(menu_frame, text = "Bike Management: ", font = ('Arial', 18), anchor = tk.W)
        menu_label.pack(side = tk.LEFT)

        #Set Action Button Frame
        act_button_frame = tk.Frame(self)
        act_button_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        edit_button = tk.Button(act_button_frame, text = "Edit", width = styleDict["buttonWidth"], 
                                command = lambda: master.switch_frame(BikeEditPage))
        edit_button.pack(side = tk.RIGHT)
        add_button = tk.Button(act_button_frame, text = "Add", width = styleDict["buttonWidth"], 
                                command = lambda: master.switch_frame(BikeAddPage))
        add_button.pack(side = tk.RIGHT, padx = styleDict["inlinePadding"])
        
        #Set Input Filter Frame
        input_filter_frame = tk.Frame(self)
        input_filter_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        
        #Filter by Bike ID
        bike_label = tk.Label(input_filter_frame, text = "Bike ID: ", width = styleDict["labelLen"], anchor = tk.W)
        bike_label.pack(side = tk.LEFT)
        
        #Get Bike ID from DB
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT ID `Bike ID` FROM bike ORDER BY ID;'''
        cursor.execute(query)
        bike_list = []
        for row in cursor.fetchall():
            bike_list.append(row)
        disconnectDB(connection)
        
        self.var_bike_id = StringVar()
        bike_id_input = ttk.Combobox(input_filter_frame, values = bike_list, state='readonly', textvariable = self.var_bike_id)
        bike_id_input.pack(side = tk.LEFT, padx = styleDict["inlinePadding"])
        
        
        #Filter by Location
        location_label = tk.Label(input_filter_frame, text = "Location: ", width = styleDict["labelLen"], anchor = tk.W)
        location_label.pack(side = tk.LEFT)
        
        #Get Location from DB
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT Zone_Name FROM location ORDER BY Zone_Name;'''
        cursor.execute(query)
        location_list = []
        for row in cursor.fetchall():
            location_list.append(row[0])
        disconnectDB(connection)
        
        self.var_location_name = StringVar()
        location_input = ttk.Combobox(input_filter_frame, values = location_list, state='readonly', textvariable = self.var_location_name)
        location_input.pack(side = tk.LEFT, padx = styleDict["inlinePadding"])
        
        #Filter by City
        city_label = tk.Label(input_filter_frame, text = "City: ", width = styleDict["labelLen"], anchor = tk.W)
        city_label.pack(side = tk.LEFT)
        
        #Get City from DB
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT City_Name `City Name` FROM city ORDER BY City_Name;'''
        cursor.execute(query)
        city_list = []
        for row in cursor.fetchall():
            city_list.append(row)
        disconnectDB(connection)
        
        self.var_city_name = StringVar()
        city_input = ttk.Combobox(input_filter_frame, values = city_list, state='readonly', textvariable = self.var_city_name)
        city_input.pack(side = tk.LEFT, padx = styleDict["inlinePadding"])
        
        
        #Add Clear & Search Button
        clear_button = tk.Button(input_filter_frame, text = "Clear", width = styleDict["buttonWidth"], 
                                command = lambda: master.switch_frame(BikeMngPage))
        clear_button.pack(side = tk.RIGHT)
        
        search_button = tk.Button(input_filter_frame, text = "Search", width = styleDict["buttonWidth"], 
                                command = self.FilterResult)
        search_button.pack(side = tk.RIGHT, padx = styleDict["inlinePadding"])
        
        
    def FilterResult(self):
        #Create Data Table Frame
        table_frame = tk.Frame(self)
        table_frame.pack(fill = tk.BOTH, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT b.ID `Bike ID`, t.Type_Name `Type Name`, b.`Condition` `Status`, b.Updated_At `Last Updated At`, l.Zone_Name `Location`, c.City_Name `City`
                    FROM bike b
                    INNER JOIN type t ON b.Type_ID = t.ID
                    INNER JOIN location l ON l.ID = b.Location_ID
                    INNER JOIN city c ON c.ID = b.City_ID
                    ORDER BY b.ID;'''
        sql = pd.read_sql_query(query, connection, params = None)

        bike_df = pd.DataFrame(sql, columns = ['Bike ID','Type Name', 'Status', 'Last Updated At', 'Location', 'City'])
        disconnectDB(connection)
        if len(self.var_bike_id.get()) != 0:
            bike_id = int(self.var_bike_id.get())
            bike_df = bike_df.loc[bike_df['Bike ID'] == bike_id]
        if len(self.var_location_name.get()) != 0:
            bike_df = bike_df.loc[bike_df['Location'] == self.var_location_name.get()]
        if len(self.var_city_name.get()) != 0:
            bike_df = bike_df.loc[bike_df['City'] == self.var_city_name.get()]  
       
        #Set Data Table Frame (Display table only have a data)
        if not bike_df.empty:
            bike_table = Table(table_frame, dataframe = bike_df, showstatusbar = True)
            bike_table.show()
        else:
            popupMsg("No data found.")
        
class BikeAddPage(tk.Frame):
    def __init__(self, master):
        
        #Initialize Frame
        tk.Frame.__init__(self, master)
        self.pack(fill = tk.BOTH, expand = True)
    

class BikeEditPage(tk.Frame):
    def __init__(self, master):
        
        #Initialize Frame
        tk.Frame.__init__(self, master)
        self.pack(fill = tk.BOTH, expand = True)



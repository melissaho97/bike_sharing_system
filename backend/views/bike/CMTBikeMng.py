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
    password = ''
    db = 'bikesharedsystem' 
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
        
        #Create Data Table Frame
        table_frame = tk.Frame(self)
        table_frame.pack(fill = tk.BOTH, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        
        #Get All Locations
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT b.ID ID, b.Condition, b.Updated_At `Last Updated At`,
                            l.Zone_Name `Location Name`,
                            t.Type_Name `Type Name`
                            FROM bike AS b
                            INNER JOIN location AS l ON b.Location_ID = l.ID
                            INNER JOIN type AS t ON b.Type_ID = t.ID;'''
        sql = pd.read_sql_query(query, connection, params = None)
        location_df = pd.DataFrame(sql, columns = ['ID','Condition','Last Updated At', 'Location Name', 'Type Name'])
        disconnectDB(connection)
        
        #Set Data Table Frame (Display table only have a data)
        if not location_df.empty:
            location_table = Table(table_frame, dataframe = location_df, showstatusbar = True)
            location_table.show()
        
class BikeAddPage(tk.Frame):
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
        menu_label = tk.Label(menu_frame, text = "Add Bike: ", font = ('Arial', 18), anchor = tk.W)
        menu_label.pack(side = tk.LEFT)
# TYPE       
        #Set Type Name Frame
        type_name_frame = tk.Frame(self)
        type_name_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        type_name_label = tk.Label(type_name_frame, text = "Type: ", width = styleDict["labelLen"], anchor = tk.W)
        type_name_label.pack(side = tk.LEFT)
        #Get Type from DB
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT ID, Type_Name `Type Name` FROM type ORDER BY Type_Name;'''
        cursor.execute(query)
        type_list = []
        for row in cursor.fetchall():
            type_list.append(row[1])
        disconnectDB(connection)
        #Set Type Combobox
        self.var_type_name = StringVar()
        type_name_input = ttk.Combobox(type_name_frame, values = type_list, state='readonly', textvariable = self.var_type_name)
        #city_name_input.current(0)
        type_name_input.pack(fill = tk.X)
        
# CITY        
        #Set City Name Frame
        city_name_frame = tk.Frame(self)
        city_name_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        self.var_city_name = StringVar()
        #Set Type Name Frame
        type_name_frame = tk.Frame(self)
        type_name_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])

        
        city_name_label = tk.Label(city_name_frame, text = "City Name: ", width = styleDict["labelLen"], anchor = tk.W)
        city_name_label.pack(side = tk.LEFT)
        
        city_name_input = tk.Entry(city_name_frame, textvariable = self.var_city_name)
        city_name_register = city_name_frame.register(chkNumber)
        city_name_input.config(validate = "key", validatecommand = (city_name_register, "%P"))
        city_name_input.pack(fill = tk.X)
        
        #Set Action Buttion Frame
        act_button_frame = tk.Frame(self)
        act_button_frame.pack(padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        back_button = tk.Button(act_button_frame, text = "Back", width = styleDict["buttonWidth"], 
                                command = lambda: master.switch_frame(BikeMngPage))
        back_button.pack(side = tk.RIGHT)
        confirm_button = tk.Button(act_button_frame, text = "Confirm", width = styleDict["buttonWidth"], 
                                command = self.addBike)
        confirm_button.pack(side = tk.RIGHT, fill = tk.X, padx = styleDict["inlinePadding"])
        
        
# CITY        
        #Set city ID Frame
        city_id_frame = tk.Frame(self)
        city_id_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        city_id_label = tk.Label(city_id_frame, text = "city name: ", width = styleDict["labelLen"], anchor = tk.W)
        city_id_label.pack(side = tk.LEFT)
        
        #Get Location from DB
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT ID, Zone_Name `Location Name` FROM location;'''
        cursor.execute(query)
        location_list = []
        for row in cursor.fetchall():
            location_list.append(row)
        disconnectDB(connection)
        #Set Location Combobox
        self.var_location_id = StringVar()
        location_id_input = ttk.Combobox(location_id_frame, values = location_list, state='readonly', textvariable = self.var_location_id)
        location_id_input.bind("<<ComboboxSelected>>", self.callback)
        #city_name_input.current(0)
        location_id_input.pack(fill = tk.X)
        
# LOCATION        
        #Set Location ID Frame
        location_id_frame = tk.Frame(self)
        location_id_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        location_id_label = tk.Label(location_id_frame, text = "Location ID: ", width = styleDict["labelLen"], anchor = tk.W)
        location_id_label.pack(side = tk.LEFT)
        #Get Location from DB
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT ID, Zone_Name `Location Name` FROM location;'''
        cursor.execute(query)
        location_list = []
        for row in cursor.fetchall():
            location_list.append(row)
        disconnectDB(connection)
        #Set Location Combobox
        self.var_location_id = StringVar()
        location_id_input = ttk.Combobox(location_id_frame, values = location_list, state='readonly', textvariable = self.var_location_id)
        location_id_input.bind("<<ComboboxSelected>>", self.callback)
        #city_name_input.current(0)
        location_id_input.pack(fill = tk.X)

        
    def addBike(self):
        #Get All Data From User Control
        tmp_type_name = self.var_type_name.get()
        tmp_location_id = self.var_location_id.get()
        tmp_city_name = self.var_city_name.get()
    
        try:
            #Get More Data from DB
            connection = connectDB()
            cursor = connection.cursor()
            query = '''SELECT ID, City_Name `City Name` FROM city WHERE City_Name = %s;'''
            cursor.execute(query, tmp_city_name)
            for row in cursor.fetchall():
                tmp_city_id = row[0]
            disconnectDB(connection)
            
            #Get More Data from DB
            connection = connectDB()
            cursor = connection.cursor()
            query = '''SELECT ID, Type_Name `Type Name` FROM type WHERE Type_Name = %s;'''
            cursor.execute(query, tmp_type_name)
            for row in cursor.fetchall():
                tmp_type_id = row[0]
            disconnectDB(connection)
        
# =============================================================================
#             #Get More Data from DB
#             connection = connectDB()
#             cursor = connection.cursor()
#             query = '''SELECT ID ID, Zone_Name `Location Name` FROM location WHERE `ID` = %s;'''
#             cursor.execute(query, tmp_location_id)
#             for row in cursor.fetchall():
#                 tmp_location_id = row[0]
#             disconnectDB(connection)
# =============================================================================
        
            #Insert Data into DB
            connection = connectDB()
            cursor = connection.cursor()
            query = '''INSERT INTO bike (`Condition`, Location_ID, City_ID, Created_At, Updated_At, Type_ID) VALUES('Available', %s, %s, NOW(), NOW(), %s);'''
            query_param = (tmp_location_id, tmp_city_id, tmp_type_id)
            cursor.execute(query, query_param)
            connection.commit()
            disconnectDB(connection)
            result = True
        except:
            result = False
        
        if result:
            msg = "Location is added successfully"
        else:
            msg = "Some thing went wrong. Sorry for an inconvenience"
        popupMsg(msg)
        
    def callback(self, event):
        self.setCurrentLocData()
        
    def setCurrentLocData(self):
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT l.ID ID, c.ID ID, c.City_Name `City Name`
                                FROM location AS l
                                INNER JOIN city AS c ON l.City_ID = c.ID
                                WHERE l.ID = %s;'''
        cursor.execute(query, self.var_location_id.get())
        for row in cursor.fetchall():
            self.var_city_name.set(row[2])    

class BikeEditPage(tk.Frame):
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

        menu_label = tk.Label(menu_frame, text = "Edit Bike: ", font = ('Arial', 18), anchor = tk.W)
        menu_label.pack(side = tk.LEFT)
# BIKE
        #Set bike Name Frame
        bike_name_frame = tk.Frame(self)
        bike_name_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        bike_name_label = tk.Label(bike_name_frame, text = "Bike Name: ", width = styleDict["labelLen"], anchor = tk.W)
        bike_name_label.pack(side = tk.LEFT)     
        #Get all bike from DB
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT ID FROM bike;'''
        cursor.execute(query)
        bike_list = []
        for row in cursor.fetchall():
            bike_list.append(row[0])
        disconnectDB(connection)
        #Set bike Combobox
        self.var_bike_id = StringVar()
        bike_id_input = ttk.Combobox(bike_name_frame, values = bike_list, state='readonly', textvariable = self.var_bike_id)
        # >> Bind onchange event to bike combobox
        bike_id_input.bind("<<ComboboxSelected>>", self.callback)
        bike_id_input.pack(fill = tk.X)
        
# CONDITION
        #Set Condition Name Frame
        condition_frame = tk.Frame(self)
        condition_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        condition_label = tk.Label(condition_frame, text = "Condition: ", width = styleDict["labelLen"], anchor = tk.W)
        condition_label.pack(side = tk.LEFT)
        #Set Condition Combobox
        self.var_condition = StringVar()
        condition_list= ["available","broken","void"]
        condition_input = ttk.Combobox(condition_frame, values = condition_list, state='readonly', textvariable = self.var_condition)
        condition_input.pack(fill = tk.X)
        
# LOCATION
        #Set location Name Frame
        location_name_frame = tk.Frame(self)
        location_name_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        location_name_label = tk.Label(location_name_frame, text = "location Name: ", width = styleDict["labelLen"], anchor = tk.W)
        location_name_label.pack(side = tk.LEFT)
        #Get all Location from DB
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT Zone_Name `Location Name` FROM location;'''
        cursor.execute(query)
        location_list = []
        for row in cursor.fetchall():
            location_list.append(row)
        disconnectDB(connection)
        #Set Location Combobox
        self.var_location_name = StringVar()
        location_name_input = ttk.Combobox(location_name_frame, values = location_list, state='readonly', textvariable = self.var_location_name)
        # >> Bind onchange event to location combobox
        location_name_input.bind("<<ComboboxSelected>>", self.callback)
        location_name_input.pack(fill = tk.X)
        
## CITY
#        #Set CITY Name Frame
#        city_name_frame = tk.Frame(self)
#        city_name_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
#        city_name_label = tk.Label(city_name_frame, text = "city Name: ", width = styleDict["labelLen"], anchor = tk.W)
#        city_name_label.pack(side = tk.LEFT)
#        #Get all Location from DB
#        connection = connectDB()
#        cursor = connection.cursor()
#        query = '''SELECT Zone_Name `Location Name` FROM location;'''
#        cursor.execute(query)
#        city_list = []
#        for row in cursor.fetchall():
#            location_list.append(row)
#        disconnectDB(connection)
##        #Set Location Combobox
##        self.var_location_name = StringVar()
##        location_name_input = ttk.Combobox(location_name_frame, values = location_list, state='readonly', textvariable = self.var_location_name)
##        # >> Bind onchange event to location combobox
##        location_name_input.bind("<<ComboboxSelected>>", self.callback)
##        location_name_input.pack(fill = tk.X)
        
# TYPE
        #Set type Name Frame
        type_id_frame = tk.Frame(self)
        type_id_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        type_id_label = tk.Label(type_id_frame, text = "type id: ", width = styleDict["labelLen"], anchor = tk.W)
        type_id_label.pack(side = tk.LEFT)
        #Get all Location from DB
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT id FROM type;'''
        cursor.execute(query)
        type_list = []
        for row in cursor.fetchall():
            type_list.append(row)
        disconnectDB(connection)
        #Set type Combobox
        self.var_type_id = StringVar()
        type_id_input = ttk.Combobox(type_id_frame, values = type_list, state='readonly', textvariable = self.var_type_id)
        # >> Bind onchange event to location combobox
        type_id_input.bind("<<ComboboxSelected>>", self.callback)
        type_id_input.pack(fill = tk.X)
        
# BUTTON        
        #Set Action Buttion Frame
        act_button_frame = tk.Frame(self)
        act_button_frame.pack(padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        back_button = tk.Button(act_button_frame, text = "Back", width = styleDict["buttonWidth"], 
                                command = lambda: master.switch_frame(BikeMngPage))
        back_button.pack(side = tk.RIGHT)
        confirm_button = tk.Button(act_button_frame, text = "Confirm", width = styleDict["buttonWidth"], 
                                command = self.editLocation)
        confirm_button.pack(side = tk.RIGHT, fill = tk.X, padx = styleDict["inlinePadding"])

    def callback(self, event):
        self.setCurrentLocData()
        
    def setCurrentLocData(self):
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT l.Zone_Name `Location Name`, c.City_Name `City Name`, l.Slot, l.`Status`
                                FROM location AS l
                                INNER JOIN city AS c ON l.City_ID = c.ID
                                WHERE l.Zone_Name = %s;'''
        cursor.execute(query, self.var_location_name.get())
        for row in cursor.fetchall():
            self.var_city_name.set(row[1])
            self.var_slot.set(row[2])
            self.var_status.set(row[3])
    
    def editLocation(self):
        #Get All Data From User Control
        tmp_condition = self.var_condition.get()
        tmp_location_name = self.var_location_name.get()
        tmp_city_name = self.var_city_name.get()
        tmp_type_id = self.var_type_id.get()
        
        try:
            #Get More Data from DB
            connection = connectDB()
            cursor = connection.cursor()
            # >> Get Location ID
            query = '''SELECT ID FROM location WHERE `Zone_Name` = %s;'''
            cursor.execute(query, tmp_location_name)
            for row in cursor.fetchall():
                tmp_location_id = row[0]            
            # >> Get City ID
            query = '''SELECT ID FROM city WHERE `City_Name` = %s;'''
            cursor.execute(query, tmp_city_name)
            for row in cursor.fetchall():
                tmp_city_id = row[0]
            disconnectDB(connection)
        
            #Update Data into DB
            connection = connectDB()
            cursor = connection.cursor()
            query = '''UPDATE bike SET `Condition` = %s, `Location_ID` = %s, City_ID = %s, Updated_At = NOW(), Type_ID = %s;'''
            query_param = (tmp_condition, tmp_location_id, tmp_location_id, tmp_city_id, tmp_type_id)
            cursor.execute(query, query_param)
            connection.commit()
            disconnectDB(connection)
            result = True
        except:
            result = False
        
        if result:
            msg = "Location is updated successfully"
        else:
            msg = "Some thing went wrong. Sorry for an inconvenience"
        popupMsg(msg)
        




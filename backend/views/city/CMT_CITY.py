#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 13:55:37 2019

@author: wang
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
    styleDict["labelLen"] = 15
    styleDict["xPadding"] = 20
    styleDict["yPadding"] = 5
    styleDict["inlinePadding"] = 5
    styleDict["topPadding"] = 150
    styleDict["fontColor"] = "black"
    styleDict["fontCity"] = "Arial"
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
    password = 'ww1214100'
    db = 'BIKE'
    try:
        connection = pymysql.connect(host, user, password, db)
        #print("Connect to DB Success")
    except pymysql.InternalError as e:
        popupMsg(e)
        #print("Connection Error", e)
    return connection

def disconnectDB(connection):
    connection.close()


class CityMngPage(tk.Frame):
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

        menu_label = tk.Label(menu_frame, text = "City Management: ", font = ('Arial', 18), anchor = tk.W)
        menu_label.pack(side = tk.LEFT)

        #Set Action Button Frame
        act_button_frame = tk.Frame(self)
        act_button_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        edit_button = tk.Button(act_button_frame, text = "Edit", width = styleDict["buttonWidth"],
                                command = lambda: master.switch_frame(CityEditPage))
        edit_button.pack(side = tk.RIGHT)
        add_button = tk.Button(act_button_frame, text = "Add", width = styleDict["buttonWidth"],
                                command = lambda: master.switch_frame(CityAddPage))
        add_button.pack(side = tk.RIGHT, padx = styleDict["inlinePadding"])

        #Create Data Table Frame
        table_frame = tk.Frame(self)
        table_frame.pack(fill = tk.BOTH, padx = styleDict["xPadding"], pady = styleDict["yPadding"])

        #Get All Citys
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT l.ID ID, l.City_Name `City Name`,
                                l.Status , l.Created_At `Created_At`, l.Updated_At, l.Last_Operator_ID
                                FROM city AS l'''
        sql = pd.read_sql_query(query, connection, params = None)
        City_df = pd.DataFrame(sql, columns = ['ID','City Name', 'Status', 'Created_At', 'Updated_At','Last_Operator_ID'])
        disconnectDB(connection)

        #Set Data Table Frame (Display table only have a data)
        if not City_df.empty:
            City_table = Table(table_frame, dataframe = City_df, showstatusbar = True)
            City_table.show()

class CityAddPage(tk.Frame):
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

        menu_label = tk.Label(menu_frame, text = "Add City: ", font = ('Arial', 18), anchor = tk.W)
        menu_label.pack(side = tk.LEFT)

        #Set City Name Frame
        City_name_frame = tk.Frame(self)
        City_name_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        City_name_label = tk.Label(City_name_frame, text = "City Name: ", width = styleDict["labelLen"], anchor = tk.W)
        City_name_label.pack(side = tk.LEFT)
        self.var_City_name = StringVar()
        City_name_input = tk.Entry(City_name_frame, textvariable = self.var_City_name)
        City_name_input.pack(fill = tk.X)

        # Set City status
        status_frame = tk.Frame(self)
        status_frame.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        status_label = tk.Label(status_frame, text="Status: ", width=styleDict["labelLen"], anchor=tk.W)
        status_label.pack(side=tk.LEFT)
        status_list = ["Active", "Inactive"]
        self.var_status = StringVar()
        status_input = ttk.Combobox(status_frame, values=status_list, state='readonly', textvariable=self.var_status)
        status_input.current(0)
        status_input.pack(fill=tk.X)

        #Set Action Buttion Frame
        act_button_frame = tk.Frame(self)
        act_button_frame.pack(padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        back_button = tk.Button(act_button_frame, text = "Back", width = styleDict["buttonWidth"],
                                command = lambda: master.switch_frame(CityMngPage))
        back_button.pack(side = tk.RIGHT)
        confirm_button = tk.Button(act_button_frame, text = "Confirm", width = styleDict["buttonWidth"],
                                command = self.addCity)
        confirm_button.pack(side = tk.RIGHT, fill = tk.X, padx = styleDict["inlinePadding"])

    def addCity(self):
        #Get All Data From User Control
        tmp_City_name = self.var_City_name.get()
        tmp_status_input = self.var_status.get()
        tmp_operator_ID = 1

        try:
            #Insert Data into DB
            connection = connectDB()
            cursor = connection.cursor()
            query = '''INSERT INTO city ('City_Name', 'Status', `Created_At`, `Updated_At`, 'Last_Operator') VALUES(%s, %s, NOW(), NOW(),%s);'''
            query_param = (tmp_City_name, tmp_status_input, tmp_operator_ID)
            cursor.execute(query, query_param)
            connection.commit()
            disconnectDB(connection)
            result = True
        except:
            result = False

        if result:
            msg = "City is added successfully"
        else:
            msg = "Some thing went wrong. Sorry for an inconvenience"
        popupMsg(msg)


class CityEditPage(tk.Frame):
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

        menu_label = tk.Label(menu_frame, text = "Edit City: ", font = ('Arial', 18), anchor = tk.W)
        menu_label.pack(side = tk.LEFT)

        #Set City Name Frame
        City_name_frame = tk.Frame(self)
        City_name_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        City_name_label = tk.Label(City_name_frame, text = "City Name: ", width = styleDict["labelLen"], anchor = tk.W)
        City_name_label.pack(side = tk.LEFT)

        #Get City from DB
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT ID, City_Name `City Name` FROM city ORDER BY City_Name;'''
        cursor.execute(query)
        City_list = []
        for row in cursor.fetchall():
            City_list.append(row[1])
        disconnectDB(connection)

        #Set City Combobox
        self.var_City_name = StringVar()
        City_name_input = ttk.Combobox(City_name_frame, values = City_list, state='readonly', textvariable = self.var_City_name)
        # >> Bind onchange event to City combobox
        City_name_input.bind("<<ComboboxSelected>>", self.callback)
        City_name_input.pack(fill = tk.X)

        # Set Status Frame
        status_frame = tk.Frame(self)
        status_frame.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        status_label = tk.Label(status_frame, text="Status: ", width=styleDict["labelLen"], anchor=tk.W)
        status_label.pack(side=tk.LEFT)
        status_list = ["Active", "Inactive"]
        self.var_status = StringVar()
        status_input = ttk.Combobox(status_frame, values=status_list, state='readonly', textvariable=self.var_status)
        status_input.pack(fill=tk.X)

        #Set Action Buttion Frame
        act_button_frame = tk.Frame(self)
        act_button_frame.pack(padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        back_button = tk.Button(act_button_frame, text = "Back", width = styleDict["buttonWidth"],
                                command = lambda: master.switch_frame(CityMngPage))
        back_button.pack(side = tk.RIGHT)
        confirm_button = tk.Button(act_button_frame, text = "Confirm", width = styleDict["buttonWidth"],
                                command = self.editCity)
        confirm_button.pack(side = tk.RIGHT, fill = tk.X, padx = styleDict["inlinePadding"])

    def callback(self, event):
        self.setCurrentCityData()

    def setCurrentCityData(self):
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT l.City_Name `City Name`, l.Slot, l.`Status`
                                FROM City AS l;'''
        cursor.execute(query, self.var_City_name.get())
        for row in cursor.fetchall():
            self.var_City_name.set(row[1])
            self.var_status.set(row[2])

    def editCity(self):
        #Get All Data From User Control
        tmp_City_name = self.var_City_name.get()
        tmp_status_input = self.var_status.get()
        tmp_operator_ID = 1

        try:
            #Get More Data from DB
            connection = connectDB()
            cursor = connection.cursor()
            # >> Get City ID
            query = '''SELECT ID, City_Name FROM city WHERE `City_Name` = %s;'''
            cursor.execute(query, tmp_City_name)
            for row in cursor.fetchall():
                tmp_City_id = row[0]
            disconnectDB(connection)

            #Update Data into DB
            connection = connectDB()
            cursor = connection.cursor()
            query = '''UPDATE City SET 'Status' = %s, 'Updated_At' = NOW(), 'Last_Operator_ID' = %s WHERE ID = %s;'''
            query_param = (tmp_status_input, tmp_City_id, tmp_operator_ID, tmp_day_price_input)
            cursor.execute(query, query_param)
            connection.commit()
            disconnectDB(connection)
            result = True
        except:
            result = False

        if result:
            msg = "City is updated successfully"
        else:
            msg = "Some thing went wrong. Sorry for an inconvenience"
        popupMsg(msg)

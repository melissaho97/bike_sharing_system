#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 13:55:37 2019

@author: melissa
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


class TypeMngPage(tk.Frame):
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

        menu_label = tk.Label(menu_frame, text = "Type Management: ", font = ('Arial', 18), anchor = tk.W)
        menu_label.pack(side = tk.LEFT)

        #Set Action Button Frame
        act_button_frame = tk.Frame(self)
        act_button_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        edit_button = tk.Button(act_button_frame, text = "Edit", width = styleDict["buttonWidth"],
                                command = lambda: master.switch_frame(TypeEditPage))
        edit_button.pack(side = tk.RIGHT)
        add_button = tk.Button(act_button_frame, text = "Add", width = styleDict["buttonWidth"],
                                command = lambda: master.switch_frame(TypeAddPage))
        add_button.pack(side = tk.RIGHT, padx = styleDict["inlinePadding"])

        #Create Data Table Frame
        table_frame = tk.Frame(self)
        table_frame.pack(fill = tk.BOTH, padx = styleDict["xPadding"], pady = styleDict["yPadding"])

        #Get All types
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT t.ID ID, t.Type_Name `Type Name`,
                                t.Fixed_Price 'Fixed Price', t.Add_Price `Add-Ons Price`, t.Day_Price `Day Price`
                                FROM type AS t'''
        sql = pd.read_sql_query(query, connection, params = None)
        type_df = pd.DataFrame(sql, columns = ['ID','Type Name', 'Fixed Price', 'Add-Ons Price', 'Day Price'])
        disconnectDB(connection)

        #Set Data Table Frame (Display table only have a data)
        if not type_df.empty:
            type_table = Table(table_frame, dataframe = type_df, showstatusbar = True)
            type_table.show()

class TypeAddPage(tk.Frame):
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

        menu_label = tk.Label(menu_frame, text = "Add Type: ", font = ('Arial', 18), anchor = tk.W)
        menu_label.pack(side = tk.LEFT)

        #Set type Name Frame
        type_name_frame = tk.Frame(self)
        type_name_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        type_name_label = tk.Label(type_name_frame, text = "Type Name: ", width = styleDict["labelLen"], anchor = tk.W)
        type_name_label.pack(side = tk.LEFT)
        self.var_type_name = StringVar()
        type_name_input = tk.Entry(type_name_frame, textvariable = self.var_type_name)
        type_name_input.pack(fill = tk.X)

        #Set Fixed Price Frame
        fixed_price_frame = tk.Frame(self)
        fixed_price_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        fixed_price_label = tk.Label(fixed_price_frame, text = "Fixed Price: ", width = styleDict["labelLen"], anchor = tk.W)
        fixed_price_label.pack(side = tk.LEFT)
        self.var_fixed_price = StringVar()
        fixed_price_input = tk.Entry(fixed_price_frame, textvariable = self.var_fixed_price)
        #fixed_price_register = fixed_price_frame.register(chkNumber)
        #fixed_price_input.config(validate = "key", validatecommand = (fixed_price_register, "%P"))
        fixed_price_input.pack(fill = tk.X)

        #Set Add Price Frame
        add_price_frame = tk.Frame(self)
        add_price_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        add_price_label = tk.Label(add_price_frame, text = "Add Price: ", width = styleDict["labelLen"], anchor = tk.W)
        add_price_label.pack(side = tk.LEFT)
        self.var_add_price = StringVar()
        add_price_input = tk.Entry(add_price_frame, textvariable = self.var_add_price)
        #add_price_register = add_price_frame.register(chkNumber)
        #add_price_input.config(validate = "key", validatecommand = (add_price_register, "%P"))
        add_price_input.pack(fill = tk.X)


        #Set Day Price Frame
        day_price_frame = tk.Frame(self)
        day_price_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        day_price_label = tk.Label(day_price_frame, text = "Add Price: ", width = styleDict["labelLen"], anchor = tk.W)
        day_price_label.pack(side = tk.LEFT)
        self.var_day_price = StringVar()
        day_price_input = tk.Entry(day_price_frame, textvariable = self.var_day_price)
        #day_price_register = day_price_frame.register(chkNumber)
        #day_price_input.config(validate = "key", validatecommand = (day_price_register, "%P"))
        day_price_input.pack(fill = tk.X)

        #Set Action Buttion Frame
        act_button_frame = tk.Frame(self)
        act_button_frame.pack(padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        back_button = tk.Button(act_button_frame, text = "Back", width = styleDict["buttonWidth"],
                                command = lambda: master.switch_frame(TypeMngPage))
        back_button.pack(side = tk.RIGHT)
        confirm_button = tk.Button(act_button_frame, text = "Confirm", width = styleDict["buttonWidth"],
                                command = self.addtype)
        confirm_button.pack(side = tk.RIGHT, fill = tk.X, padx = styleDict["inlinePadding"])

    def addtype(self):
        #Get All Data From User Control
        tmp_type_name = self.var_type_name.get()
        tmp_fixed_price_input = self.var_fixed_price.get()
        tmp_add_price_input = self.var_add_price.get()
        tmp_day_price_input = self.var_day_price.get()

        try:
            #Insert Data into DB
            connection = connectDB()
            cursor = connection.cursor()
            query = '''INSERT INTO type (`Type_Name`, `Fixed_Price`, `Add_Price`,  `Day_Price`) VALUES(%s, %s, %s, %s);'''
            query_param = (tmp_type_name, tmp_fixed_price_input, tmp_add_price_input, tmp_day_price_input)
            cursor.execute(query, query_param)
            connection.commit()
            disconnectDB(connection)
            result = True
        except:
            result = False

        if result:
            msg = "Type is added successfully"
        else:
            msg = "Something went wrong. Sorry for an inconvenience"
        popupMsg(msg)


class TypeEditPage(tk.Frame):
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

        menu_label = tk.Label(menu_frame, text = "Edit Type: ", font = ('Arial', 18), anchor = tk.W)
        menu_label.pack(side = tk.LEFT)

        #Set type Name Frame
        type_name_frame = tk.Frame(self)
        type_name_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        type_name_label = tk.Label(type_name_frame, text = "Type Name: ", width = styleDict["labelLen"], anchor = tk.W)
        type_name_label.pack(side = tk.LEFT)

        #Get type from DB
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT ID, Type_Name `Type Name` FROM type ORDER BY Type_Name;'''
        cursor.execute(query)
        type_list = []
        for row in cursor.fetchall():
            type_list.append(row[1])
        disconnectDB(connection)

        #Set type Combobox
        self.var_type_name = StringVar()
        type_name_input = ttk.Combobox(type_name_frame, values = type_list, state='readonly', textvariable = self.var_type_name)
        # >> Bind onchange event to type combobox
        type_name_input.bind("<<ComboboxSelected>>", self.callback)
        type_name_input.pack(fill = tk.X)

        #Set Fixed Price Frame
        fixed_price_frame = tk.Frame(self)
        fixed_price_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        self.var_fixed_price = StringVar()
        fixed_price_label = tk.Label(fixed_price_frame, text = "Fixed Price: ", width = styleDict["labelLen"], anchor = tk.W)
        fixed_price_label.pack(side = tk.LEFT)
        fixed_price_input = tk.Entry(fixed_price_frame, textvariable = self.var_fixed_price)
        fixed_price_input.pack(fill = tk.X)

        #Set Add Price Frame
        add_price_frame = tk.Frame(self)
        add_price_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        self.var_add_price = StringVar()
        add_price_label = tk.Label(add_price_frame, text = "Add-Ons Price: ", width = styleDict["labelLen"], anchor = tk.W)
        add_price_label.pack(side = tk.LEFT)
        add_price_input = tk.Entry(add_price_frame, textvariable = self.var_add_price)
        add_price_input.pack(fill = tk.X)

        #Set Day Price Frame
        day_price_frame = tk.Frame(self)
        day_price_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        self.var_day_price = StringVar()
        day_price_label = tk.Label(day_price_frame, text = "Day Price: ", width = styleDict["labelLen"], anchor = tk.W)
        day_price_label.pack(side = tk.LEFT)
        day_price_input = tk.Entry(day_price_frame, textvariable = self.var_day_price)
        day_price_input.pack(fill = tk.X)

        #Set Action Buttion Frame
        act_button_frame = tk.Frame(self)
        act_button_frame.pack(padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        back_button = tk.Button(act_button_frame, text = "Back", width = styleDict["buttonWidth"],
                                command = lambda: master.switch_frame(TypeMngPage))
        back_button.pack(side = tk.RIGHT)
        confirm_button = tk.Button(act_button_frame, text = "Confirm", width = styleDict["buttonWidth"],
                                command = self.editType)
        confirm_button.pack(side = tk.RIGHT, fill = tk.X, padx = styleDict["inlinePadding"])

    def callback(self, event):
        self.setCurrentTypeData()

    def setCurrentTypeData(self):
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT t.Type_Name `Type Name`, t.Fixed_Price, t.Add_Price, t.Day_Price
                                FROM type AS t
                                WHERE `Type_Name` = %s;'''
        cursor.execute(query, self.var_type_name.get())
        for row in cursor.fetchall():
            self.var_fixed_price.set(row[1])
            self.var_add_price.set(row[2])
            self.var_day_price.set(row[3])

    def editType(self):
        #Get All Data From User Control
        tmp_type_name = self.var_type_name.get()
        tmp_fixed_price_input = self.var_fixed_price.get()
        tmp_add_price_input = self.var_add_price.get()
        tmp_day_price_input = self.var_day_price.get()

        try:
            #Get More Data from DB
            connection = connectDB()
            cursor = connection.cursor()
            # >> Get type ID
            query = '''SELECT ID, Type_Name FROM type WHERE `Type_Name` = %s;'''
            cursor.execute(query, tmp_type_name)
            for row in cursor.fetchall():
                tmp_type_id = row[0]
            disconnectDB(connection)

            #Update Data into DB
            connection = connectDB()
            cursor = connection.cursor()
            query = '''UPDATE type SET 'Fixed_Price' = %s, `Add_Price` = %s, 'Day_Price' = %s WHERE ID = %s;'''
            query_param = (tmp_type_name, tmp_fixed_price_input, tmp_add_price_input, tmp_day_price_input)
            cursor.execute(query, query_param)
            connection.commit()
            disconnectDB(connection)
            result = True

        except:
            result = False

        if result:
            msg = "Type is updated successfully"
        else:
            msg = "Something went wrong. Sorry for an inconvenience"
        popupMsg(msg)

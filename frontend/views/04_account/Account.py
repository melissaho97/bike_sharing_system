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
    
class AccountMngPage(tk.Frame):
    
    def __init__(self, master):
        
        #Initialize Frame
        tk.Frame.__init__(self, master)
        self.pack(fill = tk.BOTH, expand = True)
        
        #Initialize Style Dict
        styleDict = init_styleSheet()
        
        #Set Header Frame
        h_frame = tk.Frame(self, bg = styleDict["TabHeaderBgColor"], height = styleDict["topPadding"])
        h_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        
        # --------------------------------------------------------------------------------------------
        # Section 1: User Profile Details
        # --------------------------------------------------------------------------------------------
        
        # Profile Picture [Fixed] + Username
        username_frame = tk.Frame(self)
        username_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        self.var_username = StringVar()
        username_label = tk.Label(username_frame, text = "Username: ", width = styleDict["labelLen"], anchor = tk.W)
        username_label.pack(side = tk.LEFT)
        
        # Full Name
        name_frame = tk.Frame(self)
        name_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        #self.var_name = StringVar()
        name_label = tk.Label(name_frame, text = "Full Name: ", width = styleDict["labelLen"], anchor = tk.W)
        name_label.pack(side = tk.LEFT)
        
        # Get Username and Name from DB
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT ID, Full_Name `Full Name` FROM customer WHERE ID=1;'''
        cursor.execute(query)
        name_list = []
        for row in cursor.fetchall():
            name_list.append(row[1])
        disconnectDB(connection)
        
        self.var_name = StringVar()
        name_input = ttk.Combobox(name_frame, values = name_list, state='readonly', textvariable = self.var_name)
        # >> Bind onchange event to type combobox
        name_input.bind("<<ComboboxSelected>>", self.callback)
        name_input.pack(fill = tk.X)
        
        #name_input = tk.Entry(name_frame, textvariable = self.var_name)
        #name_input.pack(fill = tk.X)
        
        # Phone Number
        phone_frame = tk.Frame(self)
        phone_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        self.var_phone = StringVar()
        phone_label = tk.Label(phone_frame, text = "Phone No.: ", width = styleDict["labelLen"], anchor = tk.W)
        phone_label.pack(side = tk.LEFT)
        phone_input = tk.Entry(phone_frame, textvariable = self.var_phone)
        phone_input.pack(fill = tk.X)
        
        # Email
        email_frame = tk.Frame(self)
        email_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        self.var_email = StringVar()
        email_label = tk.Label(email_frame, text = "Email: ", width = styleDict["labelLen"], anchor = tk.W)
        email_label.pack(side = tk.LEFT)
        email_input = tk.Entry(email_frame, textvariable = self.var_email)
        email_input.pack(fill = tk.X)
        
        # --------------------------------------------------------------------------------------------
        # Section 2: Card Details
        # --------------------------------------------------------------------------------------------        
        
        # Card No.
        card_no_frame = tk.Frame(self)
        card_no_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        self.var_card_no = StringVar()
        card_no_label = tk.Label(card_no_frame, text = "Card No.: ", width = styleDict["labelLen"], anchor = tk.W)
        card_no_label.pack(side = tk.LEFT)
        card_no_input = tk.Entry(card_no_frame, textvariable = self.var_card_no)
        card_no_input.pack(fill = tk.X)
        
        # Expiry Date
        date_frame = tk.Frame(self)
        date_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        self.var_date = StringVar()
        date_label = tk.Label(date_frame, text = "Expiry Date: ", width = styleDict["labelLen"], anchor = tk.W)
        date_label.pack(side = tk.LEFT)
        date_input = tk.Entry(date_frame, textvariable = self.var_date)
        date_input.pack(fill = tk.X)
        
        # CVV
        cvv_frame = tk.Frame(self)
        cvv_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        self.var_cvv = StringVar()
        cvv_label = tk.Label(cvv_frame, text = "CVV: ", width = styleDict["labelLen"], anchor = tk.W)
        cvv_label.pack(side = tk.LEFT)
        cvv_input = tk.Entry(cvv_frame, textvariable = self.var_cvv)
        cvv_input.pack(fill = tk.X)
        
        # --------------------------------------------------------------------------------------------
        # Section 3: Buttons
        # -------------------------------------------------------------------------------------------- 
        act_button_frame = tk.Frame(self)
        act_button_frame.pack(padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        
        # Save Button
        save_button = tk.Button(act_button_frame, text = "Save", width = styleDict["buttonWidth"],
                                command = self.editType)
        save_button.pack(side = tk.RIGHT, fill = tk.X, padx = styleDict["inlinePadding"])
        
        # Cancel Button
        cancel_button = tk.Button(act_button_frame, text = "Cancel", width = styleDict["buttonWidth"],
                                command = lambda: master.switch_frame(TypeMngPage))
        cancel_button.pack(side = tk.RIGHT)

    def callback(self, event):
        self.setCurrentTypeData()

    def setCurrentTypeData(self):
        connection = connectDB()
        cursor = connection.cursor()
        query = '''SELECT cust.Username `Username`, cust.Phone_Number `Phone Number`, cust.Full_Name `Full Name`, 
                    cust.Email `Email Address`, cust.Card_No `Card No.`, cust.Expired_Date `Expiry Date`, cust.CVV
                    FROM customer AS cust
                    WHERE `Username` = %s;'''
        cursor.execute(query, self.var_username_get())
        for row in cursor.fetchall():
            self.var_username.set(row[0])
            self.var_phone.set(row[0])
            self.var_name.set(row[1])
            self.var_email.set(row[2])
            self.var_card_no.set(row[4])
            self.var_date.set(row[5])
            self.var_cvv.set(row[6])

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
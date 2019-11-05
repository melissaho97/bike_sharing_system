#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 20:01:08 2019

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

#import other pages
import FrontEnd

def init_styleSheet():
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
    styleDict = init_styleSheet()
    popup = tk.Tk()
    popup.title(styleDict["Title"])
    msg_label = tk.Label(popup, text = msg)
    msg_label.pack()
    done_button = tk.Button(popup, text="Done", command = popup.destroy)
    done_button.pack()
    popup.mainloop()
    
def connectDB():
    host = 'localhost'
    user = 'root'
    password = 'Jb82-5fp'
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

class MyRentalHistoryPage(tk.Frame):
    def __init__(self, master):
        
        #Initialize Frame
        tk.Frame.__init__(self, master)
        self.pack(fill = tk.BOTH, expand = True)
        
        styleDict = init_styleSheet()
        
        #Set Header Frame
        h_frame = tk.Frame(self, bg = styleDict["TabHeaderBgColor"], height = styleDict["topPadding"])
        h_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        
        #Set Menu Frame
        menu_frame = tk.Frame(self)
        menu_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])

        menu_label = tk.Label(menu_frame, text = "My Rental History: ", font = ('Arial', 18), anchor = tk.W)
        menu_label.pack(side = tk.LEFT)

        #Set Action Button Frame
        act_button_frame = tk.Frame(self)
        act_button_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        current_tran_button = tk.Button(act_button_frame, text = "Go to Current Transaction", width = styleDict["buttonWidth"]+10, 
                                command = lambda: master.switch_frame(MyRentalHistoryPage))
        current_tran_button.pack(side = tk.RIGHT)
        
        #Create Data Table Frame
        table_frame = tk.Frame(self)
        table_frame.pack(fill = tk.BOTH, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        
        #Get All Transactions
        connection = connectDB()
        cursor = connection.cursor()
        # >> Need to get user id from log-in
        query = '''SELECT t.ID, DATE_FORMAT(t.Created_At, '%d/%m/%Y %H:%i') "Start Date", IFNULL(DATE_FORMAT(t.Updated_At, '%d/%m/%Y %H:%i'), "Now") "End Date",
                t.Bike_ID "Bike ID", CONCAT(l1.Zone_Name, " -> " ,IFNULL(l2.Zone_Name,"")) Station, 
                CONCAT(HOUR(TIMEDIFF(t.Updated_At,t.Created_At)), " hr ", MINUTE(TIMEDIFF(t.Updated_At,t.Created_At)), " min") "Time Duration", 
                CONCAT("£ ",t.Paid_Amount) Fee, t.`Status`
                FROM `transaction` t
                INNER JOIN location l1 ON t.Origin_ID = l1.ID
                LEFT JOIN location l2 ON t.Destination_ID = l2.ID
                WHERE t.Customer_ID = 1;'''
        sql = pd.read_sql_query(query, connection, params = None)
        transaction_df = pd.DataFrame(sql, columns = ['ID','Start Date', 'End Date', 'Bike ID', 'Station', 'Time Duration', 'Fee', 'Status'])
        print(transaction_df)
        disconnectDB(connection)
        
        #Set Data Table Frame
        if not transaction_df.empty:
            transaction_table = Table(table_frame, dataframe = transaction_df, showstatusbar = True)
            transaction_table.show()

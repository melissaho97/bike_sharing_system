#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:41:54 2019

@author: pat
"""
import tkinter as tk
from tkinter import ttk
import pandas as pd
from pandastable import Table, TableModel

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
    
def PopUpMsg(msg):
        popup = tk.Tk()
        popup.title(styleDict["Title"])
        msg_label = tk.Label(popup, text = msg)
        msg_label.pack()
        done_button = tk.Button(popup, text="Done", command = popup.destroy)
        done_button.pack()
        popup.mainloop()
    
class BackEndApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.geometry(styleDict["windowSize"])
        self.title(styleDict["Title"])
        self.switch_frame(BackEndHomePage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class BackEndHomePage(tk.Frame):
    def __init__(self, master):
        
        #Initialize Frame
        tk.Frame.__init__(self, master)
        
        #Display Back End Home Page
        tk.Label(self, text="Back End Home Page", font=(styleDict["fontType"], styleDict["fontSize"], styleDict["fontStyle"])).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go to Location Management Page",
                  command = lambda: master.switch_frame(LocationMngPage)).pack()


class LocationMngPage(tk.Frame):
    def __init__(self, master):
        
        #Initialize Frame
        tk.Frame.__init__(self, master)
        self.pack(fill = tk.BOTH, expand = True)
        
        #Set Header Frame
        h_frame = tk.Frame(self, bg = styleDict["TabHeaderBgColor"], height = styleDict["topPadding"])
        h_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        
        #Set Menu Frame
        menu_frame = tk.Frame(self)
        menu_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])

        menu_label = tk.Label(menu_frame, text = "Location Management: ", font = ('Arial', 18), anchor = tk.W)
        menu_label.pack(side = tk.LEFT)

        #Set Action Button Frame
        act_button_frame = tk.Frame(self)
        act_button_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        edit_button = tk.Button(act_button_frame, text = "Edit", width = styleDict["buttonWidth"], 
                                command = lambda: master.switch_frame(LocationEditPage))
        edit_button.pack(side = tk.RIGHT)
        add_button = tk.Button(act_button_frame, text = "Add", width = styleDict["buttonWidth"], 
                                command = lambda: master.switch_frame(LocationAddPage))
        add_button.pack(side = tk.RIGHT, padx = styleDict["inlinePadding"])
        
        #Create Data Table Frame
        table_frame = tk.Frame(self)
        table_frame.pack(fill = tk.BOTH, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        
        #Get All Locations
        #with sqlite3.connect("BikeSharedSystem.db") as db:
        # cursor = db.cursor()
        #cursor.execute(" SELECT * FROM location ORDER BY Updated_At DESC ")
        #for x in cursor.fetchall():
        # print(x)
        #db.close()
        location_data = {"ID":[1,2,3], "Location Name":["Zone A", "Zone B", "Zone C"], 
                         "City":["Glasgow","Glasgow","Glasgow"], "Slot":[10,10,20], "Status":["Active","Active","Active"],
                         "Last Updated Date":["22/10/2019 22:35","22/10/2019 22:36","22/10/2019 22:37"], 
                         "Last Updated By":["Operator 1","Operator 1","Operator 1"]}
        
        location_df = pd.DataFrame(location_data)
        
        #Set Data Table Frame
        location_table = Table(table_frame, dataframe = location_df, showstatusbar = True)
        location_table.show()

class LocationAddPage(tk.Frame):
    def __init__(self, master):
        
        #Initialize Frame
        tk.Frame.__init__(self, master)
        self.pack(fill = tk.BOTH, expand = True)
        
        #Set Header Frame
        h_frame = tk.Frame(self, bg = styleDict["TabHeaderBgColor"], height = styleDict["topPadding"])
        h_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        
        #Set Menu Frame
        menu_frame = tk.Frame(self)
        menu_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])

        menu_label = tk.Label(menu_frame, text = "Add Location: ", font = ('Arial', 18), anchor = tk.W)
        menu_label.pack(side = tk.LEFT)
        
        #Set Location Name Frame
        location_name_frame = tk.Frame(self)
        location_name_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        location_name_label = tk.Label(location_name_frame, text = "Location Name: ", width = styleDict["labelLen"], anchor = tk.W)
        location_name_label.pack(side = tk.LEFT)
        location_name_input = tk.Entry(location_name_frame)
        location_name_input.pack(fill = tk.X)
        
        #Set City Name Frame
        city_name_frame = tk.Frame(self)
        city_name_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        city_name_label = tk.Label(city_name_frame, text = "City Name: ", width = styleDict["labelLen"], anchor = tk.W)
        city_name_label.pack(side = tk.LEFT)
        #***** Query City Name from DB
        city_list = ["Glasgow", "Aberdeen"]
        city_name_input = ttk.Combobox(city_name_frame, values = city_list)
        city_name_input.current(0)
        city_name_input.pack(fill = tk.X)
        
        
        #Set Slot Frame
        slot_frame = tk.Frame(self)
        slot_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        slot_label = tk.Label(slot_frame, text = "Slot: ", width = styleDict["labelLen"], anchor = tk.W)
        slot_label.pack(side = tk.LEFT)
        slot_input = tk.Entry(slot_frame)
        slot_input.pack(fill = tk.X)
        
        #Set Status Frame
        status_frame = tk.Frame(self)
        status_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        status_label = tk.Label(status_frame, text = "Status: ", width = styleDict["labelLen"], anchor = tk.W)
        status_label.pack(side = tk.LEFT)
        status_list = ["Active", "Inactive"]
        status_input = ttk.Combobox(status_frame, values = status_list)
        status_input.current(0)
        status_input.pack(fill = tk.X)
        
        #Set Action Buttion Frame
        act_button_frame = tk.Frame(self)
        act_button_frame.pack(padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        back_button = tk.Button(act_button_frame, text = "Back", width = styleDict["buttonWidth"], 
                                command = lambda: master.switch_frame(LocationMngPage))
        back_button.pack(side = tk.RIGHT)
        confirm_button = tk.Button(act_button_frame, text = "Confirm", width = styleDict["buttonWidth"], 
                                command = self.AddLocation)
        confirm_button.pack(side = tk.RIGHT, fill = tk.X, padx = styleDict["inlinePadding"])
        
    def AddLocation(self):
        self.ValidateLocation()
        #Insert Data into DB
        result = True
        if result:
            msg = "Location is added successfully"
        else:
            msg = "Some thing went wrong. Sorry for an inconvenience"
        PopUpMsg(msg)
    
    def ValidateLocation(self):
        print("ValidateLocation")
        
        
        
    
class LocationEditPage(tk.Frame):
    def __init__(self, master):
        
        #Initialize Frame
        tk.Frame.__init__(self, master)
        self.pack(fill = tk.BOTH, expand = True)
        
        #Set Header Frame
        h_frame = tk.Frame(self, bg = styleDict["TabHeaderBgColor"], height = styleDict["topPadding"])
        h_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        
        #Set Menu Frame
        menu_frame = tk.Frame(self)
        menu_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])

        menu_label = tk.Label(menu_frame, text = "Edit Location: ", font = ('Arial', 18), anchor = tk.W)
        menu_label.pack(side = tk.LEFT)
        
        #Set Location Name Frame
        location_name_frame = tk.Frame(self)
        location_name_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        location_name_label = tk.Label(location_name_frame, text = "Location Name: ", width = styleDict["labelLen"], anchor = tk.W)
        location_name_label.pack(side = tk.LEFT)
        #***** Query Location Name from DB
        location_list = ["Zone A", "Zone B"]
        location_name_input = ttk.Combobox(location_name_frame, values = location_list)
        location_name_input.current(0)
        location_name_input.pack(fill = tk.X)
        
        #Set City Name Frame
        city_name_frame = tk.Frame(self)
        city_name_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        city_name_label = tk.Label(city_name_frame, text = "City Name: ", width = styleDict["labelLen"], anchor = tk.W)
        city_name_label.pack(side = tk.LEFT)
        #***** Query City Name from DB
        city_list = ["Glasgow", "Aberdeen"]
        city_name_input = ttk.Combobox(city_name_frame, values = city_list)
        city_name_input.current(0)
        city_name_input.pack(fill = tk.X)
        
        
        #Set Slot Frame
        slot_frame = tk.Frame(self)
        slot_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        slot_label = tk.Label(slot_frame, text = "Slot: ", width = styleDict["labelLen"], anchor = tk.W)
        slot_label.pack(side = tk.LEFT)
        slot_input = tk.Entry(slot_frame)
        slot_input.pack(fill = tk.X)
        
        #Set Status Frame
        status_frame = tk.Frame(self)
        status_frame.pack(fill = tk.X, padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        status_label = tk.Label(status_frame, text = "Status: ", width = styleDict["labelLen"], anchor = tk.W)
        status_label.pack(side = tk.LEFT)
        status_list = ["Active", "Inactive"]
        status_input = ttk.Combobox(status_frame, values = status_list)
        status_input.current(0)
        status_input.pack(fill = tk.X)
        
        #Set Action Buttion Frame
        act_button_frame = tk.Frame(self)
        act_button_frame.pack(padx = styleDict["xPadding"], pady = styleDict["yPadding"])
        back_button = tk.Button(act_button_frame, text = "Back", width = styleDict["buttonWidth"], 
                                command = lambda: master.switch_frame(LocationMngPage))
        back_button.pack(side = tk.RIGHT)
        confirm_button = tk.Button(act_button_frame, text = "Confirm", width = styleDict["buttonWidth"], 
                                command = self.EditLocation)
        confirm_button.pack(side = tk.RIGHT, fill = tk.X, padx = styleDict["inlinePadding"])

    
    def EditLocation(self):
        #Update Data into DB
        result = True
        if result:
            msg = "Location is updated successfully"
        else:
            msg = "Some thing went wrong. Sorry for an inconvenience"
        PopUpMsg(msg)

if __name__ == "__main__":
    styleDict = init_styleSheet()
    app = BackEndApp()
    app.mainloop()
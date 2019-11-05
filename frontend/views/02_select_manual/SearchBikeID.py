from tkinter import *
import tkinter as tk
from tkinter import ttk

import pymysql
from PIL import Image, ImageTk
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
        msg_label = tk.Label(popup, text=msg)
        msg_label.pack()
        done_button = tk.Button(popup, text="Done", command=popup.destroy)
        done_button.pack()
        popup.mainloop()


def connectDB():
    host = 'localhost'
    user = 'root'
    password = '19960907'
    db = 'cMT-Bike'
    try:
        connection = pymysql.connect(host, user, password, db)
        # print("Connect to DB Success")
    except pymysql.InternalError as e:
        popupMsg(e)
        # print("Connection Error", e)
    return connection

def disconnectDB(connection):
        connection.close()


class FrontEndApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.geometry(styleDict["windowSize"])
        self.title(styleDict["Title"])
        self.switch_frame(SearchBikeID)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class SearchBikeID(tk.Frame):
    def __init__(self, master):
        # Initialize Frame
        tk.Frame.__init__(self, master)

#img_open = Image.open('user.png')
#img_png = ImageTk.PhotoImage(img_open)
#usr = Menubutton(window, relief=RAISED, image = img_png)
#usr.place(x = 931,y = 40, width = 58, height = 58)

#usermenu = Menu(usr, tearoff=False)

#usermenu.add_command(label = 'Log Out', font = ("Arial, 28"))

#usr.config(menu=usermenu)

        self.labeltext = tk.Frame(self)
        self.labeltext.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        title = tk.Label(self.labeltext, text='cMT-Bike', font=("Arial, 40"))
        title.pack(side=tk.LEFT, pady = 20)


        self.citytext = tk.Frame(self)
        self.citytext.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        city = tk.Label(self.citytext, text = 'City:', font = ("Arial, 15"))
        city.pack(side = tk.LEFT, pady=10)


        self.citybox = tk.Frame(self)
        self.citybox.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        self.citycombo = ttk.Combobox(self.citybox, width=50)
        self.citycombo['values'] = ('Select city', 'Aberdeen', 'Cardiff', 'Edinburgh', 'Glasgow', 'London')
        self.citycombo.pack(side=tk.TOP)
        self.citycombo.current(0)

        self.zonetext = tk.Frame(self)
        self.zonetext.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        self.zone = tk.Label(self.zonetext, text = 'Zone:', font = ("Arial, 15"))
        self.zone.pack(side = tk.LEFT, pady=10)

        self.zonebox = tk.Frame(self)
        self.zonebox.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        self.zonecombo = ttk.Combobox(self.zonebox, width=50)
        self.zonecombo['values'] = ('Select Zone', 'Zone A (5 available bikes)', 'Zone B (1 available bikes)', 'Zone C (none)', 'Zone D (5 available bikes)', 'Zone E (2 available bikes)')
        self.zonecombo.pack(side=tk.TOP)
        self.zonecombo.current(0)

        self.bikeIDtext = tk.Frame(self)
        self.bikeIDtext.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        self.BikeID = tk.Label(self.bikeIDtext, text = 'Bike ID:', font = ("Arial, 15"))
        self.BikeID.pack(side = tk.LEFT, pady=10)

        self.bikeidbox = tk.Frame(self)
        self.bikeidbox.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        self.BikeIDcombo = ttk.Combobox(self.bikeidbox, width=50)
        self.BikeIDcombo['values'] = ('Select Bike ID', '1', '2', '3', '4', '5')
        self.BikeIDcombo.pack(side=tk.TOP)
        self.BikeIDcombo.current(0)

        self.confirmframe = tk.Frame(self)
        self.confirmframe.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        confirm = tk.Button(self.confirmframe, text = 'confirm',font = ("Arial, 28"), width=10, height=2, command = self.confirm)
        self.confirmframe.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        confirm.pack(side=tk.TOP, pady=30)

        back = tk.Button(self.confirmframe, text = 'Return to\nthe previous page', font = ("Arial, 24"))

    def confirm(self):
        cityvar = self.citycombo.get()
        zonevar = self.zonecombo.get()
        bikeidvar= int(self.BikeIDcombo.get())



        connection = connectDB()
        cursor = connection.cursor()
        cursor.execute(("select ID from city where City_Name=%s"),(cityvar))
        num1 = cursor.fetchone()
        num11 = num1[0]
        cursor.execute(("select ID from location where Zone_Name=%s and City_ID=%s"), (zonevar, num11))
        num2 = cursor.fetchone()
        num22 = num2[0]
        a = cursor.execute(("select `Condition` from bike where City_ID=%s and Location_ID=%s and ID=%s"),(num11, num22, bikeidvar))
        x = cursor.fetchone()
        y = x[0]
        if y=="available":
            msg = "This bike is available. You have rented!"
        else:
            msg = "This bike is unavailable.Please try another bike ID"
        popupMsg(msg)
        disconnectDB(connection)


styleDict = init_styleSheet()
app = FrontEndApp()
app.mainloop()
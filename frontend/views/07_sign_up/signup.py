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
        self.switch_frame(signup)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class signup(tk.Frame):
    def __init__(self, master):
        # Initialize Frame
        tk.Frame.__init__(self, master)

        self.label1text = tk.Frame(self)
        self.label1text.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        text1 = tk.Label(self.label1text, text='cMT-Bike', font=("Arial, 40"))
        text1.pack(side=tk.LEFT)

        self.nametext = tk.Frame(self)
        self.nametext.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        namestr = tk.Label(self.nametext, text='full name', font=("Arial, 20"))
        namestr.pack(side=tk.LEFT)

        self.name = tk.StringVar()
        nameentry = tk.Entry(self.nametext, textvariable = self.name, show = None, width = 40)
        nameentry.pack()


        self.emailtext = tk.Frame(self)
        self.emailtext.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        emailstr = tk.Label(self.emailtext, text='Email', font=("Arial, 20"))
        emailstr.pack(side=tk.LEFT,padx=15)

        self.email = tk.StringVar()
        emailentry = tk.Entry(self.emailtext, textvariable=self.email, show=None,width=40)
        emailentry.pack(side=tk.LEFT,padx=40)

        self.phonetext = tk.Frame(self)
        self.phonetext.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        phonestr = tk.Label(self.phonetext, text='Phone\nNumber', font=("Arial, 20"))
        phonestr.pack(side=tk.LEFT,padx=5)

        self.phone = tk.StringVar()
        phoneentry = tk.Entry(self.phonetext, textvariable=self.phone, show=None, width=40)
        phoneentry.pack(pady=15)

        self.unametext = tk.Frame(self)
        self.unametext.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        unamestr = tk.Label(self.unametext, text='Username', font=("Arial, 20"))
        unamestr.pack(side=tk.LEFT)

        self.username = tk.StringVar()
        unameentry = tk.Entry(self.unametext, textvariable=self.username, show=None, width=40)
        unameentry.pack()

        self.pwtext = tk.Frame(self)
        self.pwtext.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        pwstr = tk.Label(self.pwtext, text='Password', font=("Arial, 20"))
        pwstr.pack(side=tk.LEFT)

        self.password = tk.StringVar()
        pwentry = tk.Entry(self.pwtext, textvariable=self.password, show=None, width=40)
        pwentry.pack()

        self.label2text = tk.Frame(self)
        self.label2text.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        text2 = tk.Label(self.label2text, text='Password should contain at least 8 characters, including alphanumeric and a symbol.', font=("Arial, 12"))
        text2.pack(side=tk.LEFT)

        self.cpwtext = tk.Frame(self)
        self.cpwtext.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        cpwstr = tk.Label(self.cpwtext, text='Confirm\nPassword', font=("Arial, 20"))
        cpwstr.pack(side=tk.LEFT)

        self.cfpassword = tk.StringVar()
        cpwentry = tk.Entry(self.cpwtext, textvariable=self.cfpassword, show=None, width=40)
        cpwentry.pack(pady=15)

        self.label3text = tk.Frame(self)
        self.label3text.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        text3 = tk.Label(self.label3text, text='Add Payment Details',font=("Arial, 30"))
        text3.pack(side=tk.LEFT)

        self.cardnotext = tk.Frame(self)
        self.cardnotext.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        cardnostr = tk.Label(self.cardnotext, text='Card No:', font=("Arial, 20"))
        cardnostr.pack(side=tk.LEFT)

        self.cardno = tk.StringVar()
        cardnoentry = tk.Entry(self.cardnotext, textvariable=self.cardno, show=None, width=40)
        cardnoentry.pack()

        self.exdatetext = tk.Frame(self)
        self.exdatetext.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        cardnostr = tk.Label(self.exdatetext, text='Expire Date:', font=("Arial, 20"))
        cardnostr.pack(side=tk.LEFT)

        self.exdate1 = tk.StringVar()
        exdate1entry1 = tk.Entry(self.exdatetext, textvariable=self.exdate1, show=None, width=10)
        exdate1entry1.insert(0,'MM')
        exdate1entry1.pack(side=tk.LEFT,padx=10)

        text4 = tk.Label(self.exdatetext, text='/', font=("Arial, 15"))
        text4.pack(side=tk.LEFT)

        self.exdate2 = tk.StringVar()
        exdate1entry2 = tk.Entry(self.exdatetext, textvariable=self.exdate2, show=None, width=10)
        exdate1entry2.insert(0,'YYYY')
        exdate1entry2.pack(side=tk.LEFT, padx=10)

        self.cvvtext = tk.Frame(self)
        self.cvvtext.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        cvvstr = tk.Label(self.cvvtext, text='CVV:', font=("Arial, 20"))
        cvvstr.pack(side=tk.LEFT)

        self.cvv = tk.StringVar()
        cvventry = tk.Entry(self.cvvtext, textvariable=self.cvv, show=None, width=10)
        cvventry.pack(side=tk.LEFT, padx=70)

        self.signup = tk.Frame(self)
        self.signup.pack(fill=tk.X, padx=styleDict["xPadding"], pady=styleDict["yPadding"])
        spbutton = tk.Button(self.signup, text='Sign Up', font=("Arial, 25"), width=10,height=2, command=self.signupcheck)
        spbutton.pack()

    def signupcheck(self):
        connection = connectDB()
        cursor = connection.cursor()
        while(True):
            if(self.password.get()==self.cfpassword.get()):
                self.exdate=self.exdate1.get()+self.exdate2.get()
                sql = "insert into customer(Full_Name, Email, Phone_Number, Username, Password, Card_No, Expired_Date, CVV)VALUES({},{},{},{},{},{},{},{})"
                sql1 = sql.format(self.name.get(), self.email.get(), self.phone.get(), self.username.get(), self.password.get(), self.cardno.get(), self.exdate,self.cvv.get())
                print(sql1)
                a=cursor.execute(sql1)
                connection.commit()
                disconnectDB(connection)
                msg = "Sign up sucessfully!"
                popupMsg(msg)
                return False
            else:
                msg = "please make sure the confirm password is same as the password you enter before!"
                popupMsg(msg)

styleDict = init_styleSheet()
app = FrontEndApp()
app.mainloop()
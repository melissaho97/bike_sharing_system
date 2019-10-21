
from tkinter import *
import tkinter.font as tkFont
from PIL import Image, ImageTk
import webbrowser

def open_url(event):
    webbrowser.open("http://www.baidu.com", new=0)

window = Tk()
window.geometry("1024x768")
ft1 = tkFont.Font(family='Arial', size=52, weight=tkFont.NORMAL)
Label1 = Label(text ="cMT-Bike" , font = ft1)
Label1.place(x=69 , y=54 , width = 248 , height = 58)
Label1["bg"]= "white"
Label1["fg"]= "#000000"
ft2 = tkFont.Font(family='Arial', size=52, weight=tkFont.BOLD)
Label2 = Label(text ="Bike ID" , font= ft2)
Label2.place(x=316 , y=149, width = 176, height = 58)
Label2["fg"]= "#000000"
ft3 = tkFont.Font(family='Arial', size=24, weight=tkFont.NORMAL)
Label3 = Label(text ="or" , font = ft3)
Label3.place(x=511 , y=243, width = 22, height = 27)
Label3["fg"]= "#6C6C6C"
textbox1 = Entry(text ="")
textbox1.place(x=525 , y=149, width = 204, height = 58)
img_open2 = Image.open('frontend-2.png')
img_png2 = ImageTk.PhotoImage(img_open2)
Label4 = Label(image = img_png2)
Label4.place(x=79.5 , y=632.5)
ft5 = tkFont.Font(family='Arial', size=25, weight=tkFont.NORMAL, underline = 1 )
link = Label( text='Find Bike Manually', font=ft5)
link.place(x=406.5, y=654, width = 212, height = 28 )
link["fg"]= "#0525F9"
link.bind("<Button-1>", open_url)

ft4 = tkFont.Font(family='Arial', size=34, weight=tkFont.BOLD)
button1 = Button(text = "Confirm", font = ft4)
button1.place(x=79 , y=514, width = 887, height = 90)
button1["bg"] = "#F5F1F1"
img_open = Image.open('fronted-1.png')
img_png = ImageTk.PhotoImage(img_open)
ft5 = tkFont.Font(family='Arial', size=24, weight=tkFont.NORMAL)
button2 = Button(text = "Scan QR Code", compound = 'bottom', font = ft5, image = img_png)
button2.place(x=418 , y=306, width = 209, height = 150)


window.mainloop()
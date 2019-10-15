import tkinter as tk
from tkinter import *
def city_name():
    name = name_box.get()


window = Tk()
window.geometry("1024x768")
Label1 = Label(text ="Add New City" )
Label1.place(x=88 , y=201, width = 330, height = 39)
Label1["bg"]= "white"
Label1["fg"]= "#01367E"
Label1.size = 60
Label2 = Label(text ="City name:" )
Label2.place(x=88 , y=340, width = 165, height = 37)
Label2["bg"]= "white"
Label2["fg"]= "#707070"
Label3 = Label(text ="Status:" )
Label3.place(x=88 , y=426, width = 165, height = 37)
Label3["bg"]= "white"
Label3["fg"]= "#707070"

textbox1 = Entry(text ="")
textbox1.place(x=378 , y=329, width = 275, height = 35)
button1 = Button(text = "Confirm", command = city_name)
button1.place(x=373 , y=540, width = 278, height = 55)
button1["bg"] = "#A3A3A3"

number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1, 2, 4, 42, 100) # 设置下拉列表的值
numberChosen.grid(column=1, row=1) # 设置其在界面中出现的位置 column代表列 row 代表行
numberChosen.current(4) # 设置下拉列表默认显示的值，0为numberChosen['values'] 的下标值

window.mainloop()
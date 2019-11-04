from tkinter import *
from PIL import Image, ImageTk
window =Tk()
window.title('cMT-Bike(Staff ONLY)')
window.geometry('1024x4768')

title = Label(window, text = 'cMT-Bike(Staff ONLY)', font = ("Arial, 30"))
title.place(x = 139,y = 40, width = 408, height = 58)

img_open1 = Image.open('menu.png')
img_png1 = ImageTk.PhotoImage(img_open1)
mb = Menubutton(window, relief=RAISED, image = img_png1)
mb.place(x = 35,y = 43, width = 55, height = 55)

img_open2 = Image.open('user.png')
img_png2 = ImageTk.PhotoImage(img_open2)
usr = Menubutton(window, relief=RAISED, image = img_png2)
usr.place(x = 931,y = 40, width = 58, height = 58)


filemenu = Menu(mb, tearoff=False)
filemenu.add_command(label = 'City Management', font = ("Arial, 28"))
filemenu.add_separator()
filemenu.add_command(label = 'Location Management', font = ("Arial, 28"))
filemenu.add_separator()
filemenu.add_command(label = 'Bike Management', font = ("Arial, 28"))
filemenu.add_separator()
filemenu.add_command(label = 'Role Management', font = ("Arial, 28"))
filemenu.add_separator()
filemenu.add_command(label = 'Sales Report', font = ("Arial, 28"))

usermenu = Menu(usr, tearoff=False)

usermenu.add_command(label = 'Reset Password', font = ("Arial, 28"))


usermenu.add_separator()
usermenu.add_command(label = 'Log Out', font = ("Arial, 28"))

mb.config(menu=filemenu)
usr.config(menu=usermenu)

a = Button(window, text = 'City\nManagement',font = ("Arial, 25"))
a.place(x = 138.55, y = 222, width = 218.45, height = 127.99)

b = Button(window, text = 'Location\nManagement', font = ("Arial, 25"))
b.place(x = 401.55, y = 222, width = 218.45, height = 127.99)

c = Button(window, text = 'Bike\nManagement', font = ("Arial, 25"))
c.place(x = 667.55, y = 222, width = 218.45, height = 127.99)

d = Button(window, text = 'Account\nManagement', font = ("Arial, 25"))
d.place(x = 138.55, y = 399, width = 218.45, height = 127.99)

d = Button(window, text = 'Account\nManagement', font = ("Arial, 25"))
d.place(x = 402.55, y = 399, width = 218.45, height = 127.99)

mainloop()
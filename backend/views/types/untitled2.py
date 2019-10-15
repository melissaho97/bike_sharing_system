# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 10:06:40 2019

@author: Melissa
"""

from tkinter import *
from tkinter import ttk

root = Tk()
#root.title("cMT-Bike")
#root.geometry("1024x768")

tree = ttk.Treeview(root)

tree["columns"]=("one","two")

tree.column("one", width=100)
tree.column("two", width=100)


tree.heading("one", text="Date modified")
tree.heading("two", text="Type")

# Level 1
folder1=tree.insert("", 1, "dir2", text="Folder 1")
#tree.insert(folder1, "end", "dir 2", text="sub dir 2", values=("2A", "2B"))

tree.insert("", 3, "dir3", text="Dir 3")
#tree.insert("dir3", 3, text="sub dir 3", values=("3A", "3B"))

tree.pack()
root.mainloop()
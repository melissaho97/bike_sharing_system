# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 22:46:30 2019

@author: Melissa
"""

from tkinter import *
from tkinter import ttk

width = 1024;
height = 768;
project_name = "cMT-Bike";

def add1(self):
    a=1

def edit(self):
    b=1
    
def main():
    window=Tk()
    window.title("cMT-Bike")
    #window.geometry("%dx%d" %(width, height))
    window.geometry("1024x768")
    
    # Title
    title=Label(window, text="Type Management")
    title.place(x= 20, y= 150)
    title["fg"] = "#01367E"
    title["font"] = "Arial 18 bold"
    
    # Buttons
    add_button = Button(text = "Add", command = add1)
    add_button.place(x = 824, y = 190, width = 80, height = 30)
    
    edit_button = Button(text = "Edit", command = edit)
    edit_button.place(x = (1024-(20+80)), y = (150+40), width = 80, height = 30)
    
    #Table
    # https://riptutorial.com/tkinter/example/31880/treeview--basic-example
    tree = ttk.Treeview(windows, columns=('Dose', 'Modification date'))
    tree["columns"]=("one","two","three")
    tree.heading('#0', text='Item')
    tree.heading('#1', text='Dose')
    tree.heading('#2', text='Modification Date')
    tree.column('#1', stretch=Tkinter.YES)
    tree.column('#2', stretch=Tkinter.YES)
    tree.column('#0', stretch=Tkinter.YES)
    tree.grid(row=4, columnspan=4, sticky='nsew')
    treeview = tree

            
    window.mainloop()

main()
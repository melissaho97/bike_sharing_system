# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:35:45 2019

@author: FlyingPIG
"""

import tkinter as tk  # 使用Tkinter前需要先导入

#  一、窗口 
window = tk.Tk()#1、实例化object，建立可视化窗口window
window.title("Bike-Type")#2、给窗口标题
window.geometry("1024x768")#3、设定窗口大小（长x宽）

#frame = tk.Frame(window)
#frame.pack()
#
##创建第二层框架frame，长在主框架frame上面
#frame_l = tk.Frame(frame)# 第二层frame，左frame，长在主frame上
#frame_r = tk.Frame(frame)# 第二层frame，右frame，长在主frame上
#frame_l.pack(side='left')
#frame_r.pack(side='right')
#
##创建三组标签，为第二层frame上面的内容，分为左区域和右区域，用不同颜色标识
#tk.Label(frame_l, text='on the frame_l1', bg='green',width=512, height=2,).pack()
#tk.Label(frame_l, text='on the frame_l2', bg='green',width=30, height=2,).pack()
#tk.Label(frame_l, text='on the frame_l3', bg='green',width=30, height=2,).pack()
#tk.Label(frame_r, text='on the frame_r1', bg='yellow',width=30, height=2,).pack()
#tk.Label(frame_r, text='on the frame_r2', bg='yellow',width=30, height=2,).pack()
#tk.Label(frame_r, text='on the frame_r3', bg='yellow',width=30, height=2,).pack()

Label_CMT_Bike = tk.Label(window, 
                              text='cMT-Bike',
                              fg='black',
#                              bg='white', 
                              font=('Arial', 28), 
                              width=30, height=2,
                              anchor='w',
                              compound='right'   
                              ).place(x=140,y=31)
Label_Staff_ONLY = tk.Label(window, 
                              text='(Staff_ONLY)',
                              fg='black',
#                              bg='white', 
                              font=('Arial', 14), 
                              width=30, height=2,
                              anchor='w',
                              compound='right'   
                              ).place(x=305,y=54)

Label_Add_New_Bike = tk.Label(window, 
                              text='Add New Bike',
                              fg='dark blue',
#                              bg='white', 
                              font=('Arial', 14), 
                              width=30, height=2,
                              anchor='w',
                              compound='right'   
                              ).place(x=100,y=192)

Label_Type = tk.Label(window, 
                              text='Type:',
                              fg='black',
#                              bg='white', 
                              font=('Arial', 14), 
                              width=30, height=2,
                              anchor='w',
                              compound='right'   
                              ).place(x=100,y=320)

Label_Location_ID = tk.Label(window, 
                              text='Location ID:',
                              fg='black',
#                              bg='white', 
                              font=('Arial', 14), 
                              width=30, height=2,
                              anchor='w',
                              compound='right'   
                              ).place(x=100,y=405)

#下拉菜单
var = tk.StringVar()
var.set("Select a Type") # initial value
Type = tk.OptionMenu(window, var, "Type1").place(x=378,y=329)
#在图形界面上设定输入框控件entry并放置控件
Enter_Location_ID = tk.Entry(window, show=None, font=('Arial', 14)).place(x=378,y=414)  # 显示成明文形式

#按钮测试标签
var = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
l = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2).place(x=380,y=800)
# 定义一个函数功能供点击Button按键时调用，调用命令参数command=函数名
on_hit = False
def Confirm():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('Confirm Success')
    else:
        on_hit = False
        var.set('')
# Button按键
Confirm = tk.Button(window, text='Confirm', font=('Arial', 12), width=25, height=2, command=Confirm).place(x=373,y=540)



window.mainloop()
# -*- coding: utf-8 -*-
"""
Created by Vincenzo Sammartano
email:  v.sammartano@gmail.com
"""
import tkinter as tk
from tkinter import  messagebox
from tkinter import font

#Tkinter Window
root = tk.Tk()
root.geometry("350x440+100+50")
root.title("Time step setting")
root.resizable(width=False, height=False)
root.iconbitmap('./fan.ico')

#Fonts
f_H12B = font.Font(family='Helvetica', size=12, weight='bold')
f_H12 = font.Font(family='Helvetica', size=12, weight='normal')
f_H11 = font.Font(family='Helvetica', size=11, weight='bold')
f_H10 = font.Font(family='Helvetica', size=10, weight='bold')
f_H08 = font.Font(family='Helvetica', size=8, weight='normal')
font.families()

####Frames texts
text0 = "Fan inputs"
text1 = "Time domain"

#main Frames
top_frame = tk.Frame(root,width=250)
top_frame.grid(row=0,column=0,rowspan=2, sticky="w")
bottom_frame = tk.Frame(root, width=250)
bottom_frame.grid(row=3,column=0,sticky="w")


#subframes
#for input/outputs
frame00 = tk.LabelFrame(top_frame,text=text0,width=280,height=150,font=f_H12B) 
frame00.grid(row=0, column=0,padx=15,pady=10,ipadx=20,ipady=5)
frame00.config(borderwidth=4)

frame01 = tk.LabelFrame(top_frame,text=text1,width=150,height=20,font=f_H12B) 
frame01.grid(row=1, column=0,padx=13,pady=10,ipadx=20,ipady=5)
frame01.config(borderwidth=4)


##########################################

##Functions

def EX():
    root.destroy()
def CalT():
    try:
        omega = float(FS_.get())
        omega_s = omega/60 #round per sec
        nb = int(NB_.get()) #number of blades
        nbi = 360/nb #angle between 2 blades
        omega_deg = omega_s * 360 #deg per sec
        res = float(RE_.get()) #spatial resolution
        
        time_st = nbi/omega_deg/res
        total_rev = 5
        total_flow = total_rev * (1/omega_s)
        total_its = (total_rev * (total_flow / time_st))
        RES = [time_st, total_flow,total_its]
        printOut(RES)

    except ZeroDivisionError:
        messagebox.showwarning("Warning","Impeller speed must be greater than 0!")

def printOut(res):
    labels = ["{:6.5f}".format(res[0]) ,"{:6.5f}".format(res[1]), "{:5.0f}".format(res[2])]              
    for i,r in enumerate(labels):
        tk.Label(frame01,text=r, bg="white",width=11,font=f_H12B,anchor='center',borderwidth=2, relief="groove").grid(row=i,column=1,padx=1)
      
###end of Functions
###########################################

###########Main    
#INPUT
fs_lab = tk.Label(frame00,text="Fan speed [rpm] = ",font=f_H12).grid(row=0,column=0,padx=15,sticky="E")
FS_ = tk.StringVar()
FS = tk.Entry(frame00,textvariable=FS_ , width=6,justify="center",font=f_H12)
FS.grid(row=0,column=1,pady=5)
FS.insert('end',0)
FS.configure(state='normal')


nb_lab = tk.Label(frame00,text="Number of blades [>2] = ",font=f_H12).grid(row=1,column=0,padx=15,sticky="E")
NB_ = tk.StringVar()
NB = tk.Entry(frame00,textvariable = NB_ , width=6,justify="center",font=f_H12)
NB.grid(row=1,column=1,pady=5)
NB.insert('end',2)
NB.configure(state='normal')


res_lab = tk.Label(frame00,text="Resolution [5-10] = ",font=f_H12).grid(row=2,column=0,padx=15,sticky="E")
RE_ = tk.StringVar()
RE = tk.Entry(frame00,textvariable = RE_ , width=6,justify="center",font=f_H12)
RE.grid(row=2,column=1,pady=5)
RE.insert('end',5)
RE.configure(state='normal')


#Outputs
VarList = ['Time step[sec]','Total flow [sec]','Total iterations [-]']
for i,var in enumerate(VarList):
    tk.Label(frame01,text=var,font=f_H12).grid(row=i,column=0,sticky="E",pady=11,padx=5)
    tk.Frame(frame01,height=32,width=125, colormap="new",relief="sunken",bd=2).grid(row=i,column=1,sticky="E",padx=12,pady=11)



###############Buttons

cc = tk.Button(bottom_frame,text="RUN",command=CalT,font=f_H12)
cc.config( height=1, width=5)
# cc.grid(row=0,column=0,padx=50,pady=15,ipadx=20)  
cc.pack(side='left',fill='x',ipadx=22,padx=48,pady=15)
ex = tk.Button(bottom_frame,text="EXIT",command=EX,font=f_H12)
ex.config(height=1, width=5)
# ex.grid(row=0,column=1,padx=10,pady=15,ipadx=20)
ex.pack(side='right',fill='x',ipadx=22)  
######################

    
root.mainloop()



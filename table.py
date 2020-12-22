import tkinter
from tkinter import *
from tkinter.constants import *
from tkinter import messagebox

tk = tkinter.Tk()
tk.title("OFFICE MANAGEMENT")
tk.geometry('%dx%d+0+0'%(tk.winfo_screenwidth(),tk.winfo_screenheight()))
tk.resizable(height=None, width=None)

frame_Allot = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame_Allot.grid(row=0,column=0,sticky="news",ipady=1000,ipadx=1000)

def completelist():
    
    def data():
         Label(frame,text="   Group Name     ",font="Time 14").grid(row=0,column=0)
         Label(frame,text="   Party Name     ",font="Time 14").grid(row=0,column=5)
         Label(frame,text="   PEN No.        ",font="Time 14").grid(row=0,column=10)
         Label(frame,text="   Department     ",font="Time 14").grid(row=0,column=15)
         Label(frame,text="   Type           ",font="Time 14").grid(row=0,column=20)
         Label(frame,text="   Description    ",font="Time 14").grid(row=0,column=25)
         Label(frame,text="      AY          ",font="Time 14").grid(row=0,column=30)
         Label(frame,text="  Recieving Date  ",font="Time 14").grid(row=0,column=35)
         Label(frame,text="  Work Status     ",font="Time 14").grid(row=0,column=40)
         Label(frame,text="  Alloted To      ",font="Time 14").grid(row=0,column=45)
     
    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"),width=1200,height=540)
    
    myframe=tkinter.Frame(frame_Allot,relief=GROOVE,width=1000,height=1000,bd=1)
    myframe.place(x=10,y=130)
    canvas=tkinter.Canvas(myframe)
    frame=tkinter.Frame(canvas)
    myscrollbar=tkinter.Scrollbar(myframe,orient="vertical",command=canvas.yview)
    myscrollbar1=tkinter.Scrollbar(myframe,orient="horizontal",command=canvas.xview)
    canvas.configure(yscrollcommand=myscrollbar.set)
    canvas.configure(xscrollcommand=myscrollbar1.set)
    myscrollbar1.pack(side="bottom",fill="x")
    myscrollbar.pack(side="right",fill="y")
    
    canvas.pack(side="left")
    canvas.create_window((0,0),window=frame,anchor='nw')
    frame.bind("<Configure>",myfunction)
    data()
    return

completelist()


tk.mainloop()

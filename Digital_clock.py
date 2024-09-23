from tkinter import *
import time

def my_time():
    current_time = time.strftime("%I:%M:%S")
    time1.config(text=current_time)
    time1.after(1000,my_time)

def date():
    dat= time.strftime("%D")
    Date.config(text=dat)
    Date.after(24*60*1000,date)
m=Tk()

Title=Label(m,text="Digital Clock",font=("Arial",45,"bold"),fg="white",background="black")
Title.grid(row=0,column=3)


time1=Label(m,text="time",font=("Verdana",100,"bold"),fg="black",background="lavender")
time1.grid(row=2,column=3,padx=450,pady=100)

Date=Label(m,text="Date",font=("Verdana",100,"bold"),fg="black",background="lavender")
Date.grid(row=3,column=3,padx=250,pady=100)
my_time()
date()

m.mainloop()

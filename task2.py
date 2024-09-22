from tkinter import *
m = Tk()
def click():
    label1=Label(m,text="Rowdy",font = ("San Serif",50,"bold","underline"),fg="purple",bg="white",padx=45,pady=25,width=-5)
    label1.pack(pady=10,side=LEFT)

    label2=Label(m,text="Rowdy",font = ("San Serif",50,"bold","underline"),fg="red",bg="white",padx=45,pady=25,width=-5)
    label2.pack(side = RIGHT)
    


input1=Entry(m,font=("Verdana",24,"bold"),fg="navy blue",bg="purple")
input1.pack(pady = 45)

button1=Button(m,text="submit",font =("Arial Black",50,"italic"),fg="brown",bg="red",command=click)
button1.pack(padx = 45,pady =50,side= BOTTOM)

m.mainloop()






















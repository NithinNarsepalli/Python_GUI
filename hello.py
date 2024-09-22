from tkinter import *
m=Tk()


def clicked():
        name=userid.get()
        greeting="Pavan"+name
        if name != " ":
            mylabel.config(text=greeting)
            userid.delete(0,END)
        if name =="":
              mylabel.config(text="please enter name")
              userid.delete(0,END)

mylabel = Label(m, text = "Rowdy",font = ("San Serif",100,"italic","underline","bold"),bg='white',fg ="black",padx=10,pady=10,highlightbackground="black")
mylabel.pack(side=TOP)       


userid = Entry(m,insertbackground="red",font=("arial",10,"normal","bold"),bg="orange",fg="white",highlightbackground="black")
userid.pack(padx=50, pady=150)

my_buttton = Button(m,highlightbackground="red",text="Submit",font= ("arial",20,"italic","underline"), fg="black",padx=50, pady=50,command=clicked)
my_buttton.pack(padx=50, pady=50,side=BOTTOM)
m.mainloop()


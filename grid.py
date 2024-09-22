from tkinter import *
m = Tk()

def click():
    userid1 = userid.get()
    mailid1 = MaildId.get()
    Address1 = Address_id.get()
    Mobile_number1 = Mobile_number.get()
    ml=len(Mobile_number1) 
    if userid1 == "" or mailid1 =="" or Address1 =="" or ml != 10 or  "@gmail.com" not in mailid1:
            Status.config(text="Fill All the details",font=("Arial Bold",20,"bold","underline"),fg="Red",bg="white")
            if "@gmail.com" not in mailid1:
                 print("Incorrect Mail id:",mailid1)
            elif ml !=10:
                 print("Incorrect Mobile Number:",Mobile_number1)
            else:
                 print("Some other Error")
    else:
        Status.config(text="Successfully Submited all the details",font=("Arial Bold",20,"bold","underline"),fg="Green",bg="white")
        userid.delete(0,END)
        MaildId.delete(0,END)
        Address_id.delete(0,END)
        Mobile_number.delete(0,END)
        print(len(Mobile_number1))
        print(mailid1)


rpage=Label(m,text="Registration Page",font=("Sanserif",45,"bold","underline"),foreground="white")
rpage.grid(row = 0,column = 2)

name=Label(m,text="Name:",font=("Arial",15,"bold"),foreground="white",padx=100,pady=100)
name.grid(row = 1,column = 0)

userid = Entry(m,insertbackground="red",font=("arial",20,"normal","bold"),bg="orange",fg="white",highlightbackground="black")
userid.grid(row = 1,column = 1)

Mail = Label(m,text = "Mail Id:",font=("Arial",15,"bold"),foreground="white",padx=10,pady=100)
Mail.grid(row = 1,column = 2)

MaildId = Entry(m,font=("Arial",20,"bold"),foreground="white",background="orange",highlightbackground="black")
MaildId.grid(row = 1,column = 3)

Mobile = Label(m,text = "Mobile Number:",font=("Arial",15,"bold"),foreground="white",padx=10,pady=100)
Mobile.grid(row = 2,column = 0)

Mobile_number = Entry(m,font=("Arial",20,"bold"),foreground="white",background="orange",highlightbackground="black")
Mobile_number.grid(row = 2,column = 1)


address=Label(m,text="Address:",font=("Arial",15,"bold"),foreground="white")
address.grid(row = 2,column = 2)

Address_id = Entry(m,insertbackground="red",font=("arial",20,"normal","bold"),bg="orange",fg="white",highlightbackground="black")
Address_id.grid(row = 2,column = 3)

submit = Button(m,text="Submit",font=("arial",20,"normal","bold"),bg="blue",foreground="white",command=click)
submit.grid(row = 3, column = 2)

Status = Label(m,text="Pending",font=("Arial Bold",20,"bold","underline"),fg="RED",bg="grey")
Status.grid(row = 4 ,column = 2)

m.mainloop()
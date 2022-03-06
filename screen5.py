from tkinter import *

root = Tk()

root.geometry('400x150')
root.configure(bg='#9bbb58')


Label1=Label(root,text="Enter admin id")
Label2=Label(root,text="Enter password")

Label1.grid(row=0,padx=10,pady=10)
Label2.grid(row=1,padx=10,pady=10)

inp1=Entry(root,width=25)
inp2=Entry(root,width=25)

inp1.grid(row=0,column=1)
inp2.grid(row=1,column=1)

Enter=Button(root,text="LOGIN",bg="white")
Enter.grid(row=2,column=1,pady=10,ipadx=20,ipady=10)

root.mainloop()

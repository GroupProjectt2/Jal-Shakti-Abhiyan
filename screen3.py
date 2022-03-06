from tkinter import *

root = Tk()

root.geometry('400x150')
root.configure(bg='#f9bf8f')


Label1=Label(root,text="Enter area pincode")

Label1.grid(row=0,padx=10,pady=10)

inp1=Entry(root,width=25)

inp1.grid(row=0,column=1)

Enter=Button(root,text="ENTER",bg="white")
Enter.grid(row=1,column=1,pady=10,ipadx=20,ipady=10)

root.mainloop()

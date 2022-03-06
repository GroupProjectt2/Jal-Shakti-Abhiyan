from tkinter import *

root = Tk()

root.geometry('400x400')
root.configure(bg='white')

def Test():
    myLabel = Label(root, text="Testing buttons!")
    myLabel.pack()

myButton1=Button(root,text="Geographic",command=Test,bg="#f9bf8f",width=10,height=3)
myButton2=Button(root,text="Financial",command=Test,bg="#f9bf8f",width=10,height=3)
myButton3=Button(root,text="Admin",command=Test,bg="#f9bf8f",width=10,height=3)
myButton4=Button(root,text="Action",command=Test,bg="#f9bf8f",width=10,height=3)


myButton1.place(relx=0.35,rely=0.35,x=10,y=10,anchor=CENTER)
myButton2.place(relx=0.35,rely=0.35,x=100,y=10,anchor=CENTER)
myButton3.place(relx=0.35,rely=0.35,x=10,y=80,anchor=CENTER)
myButton4.place(relx=0.35,rely=0.35,x=100,y=80,anchor=CENTER)


#myButton1.

root.mainloop()

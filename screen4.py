from tkinter import *
import screen2
def Screen4():
    root = Tk()
    root.title('Financial')
    root.geometry('400x150')
    root.configure(bg='#f9bf8f')


    Label1=Label(root,text="Enter area pincode")
    Label2=Label(root,text="Enter officer id")

    Label1.grid(row=0,padx=10,pady=10)
    Label2.grid(row=1,padx=10,pady=10)

    inp1=Entry(root,width=25)
    inp2=Entry(root,width=25)

    inp1.grid(row=0,column=1)
    inp2.grid(row=1,column=1)

    Enter=Button(root,text="ENTER",bg="white")
    Enter.grid(row=2,column=1,pady=10,ipadx=20,ipady=10)

    Back=Button(root,text="<- Main Menu",bg="yellow",command=lambda: [root.destroy(),screen2.Screen2()])
    Back.grid(row=2,column=3,ipadx=15,ipady=0.5)
    
    root.mainloop()
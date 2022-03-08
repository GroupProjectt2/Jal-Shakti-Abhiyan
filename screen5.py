from tkinter import *
import screen2
def Screen5():
    root = Tk()
    root.title('ADMIN')
    root.geometry('500x200')
    root.configure(bg='#9bbb58')


    Label1=Label(root,text="Enter admin id")
    Label2=Label(root,text="Enter password")

    Label1.grid(row=0,padx=10,pady=10)
    Label2.grid(row=1,padx=10,pady=10)

    inp1=Entry(root,width=25)
    inp2=Entry(root,width=25)

    inp1.grid(row=0,column=1)
    inp2.grid(row=1,column=1)


    def Onclick():
        ID=inp1.get()
        if ID=='admin':
            PWD=inp2.get()
            if PWD=='password':
                print("Login Successful with administrator privileges!")
                root.destroy()
                screen2.Screen2()
        else:
            print("Login failed with administrator privileges!")

    Enter=Button(root,text="LOGIN AS ADMIN",bg="white",command=Onclick)
    Enter.grid(row=2,column=1,pady=10,ipadx=20,ipady=10)

    Back=Button(root,text="<- Main Menu",bg="yellow",command=lambda: [root.destroy(),screen2.Screen2()])
    Back.grid(row=2,column=3,padx=70,ipadx=15,ipady=0.5)

    root.mainloop()

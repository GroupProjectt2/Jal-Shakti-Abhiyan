from tkinter import *
import screen2
def Screen1():
    root = Tk()

    root.geometry('300x150')
    root.configure(bg='white')


    Label1=Label(root,text="Enter officer id")
    Label2=Label(root,text="Enter password")

    Label1.grid(row=0,padx=10,pady=10)
    Label2.grid(row=1)

    inp1=Entry(root,width=25)
    inp2=Entry(root,width=25)

    inp1.grid(row=0,column=1)
    inp2.grid(row=1,column=1)

    def Onclick():
        ID=inp1.get()
        if ID=='123':
            PWD=inp2.get()
            if PWD=='pwd':
                print("Login Successful!")
                root.destroy()
                screen2.Screen2()
        else:
            print("Login failed!")
        
    Login=Button(root,text="LOGIN",bg="orange",command=Onclick)
    Login.grid(row=3,column=1,pady=10,ipadx=20,ipady=10)
    
    root.mainloop()

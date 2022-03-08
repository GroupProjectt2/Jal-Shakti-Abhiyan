from tkinter import *
import screen2
import action
def Screen6():
    root = Tk()
    root.title('ACTION')
    root.geometry('500x150')
    root.configure(bg='#f9bf8f')

    Label1=Label(root,text="Enter area pincode")
    Label1.grid(row=0,padx=10,pady=10)

    inp1=Entry(root,width=25)
    inp1.grid(row=0,column=1)

    def Onclick1():
        pin=inp1.get()
        if len(pin)!=0:
            print(action.action_advice(pin))
        else:
            print("Input a valid pincode to fetch details!")

    Enter=Button(root,text="Advice on current Area",bg="white",command=Onclick1)
    Enter.grid(row=1,column=1,pady=10,ipadx=20,ipady=10)

    Back=Button(root,text="<- Main Menu",bg="yellow",command=lambda: [root.destroy(),screen2.Screen2()])
    Back.grid(row=2,column=3,padx=40,ipadx=15,ipady=0.5)

    root.mainloop()

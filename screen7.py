from tkinter import *
import screen2
import admin
def Screen7():
    root = Tk()
    root.title('ADMIN')
    root.geometry('500x200')
    root.configure(bg='#9bbb58')


    Label1=Label(root,text="Enter officer id")
    Label2=Label(root,text="Enter new value")

    Label1.grid(row=0,padx=10,pady=10)
    Label2.grid(row=1,padx=10,pady=10)

    inp1=Entry(root,width=25)
    inp2=Entry(root,width=25)

    inp1.grid(row=0,column=1)
    inp2.grid(row=1,column=1)


    def Onclick1():
        oid = inp1.get()
        name = inp2.get()
        print(admin.Change_officer_name(name,oid))

    def Onclick2():
        oid = inp1.get()
        grant = inp2.get()
        print(admin.Update_grant(oid,grant))

    def Onclick3():
        oid = inp1.get()
        sal = inp2.get()
        print(admin.Update_salary(oid,sal))

    Enter=Button(root,text="Change officer name",bg="white",command=Onclick1)
    Enter.grid(row=2,column=1,pady=10,ipadx=20,ipady=10)

    Enter=Button(root,text="Update Grant",bg="white",command=Onclick2)
    Enter.grid(row=3,column=1,pady=10,ipadx=20,ipady=10)

    Enter=Button(root,text="Update Salary",bg="white",command=Onclick3)
    Enter.grid(row=2,column=2,pady=10,ipadx=20,ipady=10)

    Back=Button(root,text="<- Main Menu",bg="yellow",command=lambda: [root.destroy(),screen2.Screen2()])
    Back.grid(row=4,column=3,padx=70,ipadx=15,ipady=0.5)

    root.mainloop()

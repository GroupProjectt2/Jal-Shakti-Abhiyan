from tkinter import *
import financial_table as fin
import screen2
def Screen4():
    root = Tk()
    root.title('FINANCIAL')
    root.geometry('600x300')
    root.configure(bg='#f9bf8f')

    Label1=Label(root,text="Enter officer id")
    Label1.grid(row=0,padx=10,pady=10)

    inp1=Entry(root,width=25)
    inp1.grid(row=0,column=1)

    def Onclick1():
        oid = inp1.get()
        if len(oid)!=0:
            print(fin.Display_officerID(oid))
        else:
            print("Input a valid pincode to fetch details!")

    def Onclick2():
        oid = inp1.get()
        if len(oid)!=0:
            print(fin.Display_grant(oid))
        else:
            print("Input a valid pincode to fetch details!")

    def Onclick3():
        oid = inp1.get()
        if len(oid)!=0:
            print(fin.Display_salary(oid))
        else:
            print("Input a valid pincode to fetch details!")

    def Onclick4():
        oid = inp1.get()
        if len(oid)!=0:
            print(fin.Display_cost(oid))
        else:
            print("Input a valid pincode to fetch details!")

    def Onclick5():
        oid = inp1.get()
        if len(oid)!=0:
            print(fin.Active_months(oid))
        else:
            print("Input a valid pincode to fetch details!")

    Enter=Button(root,text="Search by Officer ID",bg="white",command = Onclick1)
    Enter.grid(row=1,column=1,pady=10,ipadx=20,ipady=10)

    Enter=Button(root,text="Display Grant",bg="white",command = Onclick2)
    Enter.grid(row=2,column=1,pady=10,ipadx=20,ipady=10)

    Enter=Button(root,text="Display Salary",bg="white",command = Onclick3)
    Enter.grid(row=2,column=2,pady=10,ipadx=20,ipady=10)

    Enter=Button(root,text="Display Cost",bg="white",command = Onclick4)
    Enter.grid(row=3,column=1,pady=10,ipadx=20,ipady=10)

    Enter=Button(root,text="Active Months",bg="white",command = Onclick5)
    Enter.grid(row=3,column=2,pady=10,ipadx=20,ipady=10)

    Back=Button(root,text="<- Main Menu",bg="yellow",command=lambda: [root.destroy(),screen2.Screen2()])
    Back.grid(row=4,column=3,ipadx=15,ipady=0.5)
    
    root.mainloop()

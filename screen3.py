from tkinter import *
import screen2
import geographic_table as geo
def Screen3():
    root = Tk()
    root.title('GEOGRAPHIC')
    root.geometry('650x300')
    root.configure(bg='#f9bf8f')

    Label1=Label(root,text="Enter area pincode")
    Label1.grid(row=0,padx=10,pady=10)

    inp1=Entry(root,width=25)
    inp1.grid(row=0,column=1)

    def Onclick1():
        pin=inp1.get()
        if len(pin)!=0:
            print(geo.SearchByPincode(pin))
        else:
            print("Input a valid pincode to fetch details!")

    def Onclick2():
        pin=inp1.get()
        if len(pin)!=0:
            print(geo.Display_Rainfall(pin))
        else:
            print("Input a valid pincode to fetch details!")

    def Onclick3():
        pin=inp1.get()
        if len(pin)!=0:
            print(geo.Display_Ground_Water(pin))
        else:
            print("Input a valid pincode to fetch details!")

    def Onclick4():
        pin=inp1.get()
        if len(pin)!=0:
            print(geo.Display_Total_Water(pin))
        else:
            print("Input a valid pincode to fetch details!")

    def Onclick5():
        pin=inp1.get()
        if len(pin)!=0:
            print(geo.Display_Required_Water(pin))
        else:
            print("Input a valid pincode to fetch details!")
        
    Enter=Button(root,text="Search by Pincode",bg="white",command=Onclick1)
    Enter.grid(row=1,column=1,pady=10,ipadx=30,ipady=10)

    Enter=Button(root,text="Display Rainfall",bg="white",command=Onclick2)
    Enter.grid(row=2,column=1,pady=10,ipadx=30,ipady=10)

    Enter=Button(root,text="Display Groundwater",bg="white",command=Onclick3)
    Enter.grid(row=2,column=2,pady=10,ipadx=26,ipady=10)

    Enter=Button(root,text="Display Total Water",bg="white",command=Onclick4)
    Enter.grid(row=3,column=1,pady=10,ipadx=20,ipady=10)

    Enter=Button(root,text="Display Required Water",bg="white",command=Onclick5)
    Enter.grid(row=3,column=2,padx=20,pady=10,ipadx=20,ipady=10)

    Back=Button(root,text="<- Main Menu",bg="yellow",command=lambda: [root.destroy(),screen2.Screen2()])
    Back.grid(row=4,column=3,ipadx=15,ipady=0.5)

    root.mainloop()

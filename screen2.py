from tkinter import *
import tkinter.font as font
import screen3
import screen4
import screen5
#import screen6
def Screen2():

    root = Tk()
    root.title('MENU')
    root.geometry('500x500')
    root.configure(bg='white')

    myFont = font.Font(size=14)

    myButton1=Button(root,text="Geographic",font=myFont,command=lambda: [root.destroy(),screen3.Screen3()],bg="#f9bf8f",width=10,height=3)
    myButton2=Button(root,text="Financial",font=myFont,command=lambda: [root.destroy(),screen4.Screen4()],bg="#f9bf8f",width=10,height=3)
    myButton3=Button(root,text="Admin",font=myFont,command=lambda: [root.destroy(),screen5.Screen5()],bg="#f9bf8f",width=10,height=3)
    myButton4=Button(root,text="Action",font=myFont,command=lambda: [root.destroy(),screen6.Screen6()],bg="#f9bf8f",width=10,height=3)


    myButton1.place(relx=0.35,rely=0.35,x=10,y=10,anchor=CENTER)
    myButton2.place(relx=0.35,rely=0.35,x=150,y=10,anchor=CENTER)
    myButton3.place(relx=0.35,rely=0.35,x=10,y=120,anchor=CENTER)
    myButton4.place(relx=0.35,rely=0.35,x=150,y=120,anchor=CENTER)

    Back=Button(root,text="Exit",bg="red",fg="white",command=root.destroy)
    Back.place(relx=0.35,rely=0.35,x=230,y=250)

    root.mainloop()

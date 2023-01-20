from tkinter import  *

cal = Tk()
cal.title("Calculator")
label1 = Label(cal ,text="Calculator For You Bro" ,width=35, bg="#D5E9DC" , fg="#000000")
label1.grid(column=0,row=0,columnspan=4)

data1 = Entry(cal,width=35,borderwidth=10,state=DISABLED)
data1.grid(column=0,row=1,columnspan=4)

but1 = Button(cal,text="9",width=7,borderwidth=5)
but1.grid(column=0,row=2)

but2 = Button(cal,text="8",width=7,borderwidth=5)
but2.grid(column=1,row=2)

but3 = Button(cal,text="7",width=7,borderwidth=5)
but3.grid(column=2,row=2)

but4 = Button(cal,text="6",width=7,borderwidth=5)
but4.grid(column=0,row=3)

but5 = Button(cal,text="5",width=7,borderwidth=5)
but5.grid(column=1,row=3)

but6 = Button(cal,text="4",width=7,borderwidth=5)
but6.grid(column=2,row=3)

but7 = Button(cal,text="3",width=7,borderwidth=5)
but7.grid(column=0,row=4)

but8 = Button(cal,text="2",width=7,borderwidth=5)
but8.grid(column=1,row=4)

but9 = Button(cal,text="1",width=7,borderwidth=5)
but9.grid(column=2,row=4)

but0 = Button(cal,text="0",width=16,borderwidth=5)
but0.grid(column=0,row=5,columnspan=2)
#
but10 = Button(cal,text="=",width=7,borderwidth=5)
but10.grid(column=2,row=5)

OPR1 = Button(cal,text="+",width=7,borderwidth=5)
OPR1.grid(column=3,row=2)

OPR2 = Button(cal,text="-",width=7,borderwidth=5)
OPR2.grid(column=3,row=3)

OPR3 = Button(cal,text="*",width=7,borderwidth=5)
OPR3.grid(column=3,row=4)

OPR4 = Button(cal,text="<--",width=7,borderwidth=5)
OPR4.grid(column=3,row=5)

cal.mainloop()

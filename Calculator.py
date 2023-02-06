from tkinter import  *
global operand1
global operand2
operand2 = 0
operand1 = 0
def click(number):
    current = data1.get()
    data1.delete(0,END)
    data1.insert(0,str(current)+str(number))

def Equals():

    global operand2
    global operand1
    operand2 = data1.get()
    if operand2 != 0:


        data1.delete(0, END)
        if math == 'Multiplication':
            sum = int(operand2) * int(operand1)
            data1.insert(0,str(sum))
        elif math == 'Addition':
            sum = int(operand1) + int(operand2)
            data1.insert(0, str(sum))
        elif math == 'Subtraction':
            sum = int(operand1) - int(operand2)
            data1.insert(0, str(sum))
        else :
            sum = 'You entered Incorrect'
            data1.insert(0, str(sum))
    else:
        data1.delete(0,END)
        data1.insert(0,"Enter Two operands")


def deleteall():// to delete pre
    global operand1
    global operand2
    operand2 = 0
    operand1 = 0
    data1.delete(0,END)
def plus():

    global operand1
    global math
    math = "Addition"
    operand1 = data1.get()
    data1.delete(0, END)


def minus():

    global operand1
    global math
    math = "Subtraction"
    operand1 = data1.get()
    data1.delete(0, END)


def mul():

    global operand1
    global  math
    math = "Multiplication"
    operand1 = data1.get()
    data1.delete(0, END)


cal = Tk()
cal.title("Calculator")
label1 = Label(cal ,text="Calculator For You Bro" ,width=35, bg="#D5E9DC" , fg="#000000")
label1.grid(column=0,row=0,columnspan=4)

data1 = Entry(cal,width=35,borderwidth=10)
data1.grid(column=0,row=1,columnspan=4)

but1 = Button(cal,text="9",width=7,borderwidth=5,command=lambda: click(9))
but1.grid(column=0,row=2)

but2 = Button(cal,text="8",width=7,borderwidth=5,command= lambda: click(8))
but2.grid(column=1,row=2)

but3 = Button(cal,text="7",width=7,borderwidth=5,command=lambda: click(7))
but3.grid(column=2,row=2)

but4 = Button(cal,text="6",width=7,borderwidth=5,command=lambda:click(6))
but4.grid(column=0,row=3)

but5 = Button(cal,text="5",width=7,borderwidth=5,command=lambda:click(5))
but5.grid(column=1,row=3)

but6 = Button(cal,text="4",width=7,borderwidth=5,command=lambda:click(4))
but6.grid(column=2,row=3)

but7 = Button(cal,text="3",width=7,borderwidth=5,command=lambda:click(3))
but7.grid(column=0,row=4)

but8 = Button(cal,text="2",width=7,borderwidth=5,command=lambda:click(2))
but8.grid(column=1,row=4)

but9 = Button(cal,text="1",width=7,borderwidth=5,command=lambda:click(1))
but9.grid(column=2,row=4)

but0 = Button(cal,text="0",width=16,borderwidth=5,command=lambda:click(0))
but0.grid(column=0,row=5,columnspan=2)


but10 = Button(cal,text="=",width=7,borderwidth=5,command=lambda:Equals())
but10.grid(column=2,row=5)

OPR1 = Button(cal,text="+",width=7,borderwidth=5,command=lambda:plus())
OPR1.grid(column=3,row=2)

OPR2 = Button(cal,text="-",width=7,borderwidth=5,command=lambda:minus())
OPR2.grid(column=3,row=3)

OPR3 = Button(cal,text="*",width=7,borderwidth=5,command=lambda:mul())
OPR3.grid(column=3,row=4)

OPR4 = Button(cal,text="<--",width=7,borderwidth=5,command=lambda:deleteall())
OPR4.grid(column=3,row=5)




cal.mainloop()

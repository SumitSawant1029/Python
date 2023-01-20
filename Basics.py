from tkinter import *

root = Tk()
 # Creating Label
label1 = Label(root, text="Hello World",fg='blue',bg='pink')
# label1.grid(column=1,row=3)
label1.pack()
#creating Button
def click1():
    label2 = Label(root, text="Hello World")
    label2.grid(column=1,row=3)

    label2.destroy()

    # print("Hello")
button1 = Button(root , text="Hello Click me!!!!!!",command=click1,padx=20,pady=10)
button1.pack()


# Input Boxes
def click2():
    label2 = Label(root,text=data1.get())
    label2.pack()


data1 = Entry(root)

button2 = Button(root , text="Submit",command=click2,padx=20,pady=10)
button2.pack()
data1.pack()


root.mainloop()

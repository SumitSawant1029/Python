
# Irritating App
from tkinter import *
global i
i=0
root = Tk()
# root.pack(padx=20,pady=20)
root.title("Irritating You")
root.iconbitmap("Hello.ico")
def click1():
    global i
    i=i+1
    but1 = Button(root, text="Click Me you Fool", width=20, borderwidth=9, command=click1)
    but1.grid(column=i, row=i)
but1 = Button(root,text= "Click Me you Fool",width=20,borderwidth=9,command=click1)
but1.grid(column=0,row=0)

root.mainloop()

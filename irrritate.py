
# Irritating App
from tkinter import *

root = Tk()
# root.pack(padx=20,pady=20)
root.title("Irritating You")
root.iconbitmap("Hello.ico")

but1 = Button(root,text= "Click Me you Fool",width=20,borderwidth=9,command=click1)
but1.grid(column=0,row=0)
but2 = Button(root,text= "Click Me you Fool",width=20,borderwidth=9,command=click2)
but2.grid(column=0,row=1)
root.mainloop()

from tkinter import *
from PIL import Image,ImageTk

global count
count = 0
root = Tk()
root.title('Image Viewer')
root.iconbitmap("Hello.ico")

img1 = ImageTk.PhotoImage(Image.open('N1.jpg'))
img2 = ImageTk.PhotoImage(Image.open('N2.jpg'))
img3 = ImageTk.PhotoImage(Image.open('N3.jpg'))
img4 = ImageTk.PhotoImage(Image.open('N4.jpg'))
img5 = ImageTk.PhotoImage(Image.open('N5.jpg'))
image_list = [img1,img2,img3,img4,img5]

lab = Label(root, image=img1)
lab.grid(columnspan=3,column=0,row=0)

def next():
    global count
    global lab
    if count==4:
        count=0
    count = count + 1

    lab.grid_forget()
    lab = Label(root, image=image_list[count],bg='#000000')
    lab.grid(columnspan=3, column=0, row=0)

def prev():
    global lab
    global count
    if count == 0:
        count = 5
    count=count - 1

    lab.grid_forget()
    lab = Label(root, image=image_list[count])
    lab.grid(columnspan=3, column=0, row=0)


Button1 = Button(root ,text='<<',bd=5,command=prev,bg='#A4C4E3')
Button1.grid(column=0,row=1,sticky=W+E)
Button2 = Button(root ,text='Exit',bd=5,command=root.quit,bg='#FF4040')
Button2.grid(column=1,row=1,sticky=W+E)
Button3 = Button(root ,text='>>',bd=5,command=next,bg='#A4C4E3')
Button3.grid(column=2,row=1,sticky=W+E)

root.mainloop()
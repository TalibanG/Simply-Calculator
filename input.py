from cProfile import label
from ctypes.wintypes import HHOOK
from tkinter import * 

root = Tk()

e = Entry(root, width=50, borderwidth=10)
e.pack()
e.insert(0, "Enter Your Name:")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton  = Button(root, text="Enter Your Stock Quote" , command=myClick)
myButton.pack()



root.mainloop()

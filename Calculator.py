from distutils import command
from email.mime import image
import math
from sqlite3 import Row
from tkinter import *
from turtle import onclick
from unicodedata import numeric 
from PIL import ImageTk, Image

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0,column=0,columnspan=3, padx=10, pady=10)

#e.insert(0," ")

def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_numer = e.get()
    global f_num 
    global math
    math = "addition"
    f_num = int(first_numer)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    
    if math == "substraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))




    

def button_subtract():
    first_numer = e.get()
    global f_num 
    global math
    math = "substraction"
    f_num = int(first_numer)
    e.delete(0, END)

def button_multiply():
    first_numer = e.get()
    global f_num 
    global math
    math = "multiplication"
    f_num = int(first_numer)
    e.delete(0, END)

def button_divide():
    first_numer = e.get()
    global f_num 
    global math
    math = "division"
    f_num = int(first_numer)
    e.delete(0, END)
    

# Define Buttons

button_1 = Button(root, text="1", padx=40,pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40,pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40,pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40,pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40,pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40,pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40,pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40,pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40,pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40,pady=20, command=lambda: button_click(0))
button_add = Button(root , padx=44,pady=20, command=button_add)
button_equal = Button(root, padx=91,pady=20, command= button_equal)
button_clear = Button(root, text="Clear", padx=79,pady=20, command= button_clear)

button_subtract = Button(root, text="-", padx=41,pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=40,pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=41,pady=20, command=button_divide)

plus_img = PhotoImage(file="E:\Python\Python\TKinter\Add.png")
my_label1 = Label(image=plus_img)

minus_img = PhotoImage(file="E:\Python\Python\TKinter\minus.png")
my_label2 = Label(image=minus_img)

multiply_img = PhotoImage(file="E:\Python\Python\TKinter\multiplication-sign.png")
my_label3 = Label(image=multiply_img)

equal_img = PhotoImage(file="E:\Python\Python\TKinter\equal.png")
my_label4 = Label(image=equal_img)

slah_img = PhotoImage(file="E:\Python\Python\TKinter\slah.png")
my_label5 = Label(image=slah_img)

clear_img = PhotoImage(file="E:\Python\Python\TKinter\clear.png")
my_label6 = Label(image=clear_img)

zero_img = PhotoImage(file="E:\Python\Python\TKinter\zero.png")
my_label7 = Label(image=zero_img)

one_img = PhotoImage(file="E:\Python\Python\TKinter\one.png")
my_label8 = Label(image=one_img)

two_img = PhotoImage(file="E:\Python\Python\TKinter\Two.png")
my_label9 = Label(image=two_img)

three_img = PhotoImage(file="E:\Python\Python\TKinter\Three.png")
my_label10 = Label(image=three_img)

four_img = PhotoImage(file=r"E:\Python\Python\TKinter\Four.png")
my_label11 = Label(image=four_img)

five_img = PhotoImage(file=r"E:\Python\Python\TKinter\Five.png")
my_label12 = Label(image=five_img)

six_img = PhotoImage(file=r"E:\Python\Python\TKinter\Six.png")
my_label13 = Label(image=six_img)

seven_img = PhotoImage(file=r"E:\Python\Python\TKinter\Seven.png")
my_label14 = Label(image=seven_img)

eight_img = PhotoImage(file=r"E:\Python\Python\TKinter\Eight.png")
my_label15 = Label(image=eight_img)

nine_img = PhotoImage(file=r"E:\Python\Python\TKinter\Nine.png")
my_label16 = Label(image=nine_img)



# Put the buttons on the screen

button_1.grid(row=3 , column=0)
button_2.grid(row=3 , column=1)
button_3.grid(row=3 , column=2)

button_4.grid(row=2 , column=0)
button_5.grid(row=2 , column=1)
button_6.grid(row=2 , column=2)

button_7.grid(row=1 , column=0)
button_8.grid(row=1 , column=1)
button_9.grid(row=1 , column=2)
button_0.grid(row=4 , column=0)

button_clear.grid(row=4, column=1,columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1,columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

my_label1.grid(row=5, column= 0)
my_label2.grid(row=6, column= 0)
my_label3.grid(row=6, column= 1)

my_label4.grid(row=5, column= 1)
my_label5.grid(row=6, column= 2)
my_label6.grid(row=4, column= 1, columnspan=2)

my_label7.grid(row=4, column= 0)
my_label8.grid(row=3, column= 0)
my_label9.grid(row=3, column= 1)

my_label10.grid(row=3, column= 2)
my_label11.grid(row=2, column= 0)
my_label12.grid(row=2, column= 1)

my_label13.grid(row=2, column= 2)
my_label14.grid(row=1, column= 0)
my_label15.grid(row=1, column= 1)

my_label16.grid(row=1, column= 2)







root.mainloop()
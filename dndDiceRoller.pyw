import random
import string
import time
from tkinter import *
from tkinter import StringVar

root = Tk()
icon_photo = PhotoImage(file = "icon.png")
root.iconphoto(False, icon_photo)
root.configure(bg = "#7B6440")

roll_response = StringVar()
roll_response.set('')


def D4():
    return random.randint(1,4)

def D6():
    return random.randint(1,6)

def D8():
	return random.randint(1,8)

def D10():
    return random.randint(1,10)

def D12():
	return random.randint(1,12)

def D20():
	return random.randint(1,20)

def roll_1():
    roll_response.set(D4())

def roll_2():
    roll_response.set(D6())

def roll_3():
    roll_response.set(D8())

def roll_4():
    roll_response.set(D10())

def roll_5():
    roll_response.set(D12())

def roll_6():
    roll_response.set(D20())


root.title("D&D Dice Roller (alpha 1.0)")
root.geometry('300x200')

label1 = Label(root, text="Which Dice Would You Like To Roll?", bg = "#7B6440").pack()
b1 = Button(root, text="D4", command=roll_1, bg = "#80524A")
b1.place(x='30', y='40')
b2 = Button(root, text="D6", command=roll_2, bg = "#80524A")
b2.place(x='120', y='40')
b3 = Button(root, text="D8", command=roll_3, bg = "#80524A")
b3.place(x='215', y='40')
b4 = Button(root, text="D10", command=roll_4, bg = "#80524A")
b4.place(x='27', y='80')
b5 = Button(root, text="D12", command=roll_5, bg = "#80524A")
b5.place(x='117', y='80')
b6 = Button(root, text="D20", command=roll_6, bg = "#80524A")
b6.place(x='211', y='80')
l2 = Label(root, textvariable=roll_response, font=("Courier", 44), bg = "#7B6440")
l2.pack(side=BOTTOM)

root.mainloop()

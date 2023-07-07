import tkinter as tk
from tkinter import *

frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('600x600')

class thingy:
    def __init__(self, name, quan, price):
        self.name = name
        self.quan = quan
        self.price = price
        
list = []

text = tk.Text(frame, height=20, width=60)
text.grid()

def printInput():
    text.delete("1.0", "end")
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Provided Input: "+inp)
    name = inp[0:inp.index(",")]
    inp = inp[inp.index(",")+1:]
    quan = inp[0:inp.index(",")]
    price = inp[inp.index(",")+1:]
    truth = True
    for i in range(len(list)):
        if list[i].name == name:
            list[i].quan = int(list[i].quan) + int(quan)
            truth = False
            for i in range(len(list)):
                if list[i].price == price:
                    list[i].price = list[i].price
                    list[i].price = float(list[i].price) + float(price)
                    truth = False
                else:
                    for i in range(len(list)):
                        Warning_Label = tk.Label(frame, text = "This is not the same price as the list. Updating Price...").grid()
                        list[i].price = price
                        list[i].price = float(list[i].price) + float(price)
                        truth = False

    if truth:
        what = thingy(name, quan, price)
        list.append(what)
    for i in range(len(list)):
        text.insert(END, str(list[i].name) + ", " +str(list[i].quan) +", "+str(list[i].price) + "\n")
    
def printnot():
    text.delete("1.0", "end")
    inp = inputtxt.get(1.0, "end-1c")
    name = inp[0:inp.index(",")]
    inp = inp[inp.index(",")+1:]
    quan = inp[0:inp.index(",")]
    price = inp[inp.index(",")+1:]
    for i in range(len(list)):
        if list[i].name == name:
            list.remove(list[i])
        
    for i in range(len(list)):
        text.insert(END, str(list[i].name) + ", " +str(list[i].quan) +", "+str(list[i].price) + "\n")

inputtxt = tk.Text(frame,
				height = 6,
				width = 20)

inputtxt.grid()

printButton = tk.Button(frame,
						text = "Add",
						command = printInput)

printButton.grid()

printButton = tk.Button(frame,
						text = "Delete",
						command = printnot)

printButton.grid()

lbl = tk.Label(frame, text = "")
lbl.grid()




    
frame.mainloop()

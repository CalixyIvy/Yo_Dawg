from tkinter import*
import tkinter as tk

ref=["milk", "eggs", "help" ]

root = tk.Tk()
root = Tk()
root.resizable(False, False)
root.title("Text Widget Example")

displaylist = Listbox(root)
displaylist.grid(row=0, column=0, columnspan=2, sticky= E)
def show():
    for thing in ref:
        displaylist.insert(END, thing)

def not_show():
    displaylist.delete("1.0", "end")
        
add = Button(root, text= "Add List! ", command=show)
add.grid()

delete = Button(root, text= "Delete List!!!", command=not_show)
delete.grid()

root.mainloop()
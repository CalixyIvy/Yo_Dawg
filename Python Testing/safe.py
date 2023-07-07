def update_label():
   global label
   label["text"]="2. Yay!! I am updated"
   
   update=ttk.Button(win, text="Update the Label", command=update_label)
update.pack(anchor=W, pady=10)
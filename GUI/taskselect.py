from tkinter import *

root = Tk()
root.geometry('400x300')
root.title('Task Selection')


f = ("Times bold", 14)

def nextPage():
    root.destroy()
    import page2

def prevPage():
    root.destroy()
    import page3
    
Label(
    root,
    text="Select the task you want to work on",
    padx=20,
    pady=20,
    font=f
).pack(expand=True, fill=BOTH)

Button(
    root, 
    text="Balance", 
    font=f,
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    root, 
    text="Onload/Offload", 
    font=f,
    command=prevPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

root.mainloop()

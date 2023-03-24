from tkinter import *
#tkinter documentation https://docs.python.org/3/library/tk.html
#manifestbalance and manifestload functions from https://pythonguides.com/go-to-next-page-in-python-tkinter/  

root = Tk()
root.geometry('400x300')
root.title('Task Selection')


f = ("Times bold", 14)

def manifestbalance():
    root.destroy()
    import manifestToLogBalance

def manifestload():
    root.destroy()
    import manifestToLogLoad
    
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
    command=manifestbalance
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    root, 
    text="Onload/Offload", 
    font=f,
    command=manifestload
    ).pack(fill=X, expand=TRUE, side=LEFT)

root.mainloop()

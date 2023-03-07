from tkinter import *

root = Tk()
root.title('Welcome')
L1=Label( text ="Welcome \n Enter your first and last name:", font = 40)
L1.grid(row=0, column=0)

E1=Entry(root, font=("Arial Black", 12))
E1.grid(row=2, column=0)

def nextPage():
    root.destroy()
    import manifest
    
B1=Button(root, text="Next", font=40, command=nextPage)
B1.grid(row=3, column=0)

root.mainloop()
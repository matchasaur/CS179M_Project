from tkinter import *
import time

root = Tk()
root.title('Welcome')
L1=Label( text ="Step 1 of 5", font = 40)
L1.grid(row=0, column=0)

t = time.localtime()
current_time = time.strftime("%H:%M", t)
L2=Label (text = current_time, font = 40)
L2.grid(row=1, column = 0)


def changeUser():
    root.destroy()
    import signin
    
B1=Button(root, text="Change User", font=40, command=changeUser)
B1.grid(row=3, column=0)

L3=Label( text ="Current User: John Doe", font = 40)
L3.grid(row=4, column=0)

L5=Label( text ="Move container labeled Sony to 1,6", font = 40)
L5.grid(row=4, column=6)

L4=Label( text ="Now Balancing: Titanic", font = 40)
L4.grid(row=0, column=13)

def logFile():
    root.destroy()
    import testLog
    
B2=Button(root, text="Log File", font=40, command=logFile)
B2.grid(row=1, column=13)

root.mainloop()
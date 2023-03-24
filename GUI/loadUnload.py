from tkinter import *
import time
import combined
#tkinter documentation https://docs.python.org/3/library/tk.html
#beginLoad function from https://www.w3docs.com/snippets/python/how-can-i-make-one-python-file-run-another.html
#logFile and changeUser functions from https://pythonguides.com/go-to-next-page-in-python-tkinter/
#time code from https://www.programiz.com/python-programming/datetime/current-time
root = Tk()
root.title('Load/Unload')

t = time.localtime()
current_time = time.strftime("%H:%M", t)
L2=Label (text = current_time, font = 40)
L2.grid(row=0, column = 0)

def beginLoad():
    with open("combined.py") as f:
        exec(f.read())

B1=Button(root, text="Begin Load/Unload", font=40, command=beginLoad)
B1.grid(row=2, column=0)

def changeUser():
    root.destroy()
    import signin
    
B1=Button(root, text="Change User", font=40, command=changeUser)
B1.grid(row=3, column=0)

L4=Label( text ="Now Loading/Unloading", font = 40)
L4.grid(row=0, column=13)

def logFile():
    root.destroy()
    import logFile
    
B2=Button(root, text="Log File", font=40, command=logFile)
B2.grid(row=1, column=13)

root.mainloop()
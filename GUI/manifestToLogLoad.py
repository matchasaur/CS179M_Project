from tkinter import *
import logging
#tkinter documentation https://docs.python.org/3/library/tk.html
#get_value function from https://www.tutorialspoint.com/how-to-get-the-value-of-an-entry-widget-in-tkinter
#nextPage function from https://pythonguides.com/go-to-next-page-in-python-tkinter/ 
#Logging code from https://docs.python.org/3/howto/logging.html
logger = logging.getLogger(__name__)

logging.basicConfig(filename='LogFile.txt',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M')

root = Tk()
root.title('Manifest Upload')
L1=Label( text ="Please input the name of the file:", font = 40)
L1.grid(row=0, column=0)

def get_value():
   manifest=E1.get()
   logger.setLevel(logging.INFO)
   logger.info("%s is opened", manifest)
   manifest_open = open(manifest, "r")

E1=Entry(root, font=("Arial Black", 12))
E1.grid(row=2, column=0)
B0=Button(root, text="Confirm", font=40, command=get_value)
B0.grid(row=3, column=0)
   
def nextPage():
    root.destroy()
    import loadUnload
    
B1=Button(root, text="Next", font=40, command=nextPage)
B1.grid(row=4, column=0)

root.mainloop()
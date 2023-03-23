from tkinter import *
import logging


logger = logging.getLogger(__name__)

logging.basicConfig(filename='LogFile.txt',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M')

root = Tk()
root.title('Welcome')
L1=Label( text ="Welcome \n Enter your first and last name:", font = 40)
L1.grid(row=0, column=0)

def get_value():
   e_text=E1.get()
   logger.setLevel(logging.INFO)
   logger.info("%s logged in", e_text)

E1=Entry(root, font=("Arial Black", 12))
E1.grid(row=2, column=0)
B0=Button(root, text="Confirm", font=40, command=get_value)
B0.grid(row=3, column=0)
   
def nextPage():
    root.destroy()
    import taskselect
    
B1=Button(root, text="Next", font=40, command=nextPage)
B1.grid(row=4, column=0)

root.mainloop()
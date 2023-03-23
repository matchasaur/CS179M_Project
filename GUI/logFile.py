from tkinter import *
from tkinter import filedialog
import logging


logger = logging.getLogger(__name__)

logging.basicConfig(filename='LogFile.txt',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M')

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()

ws = Tk()
ws.title("PythonGuides")
ws.geometry("1600x900")
ws['bg']='#fb0'

txtarea = Text(ws, width=40, height=20)
txtarea.pack(pady=20)

pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)



Button(
    ws, 
    text="Open File", 
    command=openFile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)

def get_value():
   e_text=E1.get()
   logger.setLevel(logging.INFO)
   logger.info("%s", e_text)

L1=Label( text ="Insert Comments here:", font = 12)
L1.pack()
E1=Entry(ws, font=("Arial Black", 12))
E1.pack()
B0=Button(ws, text="Confirm", font=40, command=get_value)
B0.pack()
ws.mainloop()
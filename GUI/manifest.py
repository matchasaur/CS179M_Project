# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *

# import filedialog module
from tkinter import filedialog

# Function for opening the
# file explorer window
def browseFiles():
	filename = filedialog.askopenfilename(initialdir = "/",
										title = "Select a File",
										filetypes = (("Text files",
														"*.txt*"),
													("all files",
														"*.*")))
	
	# Change label contents
	label_file_explorer.configure(text="File Opened: "+filename)
	
def nextPage():
    window.destroy()
    import taskselect
																								
# Create the root window
window = Tk()

# Set window title
window.title('Manifest Upload')

# Set window size
window.geometry("600x600")

#Set window background color
window.config(background = "white")

# Create a File Explorer label
label_file_explorer = Label(window,
							width = 100, height = 4,)

	
button_explore = Button(window,
						text = "Browse Files",
						command = browseFiles)

button_exit = Button(window,
					text = "Next",
					command = nextPage)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
L1=Label( text ="Please upload the manifest", font = 40)
L1.grid(row=0, column=0)

label_file_explorer.grid(column = 0, row = 1)

button_explore.grid(column = 0, row = 2)

button_exit.grid(column = 0,row = 3)

# Let the window wait for any events
window.mainloop()

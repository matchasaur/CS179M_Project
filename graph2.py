from tkinter import *

class GraphicalInterface:
##Initialisation of the GUI class.
    def __init__(self, height, width):
        self.block_size=25
        self.padding=1
        self.frame_height = height*self.block_size
        self.frame_width = width*self.block_size
        self.root = Tk()
        self.root.resizable(width=0, height=0)
        self.height = height
        self.width = width
        
        self.frm = Frame(self.root, height=self.frame_height+8+self.padding*(height*2),
                         width=self.frame_width+8+self.padding*(width*2), background='lightgray',
                         cursor='circle', relief='sunken', borderwidth=4)
        self.frm.grid_propagate(0)
        self.frm.grid(column=0, row=0, padx=20, pady=20)
        for i in range(0,width):
            for j in range(0,height):
                cur_frame = Frame(self.frm, height=self.block_size, width=self.block_size)
                cur_frame.grid(column=i,row=j, padx=self.padding, pady=self.padding)



    def set_all(self):
        for i in range(self.width):
            for j in range(self.height):
                self.setObstacle(i, j)
                self.root.update()
                self.root.after(250)  # like time.sleep()
                
    def run(self):
        #self.root.after(100, self.setObstacle, 0, 0)
        self.root.after(100, self.set_all)
        self.root.mainloop()
        
GraphicalInterface(8, 12).run()  
from tkinter import *

class App:
    def __init__(self, root):
        self.frames = []
        self.entries = []
        self.count = 0
        self.root = root
        self.create = Button(self.root, text="Create", command=self.draw)
        self.create.pack(side="top")
    def draw(self):
        self.frames.append(Frame(self.root, borderwidth=1, relief="solid"))
        self.frames[self.count].pack(side="left")
        self.entries.append([Entry(self.frames[self.count]), Entry(self.frames[self.count])])
        for i in self.entries[self.count]:
            i.pack()
        Button(self.frames[self.count], text="Submit", command=lambda c=self.count: self.submit(c)).pack()
        self.count += 1
    def submit(self, c):
        for i in self.entries[c]:
            print(i.get())

root = Tk()
labelText=StringVar()
labelText.set("Submit the name and weight of the containers you wish to onload here: \n First box is for Name, Second box is for Weight")
labelDir=Label(root, textvariable=labelText, height=4)
labelDir.pack(side="top")
App(root)

def nextPage():
    root.destroy()
    import manifest

B1 = Button(root, text="Next", command=nextPage)
B1.pack( side = "bottom")

root.mainloop()
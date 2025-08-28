import tkinter as tk
from tkinter import ttk
from config import colors

class ColorPallet():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Control Panel")

        self.frame = tk.Frame(self.root)
        self.bottomFrame = tk.Frame(self.root)

        self.frame.grid(column=0, row=0)
        self.bottomFrame.grid(column=0, row=1)

        self.colors = colors

        self.counter = 0
        self.amount = 6

        self.createColorPallet()

        self.update()


    
    def getColor(self): ...



    def createColorPallet(self):
        self.tiles = []
        for i in range(self.amount):
            for j in range(self.amount):
                tile = tk.Button(
                    self.root,
                    relief="groove",
                    borderwidth=1,
                    height=3,
                    width=6,
                    bg= self.getColorFromList()
                )

                self.tiles.append(tile)
                tile.grid(row=i, column=j)



    
    def getColorFromList(self):
        self.counter += 1
        if self.counter == 37: self.counter = 0

        for i in range(len(self.colors)):
            return self.colors[self.counter -1 ]
            



    def update(self):
        self.root.update()
        self.root.mainloop()



color = ColorPallet()
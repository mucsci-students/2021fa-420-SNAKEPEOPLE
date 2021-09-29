import tkinter as tk
import UMLsquare

line_list = []

class UMLline():

    def __init__(self, canvas, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        line = canvas.create_line(x1, y1, x2, y2)
    
def add_line(canvas, source, dest):
    midsourcex = canvas.coords(source)[2] - canvas.coords(source)[0]
    midsourcey = canvas.coords(source)[3] - canvas.coords(source)[1]
    middestx = canvas.coords(dest)[2] - canvas.coords(dest)[0]
    middesty = canvas.coords(dest)[3] - canvas.coords(dest)[1]
    print(midsourcex)
    print(midsourcey)
    new_line = UMLline(canvas, midsourcex, midsourcey, middestx, middesty)
    
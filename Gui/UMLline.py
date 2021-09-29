import tkinter as tk
import UMLcircle

class UMLline():

    #create a line between the center of the source circle and
    #the center of the destination circle. Lower all lines below
    #the level of the circles, saves the source and destination
    #values within a list of tuples, within the UMLcircle tuple
    def __init__(self, canvas, x1, y1, x2, y2, source, dest):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        line = canvas.create_line(x1, y1, x2, y2)
        sourcepos = findpos(source)
        destpos = findpos(dest)
        canvas.tag_lower(line)
        UMLcircle.circle_list[sourcepos][3].append(("source", line))
        UMLcircle.circle_list[destpos][3].append(("dest", line))
        
#Add the new line with the correct positioning at the 
#center of the circle
def add_line(canvas, source, dest):
    midsourcex = canvas.coords(source)[0] + 25
    midsourcey = canvas.coords(source)[1] + 25
    middestx = canvas.coords(dest)[0] + 25
    middesty = canvas.coords(dest)[1] + 25
    UMLline(canvas, midsourcex, midsourcey, middestx, middesty, source, dest)

#Find the position in the circle_list of the source
def findpos(source):
    pos = 0
    while(pos < len(UMLcircle.circle_list)):
        if source == UMLcircle.circle_list[pos][1]:
            return pos
        else:
            pos += 1

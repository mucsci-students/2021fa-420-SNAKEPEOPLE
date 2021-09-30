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
        sourcepos = findpos(source)
        destpos = findpos(dest)
        line = canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST)
        canvas.tag_lower(line)
        UMLcircle.circle_list[sourcepos][4].append(("source", line, dest))
        UMLcircle.circle_list[destpos][4].append(("dest", line, source))
        
#Add the new line with the correct positioning at the 
#center of the circle
def add_line(canvas, source : str, dest : str):
    sourceItem = UMLcircle.circle_list[findpos(source)][1]
    destItem = UMLcircle.circle_list[findpos(dest)][1]
    midsourcex = canvas.coords(sourceItem)[0]
    midsourcey = canvas.coords(sourceItem)[1] + 15
    middestx = canvas.coords(destItem)[0]
    middesty = canvas.coords(destItem)[1] + 15
    UMLline(canvas, midsourcex, midsourcey, middestx, middesty, source, dest)

#Find the position of the circle_list of the source
def findpos(source):
    pos = 0
    while(pos < len(UMLcircle.circle_list)):
        if source == UMLcircle.circle_list[pos][1]:
            return pos
        else:
            pos += 1

def delete_line(canvas, source, dest):
    sourcepos = findpos(source)
    destpos = findpos(dest)
    subpos = 0
    while subpos < len(UMLcircle.circle_list[sourcepos][4]):
        if (UMLcircle.circle_list[sourcepos][4][subpos][0] == "source" 
            and UMLcircle.circle_list[sourcepos][4][subpos][2] == dest):
            line = UMLcircle.circle_list[sourcepos][4][subpos][1]
            UMLcircle.circle_list[sourcepos][4].pop(subpos)
        subpos += 1
    subpos = 0
    while subpos < len(UMLcircle.circle_list[destpos][4]):
        if (UMLcircle.circle_list[destpos][4][subpos][0] == "dest" 
            and UMLcircle.circle_list[destpos][4][subpos][2] == source):
            UMLcircle.circle_list[destpos][4].pop(subpos)
        subpos += 1
    canvas.delete(line)
import tkinter as tk
import UMLbox

class UMLline():

    """create a line from one box to another"""
    def __init__(self, canvas, x1, y1, x2, y2, source, dest, line_type):
        sourcepos = findpos(source)
        destpos = findpos(dest)
        line = canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill=line_type, width=3)
        canvas.tag_lower(line)
        UMLbox.class_list[sourcepos][4].append(("source", line, dest))
        UMLbox.class_list[destpos][4].append(("dest", line, source))

def add_line(canvas, source : str, dest : str, line_type : str):
    sourcepos = UMLbox.find_pos_from_name(source)
    destpos = UMLbox.find_pos_from_name(dest)
    addline(canvas, UMLbox.class_list[sourcepos][1], UMLbox.class_list[destpos][1], line_type)

"""add a line cooresponding to the names of the two boxes, source and dest"""
def addline(canvas, source, dest, line_type : str):
    if(line_type == "aggregation"):
        color = 'blue'
    elif(line_type == "composition"):
        color = '#000fff000'
    elif(line_type == "inheritance"):
        color = 'red'
    else:
        color = 'black'
    sourceItem = UMLbox.class_list[findpos(source)][1]
    destItem = UMLbox.class_list[findpos(dest)][1]
    midsourcex = canvas.coords(sourceItem)[0]
    midsourcey = canvas.coords(sourceItem)[1]
    middestx = canvas.coords(destItem)[0]
    middesty = canvas.coords(destItem)[1]
    UMLline(canvas, midsourcex, midsourcey, middestx, middesty, sourceItem, destItem, color)

"""#Find the position of the class_list of the source"""
def findpos(source):
    pos = 0
    while(pos < len(UMLbox.class_list)):
        if source == UMLbox.class_list[pos][1]:
            return pos
        else:
            pos += 1

"""Fine the correct box elements of the source and dest within the class_list"""
def delete_line(canvas, source : str, dest : str):
    sourcepos = UMLbox.find_pos_from_name(source)
    destpos = UMLbox.find_pos_from_name(dest)
    deleteline(canvas, UMLbox.class_list[sourcepos][1], UMLbox.class_list[destpos][1])

"""remove a line from the class_list storage. Line is stored both ways so two deletes must occur"""
def deleteline(canvas, source, dest):
    sourcepos = findpos(source)
    destpos = findpos(dest)
    subpos = 0
    while subpos < len(UMLbox.class_list[sourcepos][4]):
        if (UMLbox.class_list[sourcepos][4][subpos][0] == "source" 
            and UMLbox.class_list[sourcepos][4][subpos][2] == dest):
            line = UMLbox.class_list[sourcepos][4][subpos][1]
            UMLbox.class_list[sourcepos][4].pop(subpos)
        subpos += 1
    subpos = 0
    while subpos < len(UMLbox.class_list[destpos][4]):
        if (UMLbox.class_list[destpos][4][subpos][0] == "dest" 
            and UMLbox.class_list[destpos][4][subpos][2] == source):
            UMLbox.class_list[destpos][4].pop(subpos)
        subpos += 1
    canvas.delete(line)
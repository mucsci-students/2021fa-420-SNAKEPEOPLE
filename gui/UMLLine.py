# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     UMLLine.py

import tkinter as tk
from gui import EventHandler, ViewChange, UMLBox

from uml_components.interfaces import (attr_interface as ai,
                                       class_interface as ci,
                                       rel_interface as ri)
from uml_components import UMLClass
from uml_components import UMLRelationship

class UMLLine():

    #create a line from one box to another#
    def __init__(self, x1, y1, x2, y2, source, dest, line_type):
        sourcepos = findpos(source)
        destpos = findpos(dest)
        if line_type == "#000fff000":
            shape = (20, 10, 7)
        # if line_type == "aggregation":
        else:
            shape = (0,0,0)
        line = UMLBox.test_canvas.create_line(x1, y1, x2, y2, arrow=tk.FIRST, fill=line_type, width=3, arrowshape=shape)
        UMLBox.test_canvas.tag_lower(line)
        #store entries for source and dest boxes that tell whether the box is the source
        #or destination of a relationship
        UMLBox.class_list[sourcepos].rels.append(("source", line, dest))
        UMLBox.class_list[destpos].rels.append(("dest", line, source))

#add a line connecting two classes by name, source and dest#
def add_line(source : str, dest : str, line_type : str):
    sourcepos = UMLBox.find_pos_from_name(source)
    destpos = UMLBox.find_pos_from_name(dest)
    if(line_type == "aggregation"):
        color = 'blue'
    elif(line_type == "composition"):
        color = '#000fff000'
    elif(line_type == "inheritance"):
        color = 'red'
    else:
        color = 'black'
    sourceItem = UMLBox.class_list[UMLBox.find_pos_from_name(source)].rec
    destItem = UMLBox.class_list[UMLBox.find_pos_from_name(dest)].rec
    midsourcex = UMLBox.test_canvas.coords(sourceItem)[0]
    midsourcey = UMLBox.test_canvas.coords(sourceItem)[1]
    middestx = UMLBox.test_canvas.coords(destItem)[0]
    middesty = UMLBox.test_canvas.coords(destItem)[1]
    UMLLine(midsourcex, midsourcey, middestx, middesty, sourceItem, destItem, color)

##Find the position of the class_list of the source#
def findpos(source):
    pos = 0
    while(pos < len(UMLBox.class_list)):
        if source == UMLBox.class_list[pos].rec:
            return pos
        else:
            pos += 1

#Fine the correct box elements of the source and dest within the class_list#
def delete_line(source : str, dest : str):
    sourcepos = UMLBox.find_pos_from_name(source)
    destpos = UMLBox.find_pos_from_name(dest)
    deleteline(UMLBox.class_list[sourcepos].rec, UMLBox.class_list[destpos].rec)

#remove a line from the class_list storage. Line is stored both ways so two deletes must occur#
def deleteline(source, dest):
    sourcepos = findpos(source)
    destpos = findpos(dest)
    subpos = 0
    #delete all line entries for a box that involve source#
    while subpos < len(UMLBox.class_list[sourcepos].rels):
        if (UMLBox.class_list[sourcepos].rels[subpos][0] == "source" 
            and UMLBox.class_list[sourcepos].rels[subpos][2] == dest):
            line = UMLBox.class_list[sourcepos].rels[subpos][1]
            UMLBox.class_list[sourcepos].rels.pop(subpos)
        subpos += 1
    subpos = 0
    #delete all line entries for a box that involve dest#
    while subpos < len(UMLBox.class_list[destpos].rels):
        if (UMLBox.class_list[destpos].rels[subpos][0] == "dest" 
            and UMLBox.class_list[destpos].rels[subpos][2] == source):
            UMLBox.class_list[destpos].rels.pop(subpos)
        subpos += 1
    #delete the line element itself#
    ViewChange.del_item(line)

def line_mediator():
    #Delete all existing relationships on the canvas
    for i in UMLBox.class_list:
        while len(i.rels) > 0:
            ViewChange.del_item(i.rels[0][1])
            i.rels.pop(0)
        i.rels = []
    #Add any relationships back to the list, if both boxes exist in the canvas
    for i in UMLRelationship.relationship_list:
        if UMLBox.find_pos_from_name(i.source) != None and UMLBox.find_pos_from_name(i.destination) != None:
            add_line(i.source, i.destination, i.type)

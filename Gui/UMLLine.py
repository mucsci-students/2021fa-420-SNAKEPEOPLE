import tkinter as tk
from gui import ViewChange
from gui import UMLBox
from uml_components.UMLRelationship import UMLRelationship
from uml_components.interfaces import (attr_interface as ai,
                                       class_interface as ci,
                                       rel_interface as ri)
from uml_components.UMLClass import UMLClass, class_dict
from uml_components.UMLRelationship import UMLRelationship, relationship_list

class UMLLine():

    #create a line from one box to another#
    def __init__(self, x1, y1, x2, y2, source, dest, line_type):
        sourcepos = findpos(source)
        destpos = findpos(dest)
        line = UMLBox.test_canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill=line_type, width=3)
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
    if ri.find_rel(source, dest)[0] == True:
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

def fix_lines():
    #Delete all existing relationships on the canvas
    for i in UMLBox.class_list:
        for k in UMLBox.class_list:
            if ri.find_rel(i.name, i.name)[0] == True:
                delete_line(i.name, k.name)
    #Add all existing relationships to the canvas
    for i in relationship_list:
        add_line(i.source, i.destination, i.type)
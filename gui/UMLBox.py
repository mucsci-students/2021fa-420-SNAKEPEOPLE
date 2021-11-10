# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     UMLBox.py

import tkinter as tk
from gui.UMLLine import deleteline, findpos
from . import UMLSavepoint
from . import EventHandler
from . import ViewChange
from . import UMLField
from gui.UMLMethod import update_methods
from uml_components.UMLAttributes import UMLMethod
from uml_components.interfaces import (attr_interface as ai,
                                       class_interface as ci,
                                       rel_interface as ri)
from uml_components import UMLClass

class_list = []
global maxx
maxx = 2000
global maxy
maxy = 2000

def init_canvas(frame : tk.Frame) -> tk.Canvas:
    global test_canvas
    test_canvas = tk.Canvas(frame,
                        bg="#D0D0D0",
                        scrollregion=(0,0,2000,2000),
                        bd=3)
    return test_canvas

def find_pos_from_name(name : str):
    pos = 0
    while pos < len(class_list):
        if class_list[pos].name == name:
            return pos
        pos += 1

class UMLsquare():

    """the list tracks the name, the square element, the class name label,
    how much padding to account for lengthy text, lines, yincrement
    field header, method header, methods text element"""
    xspace = 0
    def __init__(self, x1 : int, y1 : int, x2 : int, y2 : int, name : str):
        label = test_canvas.create_text((x1 + (x2 - x1) / 2), y1 + 12, text = name, state=tk.DISABLED, tags=name)
        textspace =3.5 * len(name)
        rec = test_canvas.create_rectangle(x1, y1, x2, y2 + 40, fill="#D1FF65", tags=name)
        fieldlabel = test_canvas.create_text(x1 + 10, y1 + 30, text = "Field(s):", state=tk.DISABLED)
        fieldtext = test_canvas.create_text((x1 + (x2 - x1) / 2), y1 + 35, text = "", state=tk.HIDDEN, anchor=tk.N)
        yincrement = 30
        methodlabel = test_canvas.create_text(x1, y1 + 50, text = "Method(s):", state=tk.DISABLED)
        methodtext = test_canvas.create_text((x1 + (x2 - x1) / 2), y1 + 60, text = "", state=tk.HIDDEN, anchor=tk.N)
        ViewChange.push_back(rec)
        self.name = name
        self.rec = rec
        self.label = label
        self.textspace = textspace
        self.rels = []
        self.fieldtext = fieldtext
        self.yinc = yincrement
        self.fieldlabel = fieldlabel
        self.methodlabel = methodlabel
        self.methodtext = methodtext
        EventHandler.can_drag(rec)
    
#add a box to the canvas#      
def create_box(name : str):
    yinc = 0
    #Make sure the class does not already exist
    placed = False
    x_place = 1
    prev_inc = False
    x1 = 60
    x2 = 140
    y1 = 40
    y2 = 65

    #Account for lenthy boxes
    last_textspace = 0
    if len(class_list) > 0:
        last_textspace = class_list[len(class_list) - 1].textspace
    if(len(name) > 8):
        current_textspace = len(name) * 10
    else:
        current_textspace = len("methods:") * 3.5

    #Find a big enough gap to place the newest class
    while not placed:
        if x1 - current_textspace < 0:
            x1 = current_textspace + 60
        if len(test_canvas.find_overlapping(x1 - current_textspace - 20, y1 - 20, x2 + current_textspace - 20, y2 + 20)) != 0:
            if x2 > maxx - current_textspace - 40:
                y1 += 25
                y2 += 25
                x1 = 60
                x2 = 140
                last_textspace = 0
            else:
                x1 += 1
                x2 += 1
        else:
            placed = True

    #Create the new box
    obj = UMLsquare(x1, y1, x2, y2, name)
    #Add the new box to the list
    class_list.append(obj)
    #Bring current box to front
    ViewChange.bring_all_front(obj)
    #update the size of the current box
    update_size(len(class_list) - 1)
    #Fix any box that may have been overlapped
    # UMLField.fix_pos(len(class_list) - 1)

def create_box_with_coords(name : str, x1 : int, y1 : int, x2 : int, y2 : int):
    obj = UMLsquare(x1, y1, x2, y2, name)
    class_list.append(obj)
    update_size(len(class_list) - 1)
    UMLField.update_vertical(len(class_list) - 1)

#Remove the box with the text = name#
def delete_box(name : str):
    pos = find_pos_from_name(name)
    if pos != None:
        subpos = 0
        #remove any lines connecting the box to any other boxes#
        while subpos < len(class_list[pos].rels):
            if(class_list[pos].rels[subpos][0] == "source"):
                deleteline(class_list[pos].rec, class_list[pos].rels[subpos][2])
                subpos -= 1
            else:
                deleteline(class_list[pos].rels[subpos][2], class_list[pos].rec)
                subpos -= 1
            subpos += 1
        #delete everything associated with the box
        ViewChange.del_item(class_list[pos].rec)
        ViewChange.del_item(class_list[pos].label)
        ViewChange.del_item(class_list[pos].fieldtext)
        ViewChange.del_item(class_list[pos].fieldlabel)
        ViewChange.del_item(class_list[pos].methodlabel)
        ViewChange.del_item(class_list[pos].methodtext)
        class_list.pop(pos)

#rename a box with the name = oldname#
def rename_box(oldname : str, newname : str):
    #Check for duplicate box names#
    if(find_pos_from_name(newname) == None):
        pos = 0
        #Find the position of the box with the old name#
        for i in class_list:
            if oldname == i.name:
                #save the box and text values#
                class_list[pos].name = newname
                break
            else:
                pos += 1
        #Change the text of the box to the updated name#
        ViewChange.item_config(class_list[pos].label, newname, None, None)
        #update the width of the box#
        update_size(pos)


#update the width of the box according to the length of the contained text#
def update_size(pos : int):
    classname = class_list[pos].name
    longest_name = 3.5 * len(class_list[pos].name)
    i = 0
    #Check class name against field and method labels
    if(len("Fields:") * 3.5 > longest_name):
        longest_name = len("Fields:") * 3.5
    if(len("Methods:") * 3.5 > longest_name):
        longest_name = len("Methods:") * 3.5
    uml : UMLClass = UMLClass.class_dict[classname]
    #Check all names in the list of fields
    for fields in uml.fields:
        name = "-" + fields.type + " " + fields.name
        if len(name) * 3.5 > longest_name:
            longest_name = len(name) * 3.5
    uml : UMLClass = UMLClass.class_dict[classname]
    method : ai.UMLMethod
    param : ai.UMLParameter
    #Check all info in the list of methods and parameters
    for method in uml.methods:
        name = method.name + " " + method.return_type + "("
        if len(name) * 3.5 > longest_name:
            longest_name = len(name) * 3.5
        for param in method.params:
            name = "  -" + param.type + " " + method.name
            if len(name) * 3.5 > longest_name:
                longest_name = len(name) * 3.5
    class_list[pos].textspace = longest_name
    #find the center and build off of it left and right using the
    #length of the longest text entry
    x1,y1,x2,y2 = test_canvas.coords(class_list[pos].rec)
    center = ((x2 - x1) / 2) + x1
    x1 = center - 40 - longest_name
    x2 = center + 40 + longest_name
    if x1 < 0:
        x1 = 10
        x2 = 10 + 80 + 2 * longest_name
    #update the box size, and shift label text elements#
    ViewChange.set_rec(class_list[pos].rec, x1, y1, x2, y2)
    ViewChange.set_text(class_list[pos].label, center, y1 + 12)
    x,y = test_canvas.coords(class_list[pos].fieldlabel)
    ViewChange.set_text(class_list[pos].fieldlabel, x1 + 25, y)
    x,y = test_canvas.coords(class_list[pos].methodlabel)
    ViewChange.set_text(class_list[pos].methodlabel, x1 + 35, y)
    return center

def get_coords(name : str):
    pos = find_pos_from_name(name)
    x1, y1, x2, y2 = test_canvas.coords(class_list[pos].rec)
    return (x1, y1, x2, y2)

#Function used to store location of the box in UMLClass
def get_xy(name : str):
    pos = find_pos_from_name(name)
    x1, y1, x2, y2 = test_canvas.coords(class_list[pos].rec)
    centerx = x1 + (x2-x1)/2
    return (centerx, y1)

#General function for telling the canvas to update the boxes
def class_mediator():
    #Delete any boxes not found in the class dict (Model)
    for i in class_list:
        if i.name not in UMLClass.class_dict:
            delete_box(i.name)
    #Add any boxes that are in the class dict (Model)
    for name, value in UMLClass.class_dict.items():
        if find_pos_from_name(name) == None:
            #If the class was created in CLI, create its representation
            #in the first available space
            if value.position_x == -1 and value.position_y == -1:
                create_box(name)
                x, y = get_xy(name)
                value.position_x = x
                value.position_y = y
            #Otherwise place the box in its correct space    
            else:
                x1, y1, x2, y2 = UMLSavepoint.make_coords(name, value.position_x, value.position_y)
                create_box_with_coords(name, x1, y1, x2, y2)
            update_methods(name)
            UMLField.update_fields(name)
    
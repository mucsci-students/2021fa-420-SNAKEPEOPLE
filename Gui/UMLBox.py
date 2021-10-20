import tkinter as tk
from gui.UMLLine import deleteline
from . import EventHandler
from . import ViewChange
from . import UMLField
from gui.UMLMethod import update_methods
from uml_components.UMLAttributes import UMLMethod
from uml_components.interfaces import (attr_interface as ai,
                                       class_interface as ci,
                                       rel_interface as ri)
from uml_components.UMLClass import UMLClass, class_dict

class_list = []

def init_canvas(frame : tk.Frame) -> tk.Canvas:
    global test_canvas 
    test_canvas = tk.Canvas(frame, 
                        width=600, 
                        height=600,
                        bg="#888",
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
    tracker = 0
    x1 = 120
    x2 = 200
    y1 = 40
    y2 = 65
    xspace = 0
    def __init__(self, x1 : int, y1 : int, x2 : int, y2 : int, name : str):
        label = test_canvas.create_text(x1 + 40, y1 + 12, text = name, state=tk.DISABLED, tags=name)
        textspace =3.5 * len(name)
        if UMLsquare.tracker % 2 == 1:
            x1 += textspace
            x2 += textspace
        rec = test_canvas.create_rectangle(x1 - textspace, y1, x2 + textspace, y2 + 40, fill="#D1FF65", tags=name)
        fieldlabel = test_canvas.create_text(x1 + 10, y1 + 30, text = "Field(s):", state=tk.DISABLED)
        fieldtext = test_canvas.create_text(x1 + 40, y1 + 35, text = "", state=tk.HIDDEN, anchor=tk.N)
        yincrement = 30
        methodlabel = test_canvas.create_text(x1, y1 + 50, text = "Method(s):", state=tk.DISABLED)
        methodtext = test_canvas.create_text(x1 + 40, y1 + 60, text = "", state=tk.HIDDEN, anchor=tk.N)
        test_canvas.tag_lower(rec)
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
    if find_pos_from_name(name) == None and ai.find_class(name)[0] == True:
        obj = UMLsquare(UMLsquare.x1, UMLsquare.y1, UMLsquare.x2, UMLsquare.y2, name)
        class_list.append(obj)
        #shift everything right after the first box in a row and then shift down after the second#
        if(UMLsquare.tracker % 2 == 0):
            UMLsquare.x1 += obj.textspace + 200
            UMLsquare.x2 += obj.textspace + 200
        else:
            UMLsquare.x1 = 120
            UMLsquare.x2 = 200
            UMLsquare.y1 += 100 + yinc
            UMLsquare.y2 += 100 + yinc
        UMLsquare.tracker += 1
        #Update width of box#
        update_size(len(class_list) - 1)

def create_box_with_coords(name : str, x1, y1, x2, y2):
    obj = UMLsquare(x1 + 40, y1, x2, y2, name)
    class_list.append(obj)
    update_size(len(class_list) - 1)
    # if len(class_dict[name].methods) > 0:
    #     update_methods(name)
    # if len(class_dict[name].fields) > 0:
    #     UMLField.update_fields(name)

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
        #delete everything associated with the box#
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
    uml : UMLClass = class_dict[classname]
    #Check all names in the list of fields
    for fields in uml.fields:
        name = "-" + fields.type + " " + fields.name
        if len(name) * 3.5 > longest_name:
            longest_name = len(name) * 3.5
    uml : UMLClass = class_dict[classname]
    method : ai.UMLMethod
    param : ai.UMLParameter
    #Check all info in the list of methods and parameters
    for method in uml.methods:
        name = method.name + " " + method.return_type + "("
        if len(name) * 3.5 > longest_name:
            longest_name = len(name) * 3.5
        for param in method.params:
            name = "    -" + param.type + " " + method.name
            if len(name) * 3.5 > longest_name:
                longest_name = len(name) * 3.5
    class_list[pos].textspace = longest_name
    #find the center and build off of it left and right using the
    #length of the longest text entry
    x1,y1,x2,y2 = test_canvas.coords(class_list[pos].rec)
    center = ((x2 - x1) / 2) + x1
    x1 = center - 40 - longest_name
    x2 = center + 40 + longest_name
    #update the box size, and shift label text elements#
    ViewChange.set_rec(class_list[pos].rec, x1, y1, x2, y2)
    x,y = test_canvas.coords(class_list[pos].fieldlabel)
    ViewChange.set_text(class_list[pos].fieldlabel, x1 + 25, y)
    x,y = test_canvas.coords(class_list[pos].methodlabel)
    ViewChange.set_text(class_list[pos].methodlabel, x1 + 35, y)
    return center

def get_coords(name : str):
    pos = find_pos_from_name(name)
    x1, y1, x2, y2 = test_canvas.coords(class_list[pos].rec)
    return (x1, y1, x2, y2)
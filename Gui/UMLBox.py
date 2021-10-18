import tkinter as tk
from gui.UMLLine import deleteline
from gui import EventHandler
from gui import ViewChange
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
        if class_list[pos][0] == name:
            return pos
        pos += 1

class UMLsquare():

    """the list tracks the name, the square element, the class name label,
    how much padding to account for lengthy text, lines, fields, yincrement due to fields,
    field header, method header, methods text element, fields and methods, and vertical increment
    due to methods and parametes"""
    tracker = 0
    x1 = 120
    x2 = 200
    y1 = 40
    y2 = 65
    xspace = 0
    def __init__(self, x1 : int, y1 : int, x2 : int, y2 : int, name : str):
        x1 = x1 + UMLsquare.xspace
        x2 = x2 + UMLsquare.xspace
        label = test_canvas.create_text(x1 + 40, y1 + 12, text = name, state=tk.DISABLED, tags=name)
        textspace =3.5 * len(name)
        if UMLsquare.tracker % 2 == 1:
            x1 += textspace
            x2 += textspace
        rec = test_canvas.create_rectangle(x1 - textspace, y1, x2 + textspace, y2 + 40, fill="#D1FF65", tags=name)
        fieldlabel = test_canvas.create_text(x1 + 10, y1 + 30, text = "Field(s):", state=tk.DISABLED)
        fieldtext = test_canvas.create_text(x1 + 40, y1 + 35, text = "", state=tk.HIDDEN, anchor=tk.N)
        yincrement = 30
        methodlabel = test_canvas.create_text(x1 + 18, y1 + 50, text = "Method(s):", state=tk.DISABLED)
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
        self.info = [name, rec, label, textspace, [], fieldtext, yincrement, fieldlabel, methodlabel, methodtext]
        class_list.append(self.info)
        EventHandler.can_drag(rec)
    
#add a box to the canvas#      
def create_box(name : str):
    addbox = True
    yinc = 0
    #Get previous row's tallest box height#

    #Check for duplicate box names#
    for i in class_list:
        if i[0] == name:
            addbox = False
    if(addbox):
        obj = UMLsquare(UMLsquare.x1, UMLsquare.y1, UMLsquare.x2, UMLsquare.y2, name)
        #shift everything right after the first box in a row and then shift down after the second#
        if(UMLsquare.tracker % 2 == 0):
            UMLsquare.x1 += obj.info[3] + 200
            UMLsquare.x2 += obj.info[3] + 200
        else:
            UMLsquare.x1 = 120
            UMLsquare.x2 = 200
            UMLsquare.y1 += 100 + yinc
            UMLsquare.y2 += 100 + yinc
            UMLsquare.xspace = 0
        UMLsquare.tracker += 1
        #Update width of box#
        update_size(len(class_list) - 1)

#Remove the box with the text = name#
def delete_box(name : str):
    pos = find_pos_from_name(name)
    subpos = 0
    #remove any lines connecting the box to any other boxes#
    while subpos < len(class_list[pos][4]):
        if(class_list[pos][4][subpos][0] == "source"):
            deleteline(class_list[pos][1], class_list[pos][4][subpos][2])
            subpos -= 1
        else:
            deleteline(class_list[pos][4][subpos][2], class_list[pos][1])
            subpos -= 1
        subpos += 1
    #delete everything associated with the box#
    ViewChange.del_item(class_list[pos][1])
    ViewChange.del_item(class_list[pos][2])
    ViewChange.del_item(class_list[pos][5])
    ViewChange.del_item(class_list[pos][7])
    ViewChange.del_item(class_list[pos][8])
    ViewChange.del_item(class_list[pos][9])
    class_list.pop(pos)

#rename a box with the name = oldname#
def rename_box(oldname : str, newname : str):
    renamebox = True
    #Check for duplicate box names#
    for i in class_list:
        if i[0] == newname:
            renamebox = False
    if(renamebox):
        pos = 0
        #Find the position of the box with the old name#
        while pos < len(class_list):
            if oldname == class_list[pos][0]:
                #save the box and text values#
                class_list[pos][0] = newname
                break
            else:
                pos += 1
        #Change the text of the box to the updated name#
        ViewChange.item_config(class_list[pos][2], newname, None, None)
        #update the width of the box#
        update_size(pos)


#update the width of the box according to the length of the contained text#
def update_size(pos : int):
    classname = class_list[pos][0]
    longest_name = 3.5 * len(class_list[pos][0])
    i = 0
    if(len("Fields:") * 3.5 > longest_name):
        longest_name = len("fields:") * 3.5
    if(len("Methods:") * 3.5 > longest_name):
        longest_name = len("methods:") * 3.5
    uml : UMLClass = class_dict[classname]
    for fields in uml.fields:
        name = "-" + fields.type + " " + fields.name
        if len(name) * 3.5 > longest_name:
            longest_name = len(name) * 3.5
    uml : UMLClass = class_dict[classname]
    method : ai.UMLMethod
    param : ai.UMLParameter
    for method in uml.methods:
        name = method.name + " " + method.return_type + "("
        if len(name) * 3.5 > longest_name:
            longest_name = len(name) * 3.5
        for param in method.params:
            name = "    -" + param.type + " " + method.name
            if len(name) * 3.5 > longest_name:
                longest_name = len(name) * 3.5
    class_list[pos][3] = longest_name
    #find the center and build off of it left and right using the#
    #length of the longest text entry#
    x1,y1,x2,y2 = test_canvas.coords(class_list[pos][1])
    center = ((x2 - x1) / 2) + x1
    x1 = center - 40 - longest_name
    x2 = center + 40 + longest_name
    #update the box size, and shift header text elements#
    ViewChange.set_rec(class_list[pos][1], x1, y1, x2, y2)
    x,y = test_canvas.coords(class_list[pos][7])
    ViewChange.set_text(class_list[pos][7], x1 + 25, y)
    x,y = test_canvas.coords(class_list[pos][8])
    ViewChange.set_text(class_list[pos][8], x1 + 35, y)
    return center

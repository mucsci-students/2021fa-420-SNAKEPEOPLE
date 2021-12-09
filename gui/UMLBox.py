# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     UMLBox.py

# External Imports
import tkinter as tk

# Internal Imports
from gui.UMLLine import (
    deleteline, 
    findpos, 
    line_mediator)
from . import UMLSavepoint
from . import EventHandler
from . import ViewChange
from . import UMLField
from gui.UMLMethod import update_methods
from uml_components.interfaces import attr_interface as ai
from uml_components import UMLClass

###################################################################################################
'''
Functions for creating the canvas and populating it with appropriate boxes.
'''
class_list = []

def init_canvas(frame : tk.Frame) -> tk.Canvas:
    size_x = 0
    size_y = 0
    for name, value in UMLClass.class_dict.items():
        if value.position_x > size_x:
            size_x = value.position_x + 1000
        if value.position_y > size_y:
            size_y = value.position_y + 1000
    global test_canvas
    test_canvas = tk.Canvas(frame,
        bg = "#D0D0D0", scrollregion = (0, 0, size_x, size_y), bd = 3)
    global maxx
    maxx = size_x
    global maxy
    maxy = size_y
    return test_canvas

def update_global(xinc, yinc):
    global maxx
    maxx = maxx + xinc
    global maxy
    maxy = maxy + yinc

def find_pos_from_name(name : str):
    pos = 0
    while pos < len(class_list):
        if class_list[pos].name == name:
            return pos
        pos += 1

###################################################################################################
'''
Class for a box object.
'''
class UMLsquare():
    '''
    The list tracks the name, the square element, the class name label,
    how much padding to account for lengthy text, lines, yincrement
    field header, method header, methods text element.
    '''
    xspace = 0
    def __init__(self, x1 : int, y1 : int, x2 : int, y2 : int, name : str):
        label = test_canvas.create_text(
            (x1 + (x2 - x1) / 2), y1 + 12, text = name, state = tk.DISABLED, tags = name)
        textspace = 3.1 * len(name)
        rec = test_canvas.create_rectangle(
            x1, y1, x2, y2 + 35, fill = "#D1FF65", tags = name, width = 2)
        fieldlabel = test_canvas.create_text(
            x1 + 10, y1 + 30, text = "Field(s):", state = tk.DISABLED)
        fieldtext = test_canvas.create_text(
            x1 + 7, y1 + 40, text = "", state = tk.HIDDEN, anchor = tk.N)
        ftop = test_canvas.create_line(
            x1, y1 + 22, x2, y1 + 22, fill = "black", width = 2)
        yincrement = 40
        mtop = test_canvas.create_line(
            x1, y1 + 57, x2, y1 + 57, fill = "black", width = 2)
        methodlabel = test_canvas.create_text(
            x1, y1 + 60, text = "Method(s):", state = tk.DISABLED)
        methodtext = test_canvas.create_text(
            (x1 + (x2 - x1) / 2), y1 + 70, text = "", state = tk.HIDDEN, anchor = tk.N)

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
        self.ftop = ftop
        self.mtop = mtop
        EventHandler.can_drag(rec)

###################################################################################################
'''
Add a box to the canvas, with coordinates being tracked.
'''     
def create_box(name : str):
    yinc = 0

    # Make sure the class does not already exist.
    placed = False
    x_place = 1
    prev_inc = False
    x1 = 60
    x2 = 140
    y1 = 40
    y2 = 65

    # Account for lenthy boxes.
    last_textspace = 0
    if len(class_list) > 0:
        last_textspace = class_list[len(class_list) - 1].textspace
    if(len(name) > 8):
        current_textspace = len(name) * 10
    else:
        current_textspace = len("methods:") * 3.1

    # Find a big enough gap to place the newest class.
    while not placed:
        if x1 - current_textspace < 0:
            x1 = current_textspace + 60
        if len(test_canvas.find_overlapping(
                x1 - current_textspace - 20, y1 - 20, x2 + current_textspace - 20, y2 + 20)
                ) != 0:
            if x2 > maxx - current_textspace - 40:
                y1 += 25
                y2 += 25
                x1 = 60
                x2 = 140
                last_textspace = 0
            else:
                x1 += 1
                x2 += 1
            if x2 > maxx - current_textspace - 40 and y2 > maxy:
                update_global(1000, 1000)
                test_canvas.config(scrollregion = (0, 0, maxx, maxy))
        else:
            placed = True

    # Create the new box.
    obj = UMLsquare(x1, y1, x2, y2, name)
    # Add the new box to the list.
    class_list.append(obj)
    # Bring current box to front.
    ViewChange.bring_all_front(obj)
    # Update the size of the current box.
    update_size(len(class_list) - 1)

def create_box_with_coords(name : str, x1 : int, y1 : int, x2 : int, y2 : int):
    obj = UMLsquare(x1, y1, x2, y2, name)
    class_list.append(obj)
    update_size(len(class_list) - 1)
    UMLField.update_vertical(len(class_list) - 1)

###################################################################################################
'''
Changing existing boxes on the canvas.
'''
# Remove the box with the text = name.
def delete_box(name : str):
    pos = find_pos_from_name(name)

    # Delete everything associated with the box.
    ViewChange.del_item(class_list[pos].rec)
    ViewChange.del_item(class_list[pos].label)
    ViewChange.del_item(class_list[pos].fieldtext)
    ViewChange.del_item(class_list[pos].fieldlabel)
    ViewChange.del_item(class_list[pos].methodlabel)
    ViewChange.del_item(class_list[pos].methodtext)
    ViewChange.del_item(class_list[pos].ftop)
    ViewChange.del_item(class_list[pos].mtop)
    class_list.pop(pos)
    line_mediator()

# Rename a box with the name = oldname.
def rename_box(oldname : str, newname : str):
    # Check for duplicate box names.
    if(find_pos_from_name(newname) == None):
        pos = 0

        # Find the position of the box with the old name.
        for i in class_list:
            if oldname == i.name:
                # Save the box and text values.
                class_list[pos].name = newname
                break
            else:
                pos += 1

        # Change the text of the box to the updated name.
        ViewChange.item_config(class_list[pos].label, newname, None, None, None)

        # Update the width of the box.
        update_size(pos)

###################################################################################################
'''
Updating an existing box's size when new things get added to a class, fitting to the
    size of the text that needs to be displayed.
'''
def update_size(pos : int):
    classname = class_list[pos].name
    longest_name = 3.1 * len(class_list[pos].name)
    i = 0

    # Check class name against field and method labels.
    if(len("Fields:") * 3.1 > longest_name):
        longest_name = len("Fields:") * 3.1
    if(len("Methods:") * 3.1 > longest_name):
        longest_name = len("Methods:") * 3.1
    uml : UMLClass = UMLClass.class_dict[classname]

    # Check all names in the list of fields.
    for fields in uml.fields:
        name = "-" + fields.type + " " + fields.name
        if len(name) * 3.1 > longest_name:
            longest_name = len(name) * 3.1
    uml : UMLClass = UMLClass.class_dict[classname]
    method : ai.UMLMethod
    param : ai.UMLParameter
    newtext = ""

    # Check all info in the list of methods and parameters.
    for method in uml.methods:
        newtext = newtext + "+ " + method.name + " ("
        first_param = True
        for param in method.params:
            if first_param:
                newtext = newtext + param.name + " : " + param.type
                first_param = False
            else:
                newtext = newtext + ", " + param.name + " : " + param.type
        newtext = newtext + ") : " + method.return_type
        if len(newtext) * 2.8 > longest_name:
            longest_name = len(newtext) * 2.8
        newtext = ""
    class_list[pos].textspace = longest_name

    # Find the center and build off of it left and right using the
    #   length of the longest text entry.
    x1, y1, x2, y2 = test_canvas.coords(class_list[pos].rec)
    center = ((x2 - x1) / 2) + x1
    x1 = center - 40 - longest_name
    x2 = center + 40 + longest_name
    if x1 < test_canvas.canvasx(0):
        x1 = test_canvas.canvasx(10)
        x2 = test_canvas.canvasx(10) + 80 + 2 * longest_name

    # Update the box size, and shift label text elements.
    ViewChange.set_rec(class_list[pos].rec, x1, y1, x2, y2)
    ViewChange.set_text(class_list[pos].label, center, y1 + 12)
    ViewChange.set_line(class_list[pos].ftop, x1, y1 + 22, x2, y1 + 22)

    x, y = test_canvas.coords(class_list[pos].fieldlabel)
    ViewChange.set_text(class_list[pos].fieldlabel, x1 + 25, y)

    x, y = test_canvas.coords(class_list[pos].fieldtext)
    ViewChange.set_text(class_list[pos].fieldtext, x1 + 22, y)

    x, y = test_canvas.coords(class_list[pos].methodlabel)
    ViewChange.set_line(class_list[pos].mtop, x1, y - 8, x2, y - 8)
    ViewChange.set_text(class_list[pos].methodlabel, x1 + 35, y)

    x, y = test_canvas.coords(class_list[pos].methodtext)
    ViewChange.set_text(class_list[pos].methodtext, x1 + 20, y)

    return center

###################################################################################################
'''
Functions for getting the coordinates of a specific box, and for using the coords to
    store the object correctly.
'''
def get_coords(name : str):
    pos = find_pos_from_name(name)
    x1, y1, x2, y2 = test_canvas.coords(class_list[pos].rec)
    return (x1, y1, x2, y2)

def get_xy(name : str):
    pos = find_pos_from_name(name)
    x1, y1, x2, y2 = test_canvas.coords(class_list[pos].rec)
    centerx = x1 + (x2-x1)/2
    return (centerx, y1)

###################################################################################################
'''
General function for telling the canvas to update the boxes
'''
def class_mediator():
    # Delete any boxes not found in the class dict (Model).
    for i in class_list:
        if i.name not in UMLClass.class_dict:
            delete_box(i.name)

    # Add any boxes that are in the class dict (Model).
    for name, value in UMLClass.class_dict.items():
        if find_pos_from_name(name) == None:
            # If the class was created in CLI, create its representation
            #   in the first available space.
            if value.position_x == -1 and value.position_y == -1:
                create_box(name)
                x, y = get_xy(name)
                value.position_x = x
                value.position_y = y

            # Otherwise place the box in its correct space.   
            else:
                x1, y1, x2, y2 = UMLSavepoint.make_coords(name, value.position_x, value.position_y)
                create_box_with_coords(name, x1, y1, x2, y2)
            update_methods(name)
            UMLField.update_fields(name)

    size_x = 0
    size_y = 0
    for name, value in UMLClass.class_dict.items():
        if value.position_x > size_x:
            size_x = value.position_x + 1000
        if value.position_y > size_y:
            size_y = value.position_y + 1000

    global maxx
    maxx = size_x
    global maxy
    maxy = size_y
    test_canvas.config(scrollregion=(0,0, maxx, maxy))

###################################################################################################
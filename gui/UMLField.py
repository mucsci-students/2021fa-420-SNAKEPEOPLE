# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     UMLField.py

# External Imports
import tkinter as tk

# Internal Imports
from gui import (
    UMLBox, 
    UMLLine, 
    UMLMethod, 
    ViewChange)
from uml_components.interfaces import attr_interface as ai
from uml_components import UMLClass

###################################################################################################

# Every time the class_dict changes its methods or parameters,
#   change the view to reflect that change.
def update_fields(classname : str):
    pos = UMLBox.find_pos_from_name(classname)
    newtext = new_fieldText(classname)

    # Change the text.
    ViewChange.item_config(UMLBox.class_list[pos].fieldtext, 
        text = newtext, anchor = 'nw', justify = tk.LEFT, state = tk.DISABLED)
    
    # Update horizontal size of box.
    UMLBox.update_size(pos)
    
    # Update vertical size of box.
    update_vertical(pos)

# Create a new block of text conaining the formated parameters.
def new_fieldText(classname : str):
    newtext = ""
    uml : UMLClass = UMLClass.class_dict[classname]

    # Format every field in the form "{type} {name}"
    #   and display each field on a new line.
    for field in uml.fields:
        newtext = newtext + "- " + field.name + ": " + field.type + "\n"
    return newtext

def update_vertical(pos : int):
    UMLBox.class_list[pos].yinc = 40
    classname = UMLBox.class_list[pos].name
    spacer = 0

    # Find an appropriate vertical spacing to contain the field.
    uml : UMLClass = UMLClass.class_dict[classname]
    for fields in uml.fields:
        UMLBox.class_list[pos].yinc += 15
    uml : UMLClass = UMLClass.class_dict[classname]
    method : ai.UMLMethod
    param : ai.UMLParameter

    # Find an appropriate vertical spacing to contain the methods and parameters.
    for method in uml.methods:
        UMLBox.class_list[pos].yinc += 15
    if(len(uml.fields) == 0):
        spacer = 10
    else:
        spacer = 0

    # Box coords.
    x1,y1,x2,y2 = UMLBox.test_canvas.coords(UMLBox.class_list[pos].rec)

    # Field label coords.
    x,y = UMLBox.test_canvas.coords(UMLBox.class_list[pos].fieldlabel)

    # Method text coords.
    xl,yl = UMLBox.test_canvas.coords(UMLBox.class_list[pos].methodtext)

    # Method label coords.
    xm,ym = UMLBox.test_canvas.coords(UMLBox.class_list[pos].methodlabel)
    
    # Move the methodlabel according to the number of the fields.
    ViewChange.set_text(UMLBox.class_list[pos].methodlabel, xm, y + 20 + 15 * len(uml.fields) + spacer)

    # Method label coords.
    xm,ym = UMLBox.test_canvas.coords(UMLBox.class_list[pos].methodlabel)
    ViewChange.set_line(UMLBox.class_list[pos].mtop, x1, ym - 8, x2, ym - 8)

    # Move the method text according to the method label.
    ViewChange.set_text(UMLBox.class_list[pos].methodtext, xl, ym + 10)

    # Move the box.
    ViewChange.set_rec(UMLBox.class_list[pos].rec, x1, y1, x2, y1 + UMLBox.class_list[pos].yinc + 20 + spacer)

    # Fix any missing lines.
    UMLLine.line_mediator()
    ViewChange.bring_all_front(UMLBox.class_list[pos])

###################################################################################################

# WIP function for respacing boxes.
def fix_pos(name : str):
    pos = UMLBox.find_pos_from_name(name)
    classname = UMLBox.class_list[pos].name
    coords = UMLBox.get_coords(classname)
    overlap_list = UMLBox.test_canvas.find_overlapping(coords[0], coords[1], coords[2], coords[3])
    overlap_class = []

    if len(overlap_list) > 0:
        # Find the name of all boxes being covered by the most recently updated box.
        for i in overlap_list:
            for k in UMLBox.class_list:
                if i == k.rec and k.name != classname:
                    overlap_class.append(k.name)

    # Move any boxes below the box most recently changed to an open spot on the canvas.
    for i in overlap_class:
        UMLBox.delete_box(i)
        UMLBox.create_box(i)
        UMLMethod.update_methods(i)
        update_fields(i)

###################################################################################################
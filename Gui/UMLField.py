import tkinter as tk
from gui import UMLBox
from gui import ViewChange
from uml_components.interfaces import (attr_interface as ai,
                                       class_interface as ci,
                                       rel_interface as ri)
from uml_components.UMLClass import UMLClass, class_dict

#Every time the class_dict changes its methods or parameters,
#change the view to reflect that change
def update_fields(classname : str):
    pos = UMLBox.find_pos_from_name(classname)
    newtext = new_fieldText(classname)
    #Change the text
    ViewChange.item_config(UMLBox.class_list[pos].fieldtext, text = newtext, justify = tk.LEFT, state=tk.DISABLED)
    #Update horizontal size of box
    UMLBox.update_size(pos)
    #Update vertical size of box
    update_vertical(pos, classname)

#create a new block of text conaining the formated parameters#
def new_fieldText(classname):
    newtext = ""
    uml : UMLClass = class_dict[classname]
    #format every field in the form "{type} {name}"
    #and display each field on a new line
    for field in uml.fields:
        newtext = newtext + "-" + field.type + " " + field.name + "\n"
    return newtext

def update_vertical(pos, classname):
    UMLBox.class_list[pos].yinc = 30
    spacer = 0
    #Find an appropriate vertical spacing to contain the field
    uml : UMLClass = class_dict[classname]
    for fields in uml.fields:
        UMLBox.class_list[pos].yinc += 15
    uml : UMLClass = class_dict[classname]
    method : ai.UMLMethod
    param : ai.UMLParameter
    #Find an appropriate vertical spacing to contain the methods and parameters
    for method in uml.methods:
        UMLBox.class_list[pos].yinc += 45
        for param in method.params:
            UMLBox.class_list[pos].yinc += 15
    if(len(uml.fields) == 0):
        spacer = 10
    else:
        spacer = 0
    #Update the view
    x1,y1,x2,y2 = UMLBox.test_canvas.coords(UMLBox.class_list[pos].rec)
    x,y = UMLBox.test_canvas.coords(UMLBox.class_list[pos].fieldlabel)
    xm,ym = UMLBox.test_canvas.coords(UMLBox.class_list[pos].methodlabel)
    xl,yl = UMLBox.test_canvas.coords(UMLBox.class_list[pos].methodtext)
    ViewChange.set_text(UMLBox.class_list[pos].methodlabel, xm, y + 10 + 15 * len(uml.fields) + spacer)
    ViewChange.set_text(UMLBox.class_list[pos].methodtext, xl, y + 30 +  15 * len(uml.fields))
    ViewChange.set_rec(UMLBox.class_list[pos].rec, x1, y1, x2, y1 + UMLBox.class_list[pos].yinc + 25 + spacer)
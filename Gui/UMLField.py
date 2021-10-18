import tkinter as tk
from gui import UMLBox
from gui import ViewChange
from uml_components.interfaces import (attr_interface as ai,
                                       class_interface as ci,
                                       rel_interface as ri)
from uml_components.UMLClass import UMLClass, class_dict


def update_fields(classname : str):
    pos = UMLBox.find_pos_from_name(classname)
    newtext = new_fieldText(classname)
    ViewChange.item_config(UMLBox.class_list[pos][5], text = newtext, justify = tk.CENTER, state=tk.DISABLED)
    UMLBox.update_size(pos)
    update_vertical(pos, classname)
    uml : UMLClass = class_dict[classname]

#create a new block of text conaining the formated parameters#
def new_fieldText(classname):
    newtext = ""
    uml : UMLClass = class_dict[classname]
    for field in uml.fields:
        newtext = newtext + "-" + field.type + " " + field.name + "\n"
    return newtext

def update_vertical(pos, classname):
    UMLBox.class_list[pos][6] = 30
    spacer = 0
    #Find an appropriate vertical spacing to contain the methods and parameters#
    uml : UMLClass = class_dict[classname]
    for fields in uml.fields:
        UMLBox.class_list[pos][6] += 15
    uml : UMLClass = class_dict[classname]
    method : ai.UMLMethod
    param : ai.UMLParameter
    for method in uml.methods:
        UMLBox.class_list[pos][6] += 45
        for param in method.params:
            UMLBox.class_list[pos][6] += 15
    if(len(uml.fields) == 0):
        spacer = 10
    else:
        spacer = 0
    #Update the view#
    x1,y1,x2,y2 = UMLBox.test_canvas.coords(UMLBox.class_list[pos][1])
    x,y = UMLBox.test_canvas.coords(UMLBox.class_list[pos][7])
    xm,ym = UMLBox.test_canvas.coords(UMLBox.class_list[pos][8])
    xl,yl = UMLBox.test_canvas.coords(UMLBox.class_list[pos][9])
    ViewChange.set_text(UMLBox.class_list[pos][8], xm, y + 10 + 15 * len(uml.fields) + spacer)
    ViewChange.set_text(UMLBox.class_list[pos][9], xl, y + 20 +  15 * len(uml.fields) + spacer)
    ViewChange.set_rec(UMLBox.class_list[pos][1], x1, y1, x2, y1 + UMLBox.class_list[pos][6] + 25 + spacer)
import tkinter as tk
from gui import UMLBox
from gui import ViewChange
from gui import UMLField
from uml_components.interfaces import (attr_interface as ai,
                                       class_interface as ci,
                                       rel_interface as ri)
from uml_components.UMLClass import UMLClass, class_dict

def update_methods(classname : str):
    pos = UMLBox.find_pos_from_name(classname)
    newtext = block_text(classname)
    ViewChange.item_config(UMLBox.class_list[pos][9], text = newtext, justify = tk.CENTER, state=tk.DISABLED)
    UMLBox.update_size(pos)
    UMLField.update_vertical(pos, classname)
    uml : UMLClass = class_dict[classname]

#create a new block of text that contains the formatted method list#
def block_text(classname):
    newtext = ""
    uml : UMLClass = class_dict[classname]
    method : ai.UMLMethod
    param : ai.UMLParameter
    for method in uml.methods:
        newtext = newtext + method.name + " " + method.return_type + "(\n"
        for param in method.params:
            newtext = newtext + "    -" + param.type + " " + param.name + "\n"
        newtext = newtext + ")\n\n"
    return newtext

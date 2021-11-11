# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     UMLMethod.py

import tkinter as tk
from gui import UMLBox
from gui import ViewChange
from gui import UMLField
from uml_components.interfaces import (attr_interface as ai,
                                       class_interface as ci,
                                       rel_interface as ri)
from uml_components import UMLClass

def update_methods(classname : str):
    pos = UMLBox.find_pos_from_name(classname)
    newtext = block_text(classname)
    #Update the method/parameter text
    ViewChange.item_config(UMLBox.class_list[pos].methodtext, text = newtext, justify = tk.LEFT, state=tk.DISABLED)
    #Update horizontal size of box
    UMLBox.update_size(pos)
    #Update vertical size of box
    UMLField.update_vertical(pos)

#create a new block of text that contains the formatted method list#
def block_text(classname : str):
    newtext = ""
    uml : UMLClass = UMLClass.class_dict[classname]
    method : ai.UMLMethod
    param : ai.UMLParameter
    #Put every method/paramter in the form 
    #{method_name} {method_type} (
    #     -{param_type} {param_name}
    # )
    for method in uml.methods:
        newtext = newtext + method.name + " " + method.return_type + " (\n"
        for param in method.params:
            newtext = newtext + "    -" + param.type + " " + param.name + "\n"
        newtext = newtext + ")\n"
    return newtext

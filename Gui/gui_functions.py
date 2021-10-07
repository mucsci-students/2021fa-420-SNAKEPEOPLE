# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     gui_functions.py

# External Imports
import sys
import os.path
import tkinter as tk
from tkinter import *

# Internal Imports
from uml_components.interfaces import (attr_interface as ai,
                                       class_interface as ci,
                                       rel_interface as ri)
from . import gui_windows as gw
from . import gui_buttons as gb
from . import UMLBox
from . import UMLField
from . import UMLLine
from . import UMLMethod

import snake_uml

###################################################################################################

'''
Functions that are assigned to each button's respective popup window.

Each function executes the back-end commands to fulfill the user's requested action,
and give them feedback on whether it was successful or not.
'''

def b_add_class(name: str, label : tk.Label) -> None: 
    output = ci.add_class(name)
    label.configure(text = output)
    UMLBox.create_box(name)



def b_delete_class(name: str, label : tk.Label) -> None:
    output = ci.delete_class(name)
    label.configure(text = output)
    UMLBox.delete_box(name)


def b_rename_class(old_name: str, 
                   new_name : str, 
                   label : tk.Label) -> None:
    output = ci.rename_class(old_name, new_name)
    label.configure(text = output)
    UMLBox.rename_box(old_name, new_name)


def b_add_method(class_name: str, 
                 method_name : str,
                 method_type : str, 
                 label : tk.Label) -> None:
    output = ai.add_method(class_name, method_name, method_type)
    label.configure(text = output)
    UMLMethod.add_method(class_name, method_name+" "+method_type+"()", [])


def b_delete_method(class_name : str, 
                    method_name : str, 
                    label : tk.Label) -> None:
    output = ai.delete_method(class_name, method_name)
    label.configure(text = output)
    UMLMethod.del_method(class_name, method_name)


def b_rename_method(class_name : str, 
                    old_name : str, 
                    new_name : str, 
                    label : tk.Label) -> None:
    output = ai.rename_method(class_name, old_name, new_name)
    label.configure(text = output)
    UMLMethod.rename_method(class_name, old_name, new_name)

def b_add_field(class_name : str,
                field_name : str,
                field_type : str,
                label : tk.Label) -> None:
    output = ai.add_field(class_name, field_name, field_type)
    label.configure(text = output)
    UMLField.add_field(class_name, field_name + " " + field_type)


def b_delete_field(class_name : str,
                   field_name : str,
                   label : tk.Label) -> None:
    output = ai.delete_field(class_name, field_name)
    label.configure(text = output)
    UMLField.del_field(class_name, field_name)

def b_rename_field(class_name : str,
                   old_name : str,
                   new_name :str,
                   label : tk.Label) -> None:
    output = ai.rename_field(class_name, old_name, new_name)
    label.configure(text = output)
    UMLField.rename_field(class_name, old_name, new_name)


def b_add_relation(class1 : str, 
                   class2 : str, 
                   type : str, 
                   label : tk.Label) -> None:
    output = ri.add_relationship(class1, class2, type)
    label.configure(text = output)
    UMLLine.add_line(class1, class2, type)


def b_delete_relation(class1 : str, 
                      class2 : str, 
                      label : tk.Label) -> None:
    output = ri.delete_relationship(class1, class2)
    label.configure(text = output)
    UMLLine.delete_line(class1, class2)


def b_delete_param(class_name : str, 
                   method_name : str, 
                   param_name : str, 
                   label : tk.Label) -> None:
    output = ai.delete_param(class_name, method_name, param_name)
    label.configure(text = output)
    #UMLMethod.del_params(class_name, method_name, [param_name])


def b_rename_param(class_name : str, 
                   method_name : str, 
                   old_name : str, 
                   new_name : str, 
                   label : tk.Label) -> None:
    output = ai.rename_param(class_name, method_name, old_name, new_name)
    label.configure(text = output)


def b_save_file(file_name : str, label : tk.Label) -> None:
    output = snake_uml.save_classes(file_name)
    label.configure(text = output)


def b_load_file(file_name : str, label : tk.Label) -> None:
    output = snake_uml.load_classes(file_name)
    label.configure(text = output)

###################################################################################################

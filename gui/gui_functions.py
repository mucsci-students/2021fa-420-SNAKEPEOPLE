# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     gui_functions.py

# External Imports
import sys
import os.path
import tkinter as tk
from tkinter import *
from uml_components.UMLClass import UMLClass, class_dict
from uml_components.UMLRelationship import UMLRelationship, relationship_list

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
from . import UMLSavepoint

import snake_uml

###################################################################################################

'''
Functions that are assigned to each button's respective popup window.

Each function executes the back-end commands to fulfill the user's requested action,
and give them feedback on whether it was successful or not.
'''

def b_add_class(name: str, label : tk.Label) -> None: 
    UMLSavepoint.save_point()
    output = ci.add_class(name)
    if(output.split(' ')[0] != "<Added" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.undo_stack.get()
    if(output.split(' ')[0] == "<Added"):
        UMLSavepoint.clear_stack()
        UMLBox.class_adapter()
    label.configure(text = output)


def b_delete_class(name: str, label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ci.delete_class(name)
    if(output.split(' ')[0] != "<Deleted" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output.split(' ')[0] == "<Deleted"):
        UMLSavepoint.clear_stack()
        UMLBox.class_adapter()
    label.configure(text = output)

def b_rename_class(old_name: str, 
                   new_name : str, 
                   label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ci.rename_class(old_name, new_name)
    if(output.split(' ')[0] != "<Renamed" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output.split(' ')[0] == "<Renamed"):
        UMLSavepoint.clear_stack()
    label.configure(text = output)
    UMLBox.rename_box(old_name, new_name)


def b_add_method(class_name: str, 
                 method_name : str,
                 method_type : str, 
                 label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ai.add_method(class_name, method_name, method_type)
    if(output.split(' ')[0] != "Successfully" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output.split(' ')[0] == "Successfully"):
        UMLSavepoint.clear_stack()
    label.configure(text = output)
    UMLMethod.update_methods(class_name)


def b_delete_method(class_name : str, 
                    method_name : str, 
                    label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ai.delete_method(class_name, method_name)
    if(output.split(' ')[0] != "Successfully" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output.split(' ')[0] == "Successfully"):
        UMLSavepoint.clear_stack()
    label.configure(text = output)
    UMLMethod.update_methods(class_name)


def b_rename_method(class_name : str, 
                    old_name : str, 
                    new_name : str, 
                    label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ai.rename_method(class_name, old_name, new_name)
    if(output.split(' ')[0] != "Successfully" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output.split(' ')[0] == "Successfully"):
        UMLSavepoint.clear_stack()
    label.configure(text = output)
    UMLMethod.update_methods(class_name)


def b_add_field(class_name : str,
                field_name : str,
                field_type : str,
                label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ai.add_field(class_name, field_name, field_type)
    if(output.split(' ')[0] != "Successfully" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output.split(' ')[0] == "Successfully"):
        UMLSavepoint.clear_stack()
    label.configure(text = output)
    UMLField.update_fields(class_name)


def b_delete_field(class_name : str,
                   field_name : str,
                   label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ai.delete_field(class_name, field_name)
    if(output.split(' ')[0] != "Successfully" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output.split(' ')[0] == "Successfully"):
        UMLSavepoint.clear_stack()
    label.configure(text = output)
    UMLField.update_fields(class_name)


def b_rename_field(class_name : str,
                   old_name : str,
                   new_name :str,
                   label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ai.rename_field(class_name, old_name, new_name)
    if(output.split(' ')[0] != "Successfully" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output.split(' ')[0] == "Successfully"):
        UMLSavepoint.clear_stack()
    label.configure(text = output)
    UMLField.update_fields(class_name)


def b_add_relation(class1 : str, 
                   class2 : str, 
                   type : str, 
                   label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ri.add_relationship(class1, class2, type)
    if(output.split(' ')[0] == "<Added"):
        UMLLine.line_adapter()
        UMLSavepoint.clear_stack()
    if(output.split(' ')[0] != "<Added"  and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    label.configure(text = output)


def b_delete_relation(class1 : str, 
                      class2 : str, 
                      label : tk.Label) -> None:
    exists = ri.find_rel(class1, class2)[0]
    if exists:
        UMLSavepoint.save_point()
    output = ri.delete_relationship(class1, class2)
    if(output.split(' ')[0] != "<Deleted" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output.split(' ')[0] == "<Deleted"):
        UMLLine.line_adapter()
        UMLSavepoint.clear_stack()
    label.configure(text = output)


def b_add_param(class_name : str,
                method_name : str,
                param_name : str,
                param_type : str,
                label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ai.add_param(class_name, method_name, param_name, param_type)
    if(output.split(' ')[0] != "Successfuly" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output.split(' ')[0] == "Successfully"):
        UMLSavepoint.clear_stack()
    label.configure(text = output)
    UMLMethod.update_methods(class_name)


def b_delete_param(class_name : str, 
                   method_name : str, 
                   param_name : str, 
                   label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ai.delete_param(class_name, method_name, param_name)
    if(output.split(' ')[0] != "Successfuly" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output.split(' ')[0] == "Successfully"):
        UMLSavepoint.clear_stack()
    label.configure(text = output)
    UMLMethod.update_methods(class_name)


def b_rename_param(class_name : str, 
                   method_name : str, 
                   old_name : str, 
                   new_name : str, 
                   label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ai.rename_param(class_name, method_name, old_name, new_name)
    if(output.split(' ')[0] != "Successfuly" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output.split(' ')[0] == "Successfully"):
        UMLSavepoint.clear_stack()
    label.configure(text = output)
    UMLMethod.update_methods(class_name)


def b_save_file(file_name : str, label : tk.Label) -> None:
    output = snake_uml.save_classes(file_name)
    label.configure(text = output)


def b_load_file(file_name : str, label : tk.Label) -> None:
    output = snake_uml.load_classes(file_name)
    label.configure(text = output)
    UMLBox.class_adapter()
    UMLLine.line_adapter()

def b_undo() -> None:
    if UMLSavepoint.undo_stack.empty() == False:
        UMLSavepoint.undo()

def b_redo() -> None:
    if UMLSavepoint.redo_stack.empty() == False:
        UMLSavepoint.redo()


###################################################################################################

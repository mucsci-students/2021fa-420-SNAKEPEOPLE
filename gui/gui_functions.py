# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     gui_functions.py

# External Imports
import tkinter as tk
import queue

# Internal Imports
from uml_components.interfaces import (
    attr_interface as ai, 
    class_interface as ci, 
    rel_interface as ri)
from . import UMLBox
from . import UMLField
from . import UMLLine
from . import UMLMethod
from . import UMLSavepoint
from . import ImageAdapter

import snake_uml

###################################################################################################
'''
Functions that are assigned to each button's respective popup window.

Each function executes the back-end commands to fulfill the user's requested action,
and give them feedback on whether it was successful or not.
'''

def b_add_class(
        name: str, 
        label : tk.Label) -> None: 
    UMLSavepoint.save_point()
    output = ci.add_class(name)
    if(output[1].split(' ')[0] != "<Added" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.undo_stack.get()
    if(output[1].split(' ')[0] == "<Added"):
        UMLSavepoint.clear_stack()
        UMLBox.class_mediator()
    label.configure(text = output[1])


def b_delete_class(
        name: str, 
        label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ci.delete_class(name)
    if(output[1].split(' ')[0] != "<Deleted" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output[1].split(' ')[0] == "<Deleted"):
        UMLSavepoint.clear_stack()
        UMLBox.class_mediator()
    label.configure(text = output[1])


def b_rename_class(
        old_name: str, 
        new_name : str, 
        label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ci.rename_class(old_name, new_name)
    if(output[1].split(' ')[0] != "<Renamed" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output[1].split(' ')[0] == "<Renamed"):
        UMLSavepoint.clear_stack()
    label.configure(text = output[1])
    UMLBox.rename_box(old_name, new_name)


def b_add_method(
        class_name: str, 
        method_name : str, 
        method_type : str, 
        label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ai.add_method(class_name, method_name, method_type)
    if(output[1].split(' ')[0] != "Successfully" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output[1].split(' ')[0] == "Successfully"):
        UMLSavepoint.clear_stack()
    label.configure(text = output[1])
    UMLMethod.update_methods(class_name)


def b_delete_method(
        class_name : str, 
        method_name : str, 
        method_type : str, 
        label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ai.delete_method(class_name, method_name, method_type)
    if(output[1].split(' ')[0] != "Successfully" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output[1].split(' ')[0] == "Successfully"):
        UMLSavepoint.clear_stack()
    label.configure(text = output[1])
    UMLMethod.update_methods(class_name)


def b_rename_method(
        class_name : str, 
        old_name : str, 
        new_name : str, 
        method_type : str, 
        label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ai.rename_method(class_name, old_name, method_type, new_name)
    if(output[1].split(' ')[0] != "Successfully" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output[1].split(' ')[0] == "Successfully"):
        UMLSavepoint.clear_stack()
    label.configure(text = output[1])
    UMLMethod.update_methods(class_name)


def b_add_field(
        class_name : str, 
        field_name : str, 
        field_type : str, 
        label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ai.add_field(class_name, field_name, field_type)
    if(output[1].split(' ')[0] != "Successfully" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output[1].split(' ')[0] == "Successfully"):
        UMLSavepoint.clear_stack()
    label.configure(text = output[1])
    UMLField.update_fields(class_name)


def b_delete_field(
        class_name : str, 
        field_name : str, 
        label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ai.delete_field(class_name, field_name)
    if(output[1].split(' ')[0] != "Successfully" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output[1].split(' ')[0] == "Successfully"):
        UMLSavepoint.clear_stack()
    label.configure(text = output[1])
    UMLField.update_fields(class_name)


def b_rename_field(
        class_name : str, 
        old_name : str, 
        new_name :str, 
        label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ai.rename_field(class_name, old_name, new_name)
    if(output[1].split(' ')[0] != "Successfully" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output[1].split(' ')[0] == "Successfully"):
        UMLSavepoint.clear_stack()
    label.configure(text = output[1])
    UMLField.update_fields(class_name)


def b_add_relation(
        class1 : str, 
        class2 : str, 
        type : str, 
        label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ri.add_relationship(class1, class2, type)
    print(output)
    if(output[1].split(' ')[0] == "<Added"):
        UMLLine.line_mediator()
        UMLSavepoint.clear_stack()
    if(output[1].split(' ')[0] != "<Added" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    label.configure(text = output[1])


def b_delete_relation(
        class1 : str, 
        class2 : str, 
        label : tk.Label) -> None:
    exists = ri.find_rel(class1, class2)[0]
    if exists:
        UMLSavepoint.save_point()
    output = ri.delete_relationship(class1, class2)
    if(output[1].split(' ')[0] != "<Deleted" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output[1].split(' ')[0] == "<Deleted"):
        UMLLine.line_mediator()
        UMLSavepoint.clear_stack()
    label.configure(text = output[1])


def b_add_param(
        class_name : str, 
        method_name : str, 
        method_type : str, 
        param_name : str, 
        param_type : str, 
        label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ai.add_param(class_name, method_name, method_type, param_name, param_type)
    if(output[1].split(' ')[0] != "Successfuly" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output[1].split(' ')[0] == "Successfully"):
        UMLSavepoint.clear_stack()
    label.configure(text = output[1])
    UMLMethod.update_methods(class_name)


def b_delete_param(
        class_name : str, 
        method_name : str, 
        method_type : str, 
        param_name : str, 
        label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ai.delete_param(class_name, method_name, method_type, param_name)
    if(output[1].split(' ')[0] != "Successfuly" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output[1].split(' ')[0] == "Successfully"):
        UMLSavepoint.clear_stack()
    label.configure(text = output[1])
    UMLMethod.update_methods(class_name)


def b_rename_param(
        class_name : str, 
        method_name : str, 
        method_type : str, 
        old_name : str, 
        new_name : str, 
        label : tk.Label) -> None:
    UMLSavepoint.save_point()
    output = ai.rename_param(class_name, method_name, method_type, old_name, new_name)
    if(output[1].split(' ')[0] != "Successfuly" and UMLSavepoint.redo_stack.empty() == False):
        UMLSavepoint.redo_stack.get()
    if(output[1].split(' ')[0] == "Successfully"):
        UMLSavepoint.clear_stack()
    label.configure(text = output[1])
    UMLMethod.update_methods(class_name)


def b_save_file(
        file_name : str, 
        label : tk.Label) -> None:
    output = snake_uml.save(file_name)
    label.configure(text = output[1])


def b_load_file(
        file_name : str, 
        label : tk.Label) -> None:
    output = snake_uml.load(file_name)
    label.configure(text = output)
    UMLBox.test_canvas.delete("all")
    UMLBox.class_list = []
    UMLBox.class_mediator()
    UMLLine.line_mediator()
    if UMLSavepoint.undo_stack.empty() == False:
        UMLSavepoint.undo_stack = queue.LifoQueue()
    if UMLSavepoint.redo_stack.empty() == False:
        UMLSavepoint.clear_stack()

def b_export(
        file_name : str,
        label : tk.Label) -> None:
    output = ImageAdapter.save_as_png(file_name)
    label.configure(text = output)

def b_undo() -> None:
    if UMLSavepoint.undo_stack.empty() == False:
        UMLSavepoint.undo()


def b_redo() -> None:
    if UMLSavepoint.redo_stack.empty() == False:
        UMLSavepoint.redo()

###################################################################################################
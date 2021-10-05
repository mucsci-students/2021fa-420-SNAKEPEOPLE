# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     gui_buttons.py


# File containing the functionality for the buttons in the GUI.


# External Imports
import sys
import os.path
import tkinter as tk
from tkinter import *
#import UMLbox

# Internal Imports
from uml_components import (UMLClass, 
                            UMLRelationship,
                            UMLAttributes)
from uml_components.interfaces import (attr_interface as ai,
                                       class_interface as ci,
                                       rel_interface as ri)
from Gui import (EventHandler,
                 UMLbox,
                 UMLfield,
                 UMLline,
                 UMLMethod,
                 ViewChange)
import gui_application as ga

###################################################################################################

def b_add_class(input: str, label : tk.Label) -> None:
    output = ci.add_class(input)
    label.configure(text = output)


def b_delete_class(input: str, label : tk.Label):
    output = ci.delete_class(input)
    label.configure(text = output)


def b_rename_class(input1: str, input2 : str, label : tk.Label):
    output = ci.rename_class(input1, input2)
    label.configure(text = output)


def b_add_method(input1: str, input2 : str, label : tk.Label):
    name = UMLClass.class_dict[input1]
    find_pos_from_name(input1)


def b_delete_method():
    pass


def b_rename_method():
    pass


def b_add_field():
    pass


def b_delete_field():
    pass


def b_rename_field():
    pass


def b_add_relation():
    pass


def b_delete_relation():
    pass


def save_file():
    pass


def load_file():
    pass

###################################################################################################

# Function to make the frame with all the right-side buttons for the GUI.
def make_buttons() -> tk.Frame:
    '''
    Function to make the buttons on the right side of the GUI:
        [Add       Class]  [Delete    Class]  [Rename    Class]
        [Add      Method]  [Delete   Method]  [Rename   Method]
        [Add       Field]  [Delete    Field]  [Rename    Field]
        [Add    Relation]  [Delete Relation] 
        [Save       File]  [Load       File]  [     Help      ]

    '''

    # Make a new frame for the buttons.
    button_frame = tk.Frame(relief = tk.FLAT, borderwidth = 5)

    '''
    Row 1:

    [Add       Class]  [Delete    Class]  [Rename    Class]
    '''
    # Add Class Button
    add_class_button = tk.Button(
        command = ga.add_class_window,
        master = button_frame, 
        text = "Add Class", 
        width = 14, 
        font = ('bold'))
    add_class_button.grid(
        row = 0, 
        column = 0, 
        sticky = "nw",
        padx = 5,
        pady = 5)

    # Delete Class Button
    delete_class_button = tk.Button(
        command = ga.delete_class_window,
        master = button_frame, 
        text = "Delete Class", 
        width = 14, 
        font = ('bold'))
    delete_class_button.grid(
        row = 0, 
        column = 1, 
        sticky = "n",
        padx = 5,
        pady = 5)
    
    # Rename Class Button
    rename_class_button = tk.Button(
        command = ga.rename_class_window,
        master = button_frame, 
        text = "Rename Class", 
        width = 14, 
        font = ('bold'))
    rename_class_button.grid(
        row = 0, 
        column = 2, 
        sticky = "ne",
        padx = 5,
        pady = 5)

    '''
    Row 2:

    [Add      Method]  [Delete   Method]  [Rename   Method]
    '''
    # Add Method Button
    add_method_button = tk.Button(
        command = ga.add_method_window,
        master = button_frame, 
        text = "Add Method", 
        width = 14, 
        font = ('bold'))
    add_method_button.grid(
        row = 1, 
        column = 0, 
        sticky = "nw",
        padx = 5,
        pady = 5)

    # Delete Method Button
    delete_method_button = tk.Button(
        command = ga.delete_method_window,
        master = button_frame, 
        text = "Delete Method", 
        width = 14, 
        font = ('bold'))
    delete_method_button.grid(
        row = 1, 
        column = 1,
        padx = 5,
        pady = 5)
    
    # Rename Method Button
    rename_method_button = tk.Button(
        command = ga.rename_method_window,
        master = button_frame, 
        text = "Rename Method", 
        width = 14, 
        font = ('bold'))
    rename_method_button.grid(
        row = 1, 
        column = 2, 
        sticky = "ne",
        padx = 5,
        pady = 5)

    '''
    Row 3:

    [Add       Field]  [Delete    Field]  [Rename    Field]
    '''
    # Add Field Button
    add_field_button = tk.Button(
        command = ga.add_field_window,
        master = button_frame, 
        text = "Add Field", 
        width = 14, 
        font = ('bold'))
    add_field_button.grid(
        row = 2, 
        column = 0, 
        sticky = "nw",
        padx = 5,
        pady = 5)

    # Delete Field Button
    delete_field_button = tk.Button(
        command = ga.delete_field_window,
        master = button_frame, 
        text = "Delete Field", 
        width = 14, 
        font = ('bold'))
    delete_field_button.grid(
        row = 2, 
        column = 1,
        padx = 5,
        pady = 5)
    
    # Rename Method Button
    rename_field_button = tk.Button(
        command = ga.rename_field_window,
        master = button_frame, 
        text = "Rename Field", 
        width = 14, 
        font = ('bold'))
    rename_field_button.grid(
        row = 2, 
        column = 2, 
        sticky = "ne",
        padx = 5,
        pady = 5)

    '''
    Row 4:

    [Add    Relation]  [Delete Relation]  
    '''
    # Add Relationship Button
    add_rel_button = tk.Button(
        command = ga.add_relation_window,
        master = button_frame, 
        text = "Add Relation", 
        width = 14, 
        font = ('bold'))
    add_rel_button.grid(
        row = 3, 
        column = 0, 
        sticky = "nw",
        padx = 5,
        pady = 5)

    # Delete Relationship Button
    delete_rel_button = tk.Button(
        command = ga.delete_relation_window,
        master = button_frame, 
        text = "Delete Relation", 
        width = 14, 
        font = ('bold'))
    delete_rel_button.grid(
        row = 3, 
        column = 1,
        padx = 5,
        pady = 5)
    
    '''
    Row 5:

    [Save       File]  [Load       File]  [     Help      ]
    '''
    # Save Button
    save_button = tk.Button(
        command = ga.save_window,
        master = button_frame, 
        text = "Save File", 
        width = 14, 
        font = ('bold'))
    save_button.grid(
        row = 4, 
        column = 0, 
        sticky = "nw",
        padx = 5,
        pady = 5)

    # Load Button
    load_button = tk.Button(
        command = ga.load_window,
        master = button_frame, 
        text = "Load File", 
        width = 14, 
        font = ('bold'))
    load_button.grid(
        row = 4, 
        column = 1,
        padx = 5,
        pady = 5)

    # Help Button
    help_button = tk.Button(
        command = ga.help_window,
        master = button_frame,
        text = "Help",
        width = 14, 
        font = ('bold'))
    help_button.grid(
        row = 4,
        column = 2,
        padx = 5,
        pady = 5)

    return button_frame

###################################################################################################

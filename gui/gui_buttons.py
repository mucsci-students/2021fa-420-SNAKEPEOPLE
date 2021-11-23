# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     gui_buttons.py

# External Imports
import tkinter as tk

# Internal Imports
from . import gui_windows as gw

###################################################################################################
'''
Functions for use in the Side_Panel file. Used to make the buttons on each panel.
'''

def set_class_buttons(frame : tk.Frame) -> None:
    # Add Class Button
    add_button = tk.Button(
        master = frame,
        command = gw.add_class_window,
        text = "Add Class", 
        width = 20)
    add_button.grid(
        row = 0,
        column = 0,
        sticky = "n")

    # Delete Class Button
    delete_button = tk.Button(
        master = frame,
        command = gw.delete_class_window,
        text = "Delete Class", 
        width = 20)
    delete_button.grid(
        row = 0,
        column = 1,
        sticky = "n")

    # Rename Class Button
    rename_button = tk.Button(
        master = frame,
        command = gw.rename_class_window,
        text = "Rename Class", 
        width = 20)
    rename_button.grid(
        row = 0,
        column = 2,
        sticky = "n")
    
    # Blank space under the class buttons to make the panel look better.
    blank = tk.Label(master = frame)
    blank.grid(row = 1, column = 0, sticky = "w", columnspan = 10)


def set_method_buttons(frame : tk.Frame) -> None:
    # Add Method Button
    add_button = tk.Button(
        master = frame,
        command = gw.add_method_window,
        text = "Add Method", 
        width = 20)
    add_button.grid(
        row = 0,
        column = 0,
        sticky = "n")

    # Delete Method Button
    delete_button = tk.Button(
        master = frame,
        command = gw.delete_method_window,
        text = "Delete Method", 
        width = 20)
    delete_button.grid(
        row = 0,
        column = 1,
        sticky = "n")

    # Rename Method Button
    rename_button = tk.Button(
        master = frame,
        command = gw.rename_method_window,
        text = "Rename Method", 
        width = 20)
    rename_button.grid(
        row = 0,
        column = 2,
        sticky = "n")


def set_field_buttons(frame : tk.Frame) -> None:
    # Add Field Button
    add_button = tk.Button(
        master = frame,
        command = gw.add_field_window,
        text = "Add Field", 
        width = 20)
    add_button.grid(
        row = 0,
        column = 0,
        sticky = "n")

    # Delete Field Button
    delete_button = tk.Button(
        master = frame,
        command = gw.delete_field_window,
        text = "Delete Field", 
        width = 20)
    delete_button.grid(
        row = 0,
        column = 1,
        sticky = "n")

    # Rename Field Button
    rename_button = tk.Button(
        master = frame,
        command = gw.rename_field_window,
        text = "Rename Field", 
        width = 20)
    rename_button.grid(
        row = 0,
        column = 2,
        sticky = "n")


def set_param_buttons(frame : tk.Frame) -> None:
    # Add Param Button
    add_button = tk.Button(
        master = frame,
        command = gw.add_param_window,
        text = "Add Param", 
        width = 20)
    add_button.grid(
        row = 0,
        column = 0,
        sticky = "n")

    # Delete Param Button
    delete_button = tk.Button(
        master = frame,
        command = gw.delete_param_window,
        text = "Delete Param", 
        width = 20)
    delete_button.grid(
        row = 0,
        column = 1,
        sticky = "n")

    # Rename Param Button
    rename_button = tk.Button(
        master = frame,
        command = gw.rename_param_window,
        text = "Rename Param", 
        width = 20)
    rename_button.grid(
        row = 0,
        column = 2,
        sticky = "n")


def set_rel_buttons(frame : tk.Frame) -> None:
    # Add Relation Button
    add_button = tk.Button(
        master = frame,
        command = gw.add_relation_window,
        text = "Add Relation", 
        width = 20)
    add_button.grid(
        row = 0,
        column = 0,
        sticky = "n")

    # Delete Relation Button
    delete_button = tk.Button(
        master = frame,
        command = gw.delete_relation_window,
        text = "Delete Relation", 
        width = 20)
    delete_button.grid(
        row = 0,
        column = 1,
        sticky = "n")

###################################################################################################
'''
# Function to make the frame with all the right-side buttons for the GUI.
'''

def make_buttons(frame : tk.Frame) -> list:
    '''
    Function to make the buttons on the right side of the GUI:
        [Add       Class]  [Delete    Class]  [Rename    Class]
        [Add      Method]  [Delete   Method]  [Rename   Method]
        [Add       Field]  [Delete    Field]  [Rename    Field]
        [Add       Param]  [Delete    Param]  [Rename    Param]
        [Add    Relation]  [Delete Relation]
        [Save       File]  [Load       File]

    '''

    # Make a list of buttons to be returned
    buttons = []

    # Add Class Button
    add_class_button = tk.Button(frame,
        command = gw.add_class_window,
        text = "Add Class", 
        width = 20)
    buttons.append(add_class_button)


    # Delete Class Button
    delete_class_button = tk.Button(frame,
        command = gw.delete_class_window,
        text = "Delete Class", 
        width = 20)
    buttons.append(delete_class_button)
    

    # Rename Class Button
    rename_class_button = tk.Button(frame,
        command = gw.rename_class_window,
        text = "Rename Class", 
        width = 20)
    buttons.append(rename_class_button)


    # Add Method Button
    add_method_button = tk.Button(frame,
        command = gw.add_method_window,
        text = "Add Method", 
        width = 20)
    buttons.append(add_method_button)


    # Delete Method Button
    delete_method_button = tk.Button(frame,
        command = gw.delete_method_window,
        text = "Delete Method", 
        width = 20)
    buttons.append(delete_method_button)
    

    # Rename Method Button
    rename_method_button = tk.Button(frame,
        command = gw.rename_method_window,
        text = "Rename Method", 
        width = 20)
    buttons.append(rename_method_button)


    # Add Field Button
    add_field_button = tk.Button(frame,
        command = gw.add_field_window,
        text = "Add Field", 
        width = 20)
    buttons.append(add_field_button)


    # Delete Field Button
    delete_field_button = tk.Button(frame,
        command = gw.delete_field_window,
        text = "Delete Field", 
        width = 20)
    buttons.append(delete_field_button)
    

    # Rename Field Button
    rename_field_button = tk.Button(frame,
        command = gw.rename_field_window,
        text = "Rename Field", 
        width = 20)
    buttons.append(rename_field_button)


    # Add Parameter Button
    add_param_button = tk.Button(frame,
        command = gw.add_param_window,
        text = "Add Param",
        width = 20)
    buttons.append(add_param_button)


    # Delete Parameter Button
    delete_param_button = tk.Button(frame,
        command = gw.delete_param_window,
        text = "Delete Param",
        width = 20)
    buttons.append(delete_param_button)
    

    # Rename Parameter Button
    rename_param_button = tk.Button(frame,
        command = gw.rename_param_window,
        text = "Rename Param",
        width = 20)
    buttons.append(rename_param_button)


    # Add Relationship Button
    add_rel_button = tk.Button(frame,
        command = gw.add_relation_window,
        text = "Add Relation", 
        width = 20)
    buttons.append(add_rel_button)


    # Delete Relationship Button
    delete_rel_button = tk.Button(frame,
        command = gw.delete_relation_window,
        text = "Delete Relation", 
        width = 20)
    buttons.append(delete_rel_button)
    

    # Save Button
    # save_button = tk.Button(
    #     command = gw.save_window,
    #     text = "Save File", 
    #     width = 20)
    # buttons.append(save_button)


    # Load Button
    # load_button = tk.Button(
    #     command = gw.load_window,
    #     text = "Load File", 
    #     width = 20)
    # buttons.append(load_button)


    return buttons

###################################################################################################
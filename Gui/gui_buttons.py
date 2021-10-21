# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     gui_buttons.py

# External Imports
import sys
import os.path
import tkinter as tk
from tkinter import *
from tkinter.tix import *
#import UMLbox

# Internal Imports
from . import gui_windows as gw
from . import gui_functions as gf

###################################################################################################

def make_panel() -> Frame:
    # Main frame to be put in the GUI
    panel = Frame(
        relief = SUNKEN,
        borderwidth = 3)

    frames = {}

    class_frame = Frame(
        master = panel,
        relief = SUNKEN,
        borderwidth = 3)
    frames["Class"] = class_frame

    method_frame = Frame(
        master = panel,
        relief = SUNKEN,
        borderwidth = 3)
    frames["Method"] = method_frame

    field_frame = Frame(
        master = panel,
        relief = SUNKEN,
        borderwidth = 3)
    frames["Field"] = field_frame

    param_frame = Frame(
        master = panel,
        relief = SUNKEN,
        borderwidth = 3)
    frames["Param"] = param_frame

    relation_frame = Frame(
        master = panel,
        relief = SUNKEN,
        borderwidth = 3)
    frames["Relation"] = relation_frame

    set_add_buttons(frames)


    '''
    Making the main buttons for the top of the panel, in which you can select
    which frame to view.
        [C]  [M]  [F]  [P]  [R]
    '''
    btn1 = Button(
        master = panel,
        command = lambda: class_frame.grid(),
        text = "C",
        height = 1,
        width = 3, 
        font = ('bold'))
    btn1.grid(
        row = 0,
        column = 0,
        sticky = "n")

    btn2 = Button(
        master = panel,
        text = "M",
        height = 1,
        width = 3, 
        font = ('bold'))
    btn2.grid(
        row = 0,
        column = 1,
        sticky = "n")

    btn3 = Button(
        master = panel,
        text = "F",
        height = 1,
        width = 3, 
        font = ('bold'))
    btn3.grid(
        row = 0,
        column = 2,
        sticky = "n")

    btn4 = Button(
        master = panel,
        text = "P",
        height = 1,
        width = 3, 
        font = ('bold'))
    btn4.grid(
        row = 0,
        column = 3,
        sticky = "n")

    btn5 = Button(
        master = panel,
        text = "R",
        height = 1,
        width = 3, 
        font = ('bold'))
    btn5.grid(
        row = 0,
        column = 4,
        sticky = "n")

    return panel

###################################################################################################

def grid_class() -> None:
    pass


###################################################################################################

def set_add_buttons(frames : dict[str, Frame]) -> None:
    # Add Class Button
    add_class_button = tk.Button(frames["Class"],
        command = gw.add_class_window,
        text = "Add Class", 
        width = 20)
    add_class_button.grid(
        row = 0,
        column = 0,
        sticky = "n")

    # Delete Class Button
    delete_class_button = tk.Button(frames["Class"],
        command = gw.delete_class_window,
        text = "Delete Class", 
        width = 20)
    delete_class_button.grid(
        row = 1,
        column = 0,
        sticky = "n")

    # Rename Class Button
    rename_class_button = tk.Button(frames["Class"],
        command = gw.rename_class_window,
        text = "Rename Class", 
        width = 20)
    rename_class_button.grid(
        row = 2,
        column = 0,
        sticky = "n")

###################################################################################################

'''
Create the frames to be used in the right-side panels of the GUI.

Frames can be accessed by one of the following keys:
    Class, Method, Field, Param, Relation
'''
def make_frames() -> dict[str, Frame]:
    frames = {}

    class_frame = Frame(
        relief = SUNKEN,
        borderwidth = 3)
    frames["Class"] = class_frame

    method_frame = Frame(
        relief = SUNKEN,
        borderwidth = 3)
    frames["Method"] = method_frame

    field_frame = Frame(
        relief = SUNKEN,
        borderwidth = 3)
    frames["Field"] = field_frame

    param_frame = Frame(
        relief = SUNKEN,
        borderwidth = 3)
    frames["Param"] = param_frame

    relation_frame = Frame(
        relief = SUNKEN,
        borderwidth = 3)
    frames["Relation"] = relation_frame

    set_add_buttons(frames)

    return frames

###################################################################################################

# Function to make the frame with all the right-side buttons for the GUI.
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

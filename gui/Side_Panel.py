# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     Side_Panel.py

# External Imports
import sys
import os.path
import tkinter as tk
from tkinter import *
from tkinter.tix import *
from tkinter import ttk

# Internal Imports
from . import gui_buttons as gb

###################################################################################################
'''
Main function for creating the sidebar of the GUI with all the panels.

Creates the frames for each panel and puts them under the appropriate spot.

Repurposes the functions in the gui_windows file in order to
    populate each panel.
'''
def init_notebook(frame : Frame) -> ttk.Notebook:
    # Making the contents of the Main Panel
    # [Class]  [Relation]
    panel = ttk.Notebook(frame)

    class_frame = Frame(master = panel, borderwidth = 3)
    panel.add(class_frame, text = "Class")
    panel.insert(0, class_frame)

    relation_frame = Frame(master = panel, borderwidth = 3)
    panel.add(relation_frame, text = "Relation")
    panel.insert(1, relation_frame)


    # Making the contents of the Relation Panel
    # [Add]  [Delete]
    relation_panel = ttk.Notebook(master = relation_frame)

    gb.set_rel_buttons(relation_frame)

    relation_panel.grid(row = 2, column = 0, sticky = "w", columnspan = 10)


    # Making the contents of the Class Panel
    # [Add]  [Delete]  [Rename]
    # [Method]  [Field]  [Param]
    class_panel = ttk.Notebook(master = class_frame)

    gb.set_class_buttons(class_frame)

    method_frame = Frame(master = class_panel, borderwidth = 3)
    class_panel.add(method_frame, text = "Method")
    class_panel.insert(0, method_frame)
    gb.set_method_buttons(method_frame)

    field_frame = Frame(master = class_panel, borderwidth = 3)
    class_panel.add(field_frame, text = "Field")
    class_panel.insert(1, field_frame)
    gb.set_field_buttons(field_frame)

    param_frame = Frame(master = class_panel, borderwidth = 3)
    class_panel.add(param_frame, text = "Param")
    class_panel.insert(2, param_frame)
    gb.set_param_buttons(param_frame)

    class_panel.grid(row = 3, column = 0, sticky = "w", columnspan = 10)


    return panel

###################################################################################################

if __name__ == "__main__":
    root = Tk()
    frame = Frame(root)
    panel = init_notebook(frame)
    panel.pack()
    frame.pack()
    root.mainloop()
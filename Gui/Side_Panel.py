# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     Side_Panel.py

# External Imports
import sys
import os.path
import tkinter as tk
from tkinter import *
from tkinter.tix import *
from tkinter import ttk
#import UMLbox

# Internal Imports
#import gui_windows
#from . import gui_functions as gf




def init_notebook(frame : Frame) -> ttk.Notebook:
    # Main Panel
    # [Class]  [Relation]
    panel = ttk.Notebook(frame)
    class_frame = Frame(master = panel, borderwidth = 3)
    relation_frame = Frame(master = panel, borderwidth = 3)

    # Making the contents of the Main Panel
    class_panel1 = ttk.Notebook(master = class_frame)
    class_panel2 = ttk.Notebook(master = class_frame)
    method_frame = Frame(master = class_panel2, borderwidth = 3)
    field_frame = Frame(master = class_panel2, borderwidth = 3)
    
    # Making the contents of the upper Class Panel
    add_frame = Frame(master = class_panel1, borderwidth = 3)
    delete_frame = Frame(master = class_panel1, borderwidth = 3)
    rename_frame = Frame(master = class_panel1, borderwidth = 3)

    # Making the contents of the lower Class Panel
    na_frame = Frame(master = class_panel2, borderwidth = 3)
    method_frame = Frame(master = class_panel2, borderwidth = 3)
    field_frame = Frame(master = class_panel2, borderwidth = 3)
    
    # Adding the tabs to the upper Class Panel
    class_panel1.add(add_frame, text = "Add Class")
    class_panel1.insert(0, add_frame)
    class_panel1.add(delete_frame, text = "Delete Class")
    class_panel1.insert(1, delete_frame)
    class_panel1.add(rename_frame, text = "Rename Class")
    class_panel1.insert(2, rename_frame)
    class_panel1.grid(row = 0, column = 0, sticky = "w")

    # Adding the tabs to the lower Class Panel
    class_panel2.add(na_frame, text = "N/A")
    class_panel2.insert(0, na_frame)
    class_panel2.add(method_frame, text = "Method")
    class_panel2.insert(1, method_frame)
    class_panel2.add(field_frame, text = "Field")
    class_panel2.insert(2, field_frame)
    class_panel2.grid(row = 2, column = 0, sticky = "w")

    # Adding the tabs to the Main Panel
    panel.add(class_frame, text = "Class")
    panel.insert(0, class_frame)
    panel.add(relation_frame, text = "Relation")
    panel.insert(1, relation_frame)

    return panel

if __name__ == "__main__":
    root = Tk()
    frame = Frame(root)
    panel = init_notebook(frame)
    panel.pack()
    frame.pack()
    root.mainloop()
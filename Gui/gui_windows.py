# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     gui_windows.py

# External Imports
import sys
import os.path
import tkinter as tk
from tkinter import *

# Internal Imports
from . import gui_buttons as gb
from . import gui_functions as gf

###################################################################################################

'''
Functions that are used to bring up new windows when each respective button is pressed.

Each new window takes some user input for a thing(s) they would like to change, and
does the action when they press another button to confirm their action.
'''

def add_class_window() -> None:
    # Window for adding a new Class to the system.
    root = tk.Toplevel(name = 'dn')
    root.title("Add Class")

    # Frame containing the elements.
    frame = tk.Frame(
        master = root,  
        relief = tk.SUNKEN,  
        borderwidth = 3)
    frame.pack(ipadx = 10)

    # Label: "Class Name"
    lbl1 = tk.Label(
        master = frame,  
        text = "Class Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 0, 
        column = 0, 
        sticky = "w")

    # Label: Output Message
    lbl2 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl2.grid(
        row = 1, 
        column = 0, 
        sticky = "w")

    # Entry where the user can enter their class name.
    etr = tk.Entry(
        master = frame, 
        width = 50)
    etr.grid(
        row = 0, 
        column = 1, 
        sticky = "w")

    # Confirm Button, command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_add_class(etr.get(), lbl2),
        master = frame, 
        text = "Confirm", 
        font = ('bold'))
    btn.grid(
        row = 1, 
        column = 1, 
        sticky = "e", 
        padx = 5, 
        pady = 5)

    # Generate the window.
    root.mainloop()


def delete_class_window() -> None:
    # Window for deleting an existing Class from the system.
    root = tk.Toplevel(name = 'dn')
    root.title("Delete Class")

    # Frame containing the elements.
    frame = tk.Frame(
        master = root,  
        relief = tk.SUNKEN,  
        borderwidth = 3)
    frame.pack(ipadx = 10)

    # Label: "Class Name"
    lbl1 = tk.Label(
        master = frame,  
        text = "Class Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 0, 
        column = 0, 
        sticky = "w")

    # Label: Output Message
    lbl2 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl2.grid(
        row = 1, 
        column = 0, 
        sticky = "w")

    # Entry where the user can enter their class name.
    etr = tk.Entry(
        master = frame, 
        width = 50)
    etr.grid(
        row = 0, 
        column = 1, 
        sticky = "w")

    # Confirm Button, command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_delete_class(etr.get(), lbl2),
        master = frame, 
        text = "Confirm", 
        font = ('bold'))
    btn.grid(
        row = 1, 
        column = 1, 
        sticky = "e", 
        padx = 5, 
        pady = 5)

    # Generate the window.
    root.mainloop()


def rename_class_window() -> None:
    # Window for renaming an existing Class in the system.
    root = tk.Toplevel(name = 'dn')
    root.title("Rename Class")

    # Frame containing the elements.
    frame = tk.Frame(
        master = root,  
        relief = tk.SUNKEN,  
        borderwidth = 3)
    frame.pack(ipadx = 10)

    # Label: "Old Class Name"
    lbl1 = tk.Label(
        master = frame,  
        text = "Old Class Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 0, 
        column = 0, 
        sticky = "w")

    # Label: "New Class Name"
    lbl2 = tk.Label(
        master = frame,  
        text = "New Class Name:", 
        font = ('bold'))
    lbl2.grid(
        row = 1, 
        column = 0, 
        sticky = "w")

    # Label: Output Message
    lbl3 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl3.grid(
        row = 2, 
        column = 0, 
        sticky = "w")

    # Entry where the user can enter their old class name.
    etr1 = tk.Entry(
        master = frame, 
        width = 50)
    etr1.grid(
        row = 0, 
        column = 1, 
        sticky = "w")

    # Entry where the user can enter their new class name.
    etr2 = tk.Entry(
        master = frame, 
        width = 50)
    etr2.grid(
        row = 1, 
        column = 1, 
        sticky = "w")

    # Confirm Button, command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_rename_class(etr1.get(), etr2.get(), lbl3),
        master = frame, 
        text = "Confirm", 
        font = ('bold'))
    btn.grid(
        row = 2, 
        column = 1, 
        sticky = "e", 
        padx = 5, 
        pady = 5)

    # Generate the window.
    root.mainloop()


def add_method_window() -> None:
    # Window for adding a Method to an existing Class in the system.
    root = tk.Toplevel(name = 'dn')
    root.title("Add Method")

    # Frame containing the elements.
    frame = tk.Frame(
        master = root,  
        relief = tk.SUNKEN,  
        borderwidth = 3)
    frame.pack(ipadx = 10)

    # Label: "Class Name"
    lbl1 = tk.Label(
        master = frame,  
        text = "Class Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 0, 
        column = 0, 
        sticky = "w")

    # Label: "Method Name"
    lbl2 = tk.Label(
        master = frame,  
        text = "Method Name:", 
        font = ('bold'))
    lbl2.grid(
        row = 1, 
        column = 0, 
        sticky = "w")

    # Label: "Method Type"
    lbl3 = tk.Label(
        master = frame,  
        text = "Method Name:", 
        font = ('bold'))
    lbl3.grid(
        row = 2, 
        column = 0, 
        sticky = "w")

    # Label: Output Message
    lbl4 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl4.grid(
        row = 3, 
        column = 0, 
        sticky = "w")

    # Entry where the user can enter their class name.
    etr1 = tk.Entry(
        master = frame, 
        width = 50)
    etr1.grid(
        row = 0, 
        column = 1, 
        sticky = "w")

    # Entry where the user can enter their method name.
    etr2 = tk.Entry(
        master = frame, 
        width = 50)
    etr2.grid(
        row = 1, 
        column = 1, 
        sticky = "w")

    # Entry where the user can enter their method type.
    etr3 = tk.Entry(
        master = frame, 
        width = 50)
    etr3.grid(
        row = 2, 
        column = 1, 
        sticky = "w")

    # Confirm Button, command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_add_method(etr1.get(), etr2.get(), etr3.get(), lbl4),
        master = frame, 
        text = "Confirm", 
        font = ('bold'))
    btn.grid(
        row = 3, 
        column = 1, 
        sticky = "e", 
        padx = 5, 
        pady = 5)

    # Generate the window.
    root.mainloop()


def delete_method_window() -> None:
    # Window for deleting a Method from an existing Class in the system.
    root = tk.Toplevel(name = 'dn')
    root.title("Delete Method")

    # Frame containing the elements.
    frame = tk.Frame(
        master = root,  
        relief = tk.SUNKEN,  
        borderwidth = 3)
    frame.pack(ipadx = 10)

    # Label: "Class Name"
    lbl1 = tk.Label(
        master = frame,  
        text = "Class Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 0, 
        column = 0, 
        sticky = "w")

    # Label: "Method Name"
    lbl2 = tk.Label(
        master = frame,  
        text = "Method Name:", 
        font = ('bold'))
    lbl2.grid(
        row = 1, 
        column = 0, 
        sticky = "w")

    # Label: Output Message
    lbl3 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl3.grid(
        row = 2, 
        column = 0, 
        sticky = "w")

    # Entry where the user can enter their class name.
    etr1 = tk.Entry(
        master = frame, 
        width = 50)
    etr1.grid(
        row = 0, 
        column = 1, 
        sticky = "w")

    # Entry where the user can enter their method name.
    etr2 = tk.Entry(
        master = frame, 
        width = 50)
    etr2.grid(
        row = 1, 
        column = 1, 
        sticky = "w")

    # Confirm Button, command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_delete_method(etr1.get(), etr2.get(), lbl3),
        master = frame, 
        text = "Confirm", 
        font = ('bold'))
    btn.grid(
        row = 2, 
        column = 1, 
        sticky = "e", 
        padx = 5, 
        pady = 5)

    # Generate the window.
    root.mainloop()


def rename_method_window() -> None:
    # Window for renaming a Method in an existing Class in the system.
    root = tk.Toplevel(name = 'dn')
    root.title("Rename Method")

    # Frame containing the elements.
    frame = tk.Frame(
        master = root,  
        relief = tk.SUNKEN,  
        borderwidth = 3)
    frame.pack(ipadx = 10)

    # Label: "Class Name"
    lbl1 = tk.Label(
        master = frame,  
        text = "Class Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 0, 
        column = 0, 
        sticky = "w")

    # Label: "Old Method Name"
    lbl2 = tk.Label(
        master = frame,  
        text = "Old Method Name:", 
        font = ('bold'))
    lbl2.grid(
        row = 1, 
        column = 0, 
        sticky = "w")

    # Label: "New Method Name"
    lbl3 = tk.Label(
        master = frame,  
        text = "New Method Name:", 
        font = ('bold'))
    lbl3.grid(
        row = 2, 
        column = 0, 
        sticky = "w")

    # Label: Output Message
    lbl4 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl4.grid(
        row = 3, 
        column = 0, 
        sticky = "w")

    # Entry where the user can enter their class name.
    etr1 = tk.Entry(
        master = frame, 
        width = 50)
    etr1.grid(
        row = 0, 
        column = 1, 
        sticky = "w")

    # Entry where the user can enter their old method name.
    etr2 = tk.Entry(
        master = frame, 
        width = 50)
    etr2.grid(
        row = 1, 
        column = 1, 
        sticky = "w")

    # Entry where the user can enter their new method name.
    etr3 = tk.Entry(
        master = frame, 
        width = 50)
    etr3.grid(
        row = 2, 
        column = 1, 
        sticky = "w")

    # Confirm Button, command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_rename_method(etr1.get(), etr2.get(), etr3.get(), lbl4),
        master = frame, 
        text = "Confirm", 
        font = ('bold'))
    btn.grid(
        row = 3, 
        column = 1, 
        sticky = "e", 
        padx = 5, 
        pady = 5)

    # Generate the window.
    root.mainloop()


def add_field_window() -> None:
    # Window for adding a Field to an existing Class in the system.
    root = tk.Toplevel(name = 'dn')
    root.title("Add Field")

    # Frame containing the elements.
    frame = tk.Frame(
        master = root,  
        relief = tk.SUNKEN,  
        borderwidth = 3)
    frame.pack(ipadx = 10)

    # Label: "Class Name"
    lbl1 = tk.Label(
        master = frame,  
        text = "Class Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 0, 
        column = 0, 
        sticky = "w")

    # Label: "Field Name"
    lbl2 = tk.Label(
        master = frame,  
        text = "Field Name:", 
        font = ('bold'))
    lbl2.grid(
        row = 1, 
        column = 0, 
        sticky = "w")

    # Label: "Field Type"
    lbl3 = tk.Label(
        master = frame,  
        text = "Field Type:", 
        font = ('bold'))
    lbl3.grid(
        row = 2, 
        column = 0, 
        sticky = "w")

    # Label: Output Message
    lbl4 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl4.grid(
        row = 3, 
        column = 0, 
        sticky = "w")

    # Entry where the user can enter their class name.
    etr1 = tk.Entry(
        master = frame, 
        width = 50)
    etr1.grid(
        row = 0, 
        column = 1, 
        sticky = "w")

    # Entry where the user can enter their field name.
    etr2 = tk.Entry(
        master = frame, 
        width = 50)
    etr2.grid(
        row = 1, 
        column = 1, 
        sticky = "w")
    
    # Entry where the user can enter their field type.
    etr3 = tk.Entry(
        master = frame, 
        width = 50)
    etr3.grid(
        row = 2, 
        column = 1, 
        sticky = "w")

    # Confirm Button, command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_add_field(etr1.get(), etr2.get(), etr3.get(), lbl4),
        master = frame, 
        text = "Confirm", 
        font = ('bold'))
    btn.grid(
        row = 3, 
        column = 1, 
        sticky = "e", 
        padx = 5, 
        pady = 5)

    # Generate the window.
    root.mainloop()


def delete_field_window() -> None:
    # Window for deleting a Field from an existing Class in the system.
    root = tk.Toplevel(name = 'dn')
    root.title("Delete Field")

    # Frame containing the elements.
    frame = tk.Frame(
        master = root,  
        relief = tk.SUNKEN,  
        borderwidth = 3)
    frame.pack(ipadx = 10)

    # Label: "Class Name"
    lbl1 = tk.Label(
        master = frame,  
        text = "Class Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 0, 
        column = 0, 
        sticky = "w")

    # Label: "Field Name"
    lbl2 = tk.Label(
        master = frame,  
        text = "Field Name:", 
        font = ('bold'))
    lbl2.grid(
        row = 1, 
        column = 0, 
        sticky = "w")

    # Label: Output Message
    lbl3 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl3.grid(
        row = 2, 
        column = 0, 
        sticky = "w")

    # Entry where the user can enter their class name.
    etr1 = tk.Entry(
        master = frame, 
        width = 50)
    etr1.grid(
        row = 0, 
        column = 1, 
        sticky = "w")

    # Entry where the user can enter their field name.
    etr2 = tk.Entry(
        master = frame, 
        width = 50)
    etr2.grid(
        row = 1, 
        column = 1, 
        sticky = "w")

    # Confirm Button, command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_delete_field(etr1.get(), etr2.get(), lbl3),
        master = frame, 
        text = "Confirm", 
        font = ('bold'))
    btn.grid(
        row = 2, 
        column = 1, 
        sticky = "e", 
        padx = 5, 
        pady = 5)

    # Generate the window.
    root.mainloop()


def rename_field_window() -> None:
    # Window for renaming a Field in an existing Class in the system.
    root = tk.Toplevel(name = 'dn')
    root.title("Rename Field")

    # Frame containing the elements.
    frame = tk.Frame(
        master = root,  
        relief = tk.SUNKEN,  
        borderwidth = 3)
    frame.pack(ipadx = 10)

    # Label: "Class Name"
    lbl1 = tk.Label(
        master = frame,  
        text = "Class Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 0, 
        column = 0, 
        sticky = "w")

    # Label: "Old Field Name"
    lbl2 = tk.Label(
        master = frame,  
        text = "Old Field Name:", 
        font = ('bold'))
    lbl2.grid(
        row = 1, 
        column = 0, 
        sticky = "w")

    # Label: "New Field Name"
    lbl3 = tk.Label(
        master = frame,  
        text = "New Field Name:", 
        font = ('bold'))
    lbl3.grid(
        row = 2, 
        column = 0, 
        sticky = "w")

    # Label: Output Message
    lbl4 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl4.grid(
        row = 3, 
        column = 0, 
        sticky = "w")

    # Entry where the user can enter their class name.
    etr1 = tk.Entry(
        master = frame, 
        width = 50)
    etr1.grid(
        row = 0, 
        column = 1, 
        sticky = "w")

    # Entry where the user can enter their old field name.
    etr2 = tk.Entry(
        master = frame, 
        width = 50)
    etr2.grid(
        row = 1, 
        column = 1, 
        sticky = "w")

    # Entry where the user can enter their new field name.
    etr3 = tk.Entry(
        master = frame, 
        width = 50)
    etr3.grid(
        row = 2, 
        column = 1, 
        sticky = "w")

    # Confirm Button, command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_rename_field(etr1.get(), etr2.get(), etr3.get(), lbl4),
        text = "Confirm", 
        font = ('bold'))
    btn.grid(
        row = 3, 
        column = 1, 
        sticky = "e", 
        padx = 5, 
        pady = 5)

    # Generate the window.
    root.mainloop()


def add_relation_window() -> None:
    # Window for adding a Relationship between 2 Classes.
    root = tk.Toplevel(name = 'dn')
    root.title("Add Relation")

    # Frame containing the elements.
    frame = tk.Frame(
        master = root,  
        relief = tk.SUNKEN,  
        borderwidth = 3)
    frame.pack(ipadx = 10)

    # Label: "Class 1 Name"
    lbl1 = tk.Label(
        master = frame,  
        text = "Class 1 Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 0, 
        column = 0, 
        sticky = "w")
    
    # Label: "Class 2 Name"
    lbl2 = tk.Label(
        master = frame,  
        text = "Class 2 Name:", 
        font = ('bold'))
    lbl2.grid(
        row = 1,  
        column = 0,  
        sticky = "w")

    # Label: Output Message
    lbl3 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl3.grid(
        row = 2, 
        column = 0, 
        sticky = "w")

    # Label: Option Select
    lbl4 = tk.Label(
        master = frame,  
        text = "Select 1 Type:", 
        font = ('bold'))
    lbl4.grid(
        row = 3,  
        column = 0,  
        sticky = "w")

    # Creating the togglable buttons for the 4 types of Relationships
    type = tk.IntVar()
    types = ["aggregation", "composition", "inheritance", "realization"]
    for index in range(len(types)):
        rdo = Radiobutton(
            master = frame, 
            text = types[index], 
            value = index, 
            variable = type, 
            font = ('bold'))
        rdo.grid(
            row = 4 + index, 
            column = 0, 
            sticky = "w")

    # Entry where the user can enter their 1st class name.
    etr1 = tk.Entry(
        master = frame, 
        width = 50)
    etr1.grid(
        row = 0, 
        column = 1, 
        sticky = "w")

    # Entry where the user can enter their 2nd class name.
    etr2 = tk.Entry(
        master = frame, 
        width = 50)
    etr2.grid(
        row = 1, 
        column = 1, 
        sticky = "w")

    # Confirm Button, command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_add_relation(etr1.get(), etr2.get(), types[type.get()], lbl4),
        master = frame, 
        text = "Confirm", 
        font = ('bold'))
    btn.grid(
        row = 7, 
        column = 1, 
        sticky = "e", 
        padx = 5, 
        pady = 5)

    # Generate the window.
    root.mainloop()


def delete_relation_window() -> None:
    # Window for deleting a Relationship between 2 Classes.
    root = tk.Toplevel(name = 'dn')
    root.title("Delete Relation")

    # Frame containing the elements.
    frame = tk.Frame(
        master = root,  
        relief = tk.SUNKEN,  
        borderwidth = 3)
    frame.pack(ipadx = 10)

    # Label: "Class 1 Name"
    lbl1 = tk.Label(
        master = frame,  
        text = "Class 1 Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 0, 
        column = 0, 
        sticky = "w")
    
    # Label: "Class 2 Name"
    lbl2 = tk.Label(
        master = frame,  
        text = "Class 2 Name:", 
        font = ('bold'))
    lbl2.grid(
        row = 1,  
        column = 0,  
        sticky = "w")

    # Label: Output Message
    lbl3 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl3.grid(
        row = 2, 
        column = 0, 
        sticky = "w")

    # Entry where the user can enter their 1st class name.
    etr1 = tk.Entry(
        master = frame, 
        width = 50)
    etr1.grid(
        row = 0, 
        column = 1, 
        sticky = "w")

    # Entry where the user can enter their 2nd class name.
    etr2 = tk.Entry(
        master = frame, 
        width = 50)
    etr2.grid(
        row = 1, 
        column = 1, 
        sticky = "w")

    # Confirm Button, command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_delete_relation(etr1.get(), etr2.get(), lbl3),
        master = frame, 
        text = "Confirm", 
        font = ('bold'))
    btn.grid(
        row = 2, 
        column = 1, 
        sticky = "e", 
        padx = 5, 
        pady = 5)

    # Generate the window.
    root.mainloop()


def delete_param_window() -> None:
   # Window for Deleting a Parameter from a Method in a Class.
    root = tk.Toplevel(name = 'dn')
    root.title("Delete Parameter")

    # Frame containing the elements.
    frame = tk.Frame(
        master = root,  
        relief = tk.SUNKEN,  
        borderwidth = 3)
    frame.pack(ipadx = 10)

    # Label: "Class Name"
    lbl1 = tk.Label(
        master = frame,  
        text = "Class Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 0, 
        column = 0, 
        sticky = "w")

    # Label: "Method Name"
    lbl2 = tk.Label(
        master = frame,  
        text = "Method Name:", 
        font = ('bold'))
    lbl2.grid(
        row = 1, 
        column = 0, 
        sticky = "w")

    # Label: "Param Name"
    lbl3 = tk.Label(
        master = frame,  
        text = "Param Name:", 
        font = ('bold'))
    lbl3.grid(
        row = 2, 
        column = 0, 
        sticky = "w")

    # Label: Output Message
    lbl4 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl4.grid(
        row = 3, 
        column = 0, 
        sticky = "w")

    # Entry where the user can enter their class name.
    etr1 = tk.Entry(
        master = frame, 
        width = 50)
    etr1.grid(
        row = 0, 
        column = 1, 
        sticky = "w")

    # Entry where the user can enter their method name.
    etr2 = tk.Entry(
        master = frame, 
        width = 50)
    etr2.grid(
        row = 1, 
        column = 1, 
        sticky = "w")

    # Entry where the user can enter their param name.
    etr3 = tk.Entry(
        master = frame, 
        width = 50)
    etr3.grid(
        row = 2, 
        column = 1, 
        sticky = "w")

    # Confirm Button, command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_delete_param(etr1.get(), etr2.get(), etr3.get(), lbl4),
        master = frame, 
        text = "Confirm", 
        font = ('bold'))
    btn.grid(
        row = 3, 
        column = 1, 
        sticky = "e", 
        padx = 5, 
        pady = 5)
    
    # Generate the window.
    root.mainloop()


def rename_param_window() -> None:
   # Window for Renaming a Parameter in a Method in a Class.
    root = tk.Toplevel(name = 'dn')
    root.title("Rename Parameter")

    # Frame containing the elements.
    frame = tk.Frame(
        master = root,  
        relief = tk.SUNKEN,  
        borderwidth = 3)
    frame.pack(ipadx = 10)

    # Label: "Class Name"
    lbl1 = tk.Label(
        master = frame,  
        text = "Class Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 0, 
        column = 0, 
        sticky = "w")

    # Label: "Method Name"
    lbl2 = tk.Label(
        master = frame,  
        text = "Method Name:", 
        font = ('bold'))
    lbl2.grid(
        row = 1, 
        column = 0, 
        sticky = "w")

    # Label: "Old Param Name"
    lbl3 = tk.Label(
        master = frame,  
        text = "Old Param Name:", 
        font = ('bold'))
    lbl3.grid(
        row = 2, 
        column = 0, 
        sticky = "w")

    # Label: "New Param Name"
    lbl4 = tk.Label(
        master = frame,  
        text = "New Param Name:", 
        font = ('bold'))
    lbl4.grid(
        row = 3, 
        column = 0, 
        sticky = "w")

    # Label: Output Message
    lbl5 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl5.grid(
        row = 4, 
        column = 0, 
        sticky = "w")

    # Entry where the user can enter their class name.
    etr1 = tk.Entry(
        master = frame, 
        width = 50)
    etr1.grid(
        row = 0, 
        column = 1, 
        sticky = "w")

    # Entry where the user can enter their method name.
    etr2 = tk.Entry(
        master = frame, 
        width = 50)
    etr2.grid(
        row = 1, 
        column = 1, 
        sticky = "w")

    # Entry where the user can enter their old param name.
    etr3 = tk.Entry(
        master = frame, 
        width = 50)
    etr3.grid(
        row = 2, 
        column = 1, 
        sticky = "w")

    # Entry where the user can enter their new param name.
    etr4 = tk.Entry(
        master = frame, 
        width = 50)
    etr4.grid(
        row = 3, 
        column = 1, 
        sticky = "w")

    # Confirm Button, command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_rename_param(etr1.get(), etr2.get(), etr3.get(), etr4.get(), lbl4),
        master = frame, 
        text = "Confirm", 
        font = ('bold'))
    btn.grid(
        row = 4, 
        column = 1, 
        sticky = "e", 
        padx = 5, 
        pady = 5)
    
    # Generate the window.
    root.mainloop()


def save_window() -> None:
    # Window for Saving all the current data to a file.
    root = tk.Toplevel(name = 'dn')
    root.title("Save Data")

    # Frame containing the elements.
    frame = tk.Frame(
        master = root,  
        relief = tk.SUNKEN,  
        borderwidth = 3)
    frame.pack(ipadx = 10)

    # Label: "File Name"
    lbl1 = tk.Label(
        master = frame,  
        text = "File Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 0, 
        column = 0, 
        sticky = "w")

    # Label: Output Message
    lbl2 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl2.grid(
        row = 1, 
        column = 0, 
        sticky = "w")

    # Entry where the user can enter their file name.
    etr = tk.Entry(
        master = frame, 
        width = 50)
    etr.grid(
        row = 0, 
        column = 1, 
        sticky = "w")

    # Confirm Button, command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_save_file(etr.get(), lbl2),
        master = frame, 
        text = "Confirm", 
        font = ('bold'))
    btn.grid(
        row = 1, 
        column = 1, 
        sticky = "e", 
        padx = 5, 
        pady = 5)

    # Generate the window.
    root.mainloop()


def load_window() -> None:
    # Window for Loading data from an existing file.
    root = tk.Toplevel(name = 'dn')
    root.title("Load Data")

    # Frame containing the elements.
    frame = tk.Frame(
        master = root,  
        relief = tk.SUNKEN,  
        borderwidth = 3)
    frame.pack(ipadx = 10)

    # Label: Warning Message
    lbl1 = tk.Label(
        master = frame,  
        text = "Warning: Loading will overwrite any unsaved changes.", 
        font = ('bold'))
    lbl1.grid(
        row = 0, 
        column = 0, 
        sticky = "w")

    # Label: "File Name"
    lbl2 = tk.Label(
        master = frame,  
        text = "File Name:", 
        font = ('bold'))
    lbl2.grid(
        row = 1, 
        column = 0, 
        sticky = "w")

    # Label: Output Message
    lbl3 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl3.grid(
        row = 2, 
        column = 0, 
        sticky = "w")

    # Entry where the user can enter their file name.
    etr = tk.Entry(
        master = frame, 
        width = 50)
    etr.grid(
        row = 1, 
        column = 1, 
        sticky = "w")

    # Confirm Button, command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_load_file(etr.get(), lbl3),
        master = frame, 
        text = "Confirm", 
        font = ('bold'))
    btn.grid(
        row = 2, 
        column = 1, 
        sticky = "e", 
        padx = 5, 
        pady = 5)

    # Generate the window.
    root.mainloop()

###################################################################################################
'''
# Entry Point
if __name__ == '__main__':
    main(sys.argv)

'''
# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     gui_windows.py

# External Imports
import tkinter as tk
from tkinter import ttk

# Internal Imports
from . import gui_functions as gf
from uml_components import (UMLClass, UMLAttributes)

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
    root.bind('<Return>', 
        lambda event: gf.b_add_class(etr.get(), lbl2))
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
    root.bind('<Return>', 
        lambda event: gf.b_delete_class(etr.get(), lbl2))
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
    root.bind('<Return>', 
        lambda event: gf.b_rename_class(etr1.get(), etr2.get(), lbl3))
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

    # List of classes in the current system.
    classes = []
    for class_name in UMLClass.class_dict:
        classes.append(class_name)

    # Label: Select a Class.
    classlabel = tk.Label(frame, text = "Select a Class: ", font = ('bold'))
    classlabel.grid(row = 0, column = 0, sticky = "w")

    # Creating the classes dropdown.
    classvar = tk.StringVar(frame)
    classvar.set("Click to Select") # Default value
    class_dropdown = tk.OptionMenu(frame, classvar, *classes, value = "")
    class_dropdown.config(width = 20) # Set the width of the dropdown
    class_dropdown.grid(row = 1, column = 0, sticky = "w")

    # Label/Entry for Method Name
    label1 = tk.Label(frame, text = "Method Name :", font = ('bold'))
    label1.grid(row = 2, column = 0, sticky = "w")
    entry1 = tk.Entry(frame, width = 50)
    entry1.grid(row = 3, column = 0, sticky = "w")

    # Label/Entry for Method Type
    label2 = tk.Label(frame, text = "Method Type :", font = ('bold'))
    label2.grid(row = 4, column = 0, sticky = "w")
    entry2 = tk.Entry(frame, width = 50)
    entry2.grid(row = 5, column = 0, sticky = "w")

    # Adding Parameters Section
    paramlist = []
    separator = ttk.Separator(frame, orient = "horizontal")
    separator.grid(row = 7, column = 0, sticky = "ew")

    label3 = tk.Label(frame,text = "Parameters w/ Methods", font = ('bold'))
    label3.grid(row = 8, column = 0)

    label4 = tk.Label(frame, text = "Param Name :", font = ('bold'))
    label4.grid(row = 9, column = 0, sticky = "w")
    entry4 = tk.Entry(frame, width = 50)
    entry4.grid(row = 10, column = 0, sticky = "w")

    label5 = tk.Label(frame, text = "Param Type :", font = ('bold'))
    label5.grid(row = 11, column = 0, sticky = "w")
    entry5 = tk.Entry(frame, width = 50)
    entry5.grid(row = 12, column = 0, sticky = "w")

    new_param_btn = tk.Button(
        command = lambda: paramlist.append(UMLAttributes.UMLParameter(entry4.get(), entry5.get())),
        master = frame,
        text = "+ Param",
        font = ('bold'))
    new_param_btn.grid(
        row = 13, 
        column = 0, 
        sticky = "e", 
        padx = 5, 
        pady = 5)

    # Label for Program Output
    outputlabel = tk.Label(frame, text = "", font = ('bold'))
    outputlabel.grid(row = 4, column = 0, sticky = "w")

    # Confirm Button, command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_add_method(classvar.get(), entry1.get(), entry2.get(), outputlabel),
        master = frame, 
        text = "Confirm", 
        font = ('bold'))
    btn.grid(
        row = 6, 
        column = 0, 
        sticky = "e", 
        padx = 5, 
        pady = 5)

    # Generate the window.
    root.bind('<Return>', 
        lambda event: gf.b_add_method(classvar.get(), entry1.get(), entry2.get(), outputlabel))
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

    # Label: "Method Type"
    lbl3 = tk.Label(
        master = frame,  
        text = "Method Type:", 
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
        command = lambda: gf.b_delete_method(etr1.get(), etr2.get(), etr3.get(), lbl4),
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
    root.bind('<Return>', 
        lambda event: gf.b_delete_method(etr1.get(), etr2.get(), etr3.get(), lbl4))
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

    # Label: "Method Type"
    lbl4 = tk.Label(
        master = frame,  
        text = "Method Type:", 
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

    # Entry where the user can enter their method type.
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
        command = lambda: gf.b_rename_method(etr1.get(), etr2.get(), etr3.get(), etr4.get(), lbl5),
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
    root.bind('<Return>', 
        lambda event: gf.b_rename_method(etr1.get(), etr2.get(), etr3.get(), etr4.get(), lbl5))
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
    root.bind('<Return>', 
        lambda event: gf.b_add_field(etr1.get(), etr2.get(), etr3.get(), lbl4))
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
    root.bind('<Return>', 
        lambda event: gf.b_delete_field(etr1.get(), etr2.get(), lbl3))
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
    root.bind('<Return>', 
        lambda event: gf.b_rename_field(etr1.get(), etr2.get(), etr3.get(), lbl4))
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
        rdo = tk.Radiobutton(
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
    root.bind('<Return>', 
        lambda event: gf.b_add_relation(etr1.get(), etr2.get(), types[type.get()], lbl4))
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
    root.bind('<Return>', 
        lambda event: gf.b_delete_relation(etr1.get(), etr2.get(), lbl3))
    root.mainloop()


def add_param_window() -> None:
    # Window for Adding a Parameter to a Method in a Class.
    root = tk.Toplevel(name = 'dn')
    root.title("Add Parameter")

    # Frame containing the elements.
    frame = tk.Frame(
        master = root,  
        relief = tk.SUNKEN,  
        borderwidth = 3)
    frame.pack(ipadx = 10)

    # List of classes in the current system.
    classes = []
    for class_name in UMLClass.class_dict:
        classes.append(class_name)

    # Label: Select a Class.
    classlabel = tk.Label(frame, text = "Select a Class: ", font = ('bold'))
    classlabel.grid(row = 0, column = 0, sticky = "w")

    # Creating the classes dropdown.
    classvar = tk.StringVar(frame)
    classvar.set("Click to Select") # Default value
    class_dropdown = tk.OptionMenu(frame, classvar, *classes)
    class_dropdown.config(width = 20) # Set the width of the dropdown
    class_dropdown.grid(row = 0, column = 1, sticky = "w")

    # List of methods
    methods = []
    classname = classvar.get()
    selected_class = UMLClass.class_dict[classname]
    for method in selected_class.methods:
        methods.append(method)

    # Label: Select a Method.
    methodlabel = tk.Label(frame, text = "Select a Method: ", font = ('bold'))
    methodlabel.grid(row = 1, column = 0, sticky = "w")
    
    # Creating the methods dropdown.
    methodvar = tk.StringVar(master = frame)
    methodvar.set("Click to Select") # Default value
    method_dropdown = tk.OptionMenu(frame, methodvar, *methods)
    method_dropdown.config(width = 50) # Set the width of the dropdown
    method_dropdown.grid(row = 1, column = 1, sticky = "w")

    # Confirm Button, command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_add_param(etr1.get(), etr2.get(), etr3.get(), etr4.get(), etr5.get(), lbl6),
        master = frame, 
        text = "Confirm", 
        font = ('bold'))
    btn.grid(
        row = 5, 
        column = 1, 
        sticky = "e", 
        padx = 5, 
        pady = 5)
    
    # Generate the window.
    root.bind('<Return>', 
        lambda event: gf.b_add_param(etr1.get(), etr2.get(), etr3.get(), etr4.get(), etr5.get(), lbl6))
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

    # Label: "Method Type"
    lbl3 = tk.Label(
        master = frame,  
        text = "Method Type:", 
        font = ('bold'))
    lbl3.grid(
        row = 2, 
        column = 0, 
        sticky = "w")

    # Label: "Param Name"
    lbl4 = tk.Label(
        master = frame,  
        text = "Param Name:", 
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

    # Entry where the user can enter their method type.
    etr3 = tk.Entry(
        master = frame, 
        width = 50)
    etr3.grid(
        row = 2, 
        column = 1, 
        sticky = "w")

    # Entry where the user can enter their param name.
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
        command = lambda: gf.b_delete_param(etr1.get(), etr2.get(), etr3.get(), etr4.get(), lbl5),
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
    root.bind('<Return>', 
        lambda event: gf.b_delete_param(etr1.get(), etr2.get(), etr3.get(), etr4.get(), lbl5))
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

    # Label: "Method Type"
    lbl3 = tk.Label(
        master = frame,  
        text = "Method Type:", 
        font = ('bold'))
    lbl3.grid(
        row = 2, 
        column = 0, 
        sticky = "w")

    # Label: "Old Param Name"
    lbl4 = tk.Label(
        master = frame,  
        text = "Old Param Name:", 
        font = ('bold'))
    lbl4.grid(
        row = 3, 
        column = 0, 
        sticky = "w")

    # Label: "New Param Name"
    lbl5 = tk.Label(
        master = frame,  
        text = "New Param Name:", 
        font = ('bold'))
    lbl5.grid(
        row = 4, 
        column = 0, 
        sticky = "w")

    # Label: Output Message
    lbl6 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl6.grid(
        row = 5, 
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

    # Entry where the user can enter their old param name.
    etr4 = tk.Entry(
        master = frame, 
        width = 50)
    etr4.grid(
        row = 3, 
        column = 1, 
        sticky = "w")

    # Entry where the user can enter their new param name.
    etr5 = tk.Entry(
        master = frame, 
        width = 50)
    etr5.grid(
        row = 4, 
        column = 1, 
        sticky = "w")

    # Confirm Button, command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_rename_param(etr1.get(), etr2.get(), etr3.get(), etr4.get(), etr5.get(), lbl6),
        master = frame, 
        text = "Confirm", 
        font = ('bold'))
    btn.grid(
        row = 5, 
        column = 1, 
        sticky = "e", 
        padx = 5, 
        pady = 5)
    
    # Generate the window.
    root.bind('<Return>', 
        lambda event: gf.b_rename_param(etr1.get(), etr2.get(), etr3.get(), etr4.get(), etr5.get(), lbl6))
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

def export_window() -> None:
    # Window for Loading data from an existing file.
    root = tk.Toplevel(name = 'dn')
    root.title("Export Image")
    # Frame containing the elements.
    frame = tk.Frame(
        master = root,  
        relief = tk.SUNKEN,  
        borderwidth = 3)
    frame.pack(ipadx = 10)

    # Label: Warning Message
    lbl1 = tk.Label(
        master = frame,  
        text = "Warning: Saving duplicate file names will override previous ones.", 
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
        command = lambda: gf.b_export(etr.get(), lbl3),
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
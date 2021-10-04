# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     gui_application.py

# Imports:
import sys
import os.path

# import class_interface

import tkinter as tk
from tkinter import *
import tkinter.messagebox as mb


def main(args : list) -> None:
    '''
    Main function for the program.

    Parameters:\n
    args : list -> A list of command-line arguments provided to the program.
    '''
    make_buttons()

###################################################################################################

'''
Functions that are used to bring up new windows when each respective button is pressed.

Each new window takes some user input for a thing(s) they would like to change, and
does the action when they press another button to confirm their action.
'''

# Testing function, what you've typed into an entry gets put into the appropriate label
def label_updating_testing(lbl: tk.Label, msg : str):
    lbl.configure(text = msg)

# good to go until action can actually be implemented into it
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

    # Label: Potential Error Message
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

    # Confirm Button, # TODO command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: label_updating_testing(lbl2, etr.get()),
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

# good to go until action can actually be implemented into it
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

    # Label: Potential Error Message
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

    # Confirm Button, # TODO command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: label_updating_testing(lbl2, etr.get()),
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

# good to go until action can actually be implemented into it
def rename_class_window() -> None:
    # Window for renaming an existing Class from the system.
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
    lbl1 = tk.Label(
        master = frame,  
        text = "New Class Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 1, 
        column = 0, 
        sticky = "w")

    # Label: Potential Error Message
    lbl2 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl2.grid(
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

    # Confirm Button, # TODO command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: label_updating_testing(lbl2, etr1.get()),
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

# good to go until action can actually be implemented into it
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
    lbl1 = tk.Label(
        master = frame,  
        text = "Method Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 1, 
        column = 0, 
        sticky = "w")

    # Label: Potential Error Message
    lbl2 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl2.grid(
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

    # Confirm Button, # TODO command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: label_updating_testing(lbl2, etr1.get()),
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

# good to go until action can actually be implemented into it
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
    lbl1 = tk.Label(
        master = frame,  
        text = "Method Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 1, 
        column = 0, 
        sticky = "w")

    # Label: Potential Error Message
    lbl2 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl2.grid(
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

    # Confirm Button, # TODO command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: label_updating_testing(lbl2, etr1.get()),
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

# good to go until action can actually be implemented into it
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
    lbl1 = tk.Label(
        master = frame,  
        text = "Old Method Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 1, 
        column = 0, 
        sticky = "w")

    # Label: "New Method Name"
    lbl1 = tk.Label(
        master = frame,  
        text = "New Method Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 2, 
        column = 0, 
        sticky = "w")

    # Label: Potential Error Message
    lbl2 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl2.grid(
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

    # Confirm Button, # TODO command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: label_updating_testing(lbl2, etr1.get()),
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

# good to go until action can actually be implemented into it
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
    lbl1 = tk.Label(
        master = frame,  
        text = "Field Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 1, 
        column = 0, 
        sticky = "w")

    # Label: Potential Error Message
    lbl2 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl2.grid(
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

    # Confirm Button, # TODO command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: label_updating_testing(lbl2, etr1.get()),
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

# good to go until action can actually be implemented into it
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
    lbl1 = tk.Label(
        master = frame,  
        text = "Field Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 1, 
        column = 0, 
        sticky = "w")

    # Label: Potential Error Message
    lbl2 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl2.grid(
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

    # Confirm Button, # TODO command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: label_updating_testing(lbl2, etr1.get()),
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

# good to go until action can actually be implemented into it
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
    lbl1 = tk.Label(
        master = frame,  
        text = "Old Field Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 1, 
        column = 0, 
        sticky = "w")

    # Label: "New Method Name"
    lbl1 = tk.Label(
        master = frame,  
        text = "New Field Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 2, 
        column = 0, 
        sticky = "w")

    # Label: Potential Error Message
    lbl2 = tk.Label(
        master = frame,  
        text = "", 
        font = ('bold'))
    lbl2.grid(
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

    # Confirm Button, # TODO command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: label_updating_testing(lbl2, etr1.get()),
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

# good to go until action can actually be implemented into it
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

    # Label: Potential Error Message
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
    types = ["Aggregation", "Composition", "Inheritence", "Realization"]
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

    # Confirm Button, # TODO command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: label_updating_testing(lbl3, etr1.get()),
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

# good to go until action can actually be implemented into it
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

    # Label: Potential Error Message
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

    # Confirm Button, # TODO command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: label_updating_testing(lbl3, etr1.get()),
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

# good to go until action can actually be implemented into it
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

    # Label: Potential Error Message
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

    # Confirm Button, # TODO command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: label_updating_testing(lbl2, etr.get()),
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

# good to go until action can actually be implemented into it
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

    # Label: "File Name"
    lbl1 = tk.Label(
        master = frame,  
        text = "File Name:", 
        font = ('bold'))
    lbl1.grid(
        row = 0, 
        column = 0, 
        sticky = "w")

    # Label: Potential Error Message
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

    # Confirm Button, # TODO command is the helper checking the user input
    #     and executing the appropriate function.
    btn = tk.Button(
        command = lambda: label_updating_testing(lbl2, etr.get()),
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

# will write later
def help_window() -> None:
    pass


###################################################################################################

def add_helper(lbl : tk.Text, name : str) -> str:
    
    #empty
    #already exist
    """ 
    valid = add_class(name)
    if not (0 == valid):
        if valid == 1:
            pass
        elif valid == 2:
            pass
    """
    lbl.insert(tk.INSERT, name)
    return name

###################################################################################################

def make_buttons() -> None:
    '''
    Function to make the buttons on the right side of the GUI:
        [Add       Class]  [Delete    Class]  [Rename    Class]
        [Add      Method]  [Delete   Method]  [Rename   Method]
        [Add       Field]  [Delete    Field]  [Rename    Field]
        [Add    Relation]  [Delete Relation] 
        [Save       File]  [Load       File]  [     Help      ]

    '''
    # Make a new window
    window = tk.Tk()
    window.title("SNAKE PEOPLE UML Editor")

    # Make a new frame for the buttons
    button_frame = tk.Frame(relief = tk.FLAT, borderwidth = 5)
    button_frame.pack(side = tk.RIGHT, padx = 10)

    '''
    Row 1:

    [Add       Class]  [Delete    Class]  [Rename    Class]
    '''
    # Add Class Button
    add_class_button = tk.Button(
        command = add_class_window,
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
        command = delete_class_window,
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
        command = rename_class_window,
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
        command = add_method_window,
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
        command = delete_method_window,
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
        command = rename_method_window,
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
        command = add_field_window,
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
        command = delete_field_window,
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
        command = rename_field_window,
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
        command = add_relation_window,
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
        command = delete_relation_window,
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
        command = save_window,
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
        command = load_window,
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
        command = help_window,
        master = button_frame,
        text = "Help",
        width = 14, 
        font = ('bold'))
    help_button.grid(
        row = 4,
        column = 2,
        padx = 5,
        pady = 5)

    # Generate the window
    window.mainloop()

###################################################################################################

# Entry Point
if __name__ == '__main__':
    main(sys.argv)


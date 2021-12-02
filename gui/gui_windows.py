# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     gui_windows.py

# External Imports
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# Internal Imports
from . import gui_functions as gf
from uml_components import (UMLClass, UMLAttributes)

###################################################################################################
'''
Functions that are used to bring up new windows when each respective button is pressed.

Each new window takes some user input for a thing(s) they would like to change, and
does the action when they press another button to confirm their action.
'''

global current_method
current_method = None

def add_class_window() -> None:
    # Window for adding a new Class to the system.
    root = tk.Toplevel(name = 'dn')
    root.title("Add Class")

    # Frame containing the elements.
    frame = tk.Frame(master = root,  relief = tk.SUNKEN,  borderwidth = 3)
    frame.pack()

    # Label/Entry for Class Name.
    label = tk.Label(frame, text = "Class Name :", font = ('bold'))
    label.grid(row = 0, column = 0)
    entry = tk.Entry(frame, width = 50)
    entry.grid(row = 1, column = 0)

    # Confirm Button, command is the helper checking the user input
    #   and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_add_class(
            entry.get(), outputlabel),
        master = frame, text = "Confirm", font = ('bold'))
    btn.grid(row = 2, column = 0, padx = 5, pady = 5)

    # Thin Line Separator.
    separator = ttk.Separator(frame, orient = "horizontal")
    separator.grid(row = 3, column = 0, sticky = "ew")

    # Label for Program Output.
    outputlabel = tk.Label(frame, text = "")
    outputlabel.grid(row = 4, column = 0)

    # Bind the enter key to confirming the user's action, same as if they
    #   were to press the Confirm button.
    root.bind('<Return>', 
        lambda event: gf.b_add_class(
            entry.get(), outputlabel))
    
    # Generate the window.
    root.mainloop()


def delete_class_window() -> None:
    # Window for deleting an existing Class from the system.
    root = tk.Toplevel(name = 'dn')
    root.title("Delete Class")

    # Frame containing the elements.
    frame = tk.Frame(master = root,  relief = tk.SUNKEN,  borderwidth = 3)
    frame.pack()

    # Label/Entry for Class Name.
    label = tk.Label(frame, text = "Class Name :", font = ('bold'))
    label.grid(row = 0, column = 0)
    entry = tk.Entry(frame, width = 50)
    entry.grid(row = 1, column = 0)

    # Confirm Button, command is the helper checking the user input
    #   and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_delete_class(
            entry.get(), outputlabel),
        master = frame, text = "Confirm", font = ('bold'))
    btn.grid(row = 2, column = 0, padx = 5, pady = 5)

    # Thin Line Separator.
    separator = ttk.Separator(frame, orient = "horizontal")
    separator.grid(row = 3, column = 0, sticky = "ew")

    # Label for Program Output.
    outputlabel = tk.Label(frame, text = "")
    outputlabel.grid(row = 4, column = 0)

    # Bind the enter key to confirming the user's action, same as if they
    #   were to press the Confirm button.
    root.bind('<Return>', 
        lambda event: gf.b_delete_class(
            entry.get(), outputlabel))
    
    # Generate the window.
    root.mainloop()


def rename_class_window() -> None:
    # Window for renaming an existing Class in the system.
    root = tk.Toplevel(name = 'dn')
    root.title("Rename Class")

    # Frame containing the elements.
    frame = tk.Frame(master = root,  relief = tk.SUNKEN,  borderwidth = 3)
    frame.pack()

    # Label/Entry for Old Method Type.
    label1 = tk.Label(frame, text = "Old Class Name :", font = ('bold'))
    label1.grid(row = 0, column = 0)
    entry1 = tk.Entry(frame, width = 50)
    entry1.grid(row = 1, column = 0)

    # Label/Entry for New Method Name.
    label2 = tk.Label(frame, text = "New Class Name :", font = ('bold'))
    label2.grid(row = 2, column = 0)
    entry2 = tk.Entry(frame, width = 50)
    entry2.grid(row = 3, column = 0)

    # Confirm Button, command is the helper checking the user input
    #   and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_rename_class(
            entry1.get(), entry2.get(), outputlabel),
        master = frame, text = "Confirm", font = ('bold'))
    btn.grid(row = 4, column = 0, padx = 5, pady = 5)

    # Thin Line Separator.
    separator = ttk.Separator(frame, orient = "horizontal")
    separator.grid(row = 5, column = 0, sticky = "ew")

    # Label for Program Output.
    outputlabel = tk.Label(frame, text = "")
    outputlabel.grid(row = 6, column = 0)

    # Bind the enter key to confirming the user's action, same as if they
    #   were to press the Confirm button.
    root.bind('<Return>', 
        lambda event: gf.b_rename_class(
            entry1.get(), entry2.get(), outputlabel))

    # Generate the window.
    root.mainloop()


def add_method_window() -> None:
    # Window for adding a Method to an existing Class in the system.
    root = tk.Toplevel(name = 'dn')
    root.title("Add Method")

    # Frame containing the elements.
    frame = tk.Frame(master = root, relief = tk.SUNKEN, borderwidth = 3)
    frame.pack()

    # Check to see if there are any classes.
    #   Does not allow the user to continue if no classes exist yet.
    if len(UMLClass.class_dict) == 0:
        label1 = tk.Label(frame, 
            text = "There are no classes in the system.", font = ('bold'))
        label1.grid(row = 0, column = 0)
        label2 = tk.Label(frame, 
            text = "Please add some classes first.", font = ('bold'))
        label2.grid(row = 1, column = 0)

    else:
        # List of classes in the current system.
        classes = []
        for class_name in UMLClass.class_dict:
            classes.append(class_name)

        # Label: Select a Class.
        classlabel = tk.Label(frame, text = "Select a Class: ", font = ('bold'))
        classlabel.grid(row = 0, column = 0)

        # Creating the classes dropdown.
        classvar = tk.StringVar(frame)
        classvar.set(list(UMLClass.class_dict)[0]) # Default value.
        class_dropdown = tk.OptionMenu(frame, classvar, *classes)
        class_dropdown.config(width = 20) # Set the width of the dropdown.
        class_dropdown.grid(row = 1, column = 0)

        # Label/Entry for Method Name.
        label1 = tk.Label(frame, text = "Method Name :", font = ('bold'))
        label1.grid(row = 2, column = 0)
        entry1 = tk.Entry(frame, width = 50)
        entry1.grid(row = 3, column = 0)

        # Label/Entry for Method Type.
        label2 = tk.Label(frame, text = "Method Type :", font = ('bold'))
        label2.grid(row = 4, column = 0)
        entry2 = tk.Entry(frame, width = 50)
        entry2.grid(row = 5, column = 0)

        # Confirm Button, command is the helper checking the user input
        #   and executing the appropriate function.
        btn = tk.Button(
            command = lambda: gf.b_add_method(
                classvar.get(), entry1.get(), entry2.get(), paramlist, outputlabel, paramoutput),
            master = frame, text = "Confirm", font = ('bold'))
        btn.grid(row = 6, column = 0, padx = 5, pady = 5)

        # Thin Line Separator.
        separator = ttk.Separator(frame, orient = "horizontal")
        separator.grid(row = 7, column = 0, sticky = "ew")

        # Adding Parameters Section.
        label3 = tk.Label(frame,text = "Parameters w/ Methods:", font = ('bold'))
        label3.grid(row = 8, column = 0)

        # Label/Entry for Param Name.
        label4 = tk.Label(frame, text = "Param Name :", font = ('bold'))
        label4.grid(row = 9, column = 0)
        entry4 = tk.Entry(frame, width = 50)
        entry4.grid(row = 10, column = 0)

        # Label/Entry for Param Type.
        label5 = tk.Label(frame, text = "Param Type :", font = ('bold'))
        label5.grid(row = 11, column = 0)
        entry5 = tk.Entry(frame, width = 50)
        entry5.grid(row = 12, column = 0)

        # Section for properly setting the paramlist to add to a new method.
        global paramlist
        paramlist = []
        def paramlist_helper():
            if entry4.get() == "" or entry5.get() == "" or str.isspace(entry4.get()) == True or str.isspace(entry5.get()) == True:
                paramoutput.configure(text = "Parameter names and types cannot be empty")
            else:
                paramlist.append(UMLAttributes.UMLParameter(entry4.get(), entry5.get()))
                paramoutput.configure(text = "Queued param \"" + entry4.get() + "\" to add.")
                entry4.delete(0, tk.END)
                entry5.delete(0, tk.END)

        # Button for adding a Param to the list to be added to the current method.
        #   Does not work with pressing the enter key.
        new_param_btn = tk.Button(
            command = paramlist_helper,
            master = frame,text = "+ Param",font = ('bold'))
        new_param_btn.grid(row = 13, column = 0, padx = 5, pady = 5)

        # Thin Line Separator.
        separator = ttk.Separator(frame, orient = "horizontal")
        separator.grid(row = 14, column = 0, sticky = "ew")

        # Label for Program Output.
        outputlabel = tk.Label(frame, text = "")
        outputlabel.grid(row = 15, column = 0)

        # Label for output from the section for adding params with methods.
        paramoutput = tk.Label(frame, text = "")
        paramoutput.grid(row = 16, column = 0)

        # Bind the enter key to confirming the user's action, same as if they
        #   were to press the Confirm button.
        root.bind('<Return>', 
            lambda event: gf.b_add_method(
                classvar.get(), entry1.get(), entry2.get(), paramlist, outputlabel, paramoutput))
    
    # Generate the window.
    root.mainloop()


def delete_method_window() -> None:
    # Window for deleting a Method from an existing Class in the system.
    root = tk.Toplevel(name = 'dn')
    root.title("Delete Method")

    # Frame containing the elements.
    frame = tk.Frame(master = root, relief = tk.SUNKEN,  borderwidth = 3)
    frame.pack()

    # Check to see if there are any classes.
    #   Does not allow the user to continue if no classes exist yet.
    if len(UMLClass.class_dict) == 0:
        label1 = tk.Label(frame, text = "There are no classes in the system.", font = ('bold'))
        label1.grid(row = 0, column = 0)
        label2 = tk.Label(frame, text = "Please add some classes first.", font = ('bold'))
        label2.grid(row = 1, column = 0)

    else:
        # List of classes in the current system.
        classes = []
        for class_name in UMLClass.class_dict:
            classes.append(class_name)

        # Label: Select a Class.
        classlabel = tk.Label(frame, text = "Select a Class: ", font = ('bold'))
        classlabel.grid(row = 0, column = 0)

        # Creating the classes dropdown.
        global classvar
        classvar = tk.StringVar(frame)
        classvar.set(list(UMLClass.class_dict)[0]) # Default value.
        class_dropdown = tk.OptionMenu(frame, classvar, *classes)
        class_dropdown.config(width = 20) # Set the width of the dropdown.
        class_dropdown.grid(row = 1, column = 0)

        # Label for Method Name.
        label1 = tk.Label(frame, text = "Method Name :", font = ('bold'))
        label1.grid(row = 2, column = 0)

        # Creating the list of methods associated with the currently selected class.
        methods = []
        uml : UMLClass.UMLClass = UMLClass.class_dict[classvar.get()]
        string = ""
        for method in uml.methods:
            string = ""
            string += method.name + " " + method.return_type + "("
            for param in method.params:
                if string[-1] != "(":
                    string = string + ","
                string += param.type + " " + param.name
            string += ")"
        methods.append(string)
        global methodvar
        methodvar = tk.StringVar()
        if len(methods) == 0:
            methodvar.set("No methods available")
        else:
            methodvar.set("Select a method")
        
        # Creating the methods dropdown.
        global method_dropdown
        method_dropdown = tk.OptionMenu(frame, methodvar, *methods)
        update_methods()
        classvar.trace_add('write', lambda *args: update_methods())
        method_dropdown.grid(row = 3, column = 0)

        # Keeping track of the currently selected method in the dropdown,
        #   in order to pass the correct values to the backend upon 
        #   the user confirming their action.
        global method_name
        method_name = methodvar.get().split(" ")[0]
        global method_type
        method_type = methodvar.get().split(" ")[1].split("(")[0]
        methodvar.trace_add("write", lambda *args: update_params())

        # Confirm Button, command is the helper checking the user input
        #   and executing the appropriate function.
        btn = tk.Button(
            command = lambda: gf.b_delete_method(
                classvar.get(), current_method, outputlabel),
            master = frame, text = "Confirm", font = ('bold'))
        btn.grid(row = 4, column = 0, padx = 5, pady = 5)

        # Thin Line Separator.
        separator = ttk.Separator(frame, orient = "horizontal")
        separator.grid(row = 5, column = 0, sticky = "ew")

        # Label for Program Output.
        outputlabel = tk.Label(frame, text = "", width = 40)
        outputlabel.grid(row = 6, column = 0)

        # Bind the enter key to confirming the user's action, same as if they
        #   were to press the Confirm button.
        root.bind('<Return>', 
            lambda event: gf.b_delete_method(
                classvar.get(), current_method, outputlabel))
    
    # Generate the window.
    root.mainloop()
    

def rename_method_window() -> None:
    # Window for renaming a Method in an existing Class in the system.
    root = tk.Toplevel(name = 'dn')
    root.title("Rename Method")

    # Frame containing the elements.
    frame = tk.Frame(master = root, relief = tk.SUNKEN,  borderwidth = 3)
    frame.pack()

    # Check to see if there are any classes.
    #   Does not allow the user to continue if no classes exist yet.
    if len(UMLClass.class_dict) == 0:
        label1 = tk.Label(frame, text = "There are no classes in the system.", font = ('bold'))
        label1.grid(row = 0, column = 0)
        label2 = tk.Label(frame, text = "Please add some classes first.", font = ('bold'))
        label2.grid(row = 1, column = 0)

    else:
        # List of classes in the current system.
        classes = []
        for class_name in UMLClass.class_dict:
            classes.append(class_name)

        # Label: Select a Class.
        classlabel = tk.Label(frame, text = "Select a Class: ", font = ('bold'))
        classlabel.grid(row = 0, column = 0)

        # Creating the classes dropdown.
        global classvar
        classvar = tk.StringVar(frame)
        classvar.set(list(UMLClass.class_dict)[0]) # Default value.
        class_dropdown = tk.OptionMenu(frame, classvar, *classes)
        class_dropdown.config(width = 20) # Set the width of the dropdown.
        class_dropdown.grid(row = 1, column = 0)

        # Label for Old Method Name.
        label1 = tk.Label(frame, text = "Old Method Name :", font = ('bold'))
        label1.grid(row = 2, column = 0)

        # Creating the list of methods associated with the currently selected class.
        methods = []
        uml : UMLClass.UMLClass = UMLClass.class_dict[classvar.get()]
        string = ""
        for method in uml.methods:
            string = ""
            string += method.name + " " + method.return_type + "("
            for param in method.params:
                if string[-1] != "(":
                    string = string + ","
                string += param.type + " " + param.name
            string += ")"
        methods.append(string)
        global methodvar
        methodvar = tk.StringVar()
        if len(methods) == 0:
            methodvar.set("No methods available")
        else:
            methodvar.set("Select a method")

        # Creating the methods dropdown.
        global method_dropdown
        method_dropdown = tk.OptionMenu(frame, methodvar, *methods)
        update_methods()
        classvar.trace_add('write', lambda *args: update_methods())
        method_dropdown.grid(row = 3, column = 0)

        # Label/Entry for New Method Name.
        label2 = tk.Label(frame, text = "New Method Name :", font = ('bold'))
        label2.grid(row = 6, column = 0)
        entry2 = tk.Entry(frame, width = 50)
        entry2.grid(row = 7, column = 0)

        # Keeping track of the currently selected method in the dropdown,
        #   in order to pass the correct values to the backend upon 
        #   the user confirming their action.
        global method_name
        method_name = methodvar.get().split(" ")[0]
        global method_type
        method_type = methodvar.get().split(" ")[1].split("(")[0]
        methodvar.trace_add("write", lambda *args: update_params())

        # Confirm Button, command is the helper checking the user input
        #   and executing the appropriate function.
        btn = tk.Button(
            command = lambda: gf.b_rename_method(
                classvar.get(), current_method, entry2.get(), outputlabel),
            master = frame, text = "Confirm", font = ('bold'))
        btn.grid(row = 8, column = 0, padx = 5, pady = 5)

        # Thin Line Separator.
        separator = ttk.Separator(frame, orient = "horizontal")
        separator.grid(row = 9, column = 0, sticky = "ew")

        # Label for Program Output.
        outputlabel = tk.Label(frame, text = "")
        outputlabel.grid(row = 10, column = 0)

        # Bind the enter key to confirming the user's action, same as if they
        #   were to press the Confirm button.
        root.bind('<Return>', 
            lambda event: gf.b_rename_method(
                classvar.get(), current_method, entry2.get(), outputlabel))

    # Generate the window.
    root.mainloop()


def add_field_window() -> None:
    # Window for adding a Field to an existing Class in the system.
    root = tk.Toplevel(name = 'dn')
    root.title("Add Field")

    # Frame containing the elements.
    frame = tk.Frame(master = root, relief = tk.SUNKEN, borderwidth = 3)
    frame.pack()

    # Check to see if there are any classes.
    #   Does not allow the user to continue if no classes exist yet.
    if len(UMLClass.class_dict) == 0:
        label1 = tk.Label(frame, text = "There are no classes in the system.", font = ('bold'))
        label1.grid(row = 0, column = 0)
        label2 = tk.Label(frame, text = "Please add some classes first.", font = ('bold'))
        label2.grid(row = 1, column = 0)

    else:
        # List of classes in the current system.
        classes = []
        for class_name in UMLClass.class_dict:
            classes.append(class_name)

        # Label: Select a Class.
        classlabel = tk.Label(frame, text = "Select a Class: ", font = ('bold'))
        classlabel.grid(row = 0, column = 0)

        # Creating the classes dropdown.
        classvar = tk.StringVar(frame)
        classvar.set(list(UMLClass.class_dict)[0]) # Default value.
        class_dropdown = tk.OptionMenu(frame, classvar, *classes)
        class_dropdown.config(width = 20) # Set the width of the dropdown.
        class_dropdown.grid(row = 1, column = 0)

        # Label/Entry for Field Name.
        label1 = tk.Label(frame, text = "Field Name :", font = ('bold'))
        label1.grid(row = 2, column = 0)
        entry1 = tk.Entry(frame, width = 50)
        entry1.grid(row = 3, column = 0)

        # Label/Entry for Field Type.
        label2 = tk.Label(frame, text = "Field Type :", font = ('bold'))
        label2.grid(row = 4, column = 0)
        entry2 = tk.Entry(frame, width = 50)
        entry2.grid(row = 5, column = 0)

        # Confirm Button, command is the helper checking the user input
        #   and executing the appropriate function.
        btn = tk.Button(
            command = lambda: gf.b_add_field(
                classvar.get(), entry1.get(), entry2.get(), outputlabel),
            master = frame, text = "Confirm", font = ('bold'))
        btn.grid(row = 6, column = 0, padx = 5, pady = 5)

        # Thin Line Separator.
        separator = ttk.Separator(frame, orient = "horizontal")
        separator.grid(row = 7, column = 0, sticky = "ew")

        # Label for Program Output.
        outputlabel = tk.Label(frame, text = "")
        outputlabel.grid(row = 8, column = 0)

        # Bind the enter key to confirming the user's action, same as if they
        #   were to press the Confirm button.
        root.bind('<Return>', 
            lambda event: gf.b_add_field(
                classvar.get(), entry1.get(), entry2.get(), outputlabel))
    
    # Generate the window.
    root.mainloop()


def delete_field_window() -> None:
    # Window for deleting a Field from an existing Class in the system.
    root = tk.Toplevel(name = 'dn')
    root.title("Delete Field")

    # Frame containing the elements.
    frame = tk.Frame(master = root, relief = tk.SUNKEN, borderwidth = 3)
    frame.pack()

    # Check to see if there are any classes.
    #   Does not allow the user to continue if no classes exist yet.
    if len(UMLClass.class_dict) == 0:
        label1 = tk.Label(frame, text = "There are no classes in the system.", font = ('bold'))
        label1.grid(row = 0, column = 0)
        label2 = tk.Label(frame, text = "Please add some classes first.", font = ('bold'))
        label2.grid(row = 1, column = 0)

    else:
        # List of classes in the current system.
        classes = []
        for class_name in UMLClass.class_dict:
            classes.append(class_name)

        # Label: Select a Class.
        classlabel = tk.Label(frame, text = "Select a Class: ", font = ('bold'))
        classlabel.grid(row = 0, column = 0)

        # Creating the classes dropdown.
        classvar = tk.StringVar(frame)
        classvar.set(list(UMLClass.class_dict)[0]) # Default value.
        class_dropdown = tk.OptionMenu(frame, classvar, *classes)
        class_dropdown.config(width = 20) # Set the width of the dropdown.
        class_dropdown.grid(row = 1, column = 0)

        # Label/Entry for Field Name.
        label1 = tk.Label(frame, text = "Field Name :", font = ('bold'))
        label1.grid(row = 2, column = 0)
        entry1 = tk.Entry(frame, width = 50)
        entry1.grid(row = 3, column = 0)

        # Label/Entry for Field Type.
        label2 = tk.Label(frame, text = "Field Type :", font = ('bold'))
        label2.grid(row = 4, column = 0)
        entry2 = tk.Entry(frame, width = 50)
        entry2.grid(row = 5, column = 0)

        # Confirm Button, command is the helper checking the user input
        #   and executing the appropriate function.
        btn = tk.Button(
            command = lambda: gf.b_delete_field(
                classvar.get(), entry1.get(), entry2.get(), outputlabel),
            master = frame, text = "Confirm", font = ('bold'))
        btn.grid(row = 6, column = 0, padx = 5, pady = 5)

        # Thin Line Separator.
        separator = ttk.Separator(frame, orient = "horizontal")
        separator.grid(row = 7, column = 0, sticky = "ew")

        # Label for Program Output.
        outputlabel = tk.Label(frame, text = "")
        outputlabel.grid(row = 8, column = 0)

        # Bind the enter key to confirming the user's action, same as if they
        #   were to press the Confirm button.
        root.bind('<Return>', 
            lambda event: gf.b_delete_field(
                classvar.get(), entry1.get(), entry2.get(), outputlabel))
    
    # Generate the window.
    root.mainloop()


def rename_field_window() -> None:
    # Window for renaming a Field in an existing Class in the system.
    root = tk.Toplevel(name = 'dn')
    root.title("Rename Field")

    # Frame containing the elements.
    frame = tk.Frame(master = root, relief = tk.SUNKEN,  borderwidth = 3)
    frame.pack()

    # Check to see if there are any classes.
    #   Does not allow the user to continue if no classes exist yet.
    if len(UMLClass.class_dict) == 0:
        label1 = tk.Label(frame, text = "There are no classes in the system.", font = ('bold'))
        label1.grid(row = 0, column = 0)
        label2 = tk.Label(frame, text = "Please add some classes first.", font = ('bold'))
        label2.grid(row = 1, column = 0)

    else:
        # List of classes in the current system.
        classes = []
        for class_name in UMLClass.class_dict:
            classes.append(class_name)

        # Label: Select a Class.
        classlabel = tk.Label(frame, text = "Select a Class: ", font = ('bold'))
        classlabel.grid(row = 0, column = 0)

        # Creating the classes dropdown.
        classvar = tk.StringVar(frame)
        classvar.set(list(UMLClass.class_dict)[0]) # Default value.
        class_dropdown = tk.OptionMenu(frame, classvar, *classes)
        class_dropdown.config(width = 20) # Set the width of the dropdown.
        class_dropdown.grid(row = 1, column = 0)

        # Label/Entry for Old Field Name.
        label1 = tk.Label(frame, text = "Old Field Name :", font = ('bold'))
        label1.grid(row = 2, column = 0)
        entry1 = tk.Entry(frame, width = 50)
        entry1.grid(row = 3, column = 0)

        # Label/Entry for Old Field Type.
        label2 = tk.Label(frame, text = "Old Field Type :", font = ('bold'))
        label2.grid(row = 4, column = 0)
        entry2 = tk.Entry(frame, width = 50)
        entry2.grid(row = 5, column = 0)

        # Label/Entry for New Field Name.
        label3 = tk.Label(frame, text = "New Field Name :", font = ('bold'))
        label3.grid(row = 6, column = 0)
        entry3 = tk.Entry(frame, width = 50)
        entry3.grid(row = 7, column = 0)

        # Confirm Button, command is the helper checking the user input
        #   and executing the appropriate function.
        btn = tk.Button(
            command = lambda: gf.b_rename_field(
                classvar.get(), entry1.get(), entry2.get(), entry3.get(), outputlabel),
            master = frame, text = "Confirm", font = ('bold'))
        btn.grid(row = 8, column = 0, padx = 5, pady = 5)

        # Thin Line Separator.
        separator = ttk.Separator(frame, orient = "horizontal")
        separator.grid(row = 9, column = 0, sticky = "ew")

        # Label for Program Output.
        outputlabel = tk.Label(frame, text = "")
        outputlabel.grid(row = 10, column = 0)

        # Bind the enter key to confirming the user's action, same as if they
        #   were to press the Confirm button.
        root.bind('<Return>', 
            lambda event: gf.b_rename_field(
                classvar.get(), entry1.get(), entry2.get(), entry3.get(), outputlabel))
    
    # Generate the window.
    root.mainloop()


def add_relation_window() -> None:
    # Window for adding a Relationship between 2 Classes.
    root = tk.Toplevel(name = 'dn')
    root.title("Add Relation")

    # Frame containing the elements.
    frame = tk.Frame(master = root,  relief = tk.SUNKEN,  borderwidth = 3)
    frame.pack()

    # Label/Entry for Class 1 Name.
    label1 = tk.Label(frame, text = "Class 1 Name :", font = ('bold'))
    label1.grid(row = 0, column = 0)
    entry1 = tk.Entry(frame, width = 50)
    entry1.grid(row = 1, column = 0)

    # Label/Entry for Class 2 Name.
    label2 = tk.Label(frame, text = "Class 2 Name :", font = ('bold'))
    label2.grid(row = 2, column = 0)
    entry2 = tk.Entry(frame, width = 50)
    entry2.grid(row = 3, column = 0)

    # Creating the togglable buttons for the 4 types of Relationships.
    type = tk.IntVar()
    types = ["aggregation", "composition", "inheritance", "realization"]
    for index in range(len(types)):
        rdo = tk.Radiobutton(
            master = frame, text = types[index], value = index, variable = type, font = ('bold'))
        rdo.grid(row = 4 + index, column = 0)

    # Confirm Button, command is the helper checking the user input
    #   and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_add_relation(
            entry1.get(), entry2.get(), types[type.get()], outputlabel),
        master = frame, text = "Confirm", font = ('bold'))
    btn.grid(row = 8, column = 0, padx = 5, pady = 5)

    # Thin Line Separator.
    separator = ttk.Separator(frame, orient = "horizontal")
    separator.grid(row = 9, column = 0, sticky = "ew")

    # Label for Program Output.
    outputlabel = tk.Label(frame, text = "")
    outputlabel.grid(row = 10, column = 0)

    # Bind the enter key to confirming the user's action, same as if they
    #   were to press the Confirm button.
    root.bind('<Return>', 
        lambda event: gf.b_add_relation(
            entry1.get(), entry2.get(), types[type.get()], outputlabel))
    
    # Generate the window.
    root.mainloop()


def delete_relation_window() -> None:
    # Window for deleting a Relationship between 2 Classes.
    root = tk.Toplevel(name = 'dn')
    root.title("Delete Relation")

    # Frame containing the elements.
    frame = tk.Frame(master = root,  relief = tk.SUNKEN,  borderwidth = 3)
    frame.pack()

    # Label/Entry for Class 1 Name.
    label1 = tk.Label(frame, text = "Class 1 Name :", font = ('bold'))
    label1.grid(row = 0, column = 0)
    entry1 = tk.Entry(frame, width = 50)
    entry1.grid(row = 1, column = 0)

    # Label/Entry for Class 2 Name.
    label2 = tk.Label(frame, text = "Class 2 Name :", font = ('bold'))
    label2.grid(row = 2, column = 0)
    entry2 = tk.Entry(frame, width = 50)
    entry2.grid(row = 3, column = 0)

    # Confirm Button, command is the helper checking the user input
    #   and executing the appropriate function.
    btn = tk.Button(
        command = lambda: gf.b_delete_relation(
            entry1.get(), entry2.get(), outputlabel),
        master = frame, text = "Confirm", font = ('bold'))
    btn.grid(row = 4, column = 0, padx = 5, pady = 5)

    # Thin Line Separator.
    separator = ttk.Separator(frame, orient = "horizontal")
    separator.grid(row = 5, column = 0, sticky = "ew")

    # Label for Program Output.
    outputlabel = tk.Label(frame, text = "")
    outputlabel.grid(row = 6, column = 0)

    # Bind the enter key to confirming the user's action, same as if they
    #   were to press the Confirm button.
    root.bind('<Return>', 
        lambda event: gf.b_delete_relation(
            entry1.get(), entry2.get(), outputlabel))
    
    # Generate the window.
    root.mainloop()


def add_param_window() -> None:
    # Window for Adding a Parameter to a Method in a Class.
    root = tk.Toplevel(name = 'dn')
    root.title("Add Parameter")

    # Frame containing the elements.
    frame = tk.Frame(master = root,  relief = tk.SUNKEN,  borderwidth = 3)
    frame.pack()

    # Check to see if there are any classes.
    #   Does not allow the user to continue if no classes exist yet.
    if len(UMLClass.class_dict) == 0:
        label1 = tk.Label(frame, text = "There are no classes in the system.", font = ('bold'))
        label1.grid(row = 0, column = 0)
        label2 = tk.Label(frame, text = "Please add some classes first.", font = ('bold'))
        label2.grid(row = 1, column = 0)

    else:
        # List of classes in the current system.
        classes = []
        for class_name in UMLClass.class_dict:
            classes.append(class_name)

        # Label: Select a Class.
        classlabel = tk.Label(frame, text = "Select a Class: ", font = ('bold'))
        classlabel.grid(row = 0, column = 0)

        # Creating the classes dropdown.
        global classvar
        classvar = tk.StringVar(frame)
        classvar.set(list(UMLClass.class_dict)[0]) # Default value.
        class_dropdown = tk.OptionMenu(frame, classvar, *classes)
        class_dropdown.config(width = 20) # Set the width of the dropdown.
        class_dropdown.grid(row = 1, column = 0)

        # Label for Method Name.
        label1 = tk.Label(frame, text = "Old Method Name :", font = ('bold'))
        label1.grid(row = 2, column = 0)

        # Creating the list of methods associated with the currently selected class.
        methods = []
        uml : UMLClass.UMLClass = UMLClass.class_dict[classvar.get()]
        string = ""
        for method in uml.methods:
            string = ""
            string += method.name + " " + method.return_type + "("
            for param in method.params:
                if string[-1] != "(":
                    string = string + ","
                string += param.type + " " + param.name
            string += ")"
        methods.append(string)
        global methodvar
        methodvar = tk.StringVar()
        if len(methods) == 0:
            methodvar.set("No methods available")
        else:
            methodvar.set("Select a method")

        # Creating the methods dropdown.
        global method_dropdown
        method_dropdown = tk.OptionMenu(frame, methodvar, *methods)
        update_methods()
        classvar.trace_add('write', lambda *args: update_methods())
        method_dropdown.grid(row = 3, column = 0)

        # Keeping track of the currently selected method in the dropdown,
        #   in order to pass the correct values to the backend upon 
        #   the user confirming their action.
        global method_name
        method_name = methodvar.get().split(" ")[0]
        global method_type
        method_type = methodvar.get().split(" ")[1].split("(")[0]
        methodvar.trace_add("write", lambda *args: update_params())

        # Label/Entry for Param Name.
        label2 = tk.Label(frame, text = "Param Name :", font = ('bold'))
        label2.grid(row = 4, column = 0)
        entry2 = tk.Entry(frame, width = 50)
        entry2.grid(row = 5, column = 0)

        # Label/Entry for Param Type.
        label3 = tk.Label(frame, text = "Param Type :", font = ('bold'))
        label3.grid(row = 6, column = 0)
        entry3 = tk.Entry(frame, width = 50)
        entry3.grid(row = 7, column = 0)

        # Confirm Button, command is the helper checking the user input
        #   and executing the appropriate function.
        btn = tk.Button(
            command = lambda: gf.b_add_param(
                classvar.get(), current_method, entry2.get(), entry3.get(), outputlabel),
            master = frame, text = "Confirm", font = ('bold'))
        btn.grid(row = 8, column = 0, padx = 5, pady = 5)

        # Thin Line Separator.
        separator = ttk.Separator(frame, orient = "horizontal")
        separator.grid(row = 9, column = 0, sticky = "ew")

        # Label for Program Output.
        outputlabel = tk.Label(frame, text = "")
        outputlabel.grid(row = 10, column = 0)

        # Bind the enter key to confirming the user's action, same as if they
        #   were to press the Confirm button.
        root.bind('<Return>', 
            lambda event: gf.b_add_param(
                classvar.get(), current_method, entry2.get(), entry3.get(), outputlabel))
    
    # Generate the window.
    root.mainloop()


def delete_param_window() -> None:
   # Window for Deleting a Parameter from a Method in a Class.
    root = tk.Toplevel(name = 'dn')
    root.title("Delete Parameter")

    # Frame containing the elements.
    frame = tk.Frame(master = root,  relief = tk.SUNKEN,  borderwidth = 3)
    frame.pack()

    # Check to see if there are any classes.
    #   Does not allow the user to continue if no classes exist yet.
    if len(UMLClass.class_dict) == 0:
        label1 = tk.Label(frame, text = "There are no classes in the system.", font = ('bold'))
        label1.grid(row = 0, column = 0)
        label2 = tk.Label(frame, text = "Please add some classes first.", font = ('bold'))
        label2.grid(row = 1, column = 0)

    else:
        # List of classes in the current system.
        classes = []
        for class_name in UMLClass.class_dict:
            classes.append(class_name)

        # Label: Select a Class.
        classlabel = tk.Label(frame, text = "Select a Class: ", font = ('bold'))
        classlabel.grid(row = 0, column = 0)

        # Creating the classes dropdown.
        global classvar
        classvar = tk.StringVar(frame)
        classvar.set(list(UMLClass.class_dict)[0]) # Default value.
        class_dropdown = tk.OptionMenu(frame, classvar, *classes)
        class_dropdown.config(width = 20) # Set the width of the dropdown.
        class_dropdown.grid(row = 1, column = 0)

        # Label for Method Name.
        label1 = tk.Label(frame, text = "Old Method Name :", font = ('bold'))
        label1.grid(row = 2, column = 0)

        # Creating the list of methods associated with the currently selected class.
        methods = []
        uml : UMLClass.UMLClass = UMLClass.class_dict[classvar.get()]
        string = ""
        for method in uml.methods:
            string = ""
            string += method.name + " " + method.return_type + "("
            for param in method.params:
                if string[-1] != "(":
                    string = string + ","
                string += param.type + " " + param.name
            string += ")"
        methods.append(string)
        global methodvar
        methodvar = tk.StringVar()
        if len(methods) == 0:
            methodvar.set("No methods available")
        else:
            methodvar.set("Select a method")

        # Creating the methods dropdown.
        global method_dropdown
        method_dropdown = tk.OptionMenu(frame, methodvar, *methods)
        update_methods()
        classvar.trace_add('write', lambda *args: update_methods())
        method_dropdown.grid(row = 3, column = 0)

        # Keeping track of the currently selected method in the dropdown,
        #   in order to pass the correct values to the backend upon 
        #   the user confirming their action.
        global method_name
        method_name = methodvar.get().split(" ")[0]
        global method_type
        method_type = methodvar.get().split(" ")[1].split("(")[0]
        methodvar.trace_add("write", lambda *args: update_params())

        # Label/Entry for Param Name.
        label2 = tk.Label(frame, text = "Param Name :", font = ('bold'))
        label2.grid(row = 4, column = 0)
        entry2 = tk.Entry(frame, width = 50)
        entry2.grid(row = 5, column = 0)

        # Label/Entry for Param Type.
        label3 = tk.Label(frame, text = "Param Type :", font = ('bold'))
        label3.grid(row = 6, column = 0)
        entry3 = tk.Entry(frame, width = 50)
        entry3.grid(row = 7, column = 0)

        # Confirm Button, command is the helper checking the user input
        #   and executing the appropriate function.
        btn = tk.Button(
            command = lambda: gf.b_delete_param(
                classvar.get(), current_method, entry2.get(), entry3.get(), outputlabel),
            master = frame, text = "Confirm", font = ('bold'))
        btn.grid(row = 8, column = 0, padx = 5, pady = 5)

        # Thin Line Separator.
        separator = ttk.Separator(frame, orient = "horizontal")
        separator.grid(row = 9, column = 0, sticky = "ew")

        # Label for Program Output.
        outputlabel = tk.Label(frame, text = "")
        outputlabel.grid(row = 10, column = 0)

        # Bind the enter key to confirming the user's action, same as if they
        #   were to press the Confirm button.
        root.bind('<Return>', 
            lambda event: gf.b_delete_param(
                classvar.get(), current_method, entry2.get(), entry3.get(), outputlabel))

    # Generate the window.
    root.mainloop()


def rename_param_window() -> None:
   # Window for Renaming a Parameter in a Method in a Class.
    root = tk.Toplevel(name = 'dn')
    root.title("Rename Parameter")

    # Frame containing the elements.
    frame = tk.Frame(master = root,  relief = tk.SUNKEN,  borderwidth = 3)
    frame.pack()

    # Check to see if there are any classes.
    #   Does not allow the user to continue if no classes exist yet.
    if len(UMLClass.class_dict) == 0:
        label1 = tk.Label(frame, text = "There are no classes in the system.", font = ('bold'))
        label1.grid(row = 0, column = 0)
        label2 = tk.Label(frame, text = "Please add some classes first.", font = ('bold'))
        label2.grid(row = 1, column = 0)

    else:
        # List of classes in the current system.
        classes = []
        for class_name in UMLClass.class_dict:
            classes.append(class_name)

        # Label: Select a Class.
        classlabel = tk.Label(frame, text = "Select a Class: ", font = ('bold'))
        classlabel.grid(row = 0, column = 0)

        # Creating the classes dropdown.
        global classvar
        classvar = tk.StringVar(frame)
        classvar.set(list(UMLClass.class_dict)[0]) # Default value.
        class_dropdown = tk.OptionMenu(frame, classvar, *classes)
        class_dropdown.config(width = 20) # Set the width of the dropdown.
        class_dropdown.grid(row = 1, column = 0)

        # Label/Entry for Method Name.
        label1 = tk.Label(frame, text = "Old Method Name :", font = ('bold'))
        label1.grid(row = 2, column = 0)

        # Creating the list of methods associated with the currently selected class.
        methods = []
        uml : UMLClass.UMLClass = UMLClass.class_dict[classvar.get()]
        string = ""
        for method in uml.methods:
            string = ""
            string += method.name + " " + method.return_type + "("
            for param in method.params:
                if string[-1] != "(":
                    string = string + ","
                string += param.type + " " + param.name
            string += ")"
        methods.append(string)
        global methodvar
        methodvar = tk.StringVar()
        if len(methods) == 0:
            methodvar.set("No methods available")
        else:
            methodvar.set("Select a method")

        # Creating the methods dropdown.
        global method_dropdown
        method_dropdown = tk.OptionMenu(frame, methodvar, *methods)
        update_methods()
        classvar.trace_add('write', lambda *args: update_methods())
        method_dropdown.grid(row = 3, column = 0)

        # Keeping track of the currently selected method in the dropdown,
        #   in order to pass the correct values to the backend upon 
        #   the user confirming their action.
        global method_name
        method_name = methodvar.get().split(" ")[0]
        global method_type
        method_type = methodvar.get().split(" ")[1].split("(")[0]
        methodvar.trace_add("write", lambda *args: update_params())

        # Label/Entry for Old Param Name.
        label2 = tk.Label(frame, text = "Old Param Name :", font = ('bold'))
        label2.grid(row = 4, column = 0)
        entry2 = tk.Entry(frame, width = 50)
        entry2.grid(row = 5, column = 0)

        # Label/Entry for Param Type.
        label3 = tk.Label(frame, text = "Param Type :", font = ('bold'))
        label3.grid(row = 6, column = 0)
        entry3 = tk.Entry(frame, width = 50)
        entry3.grid(row = 7, column = 0)

        # Label/Entry for New Param Name.
        label4 = tk.Label(frame, text = "New Param Name :", font = ('bold'))
        label4.grid(row = 8, column = 0)
        entry4 = tk.Entry(frame, width = 50)
        entry4.grid(row = 9, column = 0)

        # Confirm Button, command is the helper checking the user input
        #   and executing the appropriate function.
        btn = tk.Button(
            command = lambda: gf.b_rename_param(
                classvar.get(), current_method, entry2.get(), entry3.get(), entry4.get(), outputlabel),
            master = frame, text = "Confirm", font = ('bold'))
        btn.grid(row = 10, column = 0, padx = 5, pady = 5)

        # Thin Line Separator.
        separator = ttk.Separator(frame, orient = "horizontal")
        separator.grid(row = 11, column = 0, sticky = "ew")

        # Label for Program Output.
        outputlabel = tk.Label(frame, text = "")
        outputlabel.grid(row = 12, column = 0)

        # Bind the enter key to confirming the user's action, same as if they
        #   were to press the Confirm button.
        root.bind('<Return>', 
            lambda event: gf.b_rename_param(
                classvar.get(), current_method, entry2.get(), entry3.get(), entry4.get(), outputlabel))

    # Generate the window.
    root.mainloop()


def save_window() -> None:
    # Window for Saving all the current data to a file.
    root = tk.Toplevel(name = 'dn')
    root.title("Save Data")

    # Frame containing the elements.
    frame = tk.Frame(master = root,  relief = tk.SUNKEN,  borderwidth = 3)
    frame.pack()

    #Get the save directory
    root.filename = filedialog.asksaveasfilename(defaultextension=".json", initialdir="/save_files", title="Choose a folder", filetypes=(('Json', '*.json'),('Json', '*.json')))

    if root.filename == "":
        root.destroy()
    else:
        root.lift()

        #Save warning label
        wlabel = tk.Label(
            frame, text = "Warning: Saving will overwrite\nany duplicate files.", font = ('bold'))
        wlabel.grid(row = 0, column = 0)

        # Label/Entry for File Name.
        label = tk.Label(frame, text = "File Name :", font = ('bold'))
        label.grid(row = 1, column = 0)

        # Confirm Button, command is the helper checking the user input
        #   and executing the appropriate function.
        btn = tk.Button(
            command = lambda: gf.b_save_file(root.filename, label),
            master = frame, text = "Confirm", font = ('bold'))
        btn.grid(row = 3, column = 0, padx = 5, pady = 5)

        # Thin Line Separator.
        separator = ttk.Separator(frame, orient = "horizontal")
        separator.grid(row = 4, column = 0, sticky = "ew")

        # Label for Program Output.
        outputlabel = tk.Label(frame, text = "")
        outputlabel.grid(row = 5, column = 0)

        # Bind the enter key to confirming the user's action, same as if they
        #   were to press the Confirm button.
        root.bind('<Return>', 
            lambda event: gf.b_save_file(root.filename, label))

    # Generate the window.
    root.mainloop()


def load_window() -> None:
    # Window for Loading data from an existing file.
    root = tk.Toplevel(name = 'dn')
    root.title("Load Data")

    # Frame containing the elements.
    frame = tk.Frame(master = root,  relief = tk.SUNKEN,  borderwidth = 3)
    frame.pack()

    # Label/Entry for warning about overwriting unsaved data.
    label = tk.Label(
        frame, text = "Warning: Loading will overwrite\nany unsaved changes.", font = ('bold'))
    label.grid(row = 0, column = 0)

    #Get the load path
    root.filename = filedialog.askopenfilename(initialdir="/save_files", title="Choose a file", filetypes=(('Json', '*.json'),('Json', '*.json')))

    if root.filename == "":
        root.destroy()
    else:
        root.lift()

        # Label/Entry for File Name.
        label1 = tk.Label(frame, text = "Open File: " + root.filename + "?", font = ('bold'))
        label1.grid(row = 1, column = 0)

        # Confirm Button, command is the helper checking the user input
        #   and executing the appropriate function.
        btn = tk.Button(
            command = lambda: gf.b_load_file(root.filename, label),
            master = frame, text = "Confirm", font = ('bold'))
        btn.grid(row = 3, column = 0, padx = 5, pady = 5)

        # Thin Line Separator.
        separator = ttk.Separator(frame, orient = "horizontal")
        separator.grid(row = 4, column = 0, sticky = "ew")

        # Label for Program Output.
        outputlabel = tk.Label(frame, text = "")
        outputlabel.grid(row = 5, column = 0)

        # Bind the enter key to confirming the user's action, same as if they
        #   were to press the Confirm button.
        root.bind('<Return>', 
            lambda event: gf.b_load_file(root.filename, label))

    # Generate the window.
    root.mainloop()


def export_window() -> None:
    # Window for Loading data from an existing file.
    root = tk.Toplevel(name = 'dn')
    root.title("Export Image")

    # Frame containing the elements.
    frame = tk.Frame(master = root,  relief = tk.SUNKEN,  borderwidth = 3)
    frame.pack()

    #Get the folder to save the export in
    root.filename = filedialog.asksaveasfilename(defaultextension=".png", initialdir="/saved_images", title="Choose a folder", filetypes=(('PNG', '*.png'),('JPG', '*.jpg')))

    if root.filename == "":
        root.destroy()
    else:
        root.lift()

        # Label/Entry for warning about overwriting unsaved data.
        label = tk.Label(
            frame, text = "Warning: Saving duplicate file names will\noverride previous ones.", font = ('bold'))
        label.grid(row = 0, column = 0)

        # Label/Entry for File Name.
        label1 = tk.Label(frame, text = "File Name :", font = ('bold'))
        label1.grid(row = 1, column = 0)

        # Confirm Button, command is the helper checking the user input
        #   and executing the appropriate function.
        btn = tk.Button(
            command = lambda: gf.b_export(root.filename, label),
            master = frame, text = "Confirm", font = ('bold'))
        btn.grid(row = 3, column = 0, padx = 5, pady = 5)

        # Thin Line Separator.
        separator = ttk.Separator(frame, orient = "horizontal")
        separator.grid(row = 4, column = 0, sticky = "ew")

        # Label for Program Output.
        outputlabel = tk.Label(frame, text = "")
        outputlabel.grid(row = 5, column = 0)

        # Bind the enter key to confirming the user's action, same as if they
        #   were to press the Confirm button.
        root.bind('<Return>', 
            lambda event: gf.b_export(root.filename, label))

    # Generate the window.
    root.mainloop()


###################################################################################################
'''
Helper functions for the secondary dropdowns in a few windows.

Needed because when you switch the currently selected option in a Class dropdown, 
    the secondary dropdown has to be updated to reflect the things contained
    within the currently selected class.
'''

def update_params():
    global method_name
    method_name = methodvar.get().split(" ")[0]
    global method_type
    method_type = methodvar.get().split(" ")[1].split("(")[0]
    uml : UMLClass.UMLClass = UMLClass.class_dict[classvar.get()]
    for method in uml.methods:
            string = ""
            string += method.name + " " + method.return_type + "("
            for param in method.params:
                if string[-1] != "(":
                    string = string + ","
                string += param.type + " " + param.name
            string += ")"
            if string == methodvar.get():
                global current_method
                current_method = method


def update_methods():
    menu = method_dropdown["menu"]
    menu.delete(0, "end")
    method_list = []
    uml : UMLClass.UMLClass = UMLClass.class_dict[classvar.get()]
    string = ""
    for method in uml.methods:
        string = ""
        string += method.name + " " + method.return_type + "("
        for param in method.params:
            if string[-1] != "(":
                string = string + ","
            string += param.type + " " + param.name
        string += ")"
        method_list.append(string)
    for strings in method_list:
            menu.add_command(label=strings, command=tk._setit(methodvar, strings))
    if len(method_list) == 0:
        methodvar.set("No methods available")
    else:
        methodvar.set("Select a method")


###################################################################################################
'''
# Entry Point
if __name__ == '__main__':
    main(sys.argv)

'''
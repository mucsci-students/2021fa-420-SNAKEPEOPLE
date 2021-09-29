# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     gui_application.py

# Imports:
import sys
import os.path

import tkinter as tk

def main(args : list) -> None:
    '''
    Main function for the program.

    Parameters:\n
    args : list -> A list of command-line arguments provided to the program.
    '''
    make_buttons()

###################################################################################################

def make_buttons() -> None:
    '''
    Function to make the buttons on the right side of the GUI:
        [Add       Class]  [Delete    Class]  [Rename    Class]
        [Add      Method]  [Delete   Method]  [Rename   Method]
        [Add       Field]  [Delete    Field]  [Rename    Field]
        [Add    Relation]  [Delete Relation] 
        [Save       File]  [Load       File]

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
        master = button_frame, 
        text = "Add Class", 
        width = 14
    )
    add_class_button.grid(
        row = 0, 
        column = 0, 
        sticky = "nw",
        padx = 5,
        pady = 5
    )

    # Delete Class Button
    delete_class_button = tk.Button(
        master = button_frame, 
        text = "Delete Class", 
        width = 14
    )
    delete_class_button.grid(
        row = 0, 
        column = 1, 
        sticky = "n",
        padx = 5,
        pady = 5
    )
    
    # Rename Class Button
    rename_class_button = tk.Button(
        master = button_frame, 
        text = "Rename Class", 
        width = 14
    )
    rename_class_button.grid(
        row = 0, 
        column = 2, 
        sticky = "ne",
        padx = 5,
        pady = 5
    )

    '''
    Row 2:

    [Add      Method]  [Delete   Method]  [Rename   Method]
    '''
    # Add Method Button
    add_method_button = tk.Button(
        master = button_frame, 
        text = "Add Method", 
        width = 14
    )
    add_method_button.grid(
        row = 1, 
        column = 0, 
        sticky = "nw",
        padx = 5,
        pady = 5
    )

    # Delete Method Button
    delete_method_button = tk.Button(
        master = button_frame, 
        text = "Delete Method", 
        width = 14
    )
    delete_method_button.grid(
        row = 1, 
        column = 1,
        padx = 5,
        pady = 5
    )
    
    # Rename Method Button
    rename_method_button = tk.Button(
        master = button_frame, 
        text = "Rename Method", 
        width = 14
    )
    rename_method_button.grid(
        row = 1, 
        column = 2, 
        sticky = "ne",
        padx = 5,
        pady = 5
    )

    '''
    Row 3:

    [Add       Field]  [Delete    Field]  [Rename    Field]
    '''
    # Add Field Button
    add_field_button = tk.Button(
        master = button_frame, 
        text = "Add Field", 
        width = 14
    )
    add_field_button.grid(
        row = 2, 
        column = 0, 
        sticky = "nw",
        padx = 5,
        pady = 5
    )

    # Delete Field Button
    delete_field_button = tk.Button(
        master = button_frame, 
        text = "Delete Field", 
        width = 14
    )
    delete_field_button.grid(
        row = 2, 
        column = 1,
        padx = 5,
        pady = 5
    )
    
    # Rename Method Button
    rename_field_button = tk.Button(
        master = button_frame, 
        text = "Rename Field", 
        width = 14
    )
    rename_field_button.grid(
        row = 2, 
        column = 2, 
        sticky = "ne",
        padx = 5,
        pady = 5
    )

    '''
    Row 4:

    [Add    Relation]  [Delete Relation]  
    '''
    # Add Relationship Button
    add_rel_button = tk.Button(
        master = button_frame, 
        text = "Add Relation", 
        width = 14
    )
    add_rel_button.grid(
        row = 3, 
        column = 0, 
        sticky = "nw",
        padx = 5,
        pady = 5
    )

    # Delete Relationship Button
    delete_rel_button = tk.Button(
        master = button_frame, 
        text = "Delete Relation", 
        width = 14
    )
    delete_rel_button.grid(
        row = 3, 
        column = 1,
        padx = 5,
        pady = 5
    )
    
    '''
    Row 5:

    [Save       File]  [Load       File]
    '''
    # Save Button
    save_button = tk.Button(
        master = button_frame, 
        text = "Save File", 
        width = 14
    )
    save_button.grid(
        row = 4, 
        column = 0, 
        sticky = "nw",
        padx = 5,
        pady = 5
    )

    # Load Button
    load_button = tk.Button(
        master = button_frame, 
        text = "Load File", 
        width = 14
    )
    load_button.grid(
        row = 4, 
        column = 1,
        padx = 5,
        pady = 5
    )


    # Generate the window
    window.mainloop()

###################################################################################################

# Entry Point
if __name__ == '__main__':
    main(sys.argv)


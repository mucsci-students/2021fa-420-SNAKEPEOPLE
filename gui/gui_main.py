# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     gui_main.py

# External Imports
import tkinter as tk

# Internal Imports
from . import UMLBox

from . import (
    gui_functions, 
    gui_windows, 
    Side_Panel)
from uml_components import UMLClass

###################################################################################################
'''
Main function to create the GUI.
'''

def run():
    
    window = tk.Tk()
    window.title("Snake People UML Editor")
    window.state('zoomed')
    
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1,weight=1)
    window.grid_columnconfigure(1,weight=1)
    
    menubar = build_menu(window)
    window.config(menu=menubar)
    
    # Element Construction    
    main_frame = tk.Frame(window, bd=5, relief=tk.FLAT)
    side_frame = tk.Frame(window,)
    
    main_panel = UMLBox.init_canvas(main_frame)
    
    side_panel = Side_Panel.init_notebook(side_frame)
    
    
    # Element Placement
    main_frame.grid(
        row=0, 
        column=1, 
        sticky="nsew", 
        rowspan=2)
    main_frame.columnconfigure(1, weight=1)
    main_frame.rowconfigure(0,weight=1)
    
    side_frame.grid(
        row=0, 
        column=2,
        sticky="nse",
        rowspan=2)
    side_frame.columnconfigure(2, weight=1)
    side_frame.rowconfigure(0, weight=1)
    
    main_panel.grid(
        row=0, 
        column=1, 
        sticky="nsew", 
        rowspan=2)
    
    side_panel.grid(
        row = 0,
        column = 2,
        sticky = "nse",
        rowspan=2
    )
    
    window.mainloop()

###################################################################################################
'''
Clear the dictionary of classes.
'''

def clear_dict():
    UMLClass.class_dict = dict()
    UMLBox.test_canvas.delete("all")
    UMLBox.class_list = []

###################################################################################################
'''
Building the menus above the canvas.
'''

def build_menu(window : tk.Tk) -> tk.Menu:
    menubar = tk.Menu(window)

    menu_file = tk.Menu(menubar, tearoff = 0)
    menu_file.add_command(label = "New", command = clear_dict)
    menu_file.add_command(label = "Save", command = gui_windows.save_window)
    menu_file.add_command(label = "Load", command = gui_windows.load_window)
    menu_file.add_command(label = "Export", command = gui_windows.export_window)
    menu_file.add_separator()
    menu_file.add_command(label = "Exit", command = exit)
    menubar.add_cascade(label = "File", menu = menu_file)
    
    menu_edit = tk.Menu(menubar, tearoff=0)
    menu_edit.add_command(label = "Undo", command = gui_functions.b_undo)
    menu_edit.add_command(label = "Redo", command = gui_functions.b_redo)
    menubar.add_cascade(label = "Edit", menu = menu_edit)

    return menubar

###################################################################################################

if __name__ == "__main__":
    run()
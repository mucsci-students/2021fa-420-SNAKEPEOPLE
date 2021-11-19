# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     snake_uml.py

# External Imports
import JSON
from ntpath import realpath

import sys
import os.path
import tab_comp
#from typing import _Alias

# Internal Imports
from uml_components import (UMLClass, 
                            UMLRelationship,
                            UMLAttributes)
from uml_components.interfaces import (class_interface,
                                       rel_interface,
                                       attr_interface)
from gui import gui_main
from gui import ImageAdapter

def main(args : list) -> None:
    '''
    Main function for the program.

    Parameters:\n
    args : list -> A list of command-line arguments provided to the program.
    '''

    if len(args) == 2:
        # Enters CLI mode if the user selects CLI.
        if args[1] == "--cli":
            tab_comp.main()
        # Stops the program if the user selection is invalid.
        else:
            print("Invalid input.")
    # If the user does not pick either GUI or CLI, default to GUI.
    else:
        gui_main.run()
    

def check_inputs(cmd : list, num : int) -> bool:
    '''
    Checks if the number of arguments given matches the number of expected
    arguments for a given command.
    
    Parameters:\n
    - cmd : list -> a list of commands/arguments parsed from user input.
    - num : int -> the number of expected arguments
    
    return -> bool
    '''
    
    if len(cmd) != num:
        # If the number of given arguments does not match the number of expected
        # arguments, print an error and return False.
        print("<Invalid Arguments Error>\n" +
              f"{num - 1} arguments expected. {len(cmd) - 1} arguments " + 
              "received.")
        return False
    else:
        # Otherwise return True.
        return True


def help() -> None:
    '''
    Reads help information from a separate text file and prints it to the
    terminal window.
    '''
    
    with open("help.txt") as help:
        content = help.read()
        print(content)

def list_a_class(input : str) -> None:
    '''
    Given a class name, if the class exists in the system, printz the name of 
    the class and all the attributes it has.
    
    Parameters:\n
    - input : str -> the name of the class to be listed.
    '''
    
    if input in UMLClass.class_dict:
        # Accesses a class from the class dictionary, and prints it to the 
        # terminal.
        print(UMLClass.class_dict[input])
    else:
        # If the class does not exist in the class dictionary, prints an error.
        print(f"<Illegal Argument Error>: {input} does not exist as a class.")

def list_all_classes() -> None:
    '''
    Prints a list of all classes in the class dictionary and their attributes. 
    '''

    if len(UMLClass.class_dict) == 0:
        print("(none)")
    else:
        # Iterates through the class dictionary and prints each entry.
        for key in UMLClass.class_dict:
            print(UMLClass.class_dict[key])
        print()
 
def save(filename : str) -> str:
    classes = []
    relationship = []
    msg = ""
    c : UMLClass.UMLClass
    for c in list(UMLClass.class_dict.values()):
        classes.append(c.toJson())

    r : UMLRelationship.UMLRelationship
    for r in UMLRelationship.relationship_list:
        relationship.append(r.toJson())
        
    json_text = JSON.encode(classes, relationship)
    
    with open(f"save_files/{filename}.json", "w") as file:
        file.write(json_text)
        msg = "Saved Successfully"
    return msg
        
def load(filename : str) -> str:
    msg = ""
    json_text : str = ""
    try:
        with open(f"save_files/{filename}.json", "r") as file:
            file.seek(0)
            json_text = file.read()
            msg = "Loaded Successfully."
    except FileNotFoundError:
        msg = f"File {filename}.json does not exist."
    (UMLClass.class_dict, 
        UMLRelationship.relationship_list) = JSON.decode(json_text)
    return msg

# Entry Point
if __name__ == '__main__':
    main(sys.argv)
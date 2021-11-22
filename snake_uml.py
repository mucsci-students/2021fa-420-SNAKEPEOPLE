# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     snake_uml.py

# External Imports
import sys
import os

# Internal Imports
import JSON
from gui import gui_main
import tab_comp
from uml_components import UMLClass, UMLRelationship

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

def save(filename) -> str:
    return save_by_name(filename)
def save_by_name(filename : str) -> str:
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
        msg = f"Saved {filename}.json successfully"
    return msg

def save_by_path(filename: str, 
                 path: str) -> str:
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
    
    if not os.path.isdir(path):
        os.mkdir(path)
    
    fullpath = f"{path}/{filename}.json"
    with open(fullpath, "w") as file:
        file.write(json_text)
        msg = f"Saved {filename}.json successfully to {path}"
    return msg

def load_ex(path: str) -> str:
    msg: str = ""
    json_text: str = ""
    
    try:
        with open(path, "r") as file:
            file.seek(0)
            json_text = file.read()
            p_split = path.split("/")
            
            if p_split[-1].split(".")[-1].lower() != "json":
                return "<UML Load Error>: Unsupported file selected."
            
            msg = f"Loaded {p_split[-1]} Successfully.\n"
        (UMLClass.class_dict, 
         UMLRelationship.relationship_list) = JSON.decode(json_text)
    except FileNotFoundError:
        msg = f"<UML Load Error>: Unable to access file at {path}"
    return msg

def load(filename) -> str:
    return load_in(filename)
def load_in(filename: str) -> str:
    """
    Given a filename, loads a .json file from the programs internal save_files
    folder.
    """
    msg = ""
    json_text : str = ""
    try:
        with open(f"save_files/{filename}.json", "r") as file:
            file.seek(0)
            json_text = file.read()
            msg = f"Loaded {filename}.json Successfully.\n"
        (UMLClass.class_dict, 
         UMLRelationship.relationship_list) = JSON.decode(json_text)
    except FileNotFoundError:
        msg = f"File {filename}.json does not exist."
    return msg

# Entry Point
if __name__ == '__main__':
    main(sys.argv)
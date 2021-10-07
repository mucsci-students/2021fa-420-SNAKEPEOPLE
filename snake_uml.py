# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     snake_uml.py

# External Imports
import json
import sys
import os.path

# Internal Imports
# Internal Imports
from uml_components import (UMLClass, 
                            UMLRelationship,
                            UMLAttributes)
from uml_components.interfaces import (class_interface,
                                       rel_interface,
                                       attr_interface)
from gui import gui_main

def main(args : list) -> None:
    '''
    Main function for the program.

    Parameters:\n
    args : list -> A list of command-line arguments provided to the program.
    '''

    if len(args) == 2:
        # Enters CLI mode if the user selects CLI.
        if args[1] == "--cli":
            cli_loop()
        # Stops the program if the user selection is invalid.
        else:
            print("Invalid input.")
    # If the user does not pick either GUI or CLI, default to GUI.
    else:
        gui_main.run(UMLClass.class_dict)
        # gui_application.main(args)

def cli_loop() -> None:
    '''
    Processes an infinite loop waiting for a command from the user. Once input
    is given, executes a command, if valid.
    '''

    print("===============================================\n" +
          "|           Snake People UML Editor           |\n" +
          "===============================================\n" +
          "      Type 'help' for a list of commands.      \n" +
          "       Type 'exit' to close the program.       \n")
    
    aliases = {
        'exit' : ['exit', 'e',
                  'quit', 'q'],
        
        'addclass' : ['addclass'],
        
        'delclass' : ['delclass'],
        
        'renclass' : ['renclass'],
        
        'addrel' : ['addrel'],
        
        'delrel' : ['delrel'],
        
        'addattr' : ['addattr'],
        
        'delattr' : ['delattr'],
        
        'renattr' : ['renattr'],
        
        'listclass' : ['listclass'],
        
        'listrel' : ['listrel'],
        
        'save' : ['save'],
        
        'load' : ['load'],
        
        'help' : ['help'],
    }
    
    while True:
        
        cmd = input(">> ").split()
        
        if len(cmd) == 0:
            continue
        
        elif cmd[0] in aliases['exit']:
            break
        
        elif cmd[0] == 'addclass':
            if check_inputs(cmd, 2):
                class_interface.add_class(cmd[1])
            
        elif cmd[0] == 'delclass':
            if check_inputs(cmd, 2):
                class_interface.delete_class(cmd[1])
            
        elif cmd[0] == 'renclass':
            if check_inputs(cmd, 3):
                class_interface.rename_class(cmd[1], cmd[2])
                
        elif cmd[0] == 'addrel':
            if check_inputs(cmd, 4):
                rel_interface.add_relationship(cmd[1], cmd[2], cmd[3])
                
        elif cmd[0] == 'delrel':
            if check_inputs(cmd, 3):
                rel_interface.delete_relationship(cmd[1], cmd[2])
                
        elif cmd[0] == 'addfield':
            if check_inputs(cmd, 4):
                attr_interface.add_field(cmd[1], cmd[2], cmd[3])
                
        elif cmd[0] == 'addmethod':
            if check_inputs(cmd, 4):
                attr_interface.add_method(cmd[1], cmd[2], cmd[3])
                
        elif cmd[0] == 'delattr':
            if check_inputs(cmd, 3):
                attr_interface.delete_attribute(cmd[1], cmd[2])
                
        elif cmd[0] == 'renattr':
            if check_inputs(cmd, 4):
                attr_interface.rename_attribute(cmd[1], cmd[2], cmd[3])
                
        elif cmd[0] == 'listclass':
            if check_inputs(cmd, 2):
                if cmd[1] == 'all':
                    list_all_classes()
                else:
                    list_a_class(cmd[1])

        elif cmd[0] == 'listrel':
            rel_interface.list_relationships()
        
        elif cmd[0] == 'save':
            if check_inputs(cmd, 2):
                save_classes(cmd[1])
        
        elif cmd[0] == 'load':
            if check_inputs(cmd, 2):
                load_classes(cmd[1])
        
        elif cmd[0] == 'help':
            help()
        
        else:
            print("<Invalid Command Error>: " +
                  f"'{cmd[0]}' is not a valid command.\n" +
                  "Type 'help' for a list of valid commands.")
    

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
 
def save_classes(filename : str) -> str:
    '''
    Saves the dictionary of classes to a .json file.
    '''
    
    err = f"Saved {filename}."

    # Checks if the class dictionary is empty and prints an error if so.
    if len(UMLClass.class_dict) == 0:
        err = "Error: There are no classes in the class dictionary.\n" + "Save failed."
        print("Error: There are no classes in the class dictionary.\n" +
              "Save failed.")
    
    # Initializes a dictionary to store the information that will be converted
    # to JSON format.
    save_dict = dict()
    # Iterates through the dictionary of classes, encoding each entry into JSON
    for key in UMLClass.class_dict:
        # Encodes the UMLClass object stored as a value in the class dictionary
        # into an easily decodable JSON format.
        cls = jsonpickle.encode(UMLClass.class_dict[key])
        # Adds the JSON encoded object to 'save_dict' with the same key as in
        # 'class_dict'.
        save_dict.update({key : cls})
        
    # Opens a file stored in 'save_files/' where the JSON will be saved to.
    with open(f"save_files/{filename}.json", "w") as savefile:
        # Writes the contents of 'save_dict' as JSON to the file pointed to by 
        # 'savefile'.
        json.dump(save_dict, savefile)

    return err
        
def load_classes(filename : str) -> str:
    '''
    Loads the content of a .json file to the class dictionary.
    '''
    
    etr = f"Loaded {filename}."

    # Prints a warning that the current class dictionary will be overwritten 
    # upon load.
    print("Warning: Loading will overwrite any unsaved changes.")
    # Gets confirmation from user (default yes).
    cont = input("Continue loading? ([y]/n): ")
    
    # Checks if the user confirmed the load or not.
    if cont == "" or cont.lower() == "y":
        # If the user confirms the load, clears the class dictionary.
        UMLClass.class_dict.clear()

        # Checking that the file the user is trying to load is one that exists.
        if os.path.exists(f"save_files/{filename}.json"):
            # Intializes a new dictionary to store the loaded JSON data.
            load_dict = dict()
            # Opens 'classes.json' for reading, pointed to as 'loadfile'.
            with open(f"save_files/{filename}.json") as loadfile:
                # Loads the raw JSON into 'load_dict'
                load_dict = json.load(loadfile)
            
            # Iterates through the keys and values of 'load_dict'. 
            for key, value in load_dict.items():
                # Decodes the UMLClass objects and adds them as values to the class
                # dictionary.
                UMLClass.class_dict.update({key : jsonpickle.decode(value)})
        # If the file name doesn't exist, stops and tells the user.
        else:
            etr = "Load cancelled, please input the name of an existing file."
            print("Load cancelled, please input the name of an existing file.")

    else:
        # If load is not confirmed, print a cancellation message.
        print("Load cancelled.")

    return etr
 
# Entry Point
if __name__ == '__main__':
    main(sys.argv)

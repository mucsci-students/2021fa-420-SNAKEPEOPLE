# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     snake_uml.py

# External Imports
import JSON
from ntpath import realpath

import sys
import os.path
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
            cli_loop()
        # Stops the program if the user selection is invalid.
        else:
            print("Invalid input.")
    # If the user does not pick either GUI or CLI, default to GUI.
    else:
        gui_main.run()

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
                class_interface.rename_class(cmd[1], 
                                             cmd[2])
                
        elif cmd[0] == 'addrel':
            if check_inputs(cmd, 4):
                rel_interface.add_relationship(cmd[1], 
                                               cmd[2], 
                                               cmd[3])
                
        elif cmd[0] == 'delrel':
            if check_inputs(cmd, 3):
                rel_interface.delete_relationship(cmd[1], 
                                                  cmd[2])
                
        elif cmd[0] == 'addfield':
            if check_inputs(cmd, 4):
                attr_interface.add_field(cmd[1], 
                                         cmd[2], 
                                         cmd[3])
                
        elif cmd[0] == 'addmethod':
            if check_inputs(cmd, 4):
                attr_interface.add_method(cmd[1], 
                                          cmd[2], 
                                          cmd[3])
                
        elif cmd[0] == 'addparam':
            if check_inputs(cmd, 6):
                attr_interface.add_param(cmd[1], 
                                         cmd[2], 
                                         cmd[3], 
                                         cmd[4], 
                                         cmd[5])
                
        elif cmd[0] == 'delfield':
            if check_inputs(cmd, 3):
                attr_interface.delete_field(cmd[1], 
                                            cmd[2])
                
        elif cmd[0] == 'delmethod':
            if check_inputs(cmd, 4):
                attr_interface.delete_method(cmd[1], 
                                             cmd[2], 
                                             cmd[3])
                
        elif cmd[0] == 'renfield':
            if check_inputs(cmd, 4):
                attr_interface.rename_field(cmd[1], 
                                            cmd[2], 
                                            cmd[3])
                
        elif cmd[0] == 'renmethod':
            if check_inputs(cmd, 5):
                attr_interface.rename_method(cmd[1], 
                                             cmd[2], 
                                             cmd[3], 
                                             cmd[4])
                
        elif cmd[0] == 'renparam':
            if check_inputs(cmd, 4):
                attr_interface.rename_param(cmd[1], # Class Name
                                            cmd[2], # Method Name
                                            cmd[3], # Method Type
                                            cmd[4], # Old Param Name
                                            cmd[5]) # New Param Name
                
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
                save(cmd[1])
        
        elif cmd[0] == 'load':
            if check_inputs(cmd, 2):
                load(cmd[1])

        elif cmd[0] == 'export':
            if check_inputs(cmd, 2):
                adapter = ImageAdapter.ImageAdapter()
                adapter.export(cmd[1])
        
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
# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     snake_uml.py

# Imports:
import json
import jsonpickle
import sys

import uml_class
import relationships

def main(args : list) -> None:
    '''
    Processes an infinite loop waiting for a command from the user. Once input
    is given, executes a command, if valid.

    Parameters:\n
    args : list -> A list of command-line arguments provided to the program.
    '''
    
    print("=======================================\n" +
          "|       Snake People UML Editor       |\n" +
          "=======================================\n" +
          "  Type 'help' for a list of commands.\n")
    
    while True:
        
        cmd = input(">> ").split()
        
        if len(cmd) == 0:
            continue
        
        elif cmd[0] == 'exit' or cmd[0] == 'quit':
            break
        
        elif cmd[0] == 'addclass':
            if check_inputs(cmd, 2):
                uml_class.add_class(cmd[1])
            
        elif cmd[0] == 'delclass':
            if check_inputs(cmd, 2):
                uml_class.delete_class(cmd[1])
            
        elif cmd[0] == 'renclass':
            if check_inputs(cmd, 3):
                uml_class.rename_class(cmd[1], cmd[2])
                
        elif cmd[0] == 'addrel':
            if check_inputs(cmd, 3):
                relationships.add_relationship(cmd[1], cmd[2])
                
        elif cmd[0] == 'delrel':
            if check_inputs(cmd, 3):
                relationships.delete_relationship(cmd[1], cmd[2])
                
        elif cmd[0] == 'addattr':
            if check_inputs(cmd, 3):
                uml_class.add_attribute(cmd[1], cmd[2])
                
        elif cmd[0] == 'delattr':
            if check_inputs(cmd, 3):
                uml_class.delete_attribute(cmd[1], cmd[2])
                
        elif cmd[0] == 'renattr':
            if check_inputs(cmd, 4):
                uml_class.rename_attribute(cmd[1], cmd[2], cmd[3])
                
        elif cmd[0] == 'listclass':
            if check_inputs(cmd, 2):
                if cmd[1] == 'all':
                    list_all_classes()
                else:
                    list_a_class(cmd[1])
                    
        
        elif cmd[0] == 'listrel':
            relationships.list_relationships()
        
        elif cmd[0] == 'save':
            save_classes()
        
        elif cmd[0] == 'load':
            load_classes()
        
        elif cmd[0] == 'help':
            help()
        
        else:
            print("<Invalid Command Error>: " +
                  f"'{cmd[0]}' is not a valid command.\n" +
                  "Type 'help' for a list of valid commands.")
    

def check_inputs(cmd : list, num : int) -> bool:
    """
    Checks if the number of arguments given matches the number of expected
    arguments for a given command.
    
    Parameters:\n
    - cmd : list -> a list of commands/arguments parsed from user input.
    - num : int -> the number of expected arguments
    
    return -> bool
    """
    
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
    """
    Reads help information from a separate text file and prints it to the
    terminal window.
    """
    # Reading the information from the help file.
    help_file = open('help_stuff.txt')
    lines = help_file.readlines()

    # Printing everything from the help file.
    for line in lines:
        print(line)

    help_file.close()


def list_a_class(input : str) -> None:
    """
    Given a class name, if the class exists in the system, printz the name of 
    the class and all the attributes it has.
    
    Parameters:\n
    - input : str -> the name of the class to be listed.
    """
    
    if input in uml_class.class_dict:
        # Accesses a class from the class dictionary, and prints it to the 
        # terminal.
        print(uml_class.class_dict[input])
    else:
        # If the class does not exist in the class dictionary, prints an error.
        print(f"<Illegal Argument Error>: {input} does not exist as a class.")

def list_all_classes() -> None:
    """
    Prints a list of all classes in the class dictionary and their attributes. 
    """

    if len(uml_class.class_dict) == 0:
        print("(none)")
    else:
        # Iterates through the class dictionary and prints each entry.
        for key in uml_class.class_dict:
            print(uml_class.class_dict[key])
 
def save_classes() -> None:
    """
    Saves the dictionary of classes to a .json file.
    """
    
    # Checks if the class dictionary is empty and prints an error if so.
    if len(uml_class.class_dict) == 0:
        print("Error: There are no classes in the class dictionary.\n" +
              "Save failed.")
        return
    
    # Initializes a dictionary to store the information that will be converted
    # to JSON format.
    save_dict = dict()
    # Iterates through the dictionary of classes, encoding each entry into JSON
    for key in uml_class.class_dict:
        # Encodes the UMLClass object stored as a value in the class dictionary
        # into an easily decodable JSON format.
        cls = jsonpickle.encode(uml_class.class_dict[key])
        # Adds the JSON encoded object to 'save_dict' with the same key as in
        # 'class_dict'.
        save_dict.update({key : cls})
        
    # Opens a file stored in 'save_files/' where the JSON will be saved to.
    with open("save_files/classes.json", "w") as savefile:
        # Writes the contents of 'save_dict' as JSON to the file pointed to by 
        # 'savefile'.
        json.dump(save_dict, savefile)
        
def load_classes() -> None:
    """
    Loads the content of a .json file to the class dictionary.
    """
    
    # Prints a warning that the current class dictionary will be overwritten 
    # upon load.
    print("Warning: Loading will overwrite any unsaved changes.")
    # Gets confirmation from user (default yes).
    cont = input("Continue loading? ([y]/n): ")
    
    # Checks if the user confirmed the load or not.
    if cont == "" or cont.lower() == "y":
        # If the user confirms the load, clears the class dictionary.
        uml_class.class_dict.clear()
       
        # Intializes a new dictionary to store the loaded JSON data.
        load_dict = dict()
        # Opens 'classes.json' for reading, pointed to as 'loadfile'.
        with open("save_files/classes.json") as loadfile:
            # Loads the raw JSON into 'load_dict'
            load_dict = json.load(loadfile)
        
        # Iterates through the keys and values of 'load_dict'. 
        for key, value in load_dict.items():
            # Decodes the UMLClass objects and adds them as values to the class
            # dictionary.
            uml_class.class_dict.update({key : jsonpickle.decode(value)})
            
    else:
        # If load is not confirmed, print a cancellation message.
        print("Load cancelled.")
 
# Entry Point
if __name__ == '__main__':
    main(sys.argv)

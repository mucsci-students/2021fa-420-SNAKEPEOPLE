# Project:  SNAKE PEOPLE UML Editor
# File:     snake_uml.py
 
# Imports:
import json
import jsonpickle
import sys

import uml_class
import relationships
 
def main(args : list) -> None:
    '''
    The main function. Serves as a starting point for the program.
    
    Parameters:\n
    args : list -> A list of command-line arguments provided to the program.
    '''
    
    print("[ Snake People UML Editor ]")
    while True:
        # The string of user input, then is separated into a list of strings
        comm = input("SP-UML>> ")
        comm = comm.split()
 
        if comm[0] == 'add':
            # Adding a class to the system
            if comm[1] == 'class':
                uml_class.add_class(comm[2])
                print("Class added.")
            # Adding a relationship to the system
            elif comm[1] == 'relationship':
                relationships.add_relationship(comm[2], comm[3])
            # Adding an attribute to a class in the system
            elif comm[1] == 'attribute':
                uml_class.add_attribute(comm[2], comm[3])
            # If the user input after 'add' is not valid
            else:
                print('That command is not valid, please try again.')
                print('Type "help" for more assistance.')
            
 
        elif comm[0] == 'delete':
            # Deleting a class from the system
            if comm[1] == 'class':
                uml_class.delete_class(comm[2])
            # Deleting a relationship from the system
            elif comm[1] == 'relationship':
                relationships.delete_relationship(comm[2], comm[3])
            # Deleting an attribute from a class in the system
            elif comm[1] == 'attribute':
                uml_class.delete_attribute(comm[2], comm[3])
            # If the user input after 'delete' is not valid
            else:
                print('That command is not valid, please try again.')
                print('Type "help" for more assistance.')
        
        elif comm[0] == 'rename':
            # Renaming an existing class in the system
            if comm[1] == 'class':
                uml_class.rename_class(comm[2], comm[3])
            # Renaming an attribute of a class in the system
            elif comm[1] == 'attribute':
                uml_class.rename_attribute(comm[3], comm[2], comm[4])
            # If the user input after 'rename' is not valid
            else:
                print('That command is not valid, please try again.')
                print('Type "help" for more assistance.')
        
        elif comm[0] == 'load':
            load_classes()
        
        elif comm[0] == 'save':
            save_classes()
            
        elif comm[0] == 'list':
            # Check whether the user wants to list a single class, all classes,
            #     or all relationships
            if comm[1] == 'classes':
                list_all_classes()
 
            elif comm[1] == 'relations':
                relationships.list_relationships()
 
            else:
                list_a_class(comm[1])
            
        
        elif comm[0] == 'help':
            help()
        
        elif comm[0] == 'exit':
            break
 
        elif comm[0] == '':
            pass
 
        else:
            print('That command is not valid, please try again.')
            print('Type "help" for more assistance.')
 
 
 
# Pulls all the help information from a text file locally
def help() -> None:
    help_file = open('help_stuff.txt')
    lines = help_file.readlines()
    for line in lines:
        print(line)
    help_file.close()
 
 
# Given a class name, if the class exists in the system, print the name of the 
# class and all the attributes it has
def list_a_class(input : str) -> None:
    if input in uml_class.class_dict:
        print(uml_class.class_dict[input])
    else:
        print("The requested class does not exist.")
    
# Lists all the classes currently in the system, and all of their attributes
def list_all_classes() -> None:
    if len(uml_class.class_dict) == 0:
        print("No classes exist.")

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

# Project:  SNAKE PEOPLE UML Editor
# File:     snake_uml.py
 
# Imports:
import sys
import uml_class
import relationships
 
def main(args : list) -> None:
    '''
    The main function. Serves as a starting point for the program.
    
    Parameters:\n
    args : list -> A list of command-line arguments provided to the program.
    '''
    while True:
        # The string of user input, then is separated into a list of strings
        comm = input("How can I help you? ")
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
                old_class = uml_class.class_dict[comm[2]]
                uml_class.rename_class(old_class, comm[3])
            # Renaming an attribute of a class in the system
            elif comm[1] == 'attribute':
                uml_class.rename_attribute(comm[3], comm[2], comm[4])
            # If the user input after 'rename' is not valid
            else:
                print('That command is not valid, please try again.')
                print('Type "help" for more assistance.')
        
        elif comm[0] == 'load':
            # TODO
            pass
        
        elif comm[0] == 'save':
            # TODO
            pass
            
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
 
 
# Given a class name, if the class exists in the system, print the name
#     of the class and all the attributes it has
def list_a_class(input : str) -> None:
    if input in uml_class.class_dict:
        print("Class:")
        print(input)
        print("Attributes:")
        print(uml_class.class_dict[input].attr)

    else:
        print("The requested class does not exist.")
    
# Lists all the classes currently in the system, and all of their attributes
def list_all_classes() -> None:
    if len(uml_class.class_dict) == 0:
        print("No classes exist.")

    for key, value in uml_class.class_dict.items():
        print(key + " -- " + value)
 
 
 
 
# Entry Point
if __name__ == '__main__':
    main(sys.argv)

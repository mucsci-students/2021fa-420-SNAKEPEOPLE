# Project:  SNAKE PEOPLE UML Editor
# File:     snake_uml.py

# Imports:
import sys
from uml_class import class_dict

def main(args : list) -> None:
    '''
    The main function. Serves as a starting point for the program.
    
    Parameters:\n
    args : list -> A list of command-line arguments provided to the program.
    '''
    while True:
        comm = input("How can I help you? ")
        comm = comm.split()

        if comm[0] == 'add':
            # TODO
            pass

        elif comm[0] == 'delete':
            # TODO
            pass
        
        elif comm[0] == 'rename':
            # TODO
            pass
        
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
                # TODO
                pass

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




def help() -> None:
    '''
    The function 
    Pulls all the help information from a text file locally
    '''
    help_file = open('help_stuff.txt')
    lines = help_file.readlines()
    for line in lines:
        print(line)
    help_file.close()


# Given a class name, if the class exists in the system, print the name
#     of the class and all the attributes it has
def list_a_class(input : str) -> None:
    classes = class_dict
    if input in classes:
        print(input + "--" + classes[input])
    else:
        print("The requested class does not exist.")
    
# Lists all the classes currently in the system, and all of their attributes
def list_all_classes() -> None:
    classes = class_dict
    for key, value in classes.items():
        print(key + "--" + value)
 



# Entry Point
if __name__ == '__main__':
    main(sys.argv)
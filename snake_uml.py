# Project:  SNAKE PEOPLE UML Editor
# File:     snake_uml.py

# Imports:
import sys

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
            # TODO
            pass
        
        elif comm[0] == 'help':
            help()
        
        elif comm[0] == 'exit':
            break

        elif comm[0] == '':
            pass

        else:
            print('That command is not valid, please try again.')




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


# Entry Point
if __name__ == '__main__':
    main(sys.argv)
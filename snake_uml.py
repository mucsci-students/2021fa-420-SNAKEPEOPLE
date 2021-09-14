# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     snake_uml.py

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
        
        # The string of user input, then is separated into a list of strings.
        comm = input("How can I help you? ")
        comm = comm.split()

        # If the user wants to add something, checks whether the user wants
        #     to add a class, a relationship, or an attribute.
        if comm[0] == 'add':

            # Adding a class to the system.
            if comm[1] == 'class':
                uml_class.add_class(comm[2])
                print("Class added.")

            # Adding a relationship to the system.
            elif comm[1] == 'relationship':
                relationships.add_relationship(comm[2], comm[3])

            # Adding an attribute to a class in the system.
            elif comm[1] == 'attribute':
                uml_class.add_attribute(comm[2], comm[3])

            # If the user input after 'add' is not valid.
            else:
                print('That command is not valid, please try again.')
                print('Type "help" for more assistance.')


        # If the user wants to delete something, checks whether the user wants
        #     to delete a class, a relationship, or an attribute.
        elif comm[0] == 'delete':

            # Deleting a class from the system.
            if comm[1] == 'class':
                uml_class.delete_class(comm[2])

            # Deleting a relationship from the system.
            elif comm[1] == 'relationship':
                relationships.delete_relationship(comm[2], comm[3])

            # Deleting an attribute from a class in the system.
            elif comm[1] == 'attribute':
                uml_class.delete_attribute(comm[2], comm[3])

            # If the user input after 'delete' is not valid.
            else:
                print('That command is not valid, please try again.')
                print('Type "help" for more assistance.')


        # If the user wants to rename something, checks whether the user wants
        #     to rename a class or an attribute.
        elif comm[0] == 'rename':

            # Renaming an existing class in the system.
            if comm[1] == 'class':
                old_class = uml_class.class_dict[comm[2]]
                uml_class.rename_class(old_class, comm[3])

            # Renaming an attribute of a class in the system.
            elif comm[1] == 'attribute':
                uml_class.rename_attribute(comm[3], comm[2], comm[4])

            # If the user input after 'rename' is not valid.
            else:
                print('That command is not valid, please try again.')
                print('Type "help" for more assistance.')


        # If the user wants to load a JSON file.
        elif comm[0] == 'load':
            # TODO
            pass


        # If the user wants to save their work to a JSON file.
        elif comm[0] == 'save':
            # TODO
            pass


        # If the user wants to list something, checks whether the user wants
        #     to list a single class, all classes, or all relationships.
        elif comm[0] == 'list':
            
            # Lists all the classes in the system.
            if comm[1] == 'classes':
                list_all_classes()

            # Lists all the relationships in the system.
            elif comm[1] == 'relations':
                relationships.list_relationships()

            # Checks to see if the user typed anything after 'list', because
            #     they should be thrown an error if they did not.
            elif comm[1] == '' or comm[1] == None:
                print('That command is not valid, please try again.')
                print('Type "help" for more assistance.')

            # Lists a single user-defined class.
            else:
                list_a_class(comm[1])


        # If the user wants help, breaks off into the help function.
        elif comm[0] == 'help':
            help()


        # If the user wants to exit the program, exits the loop.
        elif comm[0] == 'exit':
            break


        # If the user hit enter without typing anything, continues the loop
        #     without doing anything.
        elif comm[0] == '':
            pass


        # At this point, every valid type of input was checked for, so throws
        #     an error to the user that whatever they typed is not valid.
        else:
            print('That command is not valid, please try again.')
            print('Type "help" for more assistance.')



# Pulls all the help information from a private text file.
def help() -> None:

    # Reading the information from the help file.
    help_file = open('help_stuff.txt')
    lines = help_file.readlines()

    # Printing everything from the help file.
    for line in lines:
        print(line)

    help_file.close()


# Given a class name, if the class exists in the system, print the name
#     of the class and all the attributes it has.
def list_a_class(input : str) -> None:

    if input in uml_class.class_dict:
        print(uml_class.class_dict[input].attr)

    else:
        print("The requested class does not exist.")

# Lists all the classes currently in the system, and all of their attributes.
def list_all_classes() -> None:

    # Checking if any classes are in the system, and printing an error to
    #     the user if there are none.
    if len(uml_class.class_dict) == 0:
        print("No classes exist.")

    # Printing all the classes in the system and their respective attributes.
    for key in uml_class.class_dict.items():
        print(uml_class.class_dict[key])


# Entry Point
if __name__ == '__main__':
    main(sys.argv)

import sys

import relationships
import uml_class

def main(args : list) -> None:
    
    header()
    
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
                    if len(uml_class.class_dict) > 0:
                        for entry in uml_class.class_dict:
                            print(uml_class.class_dict[entry])
                            print()
                else:
                    if cmd[1] in uml_class.class_dict:
                        print("=========================")
                        print(uml_class.class_dict[cmd[1]])
                        print("=========================")
                    else:
                        print("<Invalid Argument Error>: " + 
                              f"{cmd[1]} does not exist as the name of a class.")
                    
        
        elif cmd[0] == 'listrel':
            pass
        
        elif cmd[0] == 'save':
            pass
        
        elif cmd[0] == 'load':
            pass
        
        elif cmd[0] == 'help':
            pass
        
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
        print("<Invalid Arguments Error>\n" +
              f"{num - 1} arguments expected. {len(cmd) - 1} arguments " + 
              "received.")
        return False
    else:
        return True
        
def header() -> None:
    print("[ Snake People UML Editor ]")
    print("Type 'help' for a list of commands.\n")

if __name__ == "__main__":
    main(sys.argv)
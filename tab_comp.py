# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     tab_comp.py

# External Imports
import sys
import os.path
import keyboard

# Internal Imports
from uml_components import (UMLClass, 
                            UMLRelationship,
                            UMLAttributes)
from uml_components.interfaces import (class_interface,
                                       rel_interface,
                                       attr_interface)
from gui import gui_main
from snake_uml import *

# List of commands that can be tab completed.
valids = [
    'addclass', 
    'delclass', 
    'renclass', 

    'addrel', 
    'delrel',

    'addfield',
    'delfield',
    'renfield',

    'addmethod',
    'delmethod',
    'renmethod',

    'addparam',
    'delparam',
    'renparam',

    'listclass',
    'listrel',

    'export',
    'undo',
    'redo',
    'save',
    'load',
    'help'
]

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

#################################################################################

def cli_loop() -> None:
    '''
    Processes an infinite loop waiting for a command from the user. Once input
    is given, executes a command, if valid.
    '''

    # Addition to previous version of CLI mode, to do tab completion.
    cmd = []
    keyboard.add_hotkey('tab', when_tab, args=[cmd])

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
        
        elif cmd[0] == 'delparam':
            if check_inputs(cmd, 5):
                attr_interface.delete_param(cmd[1],
                                            cmd[2],
                                            cmd[3],
                                            cmd[4])
                
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
            if check_inputs(cmd, 6):
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
        
        elif cmd[0] == 'help':
            help()
        
        else:
            print("<Invalid Command Error>: " +
                  f"'{cmd[0]}' is not a valid command.\n" +
                  "Type 'help' for a list of valid commands.")
    
    keyboard.unhook_all_hotkeys()

def when_tab(command : list[str]):
    # If the user hasn't typed in anything, pressing tab should put in the 
    #   help command.
    if len(command) == 0:
        keyboard.write('\b\b\b\b\b\bhelp ')
        return

    # If the user has one word typed, aka the command, then we should try to
    #   tab complete the command if we can.
    elif len(command) == 1:
        word = command[0]
        
        # Conditionals checking for 'exit' command.
        if word[0] == 'e':
            if word in 'exit':
                keyboard.write('\b\b\b\b\bexit ')
                return
            else:
                return

        # Conditionals checking for 'quit' command (same as exit command).
        if word[0] == 'q':
            if word in 'quit':
                keyboard.write('\b\b\b\b\bquit ')
                return
            else:
                return

        # Conditionals checking for 'save' command.
        elif word[0] == 's':
            if word in 'save':
                keyboard.write('\b\b\b\b\bsave ')
                return
            else:
                return

        # Conditionals checking for 'undo' command.
        elif word[0] == 'u':
            if word in 'undo':
                keyboard.write('\b\b\b\b\bundo ')
                return
            else:
                return

        # Conditionals checking for 'help' command.
        elif word[0] == 'h':
            if word in 'help':
                keyboard.write('\b\b\b\b\bhelp ')
                return
            else:
                return

        # Conditionals checking for commands that start with 'l'.
        #   Defaults to 'listclass'.
        elif word[0] == 'l':
            if len(word) == 1:
                keyboard.write('\b\blistclass ')
                return
            else:
                if word in 'load':
                    keyboard.write('\b\b\b\b\bload ')
                else:
                    if len(word) <= 4 and word in 'list':
                        keyboard.write('\b\b\b\b\blistclass ')
                        return
                    elif word in 'listclass':
                        keyboard.write('\b\b\b\b\b\b\b\b\b\blistclass ')
                        return
                    elif word in 'listrel':
                        keyboard.write('\b\b\b\b\b\b\b\blistrel ')
                        return
                    else:
                        return

        # Conditionals checking for commands that start with 'a'.
        #   Defaults to 'addclass'.
        elif word[0] == 'a':
            if len(word) <= 3:
                keyboard.write('\b\b\b\baddclass ')
                return
            else:
                if word in 'addclass':
                    keyboard.write('\b\b\b\b\b\b\b\b\baddclass ')
                    return
                elif word in 'addrel':
                    keyboard.write('\b\b\b\b\b\b\baddrel ')
                    return
                elif word in 'addfield':
                    keyboard.write('\b\b\b\b\b\b\b\b\baddfield ')
                    return
                elif word in 'addmethod':
                    keyboard.write('\b\b\b\b\b\b\b\b\b\baddmethod ')
                    return
                elif word in 'addparam':
                    keyboard.write('\b\b\b\b\b\b\b\b\baddparam ')
                    return
                else:
                    return

        # Conditionals checking for commands that start with 'd'.
        #   Defaults to 'delclass'.
        elif word[0] == 'd':
            if len(word) <= 3:
                keyboard.write('\b\b\b\bdelclass ')
                return
            else:
                if word in 'delclass':
                    keyboard.write('\b\b\b\b\b\b\b\b\bdelclass ')
                    return
                elif word in 'delrel':
                    keyboard.write('\b\b\b\b\b\b\bdelrel ')
                    return
                elif word in 'delfield':
                    keyboard.write('\b\b\b\b\b\b\b\b\bdelfield ')
                    return
                elif word in 'delmethod':
                    keyboard.write('\b\b\b\b\b\b\b\b\b\bdelmethod ')
                    return
                elif word in 'delparam':
                    keyboard.write('\b\b\b\b\b\b\b\b\bdelparam ')
                    return
                else:
                    return

        # Conditionals checking for commands that start with 'r'.
        #   Defaults to 'renclass'.
        elif word[0] == 'r':
            if len(word) <= 3:
                keyboard.write('\b\b\b\brenclass ')
                return
            else:
                if word in 'redo':
                    keyboard.write('\b\b\b\b\bredo ')
                    return
                elif word in 'renclass':
                    keyboard.write('\b\b\b\b\b\b\b\b\brenclass ')
                    return
                elif word in 'renfield':
                    keyboard.write('\b\b\b\b\b\b\b\b\brenfield ')
                    return
                elif word in 'renmethod':
                    keyboard.write('\b\b\b\b\b\b\b\b\b\brenmethod ')
                    return
                elif word in 'renparam':
                    keyboard.write('\b\b\b\b\b\b\b\b\brenparam ')
                    return
                else:
                    return

    # If the user typed in a command and then an argument(s) for the command.
    #   If we wanted to implement tab completion for argument names, that would go here.
    else:
        return


def test():
    print("===============================================\n" +
          "|           Snake People UML Editor           |\n" +
          "===============================================\n" +
          "      Type 'help' for a list of commands.      \n" +
          "       Type 'exit' to close the program.       \n")
    keyboard.add_hotkey('tab', keyboard.write, args = ["\b\b\b\b\bnuts"])
    while True:
        cmd = input(">> ").split()
        
        if len(cmd) == 0:
            continue

        elif cmd[0] == 'exit':
            break

        else:
            continue

    keyboard.unhook_all_hotkeys()
'''    
    if(command == 'deez'):
        keyboard.write("\b\b\b\b\bnuts")
    else:
        keyboard.write("deez")
'''

def main():
    cli_loop()

#################################################################################

if __name__ == '__main__':
    main()
    #test()

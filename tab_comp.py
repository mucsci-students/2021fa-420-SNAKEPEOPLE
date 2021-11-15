# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     tab_comp.py

# External Imports
import sys
import os.path
import keyboard
import cmd
import readline
import pyreadline

# Internal Imports
from uml_components.interfaces import (class_interface as ci,
                                       rel_interface as ri,
                                       attr_interface as ai)
from gui import gui_main
import snake_uml

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
'''
Tesing stuff, dont pay attention, will delete later when not needed.
'''
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

#################################################################################

def main():
    TabComp().cmdloop()

class TabComp(cmd.Cmd):
    
    intro = ("===============================================\n" +
             "|           Snake People UML Editor           |\n" +
             "===============================================\n" +
             "      Type 'help' for a list of commands.      \n" +
             "       Type 'exit' to close the program.       \n")
    prompt = (">> ")

    #############################################################################

    # Doers => Do the action based on text entered.
    def do_addclass(
            self, 
            classname : str) -> None:
        '''
        NAME
            addclass
        SYNTAX
            addclass <class name>
        DESCRIPTION
            Add a new class to the system. The provided class name must not
            already exist in the system.
        '''
        ci.add_class(classname)


    def do_delclass(
            self, 
            classname : str) -> None:
        '''
        NAME
            delclass
        SYNTAX
            delclass <class name>
        DESCRIPTION
            Delete a class from the system forever. The provided class name must
            exist in the system in order to be deleted. When a class is deleted,
            all attributes attached to the class and all relationships associated
            with the class are also deleted.
        '''
        ci.delete_class(classname)


    def do_renclass(
            self,
            oldname : str,
            newname : str) -> None:
        '''
        NAME
            renclass
        SYNTAX
            renclass <class name> <new name>
        DESCRIPTION
            Rename an existing class that is in the system. All attributes
            attached to the class and all relationships associated with the class
            are also updated upon the renaming of the class.
        '''
        ci.rename_class(oldname, newname)


    def do_addrel(
            self, 
            source : str,
            dest : str, 
            type : str) -> None:
        '''
        NAME
            addrel
        SYNTAX
            addrel <source> <destination>
        DESCRIPTION
            Add a new relationship between two classes. Both the source class
            and the destination class specified by the user have to exist in
            the system.
        '''
        ri.add_relationship(source, dest, type)


    def do_delrel(
            self,
            source : str,
            dest : str) -> None:
        '''
        NAME
            delrel
        SYNTAX
            delrel <source> <destination>
        DESCRIPTION
            Delete a relationship between two classes in the system. Both
            user-specified class names must exist and must already have an
            existing relationship.
        '''
        ri.delete_relationship(source, dest)

    #############################################################################

    # Completers => Check for terminal text for tab completion
    def complete_addclass(self, text):
        if text:
            return [
                command for command in valids
                    if command.startswith(text)
            ]
        else:
            return valids


    def complete_addrel(self, text):
        if text:
            return [
                command for command in valids
                    if command.startswith(text)
            ]
        else:
            return valids


#################################################################################

if __name__ == '__main__':
    main()
    #test()
    #TabComp().cmdloop()

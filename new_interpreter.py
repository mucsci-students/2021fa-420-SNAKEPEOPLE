# External Imports
import json
from ntpath import realpath
import sys
import os.path
import cmd
from typing import _Alias
from relationships import list_relationships


# Internal Imports
from uml_components import (UMLClass, 
                            UMLRelationship,
                            UMLAttributes)
from uml_components.interfaces import (class_interface,
                                       rel_interface,
                                       attr_interface)
from gui import gui_main
    
aliases = ['addclass', 
                    'delclass', 
                    'renclass', 
                    'addrel', 
                    'delrel',
                    'addattr',
                    'delattr',
                    'renattr',
                    'listclass',
                    'listrel',
                    'save',
                    'load',
                    'help'
                    ]

#################################################################################

class SnakeREPL(cmd.Cmd):

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        self.default_delims = readline.get_completer_delims()
        super().__init__(completekey, stdin, stdout)
        
        #welcome message printed at the start of the program
        self.intro = (
            "===============================================\n" +
            "|           Snake People UML Editor           |\n" +
            "===============================================\n" +
            "      Type 'help' for a list of commands.      \n" +
            "       Type 'exit' to close the program.       \n")

        #string to be printed each time the user is asked for a new command
        self.prompt = 'SNAKEUML >> '
        

        #When printing help, these are used to format the output
        docHead = 'Type help for descriptions'
        doc_header = docHead
        
        ruler = '-'

        aliases = ['addclass', 
                    'delclass', 
                    'renclass', 
                    'addrel', 
                    'delrel',
                    'addattr',
                    'delattr',
                    'renattr',
                    'listclass',
                    'listrel',
                    'save',
                    'load',
                    'help'
                    ]
    
    

        
    def print_cmd_help(self, command):
        print(self.cmd_desc[command])

#################################################################################
    # Do functions
    # No command is created from these, they are standalone functions 
    #   that don't affect anything
    def do_add_class():
        pass

    def do_help(self, args):
        help()
    
    def do_exit(self, args):
        sys.exit()

    def do_clear(self, args):
        os.system('cls' if os.name == 'nt' else 'clear')

    def do_list_relationships(self, args):
        pass

    def do_save(self, args):
        pass

    def do_load(self, args):
        pass
    
    def do_undo(self, args):
        pass

    def do_undo(self, args):
        pass

    def do_redo(self, args):
        pass

    # Class doers
    def do_add_class(self, args):
        pass

    def do_delete_class(self, args):
        pass

    def do_rename_class(self, args):
        pass

    #relationship doers
    def do_add_relationship(self, args):
        pass

    def do_delete_relationship(self, args):
        pass

    def do_rename_relationship(self, args):
        pass

    #Method doers
    def do_add_method(self, args):
        pass

    def do_delete_method(self, args):
        pass

    def do_rename_method(self, args):
        pass

    #field doers
    def do_add_field(self, args):
        pass

    def do_delete_field(self, args):
        pass

    def do_rename_field(self, args):
        pass

    #parameter doers
    def do_add_parameter(self, args):
        pass

    def do_delete_parameters(self, args):
        pass

    def do_change_parameters(self, args):
        pass



#################################################################################

# These are help handlers that when called produce help text for the named command.
# The text will be static but it makes the formatting of the output cute.
# It is up to the help handler to actually output the help message
#   and not simply return the help text for handling elsewhere.
    def help_add_class(self, args):
        print ('\n'.join(['addclass [theclass]',
            'Add a class with the specified name']))

    def help_delete_class(self, args):
        print ('\n'.join(['delclass [theclass]',
            'Delete a class with the specified name']))

    def help_rename_class(self, args):
        print ('\n'.join(['renclass [theclass]',
            'Rename a class with the specified name']))
    
    def help_list_class(self, args):
        print ('\n'.join(['listclass [theclass]',
            'List class with specified name']))
#################################################################################

    # Complete Functions
    # Once the command is known, argument completion is 
    #   handled by methods with the prefix complete.x
    # When there is input text, complete.x() returns a list of commands
    #   that match. Otherwise the full list of commands is returned.
    def complete_add_class(self, text, line, begidx, endidx):
        if not text:
            completions = self.aliases[:]
        else:
            completions = [ f
                            for f in self.aliases
                            if f.startswith(text)
                            ]
        return completions

    def complete_delete_class(self, text, line, begidx, endidx):
        '''
        if text:
            return [
                address for address in aliases 
                if address.startswith(text)
            ]
        else:
            return aliases
        '''
        if not text:
            completions = self.aliases[:]
        else:
            completions = [ f 
                            for f in self.aliases
                            if f.startswith(text)
                            ]
        return completions
        

    def complete_rename_class(self, text, line, begidx, endidx):
        arg_completions = {
            
        }

    def complete_list_class(self, text, line, begidx, endidx):
        pass

    def complete_list_relationships(self, text, line, begidx, endidx):
        pass

    def complete_add_relationship(self, text, line, begidx, endidx):
        pass

    def complete_delete_relationship(self, text, line, begidx, endidx):
        pass

    def complete_rename_relationship(self, text, line, begidx, endidx):
        pass
    
    def complete_add_method(self, text, line, begidx, endidx):
        pass

    def complete_delete_method(self, text, line, begidx, endidx):
        pass

    def complete_rename_method(self, text, line, begidx, endidx):
        pass

    def complete_add_field(self, text, line, begidx, endidx):
        pass

    def complete_delete_field(self, text, line, begidx, endidx):
        pass

    def complete_rename_field(self, text, line, begidx, endidx):
        pass

    def complete_add_parameter(self, text, line, begidx, endidx):
        pass

    def complete_delete_parameter(self, text, line, begidx, endidx):
        pass

    def complete_change_parameter(self, text, line, begidx, endidx):
        pass

    def complete_save(self, text, line, begidx, endidx):
        pass

    def complete_load(self, text, line, begidx, endidx):
        pass



    
#################################################################################
    # repeatedly issue a prompt, accept the input, parse the input, and dispatch to acion methods 
    #   passing them the remainder of the line as argument. 

    #is the main processing loop of the interpreter. You can override it, 
    # but it is usually not necessary due to preloop() and postloop()
    def cmdloop(self, intro=None):
        print ('cmdloop(%s)') % intro
        return cmd.Cmd.cmdloop(self, intro)

    def preloop(self):
        print ('preloop()')
    
    def postloop(self):
        print ('postloop()')
        
    #Where the actual input line is parsed
    def parseline(self, line):
        print ('parseline(%s) =>') % line,
        ret = cmd.Cmd.parseline(self, line)
        print (ret)
        return ret
    
    #each iteration through cmdloop() calls onecmd() to dispatch
    #   the command to its processor
    def onecmd(self, line):
        readline.set_completer_delims(self.default_delims)

    #if the line is empty this is called. The default 
    def emptyline(self):
        pass
    
    #if no processor is found then default() is called
    def default(self, line):
        print ('default(%s)') % line
        return cmd.Cmd.default(self, line)
    
    #if the line contains a command first precmd() is called then 
    #   the processor is looked up and invoked
    def precmd(self, line):
        print ('precmd(%s)') % line
        return cmd.Cmd.precmd(self, line)
    
    #last item to be called
    def postcmd(self, stop, line):
        pass

    def help() -> None:
        with open("help.txt") as help:
            content = help.read()
            print(content)

#################################################################################

if __name__ == '__main__':
    SnakeREPL().cmdloop()
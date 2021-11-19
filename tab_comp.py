# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     tab_comp.py

# External Imports
import cmd
from uml_components.UMLAttributes import UMLField, UMLParameter
from uml_components.UMLClass import UMLClass, class_dict

# Internal Imports
from uml_components.interfaces import (
    class_interface as ci,
    rel_interface as ri,
    attr_interface as ai)

from gui import UMLSavepoint

from gui import ImageAdapter as ia

import queue

import snake_uml

################################################################################

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
    'help',
    'exit'
]

################################################################################

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
#
    def do_addclass(
            self, 
            arg : str) -> None:
        '''
        NAME
            addclass
        SYNTAX
            addclass <class name>
        DESCRIPTION
            Add a new class to the system. The provided class name must not
            already exist in the system.
        '''
        lst = arg.split()
        UMLSavepoint.save_point("cli")
        output = ci.add_class(lst[0])
        if(output[1].split(' ')[0] != "<Added" and UMLSavepoint.redo_stack.empty() == False):
            UMLSavepoint.undo_stack.get()
        if(output[1].split(' ')[0] == "<Added"):
            UMLSavepoint.clear_stack()
#
    def do_delclass(
            self, 
            arg : str) -> None:
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
        lst = arg.split()
        UMLSavepoint.save_point("cli")
        output = ci.delete_class(lst[0])
        if(output[1].split(' ')[0] != "<Deleted" and UMLSavepoint.redo_stack.empty() == False):
            UMLSavepoint.redo_stack.get()
        if(output[1].split(' ')[0] == "<Deleted"):
            UMLSavepoint.clear_stack()
#
    def do_renclass(
            self,
            arg : str) -> None:
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
        lst = arg.split()
        UMLSavepoint.save_point("cli")
        output = ci.rename_class(lst[0], lst[1])
        if(output[1].split(' ')[0] != "<Renamed" and UMLSavepoint.redo_stack.empty() == False):
            UMLSavepoint.redo_stack.get()
        if(output[1].split(' ')[0] == "<Renamed"):
            UMLSavepoint.clear_stack()
#
    def do_addrel(
            self, 
            arg : str) -> None:
        '''
        NAME
            addrel
        SYNTAX
            addrel <source> <destination> <type>
        DESCRIPTION
            Add a new relationship between two classes. Both the source class
            and the destination class specified by the user have to exist in
            the system. The relation type must be one of the following:
            "aggregation", "composition", "inheritance", "realization".
        '''
        lst = arg.split()
        UMLSavepoint.save_point("cli")
        output = ri.add_relationship(lst[0], lst[1], lst[2])
        if(output[1].split(' ')[0] == "<Added"):
            UMLSavepoint.clear_stack()
        if(output[1].split(' ')[0] != "<Added" and UMLSavepoint.redo_stack.empty() == False):
            UMLSavepoint.redo_stack.get()

    def do_delrel(
            self,
            arg : str) -> None:
        '''
        NAME
            delrel
        SYNTAX
            delrel <source> <destination> <type>
        DESCRIPTION
            Delete a relationship between two classes in the system. Both
            user-specified class names must exist and must already have an
            existing relationship. 
        '''
        lst = arg.split()
        UMLSavepoint.save_point("cli")
        output = ri.delete_relationship(lst[0], lst[1])
        if(output[1].split(' ')[0] != "<Deleted" and UMLSavepoint.redo_stack.empty() == False):
            UMLSavepoint.redo_stack.get()
        if(output[1].split(' ')[0] == "<Deleted"):
            UMLSavepoint.clear_stack()
#
    def do_addfield(
            self,
            arg : str) -> None:
        '''
        NAME
            addfield
        SYNTAX
            addfield <class name> <field name> <type>
        DESCRIPTION
            Adds a new field to a given class in the system. The class name must
            be one that exists in the system. The field must also not share a
            name with another field in the class.
        '''
        lst = arg.split()
        if len(lst) == 3:
            class_name = lst[0]
            field_name = lst[1]
            field_type = lst[2]
            
            UMLSavepoint.save_point("cli")
            output = ai.add_field(class_name, field_name, field_type)
            if(output[1].split(' ')[0] != "Successfully" and UMLSavepoint.redo_stack.empty() == False):
                UMLSavepoint.redo_stack.get()
            if(output[1].split(' ')[0] == "Successfully"):
                UMLSavepoint.clear_stack()
        else:
            print(f"Invalid Arguments Error: Expected 3, received {len(lst)}")
#
    def do_delfield(
            self,
            arg : str) -> None:
        '''
        NAME
            delfield
        SYNTAX
            delfield <class_name> <field name>
        DESCRIPTION
            Deletes a field from a class in the system. The class name and field 
            name must both be ones that exist in the system, and the field must be
            in the specified class.
        '''
        lst = arg.split()
        if len(lst) == 2:
            class_name = lst[0]
            field_name = lst[1]
            
            UMLSavepoint.save_point("cli")
            
            uml : UMLClass = class_dict[class_name]
            field = uml.get_field(field_name)
            output = ai.delete_field(class_name, field)
            
            if(output[1].split(' ')[0] != "Successfully" and UMLSavepoint.redo_stack.empty() == False):
                UMLSavepoint.redo_stack.get()
            if(output[1].split(' ')[0] == "Successfully"):
                UMLSavepoint.clear_stack()
        else:
            print(f"Invalid Arguments Error: Expected 2, received {len(lst)}")
#
    def do_renfield(
            self,
            arg : str) -> None:
        '''
        NAME
            renfield
        SYNTAX
            renfield <class name> <field name> <new name>
        DESCRIPTION
            Renames an existing field in a class in the system. The class name and
            current field name must both exist in the system, and the current field
            must be in the specified class. The new field name must not be one that
            already exists in that class.
        '''
        lst = arg.split()
        if len(lst) == 3:
            class_name = lst[0]
            field_name = lst[1]
            new_name = lst[2]
            
            uml : UMLClass = class_dict[class_name]
            field = uml.get_field(field_name)
            
            UMLSavepoint.save_point("cli")
            output = ai.rename_field(class_name, field, new_name)
            
            if(output[1].split(' ')[0] != "Successfully" and UMLSavepoint.redo_stack.empty() == False):
                UMLSavepoint.redo_stack.get()
            if(output[1].split(' ')[0] == "Successfully"):
                UMLSavepoint.clear_stack()
#
    def do_addmethod(
            self,
            arg : str) -> None:
        '''
        NAME
            addmethod
        SYNTAX
            addmethod <class name> <method name> <method return type> 
        DESCRIPTION
            Adds a new method to a given class in the system. The class name must
            be one that exists in the system. The method must also not share a
            combination of the same name and return type as another method in the
            class. 
            
            -p, --params
                Arguments following this flag pre-add parameters to the method.
                SYNTAX
                    <param name> <param_type> ...

        '''
        flags = {"-p", "--params"}
        
        lst = arg.split()
        if len(lst) >= 3:
            class_name = lst[0]
            method_name = lst[1]
            return_type = lst[2]
            
            if len(lst) >= 3:
                
                
                UMLSavepoint.save_point("cli")
                output = ai.add_method(class_name, method_name, return_type)
                if(output[1].split(' ')[0] != "Successfully" and UMLSavepoint.redo_stack.empty() == False):
                    UMLSavepoint.redo_stack.get()
                if(output[1].split(' ')[0] == "Successfully"):
                    UMLSavepoint.clear_stack()
                    
            elif lst[3] in pf and len(lst[4:]) % 2 == 0:
                
                params_raw = lst[4:]
                param_lst = []
                while params_raw != []:
                    p_name = params_raw[0]
                    p_type = params_raw[1]
                    param = UMLParameter(p_name, p_type)
                    param_lst.append(param)
                    params_raw.pop(0)
                    params_raw.pop(0)
                    
                UMLSavepoint.save_point("cli")
                output = ai.add_method(class_name, method_name, return_type, param_lst)
                if(output[1].split(' ')[0] != "Successfully" and UMLSavepoint.redo_stack.empty() == False):
                    UMLSavepoint.redo_stack.get()
                if(output[1].split(' ')[0] == "Successfully"):
                    UMLSavepoint.clear_stack()
                
#
    def do_delmethod(
            self,
            arg : str) -> None:
        '''
        NAME
            delmethod
        SYNTAX
            delmethod <class name> <method name> <method return type>
        DESCRIPTION
            Deletes a method from a class in the system. The class name and method
            name must both be ones that exist in the system, and the method must be
            in the specified class, with the specified method type.
        '''
        lst = arg.split()
        UMLSavepoint.save_point("cli")
        output = ai.delete_method(lst[0], lst[1], lst[2])
        if(output[1].split(' ')[0] != "Successfully" and UMLSavepoint.redo_stack.empty() == False):
            UMLSavepoint.redo_stack.get()
        if(output[1].split(' ')[0] == "Successfully"):
            UMLSavepoint.clear_stack()
#
    def do_renmethod(
            self,
            arg : str) -> None:
        '''
        NAME
            renmethod
        SYNTAX
            renmethod <class name> <method name> <method return type> <new name>
        DESCRIPTION
            Renames an existing method in a class in the system. The class name and
            current method name must both exist in the system, and the current
            method must be in the specified class with the specified type. The new
            method name must not be one that exists in that class already.
        '''
        lst = arg.split()
        UMLSavepoint.save_point("cli")
        output = ai.rename_method(lst[0], lst[1], lst[2], lst[3])
        if(output[1].split(' ')[0] != "Successfully" and UMLSavepoint.redo_stack.empty() == False):
            UMLSavepoint.redo_stack.get()
        if(output[1].split(' ')[0] == "Successfully"):
            UMLSavepoint.clear_stack()

    def do_addparam(
            self,
            arg : str) -> None:
        '''
        NAME
            addparam
        SYNTAX
            addparam <class name> <method name> <method type> <param name> <param type>
        DESCRIPTION
            Adds a parameter to a method in the system. The specified class name
            must have the method with the method type. The param name with the
            specified type must not already exist in that method.
        '''
        lst = arg.split()
        UMLSavepoint.save_point("cli")
        output = ai.add_param(lst[0], lst[1], lst[2], lst[3], lst[4])
        if(output[1].split(' ')[0] != "Successfuly" and UMLSavepoint.redo_stack.empty() == False):
            UMLSavepoint.redo_stack.get()
        if(output[1].split(' ')[0] == "Successfully"):
            UMLSavepoint.clear_stack()
#
    def do_delparam(
            self,
            arg : str) -> None:
        '''
        NAME
            delparam
        SYNTAX
            delparam <class_name> <method name> <method type> <param name>
        DESCRIPTION
            Deletes a parameter from a method in the system. The specified class
            name must have the method with the method type, and the param with the
            method.
        '''
        lst = arg.split()
        UMLSavepoint.save_point("cli")
        output = ai.delete_param(lst[0], lst[1], lst[2], lst[3])
        if(output[1].split(' ')[0] != "Successfuly" and UMLSavepoint.redo_stack.empty() == False):
            UMLSavepoint.redo_stack.get()
        if(output[1].split(' ')[0] == "Successfully"):
            UMLSavepoint.clear_stack()
#
    def do_renparam(
            self,
            arg : str) -> None:
        '''
        NAME
            renparam
        SYNTAX
            renparam <class_name> <method name> <method type> <param name> <new name>
        DESCRIPTION
            Renames an existing parameter in a method in the system. The specified
            class name must have the method with the method type. The new param
            name must not be one that exists in the method already.
        '''
        lst = arg.split()
        UMLSavepoint.save_point("cli")
        output = ai.rename_param(lst[0], lst[1], lst[2], lst[3], lst[4])
        if(output[1].split(' ')[0] != "Successfuly" and UMLSavepoint.redo_stack.empty() == False):
            UMLSavepoint.redo_stack.get()
        if(output[1].split(' ')[0] == "Successfully"):
            UMLSavepoint.clear_stack()
#
    def do_listclass(
            self,
            arg : str) -> None:
        '''
        NAME
            listclass
        SYNTAX
            listclass <input>
        DESCRIPTION
            If the user inputs 'all' as the input, list all the classes in the current
            system, as well as their contents. If the user inputs the name of a class
            in the system, lists the contents of the specified class.
        '''
        lst = arg.split()
        if input == 'all':
            snake_uml.list_all_classes()
        else:
            snake_uml.list_a_class(lst[0])
#
    def do_listrel(
            self) -> None:
        '''
        NAME
            listrel
        SYNTAX
            listrel
        DESCRIPTION
            List all the relationships that exist between classes in the
            current system.
        '''
        ri.list_relationships()
#
    def do_export(
            self,
            arg : str) -> None:
        '''
        NAME
            export
        SYNTAX
            export <filename>
        DESCRIPTION
            Export a picture of the current UML to the user's PC, setting the
            name of the new image file to the user-inputted name.
        '''
        lst = arg.split()
        ia.save_as_png(lst[0])
#
    def do_undo(
            self) -> None:
        '''
        NAME
            undo
        SYNTAX
            undo
        DESCRIPTION
            Undo the last performed action, returning the UML to the state it was
            previously at.
        '''
        if UMLSavepoint.undo_stack.empty() == False:
            UMLSavepoint.undo("cli")
#
    def do_redo(
            self) -> None:
        '''
        NAME
            redo
        SYNTAX
            redo
        DESCRIPTION
            Redo the last action that was undid by the user.
        '''
        if UMLSavepoint.redo_stack.empty() == False:
            UMLSavepoint.redo("cli")
#
    def do_save(
            self,
            arg : str) -> None:
        '''
        NAME
            save
        SYNTAX
            save <filename>
        DESCRIPTION
            Saves the current work to a JSONfile, with a user-specified name.
        '''
        lst = arg.split()
        snake_uml.save(lst[0])
#
    def do_load(
            self,
            arg : str) -> None:
        '''
        NAME
            load
        SYNTAX
            load <filename>
        DESCRIPTION
            Load a JSONfile, providing a name of an existing file.
        '''
        lst = arg.split()
        output = snake_uml.load(lst[0])
        if UMLSavepoint.undo_stack.empty() == False:
            UMLSavepoint.undo_stack = queue.LifoQueue()
        if UMLSavepoint.redo_stack.empty() == False:
            UMLSavepoint.clear_stack()
#
    def do_exit(self, s) -> bool:
        '''
        NAME
            exit
        SYNTAX
            exit
        DESCRIPTION
            Quit the program.
        '''
        return True


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

    def complete_delclass(self, text):
        if text:
            return [
                command for command in valids
                    if command.startswith(text)
            ]
        else:
            return valids

    def complete_renclass(self, text):
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

    def complete_delrel(self, text):
        if text:
            return [
                command for command in valids
                    if command.startswith(text)
            ]
        else:
            return valids

    def complete_addfield(self, text):
        if text:
            return [
                command for command in valids 
                    if command.startswith(text)
            ]
        else:
            return valids
        
    def complete_delfield(self, text):
        if text:
            return [
                command for command in valids
                    if command.startswith(text)
            ]
        else:
            return valids

    def complete_renfield(self, text):
        if text:
            return [ 
                command for command in valids
                    if command.startswith(text)
            ]
        else:
            return valids

    def complete_addmethod(self, text):
        if text:
            return [
                command for command in valids
                    if command.startswith(text)
            ]
        else:
            return valids

    def complete_delmethod(self, text):
        if text:
            return [
                command for command in valids
                    if command.startswith(text)
            ]
        else:
            return valids

    def complete_renmethod(self, text):
        if text:
            return [ 
                command for command in valids
                    if command.startswith(text)
            ]
        else:
            return valids

    def complete_addparam(self, text):
        if text:
            return [
                command for command in valids
                    if command.startswith(text)
            ]
        else:
            return valids

    def complete_delparam(self, text):
        if text:
            return [
                command for command in valids   
                    if command.startswith(text)
            ]
        else: 
            return valids

    def complete_renparam(self, text):
        if text:
            return [ 
                command for command in valids
                    if command.startswith(text)
            ]
        else:
            return valids
    
    def complete_listclass(self, text):
        if text:
            return [ 
                command for command in valids
                    if command.startswith(text)
            ]
        else: 
            return valids

    def complete_listrel(self, text):
        if text:
            return [ 
                command for command in valids  
                    if command.startswith(text)
            ]
        else:
            return valids
        
    def complete_export(self, text):
        if text:
            return [ 
                command for command in valids
                    if command.startswith(text)
            ]
        else: 
            return valids

    def complete_undo(self, text):
        if text:
            return [ 
                command for command in valids
                    if command.startswith(text)
            ]
        else:
            return valids
        
    def complete_redo(self, text):
        if text:
            return [ 
                command for command in valids
                    if command.startswith(text)
            ]
        else:
            return valids
    
    def complete_save(self, text):
        if text:
            return [ 
                command for command in valids   
                    if command.startswith(text)
            ]
        else:
            return valids
    
    def complete_load(self, text):
        if text:
            return [ 
                command for command in valids
                    if command.startswith(text)
            ]
        else:
            return valids

    def complete_exit(self, text):
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

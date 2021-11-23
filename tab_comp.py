# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     tab_comp.py

# External Imports
import cmd
from os.path import isdir, isfile
import queue
from sys import exit
from typing import List

# Internal Imports
from uml_components.UMLAttributes import (UMLField, UMLMethod, 
                                          UMLParameter)
from uml_components import UMLClass, UMLRelationship
from uml_components.interfaces import (class_interface as ci,
                                       rel_interface as ri,
                                       attr_interface as ai)
from gui import (UMLSavepoint,
                 ImageAdapter as ia,)
import snake_uml

################################################################################

# List of commands that can be tab completed.
valids = ['addclass', 'delclass', 'renclass', 
          'addrel', 'delrel',
          'addfield', 'delfield', 'renfield',
          'addmethod', 'delmethod', 'renmethod',
          'addparam', 'delparam', 'renparam',
          'listclass', 'listrel',
          'undo', 'redo',
          'save', 'load', 'export',
          'help',
          'exit',]

################################################################################

def main():
    TabComp().cmdloop()
    
def check_args(expected: int, received: int) -> None:
    if not expected == received:
        print("Invalid Arguments Error: " + 
              f"Expected {expected}, Received {received}")

class TabComp(cmd.Cmd):
    
    intro = ("===========================================================\n" +
             "|                                                         |\n" +
             "|                 Snake People UML Editor                 |\n" +
             "|                                                         |\n" +
             "===========================================================\n" +
             "            Type 'help' for a list of commands.            \n" +
             "             Type 'exit' to close the program.             \n")
    prompt = ("SP.UML>> ")

    #############################################################################

    # Doers => Do the action based on text entered.
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
        if len(lst) == 1:
            UMLSavepoint.save_point("cli")
            output = ci.add_class(lst[0])
            if (output[1].split(' ')[0] != "<Added" and 
                UMLSavepoint.redo_stack.empty() == False):
                UMLSavepoint.undo_stack.get()
            if (output[1].split(' ')[0] == "<Added"):
                UMLSavepoint.clear_stack()
        else:
            check_args(1, len(lst))

    def do_delclass(self, 
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
        if len(lst) == 1:
            UMLSavepoint.save_point("cli")
            output = ci.delete_class(lst[0])
            
            if (output[1].split(' ')[0] != "<Deleted" and 
                UMLSavepoint.redo_stack.empty() == False):
                UMLSavepoint.redo_stack.get()
            if (output[1].split(' ')[0] == "<Deleted"):
                UMLSavepoint.clear_stack()
        else:
            check_args(1, len(lst))

    def do_renclass(self,
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
        if len(lst) == 2:
            # Assigns the arguments to variables with more readable names.
            class_name: str = lst[0]
            new_name: str = lst[1]
            
            UMLSavepoint.save_point("cli")
            output = ci.rename_class(class_name, new_name)
            
            if(output[1].split(' ')[0] != "<Renamed" and 
               UMLSavepoint.redo_stack.empty() == False):
                UMLSavepoint.redo_stack.get()
            if(output[1].split(' ')[0] == "<Renamed"):
                UMLSavepoint.clear_stack()
        else:
            check_args(2, len(lst))

    def do_addrel(self, 
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
        if len(lst) == 3:
            # Assigns the arguments to variables with more readable names.
            source: str = lst[0]
            dest: str = lst[1]
            rel_type: str = lst[2]
            
            UMLSavepoint.save_point("cli")
            output = ri.add_relationship(source, dest, rel_type)
            
            if(output[1].split(' ')[0] == "<Added"):
                UMLSavepoint.clear_stack()
            if(output[1].split(' ')[0] != "<Added" and 
               UMLSavepoint.redo_stack.empty() == False):
                UMLSavepoint.redo_stack.get()
        else:
            check_args(3, len(lst))

    def do_delrel(self,
                  arg : str) -> None:
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
        lst = arg.split()
        if len(lst) == 2:
            # Assigns the arguments to variables with more readable names.
            source: str = lst[0]
            dest: str = lst[1]
            
            UMLSavepoint.save_point("cli")
            output = ri.delete_relationship(source, dest)
            
            if(output[1].split(' ')[0] != "<Deleted" and 
               UMLSavepoint.redo_stack.empty() == False):
                UMLSavepoint.redo_stack.get()
            if(output[1].split(' ')[0] == "<Deleted"):
                UMLSavepoint.clear_stack()
        else:
            check_args(2, len(lst))
#
    def do_addfield(self,
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
            # Assigns the arguments to variables with more readable names.
            class_name = lst[0]
            field_name = lst[1]
            field_type = lst[2]
            
            UMLSavepoint.save_point("cli")
            output = ai.add_field(class_name, field_name, field_type)
            
            if(output[1].split(' ')[0] != "Successfully" and 
               UMLSavepoint.redo_stack.empty() == False):
                UMLSavepoint.redo_stack.get()
            if(output[1].split(' ')[0] == "Successfully"):
                UMLSavepoint.clear_stack()
        else:
            check_args(3, len(lst))
#
    def do_delfield(self,
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
            # Assigns the arguments to variables with more readable names.
            class_name: str = lst[0]
            field_name: str = lst[1]
            
            uml : UMLClass.UMLClass = UMLClass.class_dict[class_name]
            field = uml.get_field(field_name)
            
            if field:
                UMLSavepoint.save_point("cli")
                output = ai.delete_field(class_name, field)
                
                if (output[1].split(' ')[0] != "Successfully" and 
                    UMLSavepoint.redo_stack.empty() == False):
                    UMLSavepoint.redo_stack.get()
                if(output[1].split(' ')[0] == "Successfully"):
                    UMLSavepoint.clear_stack()
        else:
            check_args(2, len(lst))
#
    def do_renfield(self,
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
            # Assigns the arguments to variables with more readable names.
            class_name: str = lst[0]
            field_name: str = lst[1]
            new_name: str = lst[2]
            
            uml : UMLClass.UMLClass = UMLClass.class_dict[class_name]
            field = uml.get_field(field_name)
            
            if field:
                UMLSavepoint.save_point("cli")
                output = ai.rename_field(class_name, field, new_name)
                print(output[1])
                
                if (output[1].split(' ')[0] != "Successfully" and 
                    UMLSavepoint.redo_stack.empty() == False):
                    UMLSavepoint.redo_stack.get()
                if (output[1].split(' ')[0] == "Successfully"):
                    UMLSavepoint.clear_stack()
        else:
            check_args(3, len(lst))

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
            
            FLAGS
            -p, --params
                Arguments following this flag pre-add parameters to the method.
                SYNTAX
                    <param name> <param_type> ...

        '''
        flags = {"-p", "--params"}
        
        lst = arg.split()
        if len(lst) >= 3:
            # Assigns the arguments to variables with more readable names.
            class_name: str = lst[0]
            method_name: str = lst[1]
            return_type: str = lst[2]
            param_list: List = []
            output = "default"
            
            if len(lst) >= 4: 
                if lst[3] in flags:
                    params_raw = lst[4:]

                    # Checks if the number of arguments after the flag is evenly
                    # divisible by 2. 
                    if len(params_raw) >= 2 and len(params_raw) % 2 == 0:
                        # Loops through the last n arguments, initializing
                        # UMLParameter objects and adding them to a list to be
                        # passed to the 'add_method' function.
                        while params_raw != []:
                            # Isolate the first two arguments in the list of
                            # remaining arguments.
                            p_name = params_raw[0]
                            p_type = params_raw[1]
                            # Initialize a UMLParameter object.
                            param = UMLParameter(p_name, p_type)
                            # Adds the UMLParameter to the list being passed to
                            # the 
                            param_list.append(param)
                            del params_raw[:2]
                            
                        UMLSavepoint.save_point("cli")
                        output = ai.add_method(class_name, method_name,
                                               return_type, param_list)
                        if (output[1].split(' ')[0] != "Successfully" and
                            UMLSavepoint.redo_stack.empty() == False):
                            UMLSavepoint.redo_stack.get()
                        if (output[1].split(' ')[0] == "Successfully"):
                            UMLSavepoint.clear_stack()
                    else:
                        check_args(len(lst) - 1, len(lst))
                else:
                    check_args(3, len(lst))
            else:
                UMLSavepoint.save_point("cli")
                output = ai.add_method(class_name, method_name, return_type, 
                                       param_list)
                if (output[1].split(' ')[0] != "Successfully" and
                    UMLSavepoint.redo_stack.empty() == False):
                    UMLSavepoint.redo_stack.get()
                if (output[1].split(' ')[0] == "Successfully"):
                    UMLSavepoint.clear_stack()
            
        else:
            check_args(3, len(lst))
    
    @staticmethod  
    def select_method(method_name: str,
                      method_type: str,
                      method_list: List, 
                      op: str) -> int:
        print(f"Multiple methods with name {method_name} and type " +
              f"{method_type}.\n")
        counter = 1
        for method in method_list:
            print("   " + str(counter) + ":   " + str(method))
            counter += 1
        sel = int(input(f"\nPlease select a method to {op}: "))
        if sel <= 0 or sel > len(method_list):
            print("Invalid Selection: Operation Aborted.")
            return -1
        return sel

    def do_delmethod(self,
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
        if len(lst) == 3:
            # Assigns the arguments to variables with more readable names.
            class_name: str = lst[0]
            method_name: str = lst[1]
            method_type: str = lst[2]
            
            uml : UMLClass.UMLClass = UMLClass.class_dict[class_name]
            method_list: List[UMLMethod] = [
                m for m in uml.methods if (m.name == method_name and
                                           m.return_type == method_type)
                ]
            
            if len(method_list) == 1:
                UMLSavepoint.save_point("cli")
                output = ai.delete_method(class_name, method_list[0])
                
                if(output[1].split(' ')[0] != "Successfully" and 
                   UMLSavepoint.redo_stack.empty() == False):
                    UMLSavepoint.redo_stack.get()
                if(output[1].split(' ')[0] == "Successfully"):
                    UMLSavepoint.clear_stack()
                    
            elif len(method_list) > 1:
                sel = self.select_method(method_name, method_type, method_list, 
                                         "delete") - 1
                if sel >= 0:
                    UMLSavepoint.save_point("cli")
                    output = ai.delete_method(class_name, method_list[sel])
                    
                    if(output[1].split(' ')[0] != "Successfully" and 
                       UMLSavepoint.redo_stack.empty() == False):
                        UMLSavepoint.redo_stack.get()
                    if(output[1].split(' ')[0] == "Successfully"):
                        UMLSavepoint.clear_stack()
        
        else:
            check_args(3, len(lst))
                
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
        if len(lst) == 4:
            # Assigns the arguments to variables with more readable names.
            class_name: str = lst[0]
            method_name: str = lst[1]
            method_type: str = lst[2]
            new_name: str = lst[3]
            
            uml : UMLClass.UMLClass = UMLClass.class_dict[class_name]
            method_list: List[UMLMethod] = [
                m for m in uml.methods if (m.name == method_name and
                                           m.return_type == method_type)
                ]
            
            if len(method_list) == 1:
                UMLSavepoint.save_point("cli")
                output = ai.rename_method(class_name, method_list[0], new_name)
                
                if(output[1].split(' ')[0] != "Successfully" and 
                   UMLSavepoint.redo_stack.empty() == False):
                    UMLSavepoint.redo_stack.get()
                if(output[1].split(' ')[0] == "Successfully"):
                    UMLSavepoint.clear_stack()
                    
            else:
                sel = self.select_method(method_name, method_type, method_list, 
                                         "rename") - 1
                if sel >= 0:
                    UMLSavepoint.save_point("cli")
                    output = ai.rename_method(class_name, method_list[sel], 
                                              new_name)
                    
                    if(output[1].split(' ')[0] != "Successfully" and 
                    UMLSavepoint.redo_stack.empty() == False):
                        UMLSavepoint.redo_stack.get()
                    if(output[1].split(' ')[0] == "Successfully"):
                        UMLSavepoint.clear_stack()
            
        else:
            check_args(4, len(lst))

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
        if len(lst) == 5:
            # Assigns the arguments to variables with more readable names.
            class_name: str = lst[0]
            method_name: str = lst[1]
            method_type: str = lst[2]
            param_name: str = lst[3]
            param_type: str = lst[4]
            
            uml : UMLClass.UMLClass = UMLClass.class_dict[class_name]
            method_list: List[UMLMethod] = [
                m for m in uml.methods if (m.name == method_name and
                                           m.return_type == method_type)
                ]
            
            if len(method_list) == 1:
                UMLSavepoint.save_point("cli")
                output = ai.add_param(class_name, method_list[0], param_name, 
                                      param_type)
                if(output[1].split(' ')[0] != "Successfuly" and 
                   UMLSavepoint.redo_stack.empty() == False):
                    UMLSavepoint.redo_stack.get()
                if(output[1].split(' ')[0] == "Successfully"):
                    UMLSavepoint.clear_stack()
                    
            elif len(method_list) > 1:
                sel = self.select_method(method_name, method_type, method_list, 
                                         "add parameter") - 1
                
                if sel >= 0:
                    UMLSavepoint.save_point("cli")
                    output = ai.add_param(class_name, method_list[sel], 
                                          param_name, param_type)
                    if(output[1].split(' ')[0] != "Successfuly" and 
                       UMLSavepoint.redo_stack.empty() == False):
                        UMLSavepoint.redo_stack.get()
                    if(output[1].split(' ')[0] == "Successfully"):
                        UMLSavepoint.clear_stack()
        else:
            check_args(5, len(lst))
        
#
    def do_delparam(self,
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
        if len(lst) == 4:
            # Assigns the arguments to variables with more readable names.
            class_name = lst[0]
            method_name = lst[1]
            method_type = lst[2]
            param_name = lst[3]
            
            uml: UMLClass.UMLClass = UMLClass.class_dict[class_name]
            
            # Generates a list of methods in 'uml' where the following 
            # conditions apply:
            #   1. The method's name matches the variable 'method_name'.
            #   2. The method's type matches the variable 'method_type'.
            #   3. There exists a UMLParameter object in the method whose name
            #          matches the variable 'param_name'.
            method_list: List[UMLMethod] = [
                m for m in uml.methods if (
                    m.name == method_name and
                    m.return_type == method_type and
                    param_name in [p.name for p in m.params])
                ]
            
            if len(method_list) == 1:
                param = method_list[0].get_param(param_name)
                if param:
                    UMLSavepoint.save_point("cli")
                    output = ai.delete_param(class_name, method_list[0], param)
                    if(output[1].split(' ')[0] != "Successfuly" and 
                    UMLSavepoint.redo_stack.empty() == False):
                        UMLSavepoint.redo_stack.get()
                    if(output[1].split(' ')[0] == "Successfully"):
                        UMLSavepoint.clear_stack()
            elif len(method_list) > 1:
                # Prompts user to select method from a list if multiple methods
                # have the same name and type.
                sel = self.select_method(method_name, method_type, method_list, 
                                         "delete parameter") - 1
                
                if sel >= 0:
                    param = method_list[sel].get_param(param_name)
                    
                    if param:
                        UMLSavepoint.save_point("cli")
                        output = ai.delete_param(class_name, method_list[sel], 
                                                 param)
                        if(output[1].split(' ')[0] != "Successfuly" and 
                        UMLSavepoint.redo_stack.empty() == False):
                            UMLSavepoint.redo_stack.get()
                        if(output[1].split(' ')[0] == "Successfully"):
                            UMLSavepoint.clear_stack()
            else:
                # Dummy call to ai.delete_param to invoke an error.
                ai.delete_param(class_name, 
                                UMLMethod(method_name, method_type), 
                                UMLParameter(param_name, ""))
        else:
            check_args(4, len(lst))
#
    def do_renparam(self,
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
        if len(lst) == 5:
            # Assigns the arguments to variables with more readable names.
            class_name = lst[0]
            method_name = lst[1]
            method_type = lst[2]
            param_name = lst[3]
            new_name = lst[4]
            
            uml: UMLClass.UMLClass = UMLClass.class_dict[class_name]
            
            # Generates a list of methods in 'uml' where the following 
            # conditions apply:
            #   1. The method's name matches the variable 'method_name'.
            #   2. The method's type matches the variable 'method_type'.
            #   3. There exists a UMLParameter object in the method whose name
            #          matches the variable 'param_name'.
            method_list: List[UMLMethod] = [
                m for m in uml.methods if (
                    m.name == method_name and
                    m.return_type == method_type and
                    param_name in [p.name for p in m.params])
                ]
            
            if len(method_list) == 1:
                param = method_list[0].get_param(param_name)
                if param:
                    UMLSavepoint.save_point("cli")
                    output = ai.rename_param(class_name, method_list[0], param, 
                                            new_name)
                    if(output[1].split(' ')[0] != "Successfuly" and 
                    UMLSavepoint.redo_stack.empty() == False):
                        UMLSavepoint.redo_stack.get()
                    if(output[1].split(' ')[0] == "Successfully"):
                        UMLSavepoint.clear_stack()
            
        
#
    def do_listclass(self,
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
        if len(lst) == 1:
            if lst[0] == 'all':
                snake_uml.list_all_classes()
            else:
                snake_uml.list_a_class(lst[0])
        else:
            check_args(1, len(lst))
#
    def do_listrel(self) -> None:
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
    def do_export(self,
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
        if len(lst) == 1:
            ia.save_as_png(lst[0])
        else:
            check_args(1, len(lst))
#
    def do_undo(self, arg = "") -> None:
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
    def do_redo(self, arg = "") -> None:
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
    def do_save(self,
                arg : str) -> None:
        '''
        NAME
            save
        SYNTAX
            save filename [<flag> <path>]
        DESCRIPTION
            Saves the current work to a JSONfile, with a user-specified name.
        '''
        flags = ["-p", "--path"]
        output = ""
        lst = arg.split()
        if len(lst) >= 1 and len(lst) <= 3:
            filename = lst[0]
            
            if len(lst) == 1:
                if isfile(f"save_files/{filename}.json"):
                    print(f"\n*** WARNING: {filename} already exists in "+
                        "internal save folder. ***")
                    ans = input(f"Would you like to overwrite {filename}? " + 
                                "([y]/n): ")
                    if ans.lower() == "n":
                        print("Save aborted.")
                        return
                    
                    output = snake_uml.save_by_name(filename)
            
            elif len(lst) == 3:
                flag = lst[1]
                if flag in flags:
                    path = lst[2]
                    
                    if isdir(path) and isfile(path + f"/{filename}.json"):
                        print(f"*** WARNING: {filename} already exists at " +
                              f"'{path}'")
                        ans = input("Would you like to overwrite " + 
                                    f"'{path}/{filename}.json'? ([y]/n): ")
                        if ans.lower() == "n":
                            print("Save aborted.")
                            return
                    
                    output = snake_uml.save_by_path(filename, path)
                    
            else:
                check_args(1, len(lst))
            
            print(f"{output}\n")
            
        else:
            check_args(1, len(lst))

    def do_load(self,
                arg : str) -> None:
        '''
        NAME
            load
        SYNTAX
            load <flag> [<file name> | <path to file>]
        DESCRIPTION
            Load a JSON file, providing the name or path of an existing file.
            
        FLAGS
            -e, --external
                SYNTAX
                    load [-e | --external] <path to file>
                DESCRIPTION
                    Indicates that a file is to be loaded from an external 
                    directory. A complete path to the file must be provided
                    after the flag.
                    
            -i, --internal
                SYNTAX
                    load [-i | --internal] <file name>
        '''
        lw: str = input("\n*** WARNING: Loading will overwrite any unsaved " +
                        "work. ***\n" +
                        "Continue? ([y]/n): ")
        if lw.lower() == "n":
            print("\nLoading aborted.\n")
            return
        
        flags = {"ext_load" : ['-e', '--external'],
                 "int_load" : ['-i', '--internal'],}
        
        lst = arg.split()
        output = ""
        if len(lst) == 2:
            flag = lst[0]
            if flag in flags["ext_load"]:
                path = lst[1]
                
                output = snake_uml.load_ex(path)
                if UMLSavepoint.undo_stack.empty() == False:
                    UMLSavepoint.undo_stack = queue.LifoQueue()
                if UMLSavepoint.redo_stack.empty() == False:
                    UMLSavepoint.clear_stack()
                
            elif flag in flags["int_load"]:
                filename = lst[1]
                
                output = snake_uml.load_in(filename)
                if UMLSavepoint.undo_stack.empty() == False:
                    UMLSavepoint.undo_stack = queue.LifoQueue()
                if UMLSavepoint.redo_stack.empty() == False:
                    UMLSavepoint.clear_stack()
                
        elif len(lst) == 1:
            filename = lst[0]
                
            output = snake_uml.load_in(filename)
            if UMLSavepoint.undo_stack.empty() == False:
                UMLSavepoint.undo_stack = queue.LifoQueue()
            if UMLSavepoint.redo_stack.empty() == False:
                UMLSavepoint.clear_stack()
        else:
            check_args(1, len(lst))
        print(output)
#
    def do_exit(self, s) -> None:
        '''
        NAME
            exit
        SYNTAX
            exit
        DESCRIPTION
            Quit the program.
        '''
        lw: str = input("\n*** WARNING: Exiting will overwrite any "
                        "unsaved work. ***\n" +
                        "Continue? (y/[n]): ")
        if lw.lower() == "y":
            print("Exiting...")
            exit()
        else:
            return


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

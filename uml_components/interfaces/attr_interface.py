from uml_components.UMLClass import UMLClass, class_dict
from uml_components.UMLAttributes import (Field,
                                          Method,
                                          Parameter)
from typing import Union

def add_field(class_name : str,
              field_name : str,
              field_type : str) -> str:
    """
    Adds a field to the list of fields for a given class.
    
    Parameters:
    - class_name : str -> the name of the class which will have a field added to
    it. If the name given isn't the name of an existing class, the function will
    fail.
    - field_name : str -> the name of the field to be added. Must be unique
    among all fields in the class 'class_name'. Is not allowed to be None or the
    empty string.
    - field_type : str -> the data type of the field to be added. Cannot be None
    or the empty string.
    
    returns : str -> the error message of the operation.
    """
    
    err : str = ""
    
    # Checks if 'class_name' exists as a class.
    if class_name not in class_dict:
        err = f"Class named {class_name} does not exist."
        print(f"<Field Add Error [Invalid Class]>: {err}")
        
    else:
        # Checks if 'field_name' is empty or None.
        if field_name == None or field_name == "":
            err = "Field name must not be empty."
            print(f"<Field Add Error>: {err}")
        
        # Grabs the class with the name 'class_name' that is stored in the class 
        # dictionary.           
        uml : UMLClass = class_dict[class_name]
        
        # Loops through the list of fields in the UMLClass representation 'uml'.
        found : bool = False
        for field in uml.fields:
            # If 'field_name' matches the name of a field in the list of fields,
            # prints an error message and returns.
            if field_name == field.name:
                found = True
                break
        
        if found:
            err = f"{field_name} already exists as a field of {class_name}."
            print(f"<Field Add Error>: {err}")  
        else:
            # Creates a new Field object and stores it in the list of fields for 
            # 'uml'.    
            uml.add_field(field_name, field_type)
            
    return err
        

def add_method(class_name : str,
               method_name : str,
               method_type : str):
    """
    Adds a method to the list of methods for a given class.
    
    Parameters:
    - class_name : str -> the name of the class which will have a method added 
    to it. If the name given isn't the name of an existing class, the function 
    will fail.
    - method_name : str -> the name of the method to be added. Must be unique
    among all methods in the class 'class_name'. Is not allowed to be None or 
    the empty string.
    - method_type : str -> the return type of the method to be added. Cannot be 
    None or the empty string.
    """
    
    err : str = ""
    
    # Checks if 'class_name' exists as a class.
    if class_name not in class_dict:
        err = f"Class named {class_name} does not exist."
        print(f"<Method Add Error>: {err}")
        
    else:
        # Checks if 'method_name' is empty or None.
        if method_name == None or method_name == "":
            err = "Method name must not be empty."
            print(f"<Method Add Error>: {err}")
        
        # Grabs the class with the name 'class_name' that is stored in the class 
        # dictionary.           
        uml : UMLClass = class_dict[class_name]
        
        # Loops through the list of methods in the UMLClass representation 
        # 'uml'.
        found : bool = False
        for method in uml.methods:
            # If 'method_name' matches the name of a method in the list of 
            # methods with the same return type, prints an error message and 
            # returns.
            if method_name == method.name and method_type == method.return_type:
                found = True
                break
            
        print("<Method Add Error [Invalid Name : 2]>: " +
                )
        if found:
            err = (f"{method_name} already exists as a method of " +
                   f"{class_name} with return type {method_type}.")
            print()
        # Creates a new Method object and stores it in the list of methods for 
        # 'uml'.    
        uml.add_method(method_name, method_type)
    
    return err

def add_param(class_name : str,
              method_name : str,
              param_name : str,
              param_type : str) -> None:
    """
    """     
   
def rename_field(class_name : str,
                 field_name : str,
                 new_name :str) -> None:
    """
    Renames a field of a given class.
    
    Parameters:
    - class_name : str -> the name of the class whose field will be renamed.
    - field_name : str -> the name of the field to be renamed.
    - new_name : str -> the new name of the field. Must be unique and not empty
    or None.
    """
    
    # Checks for whether class_name exists as the name of a class.
    if class_name not in class_dict:
        print("<Field Rename Error>: " + 
              f"{class_name} does not exist as the name of a class.")
        
    # Checks if new_name is not empty or None.
    elif new_name == "" or new_name == None:
        print("<Field Rename Error>: " +
              "New field name must not be empty.")
        
    else: 
        # Grabs the class named 'class_name' from the class dictionary.
        uml : UMLClass = class_dict[class_name]
        # Declares a variable to hold a field object.
        field : Union[Field, None] = None
        found : bool = False
        
        # Loops through the list of fields in 'uml', updating found to true and
        # initalizing field if a field named 'field_name' exists in the list.
        fld : Field
        for fld in uml.fields:
            if fld.name == field_name:
                found = True
                field = fld
                break
        
        # If 'field_name' is not found, prints an error, otherwise renames the
        # field to 'new_name'.
        if not found:
            print("<Field Rename Error>: " +
                  f"{field_name} does not exist as the name of a field in " + 
                  f"{class_name}.")
        else:
            field.rename(new_name)
                
    
def rename_method(class_name : str, 
                  method_name : str, 
                  new_name : str) -> None:
    """
    Renames a method of the given class.
    
    Parameters:
    - class_name : str -> the name of the class whose method will be renamed.
    - method_name : str -> the name of the method to be renamed.
    - new_name : str -> the new name of the method. Must be unique and not empty
    or None.
    """
    
    if class_name not in class_dict:
        print("<Method Rename Error>: " + 
              f"{class_name} does not exist as the name of a class.")
    
    elif new_name == "" or new_name == None:
        print("<Method Rename Error>: " + 
              f"New method name must not be empty.")
    
    else:
        uml : UMLClass = class_dict[class_name]
        method : Union[Method, None] = None
        found : bool = False
        
        mthd : Method
        for mthd in uml.methods:
            if mthd.name == method_name:
                found = True
                method = mthd
                
        if not found:
            print("<Method Rename Error>: " +
                  f"{method_name} does not exist as the name of a method in " +
                  f"{class_name}.")
        else:
            method.rename(new_name)
            
def rename_param(class_name : str,
                 method_name : str,
                 param_name : str,
                 new_name : str) -> None:
    """
    Renames a parameter of a given method of a given class.   
    """

def delete_field(class_name : str,
                 field_name : str) -> None:
    pass

def delete_method(class_name : str,
                  method_name : str) -> None:
    pass

def delete_param(class_name : str,
                 method_name : str,
                 param_name : str) -> None:
    pass
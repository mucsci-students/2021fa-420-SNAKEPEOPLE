from uml_components import UMLClass
from uml_components.UMLAttributes import (UMLField,
                                          UMLMethod,
                                          UMLParameter)
from typing import Union

# Helper Methods =============================================================

def find_class(class_name : str) -> tuple:
    """
    Checks whether a given class name is the name of a class in the class
    dictionary.
    
    Parameters:
    - class_name : str -> the class name to be checked.
    """
    if class_name in UMLClass.class_dict:
        return True, UMLClass.class_dict[class_name]
    
    return False, None
    
def find_method(uml : UMLClass.UMLClass,
                method_name : str,
                method_type : str) -> tuple:
    """
    Checks if a given method name exists as a method in a given UMLClass.
    
    Parameters:
    - uml : UMLClass -> the class whose methods will be checked.
    - method_name : str -> the method name to be checked for.
    
    returns : tuple[bool, Union[UMLMethod, None]] -> if method is found, returns
    True and the UMLMethod object corresponding with 'method_name'. Otherwise
    returns False and None.
    """
    
    method : UMLMethod
    for method in uml.methods:
        if (method.name == method_name and 
            method.return_type == method_type):
            return True, method
        
    return False, None

def find_field(uml : UMLClass.UMLClass, 
               field_name : str) -> tuple:
    """
    Checks if a given field name exists as a field in a given UMLClass.
    
    Parameters:
    - uml : UMLClass -> the class whose fields will be checked.
    - field_name : str -> the field name to be checked for.
    
    returns : tuple[bool, Union[Method, None]] -> if field is found, returns
    True and the UMLMethod object corresponding with 'field_name'. Otherwise 
    returns False and None.
    """
    
    field : UMLField
    for field in uml.fields:
        if field.name == field_name:
            return True, field
        
    return False, None

def find_param(method : UMLMethod,
               param_name : str) -> tuple:
    """
    Checks if a given parameter name exists as a parameter in a given UMLMethod
    object.
    
    Parameters:
    - method : UMLMethod -> the class whose fields will be checked.
    - field_name : str -> the field name to be checked for.
    
    returns : tuple[bool, Union[Method, None]] -> if field is found, returns
    True and the UMLMethod object corresponding with 'field_name'. Otherwise 
    returns False and None.
    """
    
    param : UMLParameter
    for param in method.params:
        if param.name == param_name:
            return True, param
        
    return False, None



# Attr Add Methods ===========================================================

def add_field(class_name : str,
              field_name : str,
              field_type : str) -> tuple:
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
    
    return : str -> the error message of the operation.
    """
    
    msg : str = f"Successfully added '{field_name}' to '{class_name}'."
    ret = None
    
    # Checks if 'class_name' exists as a class.
    if not find_class(class_name):
        msg = f"Class named {class_name} does not exist."
        print(f"<Field Add Error [Invalid Class]>: {msg}")
        
    else:
        # Checks if 'field_name' is empty or None.
        if field_name == None or field_name == "":
            msg = "Field name must not be empty."
            print(f"<Field Add Error>: {msg}")
        
        # Grabs the class with the name 'class_name' that is stored in the class 
        # dictionary.           
        uml : UMLClass.UMLClass = UMLClass.class_dict[class_name]
        
        found, _ = find_field(uml, field_name)
        
        if found:
            msg = f"{field_name} already exists as a field of {class_name}."
            print(f"<Field Add Error>: {msg}")  
        else:
            # Creates a new Field object and stores it in the list of fields for 
            # 'uml'.    
            ret = uml.add_field(field_name, field_type)
            
    return ret, msg
        
def add_method(class_name : str,
               method_name : str,
               method_type : str) -> tuple:
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
    
    return : str -> the error message of the operation.
    """
    
    msg : str = f"Successfully added '{method_name}' to '{class_name}'."
    ret = None
    
    # Checks if 'class_name' exists as a class.
    if not find_class(class_name):
        msg = f"Class named {class_name} does not exist."
        print(f"<Method Add Error>: {msg}")
        
    else:
        # Checks if 'method_name' is empty or None.
        if method_name == None or method_name == "":
            msg = "Method name must not be empty."
            print(f"<Method Add Error>: {msg}")
        
        # Grabs the class with the name 'class_name' that is stored in the class 
        # dictionary.           
        uml : UMLClass.UMLClass = UMLClass.class_dict[class_name]
        
        found, _ = find_method(uml, method_name, method_type)
            
        if found:
            msg = (f"{method_name} already exists as a method of " +
                   f"{class_name} with return type {method_type}.")
            print(f"<Method Add Error>: {msg}")
        else:
            # Creates a new UMLMethod object and stores it in the list of methods 
            # for 'uml'.    
            ret = uml.add_method(method_name, method_type)
    
    return ret, msg

def add_param(class_name : str,
              method_name : str,
              method_type : str,
              param_name : str,
              param_type : str) -> tuple:
    """
    Adds a parameter to a given method of a given class.
    
    Parameters:
    - class_name : str -> the name of the class whose method's parameter will be
    renamed.
    - method_name : str -> the name of the method whose parameter will be 
    renamed.
    - param_name : str -> the name of the parameter to be renamed.
    - param_type : str -> the new name of the parameter. Must be unique and not
    empty and None.
    
    return : str -> the error message of the operation.
    """
    
    msg : str = (f"Successfuly added parameter '{param_name}' to method " + 
                 f"'{method_name}' in class '{class_name}'.")
    ret = None
    
    # Checks if 'class_name' exists as the name of a class in the class
    # dictionary. If it does not, prints an error.
    if not find_class(class_name):
        msg = f"{class_name} does not exist as the name of a class."
        print(f"<Parameter Add Error>: {msg}")
        
    # Checks if 'param_name' is empty or None. If it is, prints an error.
    elif param_name == "" or param_name == None:
        msg = "New parameter name must not be empty."
        print(f"<Parameter Add Error>: {msg}")
         
    else:
        # Creates variable to hold a UMLClass and a UMLMethod object.
        uml : UMLClass.UMLClass = UMLClass.class_dict[class_name]
        
        # Searches for a method with the same name as 'method_name' in 'uml'.
        found_method, method = find_method(uml, method_name, method_type)
        
        if found_method:
            # If a matching method was found, searches the parameter list of 
            # that method for a parameter with the name 'param_name'.
            found_param, _ = find_param(method, param_name)
            
            # If a matching parameter was found, prints an error.
            if found_param:
                msg = (f"{param_name} already exists as the name of a " +
                       f"parameter in {method_name} in {class_name}.")
                print(f"<Parameter Add Error>: {msg}")
            # Otherwise create a new Parameter object using 'param_name' and
            # 'param_type' and add it to the method's list of parameters.
            else:
                ret = uml.add_method_param(method, param_name, param_type)
        
        # If a matching method was not found, prints an error.     
        else:
            msg = (f"{method_name} does not exist as a method in {class_name}.")
            print(f"<Parameter Add Error>: {msg}")
    
    return ret, msg
   
   
   
# Attr Rename Methods ========================================================

def rename_field(class_name : str,
                 field_name : str,
                 new_name :str) -> tuple:
    """
    Renames a field of a given class.
    
    Parameters:
    - class_name : str -> the name of the class whose field will be renamed.
    - field_name : str -> the name of the field to be renamed.
    - new_name : str -> the new name of the field. Must be unique and not empty
    or None.
    
    return : str -> the error message of the operation.
    """
    
    msg : str = (f"Successfully renamed field '{field_name}' in "+
                 f"'{class_name}' to '{new_name}'")
    ret = None
    
    # Checks for whether class_name exists as the name of a class.
    if not find_class(class_name):
        msg = f"{class_name} does not exist as the name of a class."
        print(f"<Field Rename Error>: {msg}")
        
    # Checks if new_name is not empty or None.
    elif new_name == "" or new_name == None:
        msg = "New field name must not be empty."
        print(f"<Field Rename Error>: {msg}")
        
    else: 
        # Grabs the class named 'class_name' from the class dictionary.
        uml : UMLClass.UMLClass = UMLClass.class_dict[class_name]
        # Declares a variable to hold a field object.
        found, field = find_field(uml, field_name)
        
        # If 'field_name' is not found, prints an error, otherwise renames the
        # field to 'new_name'.
        if not found:
            msg = (f"{field_name} does not exist as the name of a field in " + 
                   f"{class_name}.")
            print(f"<Field Rename Error>: {msg}")
        else:
            field.rename(new_name)
            ret = field
            
    return ret, msg
                  
def rename_method(class_name : str, 
                  method_name : str,
                  method_type : str, 
                  new_name : str) -> tuple:
    """
    Renames a method of the given class.
    
    Parameters:
    - class_name : str -> the name of the class whose method will be renamed.
    - method_name : str -> the name of the method to be renamed.
    - new_name : str -> the new name of the method. Must be unique and not empty
    or None.
    
    return : str -> the error message of the operation.
    """
    
    msg : str = (f"Successfully renamed method '{method_name}' in " +
                 f"'{class_name}' to '{new_name}'.")
    ret = None
    
    if not find_class(class_name):
        msg = f"'{class_name}' does not exist as the name of a class."
        print(f"<Method Rename Error>: {msg}")
    
    elif new_name == "" or new_name == None:
        msg = "New method name must not be empty."
        print(f"<Method Rename Error>: {msg}")
              
    else:
        uml : UMLClass.UMLClass = UMLClass.class_dict[class_name]
        
        found, method = find_method(uml, method_name, method_type)
                
        if not found:
            msg = (f"{method_name} does not exist as the name of a method in " +
                   f"{class_name}.")
            print(f"<Method Rename Error>: {msg}")
        else:
            method.rename(new_name)
            ret = method
            
    return ret, msg
            
def rename_param(class_name : str,
                 method_name : str,
                 method_type : str,
                 param_name : str,
                 new_name : str) -> tuple:
    """
    Renames a parameter of a given method of a given class.
    
    Parameters:
    - class_name : str -> 
    - method_name : str ->
    - param_name : str ->
    - new_name : str ->
    
    return : str -> the error message of the operation.
    """
    
    msg : str = (f"Successfully renamed parameter '{param_name}' to '{new_name}' " + 
                 f"in '{class_name}.{method_name}'.")
    ret = None
    
    if class_name not in UMLClass.class_dict:
        err = f"'{class_name}' does not exist as the name of a class."
        print(f"<Parameter Rename Error>: {err}")
        
    elif new_name == "" or new_name == None:
        msg = "New parameter name must not be empty."
        print(f"<Parameter Rename Error>: {msg}")
        
    else:
        uml : UMLClass.UMLClass = UMLClass.class_dict[class_name]
        found_method, method = find_method(uml, method_name, method_type)
        
        found_param, param = find_param(method, param_name)
        
        if not found_method:
            err = (f"'{method_name}' does not exist as the name of a method " +
                   f"in '{class_name}'.")
            print(f"<Parameter Rename Error>: {err}")
        elif not found_param:
            msg = (f"'{param_name}' does not exist as the name of a parameter " +
                   f"in '{class_name}.{method_name}'.")
            print(f"<Parameter Rename Error>: {msg}")
        else:
            param.rename(new_name)
            ret = param
        
    return ret, msg



# Attr Delete Methods ========================================================
                
def delete_field(class_name : str,
                 field_name : str) -> tuple:
    """
    Deletes a field from a given class.
    
    Parameters:
    - class_name : str ->
    - field_name : str ->
    
    return : str -> the error message of the operation.
    """
    
    msg : str = f"Successfully deleted field '{field_name}' from '{class_name}'."
    ret = None
    
    if not find_class(class_name):
        msg = f"'{class_name}' does not exist as the name of a class."
        print(f"<Field Delete Error>: {msg}")
    
    else:
        uml : UMLClass.UMLClass = UMLClass.class_dict[class_name]
        found, field = find_field(uml, field_name)
        
        if not found:
            msg = (f"'{field_name}' does not exist as the name of a field in " +
                   f"'{class_name}'.")
            print(f"<Field Delete Error>: {msg}")
        else:
            ret = field
            uml.delete_field(field)
    
    return ret, msg

def delete_method(class_name : str,
                  method_name : str,
                  method_type : str) -> tuple:
    """
    Deletes a method from a given class.
    
    Parameters:
    - class_name : str ->
    - field_name : str ->
    
    return : str -> the error message of the operation.
    """
    
    msg : str = f"Successfully deleted method '{method_name}' from '{class_name}'."
    ret = None
    
    if not find_class(class_name):
        msg = f"{class_name} does not exist as the name of a class."
        print(f"<Method Delete Error>: {msg}")
    else:
        uml : UMLClass.UMLClass = UMLClass.class_dict[class_name]
        found, method = find_method(uml, method_name, method_type)
        
        if not found:
            msg = (f"'{method_name}' does not exist as the name of a method in " +
                   f"'{class_name}'.")
            print(f"<Method Delete Error>: {msg}")
        else:
            ret = method
            uml.delete_method(method)
    
    return ret, msg

def delete_param(class_name : str,
                 method_name : str,
                 method_type : str,
                 param_name : str) -> tuple:
    """
    Deletes a parameter from a given method of a given class.
    
    Parameters:
    - class_name : str ->
    - method_name : str ->
    
    return : str -> the error message of the operation.
    """
    
    msg : str = (f"Successfully deleted parameter '{param_name}' from " + 
                 f"'{class_name}.{method_name}'.")
    ret = None
    
    if not find_class(class_name):
        msg = f"{class_name} does not exist as the name of a class."
        print(f"<Parameter Delete Error>: {msg}")
    else:
        uml : UMLClass.UMLClass = UMLClass.class_dict[class_name]
        found_method, method = find_method(uml, method_name, method_type)
        found_param, param = find_param(method, param_name)
        
        if not found_method:
            err = (f"'{method_name}' does not exist as the name of a method " +
                   f"in '{class_name}'.")
            print(f"<Parameter Delete Error>: {err}")
        elif not found_param:
            err = (f"'{param_name}' does not exist as the name of a " +
                   f"parameter in '{class_name}.{method_name}'.")
            print(f"<Parameter Delete Error>: {err}")
        else:
            ret = param
            uml.delete_param(method, param)
    
    return ret, msg
    
from UMLClass import UMLClass, class_dict
from UMLAttributes import *

def add_field(class_name : str,
              field_name : str,
              field_type : str):
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
    """
    
    # Checks if 'class_name' exists as a class.
    if class_name not in class_dict:
        print("<Field Add Error [Invalid Class]>: " +
             f"Class named {class_name} does not exist.")
    else:
        # Checks if 'field_name' is empty or None.
        if field_name == None or field_name == "":
            print("<Field Add Error [Invalid Name : 1]>: " +
            "Field name must not be empty.")
        
        # Grabs the class with the name 'class_name' that is stored in the class 
        # dictionary.           
        uml : UMLClass = class_dict[class_name]
        
        # Loops through the list of fields in the UMLClass representation 'uml'.
        for field in uml.fields:
            # If 'field_name' matches the name of a field in the list of fields,
            # prints an error message and returns.
            if field_name == field.name:
                print("<Field Add Error [Invalid Name : 2]>: " +
                     f"{field_name} already exists as a field of {class_name}.")
                return
        # Creates a new Field object and stores it in the list of fields for 
        # 'uml'.    
        uml.add_field(field_name, field_type)
    

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
    
    # Checks if 'class_name' exists as a class.
    if class_name not in class_dict:
        print("<Method Add Error [Invalid Class]>: " +
             f"Class named {class_name} does not exist.")
    else:
        # Checks if 'method_name' is empty or None.
        if method_name == None or method_name == "":
            print("<Method Add Error [Invalid Name : 1]>: " +
            "Method name must not be empty.")
        
        # Grabs the class with the name 'class_name' that is stored in the class 
        # dictionary.           
        uml : UMLClass = class_dict[class_name]
        
        # Loops through the list of methods in the UMLClass representation 
        # 'uml'.
        for method in uml.methods:
            # If 'method_name' matches the name of a method in the list of 
            # methods with the same return type, prints an error message and 
            # returns.
            if method_name == method.name and method_type == method.return_type:
                print("<Method Add Error [Invalid Name : 2]>: " +
                     f"{method_name} already exists as a method of " +
                     f"{class_name} with return type {method_type}.")
                return
        # Creates a new Method object and stores it in the list of methods for 
        # 'uml'.    
        uml.add_method(method_name, method_type)

        
def rename_attribute(class_name : str, 
                     old_attr_name : str, 
                     new_attr_name : str) -> None:
    """
    Renames an attribute of a given class.
    
    Parameters:\n
    - class_name : str -> the name of the class whose attribute will be renamed.
    
    - old_attr_name : str -> the name of the attribute to be renamed.
    
    - new_attr_name : str -> the new name of the attribute being renamed. Must
    be a unique and valid name for an attribute. That is, it must not already
    exists as the name of an attribute in the class named 'class_name'. It also
    must not be None or the empty string.
    """
    
    # Checks if 'class_name' exists in the class dictionary.
    if class_name not in class_dict:
        # If 'class_name' is not the name of a class in the class dictionary,
        # prints an error.
        print("<Attribute Rename Error [Invalid Class]>: " +
             f"Class named {class_name} does not exist.")
    
    # If 'class_name' exists in the class dictionary, checks the validity of 
    # 'old_attr_name' and 'new_attr_name' for 'class_name'.
    else:
        # Stores the value of the class dictionary listing for 'class_name' in 
        # a varible to be worked on.
        uml : UMLClass = class_dict[class_name]
        
        # Checks if 'old_attr_name' exists in 'uml'.
        if old_attr_name not in uml.attributes:
            # If 'old_attr_name' does not exist as the name of an attribute in
            # 'uml', prints an error.
            print("<Attribute Rename Error [Invalid Name:1]>: " +
                 f"{old_attr_name} does not exist as the name of an attribute" +
                 f" in {class_name}")
        
        # Checks if 'new_attr_name' is a valid attribute name.
        elif new_attr_name == "" or new_attr_name == None:
            # If 'new_attr_name' is invalid, prints an error.
            print("<Attribute Rename Error [Invalid Name:2]>: " +
                  "New attribute name must not be empty.")
        
        # Checks if 'new_attr_name' is a unique attribute name in 'uml'.
        elif new_attr_name in uml.attributes:
            # If 'new_attr_name' already exists as an attribute name, prints an
            # error.
            print("<Attribute Rename Error [Invalid Name:3]>: " +
                 f"{new_attr_name} already exists as an attribute in " +
                 f"{class_name}")
           
        else:
            # If all checks for 'old_attr_name' and 'new_attr_name' are valid, 
            # renames 'old_attr_name' in 'uml' to 'new_attr_name'. 
            uml.rename_attribute(old_attr_name, new_attr_name)
            

def delete_attribute(class_name : str, attr_name : str) -> None:
    """
    Deletes an attribute from the list of attributes in a class.
    
    Parameters:\n
    - class_name : str -> the name of the class whose attribute is to be 
    deleted.
    
    - attr_name : str -> the name of the attribute to be deleted from the class.
    """
    
    # Checks if 'class_name' exists in the class dictionary.
    if class_name not in class_dict:
        # If 'class_name' is not the name of a class in the class dictionary,
        # prints an error.
        print("<Attribute Delete Error [Invalid Class]>: " +
             f"Class named {class_name} does not exist.")
    
    # If 'class_name' exists in the class directory, checks the validity of
    # 'attr_name'.
    else:
        # Stores the value of the class dictionary listing for 'class_name' in 
        # a varible to be worked on.
        uml : UMLClass = class_dict[class_name]
        
        # Checks if 'attr_name' exists as an attribute of 'uml'.
        if attr_name not in uml.attributes:
            # If 'attr_name' does not exist as the name of an attribute in
            # 'uml', prints an error.
            print("<Attribute Delete Error [Invalid Name]>: " +
                  f"{attr_name} does not exist as the name of an attribute in" +
                  f" {class_name}.")
        else:
            # If 'attr_name' is valid, removes the attribute from the list of
            # attributes in 'uml'.
            uml.delete_attribute(attr_name)
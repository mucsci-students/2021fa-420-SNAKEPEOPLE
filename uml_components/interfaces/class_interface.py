from uml_components.UMLClass import UMLClass, class_dict
from uml_components.UMLRelationship import UMLRelationship, relationship_list
from uml_components.interfaces import rel_interface

from typing import Union

def add_class(name : str) -> tuple:
    """
    Adds a new, empty class to the class dictionary.
    
    Parameters:\n
    - name : str -> the name of the new class to be added. The name should be
    vaild; that is, it should not be None or the empty string.
    """
    
    msg = f"<Added Class>: {name}"
    ret = None

    # Checks if 'name' is a valid class name.
    if name == "" or name == None:
        # If 'name' is invalid, prints an error.
        msg = "Class name must not be empty."
        print("<Class Add Error [Invalid Name:1]>: " + 
              "Class name must not be empty.")
        
    # Checks if 'name' already exists as a class name.
    elif name in class_dict:
        # If 'name' already exists as a class name, prints an error.
        msg = f"Class named '{name}' already exists."
        print("<Class Add Error [Invalid Name:2]>: " + 
             f"Class named '{name}' already exists.")
    
    else:
        # If all other checks are valid, creates a new UMLCLass object with
        # name 'name' and adds it to the dict of existing classes.
        new_class = UMLClass(name)
        class_dict.update({name : new_class})
        
        ret = new_class

    return ret, msg


def delete_class(name : str) -> tuple:
    """
    Deletes an existing class in the class dictionary.
    
    Parameters:\n
    - name : str -> the name of the class to be deleted. If 'name' is not the 
    name of an existing class, an error is printed. 
    """
    
    msg = f"<Deleted Class>: {name}"
    ret = None

    # Checks if 'name' is already the name of an existing class.
    if name not in class_dict:
        # If 'name' is not the name of an existing class, prints an error.
        msg = f"Class named '{name}' does not exist."
        print("<Class Delete Error [Invalid Name]>: " +
              f"Class named '{name}' does not exist.")
    else:
        # If 'name' is the name of an existing class, deconstructs the object,
        # and then removes the listing of the class from the class dict.
        rel_interface.rel_cleanup(name)
        del_class = class_dict[name]
        class_dict.pop(name)
        print(f"<Deleted Class>: {name}")
        
        ret = del_class

    return ret, msg


def rename_class(old_name : str, 
                 new_name : str) -> tuple:
    """
    Renames a class. 
    
    Due to the limitations of the implementation of class storage, a new entry 
    is created with a different key and the same value and the old entry is 
    deleted.
    
    Parameters:\n
    - old_name : str -> the old name of the class to be renamed. This parameter 
    is used to access the class dict for the UMLClass object to be renamed.
    
    - new_name : str -> the new name of the class. Must be a valid name, that
    is, it must not be None or the empty string, and it must also not be a name
    that already exists in the class dict.
    """
    
    msg = f"<Renamed Class>: {old_name} -> {new_name}"
    ret = None

    # Checks if 'old_name' exists in the class dict.
    if old_name not in class_dict:
        # If 'old_name' doesn't exist, prints an error.
        msg = f"{old_name} does not exist as the name of a class."
        print("<Class Rename Error [Invalid Name:1]>: " + 
             f"{old_name} does not exist as the name of a class.")
        
    # If 'old_name' exists, checks the validity of 'new_name'.
    else:
        # Checks if 'new_name' is a valid class name.
        if new_name == "" or new_name == None:
            # If 'new_name' isn't valid, prints an error.
            msg = "New class name must not be empty."
            print("<Class Rename Error [Invalid Name:2]>: " +
                  "New class name must not be empty.")
        
        # Checks if 'new_name' is a unique name.
        elif new_name in class_dict:
            # If 'new_name' is not a unique class name, prints an error.
            msg = f"Class name '{new_name}' alread exists."
            print("<Class Rename Error [Invalid Name:3]>: " +
                 f"Class name '{new_name}' alread exists.")
        
        # If 'new_name' is valid and unique, removes the listing for 'old_name'
        # and creates a new listing with the updated UMLClass object.
        else:
            # Temporarily stores the UMLClass object stored in the class dict
            # under 'old_name'.
            uml : UMLClass = class_dict[old_name]
            ret = uml
            
            rel : UMLRelationship
            for rel in relationship_list:
                if rel.source == old_name:
                    rel.source = new_name
                if rel.destination == old_name:
                    rel.destination = new_name
                    
            # Changes the name of the UMLClass object to 'new_name'.
            uml.rename(new_name)
            
            # Removes the listing for 'old_name' from the class dict.
            class_dict.pop(old_name)
            # Creates a new listing for 'uml' in the class dict with the
            # key of 'new_name'.
            class_dict.update({new_name : uml})

    return ret, msg
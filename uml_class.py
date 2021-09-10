# Project Name: SNAKE PEOPLE UML Editor
# File Name:    uml_class.py

class UMLClass():
    
    """
        A representation of a class for a UML class diagram.
        
        Instance Variables:\n
        - name : str -> the name of the class. Given during object construction.
        attributes : list -> a list of attributes of the class. Is intialized
        as an empty list.
    """
    
    def __init__(self, name : str, attributes : list = []):
        self.name = name
        self.attributes = attributes
        
    def __del__(self):
        print(f"Deleting UMLCLass: <{self.name}>...")
    
    def __repr__(self):
        name = f"\n\tClass Name: {self.name}\n"
        
        attrs = "\tAttributes:\n"
        for x in self.attributes:
            attrs += "\t"
            attrs += x
            attrs += "\n"
            
        return name + attrs
            
    def rename(self, new_name : str):
        # Sets 'self.name' to be equal to 'new_name'.
        self.name = new_name
        
    def add_attribute(self, attribute : str):
        # Adds 'attribute' to the end of 'self.attributes'.
        self.attributes.append(attribute)
        
    def rename_attribute(self, old_name : str, new_name : str):
        # Gets the index of the attribute to be renamed in 'self.attributes'.
        old_pos = self.attributes.index(old_name)
        
        # Modifies the value at the index of the attribute to be renamed to the 
        # new name of the attribute.
        self.attributes[old_pos] = new_name
        
    def delete_attribute(self, attribute : str):
        # Gets the index of the attribute to be deleted in 'self.attributes'.
        attr_pos = self.attributes.index(attribute)
        
        # Pops the element at index 'attr_pos' from 'self.attributes'.
        self.attributes.pop(attr_pos)
        
class_dict = dict()

def add_class(name : str) -> None:
    """
    Adds a new, empty class to the class dictionary.
    
    Parameters:\n
    - name : str -> the name of the new class to be added. The name should be
    vaild; that is, it should not be None or the empty string.
    """
    
    # Checks if 'name' is a valid class name.
    if name == "" or name == None:
        # If 'name' is invalid, prints an error.
        print("\n<Class Add Error [Invalid Name:1]>\n" + 
              "Class name must not be empty.")
        
    # Checks if 'name' already exists as a class name.
    elif name in class_dict:
        # If 'name' already exists as a class name, prints an error.
        print("\n<Class Add Error [Invalid Name:2]>\n" + 
             f"Class named '{name}' already exists.")
    
    else:
        # If all other checks are valid, creates a new UMLCLass object with
        # name 'name' and adds it to the dict of existing classes.
        new_class = UMLClass(name)
        class_dict.update({name : new_class})
        
def delete_class(name : str) -> None:
    """
    Deletes an existing class in the class dictionary.
    
    Parameters:\n
    - name : str -> the name of the class to be deleted. If 'name' is not the 
    name of an existing class, an error is printed. 
    """
    
    # Checks if 'name' is already the name of an existing class.
    if name not in class_dict:
        # If 'name' is not the name of an existing class, prints an error.
        print("<Class Delete Error [Invalid Name]>\n" +
              f"Class named '{name}' does not exist.")
    else:
        # If 'name' is the name of an existing class, deconstructs the object,
        # and then removes the listing of the class from the class dict.
        del class_dict[name]
        class_dict.pop(name)

def rename_class(old_name : str, new_name : str) -> None:
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
    
    # Checks if 'old_name' exists in the class dict.
    if old_name not in class_dict:
        # If 'old_name' doesn't exist, prints an error.
        print("<Class Rename Error [Invalid Name:1]>\n" + 
             f"{old_name} does not exist as the name of a class.")
        
    # If 'old_name' exists, checks the validity of 'new_name'.
    else:
        # Checks if 'new_name' is a valid class name.
        if new_name == "" or new_name == None:
            # If 'new_name' isn't valid, prints an error.
            print("<Class Rename Error [Invalid Name:2]>\n" +
                  "New class name must not be empty.")
        
        # Checks if 'new_name' is a unique name.
        elif new_name in class_dict:
            # If 'new_name' is not a unique class name, prints an error.
            print("<Class Rename Error [Invalid Name:3]>\n" +
                 f"Class name '{new_name}' alread exists.")
        
        # If 'new_name' is valid and unique, removes the listing for 'old_name'
        # and creates a new listing with the updated UMLClass object.
        else:
            # Temporarily stores the UMLClass object stored in the class dict
            # under 'old_name'.
            uml_class : UMLClass = class_dict[old_name]
            # Changes the name of the UMLClass object to 'new_name'.
            uml_class.rename(new_name)
            
            # Removes the listing for 'old_name' from the class dict.
            class_dict.pop(old_name)
            # Creates a new listing for 'uml_class' in the class dict with the
            # key of 'new_name'.
            class_dict.update({new_name : uml_class})
        
def add_attribute(uml_class : UMLClass, attr_name : str) -> None:
    if uml_class.name in class_dict:
        if attr_name in uml_class.attributes:
            uml_class.add_attribute(attr_name)
        else:
            print(f"Error: {attr_name} already exists as an" +
                  "attribute of {uml_class.name}.")
    else:
        print(f"Error: {uml_class.name} does not exist as the name of a class.")
        
def rename_attribute(uml_class : UMLClass, old_name : str, 
                     new_name : str) -> None:
    if uml_class.name in class_dict:
        pass

def delete_attribute(uml_class : UMLClass, attr_name : str) -> None:
    pass
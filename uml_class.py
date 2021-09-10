# Project Name: SNAKE PEOPLE UML Editor
# File Name:    uml_class.py

class UMLClass():
    
    """
        A representation of a class for a UML class diagram.
        
        Instance variables:\n
        name : str -> the name of the class. Given during object construction.
        attributes : list -> a list of attributes of the class. Is intialized
        as an empty list.
    """
    
    def __init__(self, name : str, attributes : list = []):
        self.name = name
        self.attributes = attributes
        
    def __del__(self):
        print(f"Deleting UMLCLass: <{self.name}>...")
    
    def __repr__(self):
        name = f"Class Name:\n\t{self.name}\n"
        
        attrs = "Attributes:\n"
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
        # Gets the index of the attribute to be deleted.
        attr_pos = self.attributes.index(attribute)
        
        # Pops the element at index 'attr_pos' from 'self.attributes'.
        self.attributes.pop(attr_pos)
        
class_dict = dict()

def add_class(name : str) -> None:
    """
    Adds a new, empty class to the class dictionary.
    
    Parameters:\n
    name : str -> the name of the new class to be added. The name should be
    vaild; that is, it should not be None, the empty string, or a numeric value.
    """
    
    # Checks if 'name' is a key in the dict of existing classes.
    if name not in class_dict:
        # Checks if 'name' is a valid class name, and prints an error if it 
        # isn't.
        if (name == "" or name is None) or name.isnumeric:
            print(f"Error: Class name is empty or otherwise invalid.")
        
        # If 'name' does not already exist in the class dict and is valid, 
        # create a new class with that name, and add it to the dict.
        new_class = UMLClass(name)
        class_dict.update({name : new_class})
    else:
        # If 'name' already exists, prints an error.
        print(f"Error: {name} is already the name of an existing class.")
        
def delete_class(name : str) -> None:
    """
    Deletes an existing class in the class dictionary.
    
    Parameters:\n
    name : str -> the name of the class to be deleted. Should be a valid 
    """
    # Checks if 'name is a key in the dict of existing classes.
    if name in class_dict:
        # If 'name' already exists in the class dict, removes the entry with the
        # key equal to 'name'.
        class_dict.pop(name)
    else:
        # If 'name' does not exist, prints an error.
        print(f"Error: {name} does not exist as the name of a class.")

def rename_class(uml_class : UMLClass, new_name : str) -> None:
    if uml_class.name in class_dict:
        if new_name not in class_dict:
            # Calls the rename method of the UMLClass class.
            uml_class.rename(new_name)
        else:
            print(f"Error: {new_name} already exists as a name of a class.")
    else:
        print(f"Error: Class does not exist.")
        
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
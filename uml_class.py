# Project Name: SNAKE PEOPLE UML Editor
# File Name:    uml_class.py

class_dict = dict()

class UMLClass():
    """
        A representation of a class for a UML class diagram.
        
        Instance Variables:\n
        - name : str -> the name of the class. Given during object construction.
        attributes : list -> a list of attributes of the class. Is intialized
        as an empty list.
    """
    
    def __init__(self, 
                 name : str):
        self.name = name
        self.attributes = list()
        

    def __del__(self):
        print(f"<Deleted Class>: {self.name}")
    

    def __repr__(self):
        name = f"\nClass Name: {self.name}"
        attr = f"\nAttributes: {self.attributes}"
            
        return name + attr
            

    def rename(self, 
               new_name : str):
        # Sets 'self.name' to be equal to 'new_name'.
        print(f"<Renamed Class>: {self.name} -> {new_name}")
        self.name = new_name
        
        

    def add_attribute(self, 
                      attribute : str):
        # Adds 'attribute' to the end of 'self.attributes'.
        self.attributes.append(attribute)
        print(f"<Added Attribute>: {attribute} ({self.name})")
        

    def rename_attribute(self, 
                         old_name : str, 
                         new_name : str):
        # Gets the index of the attribute to be renamed in 'self.attributes'.
        old_pos = self.attributes.index(old_name)
        
        # Modifies the value at the index of the attribute to be renamed to the 
        # new name of the attribute.
        self.attributes[old_pos] = new_name
        print(f"<Renamed Attribute>: {old_name} -> {new_name} ({self.name})")
        

    def delete_attribute(self, 
                         attribute : str):
        # Gets the index of the attribute to be deleted in 'self.attributes'.
        attr_pos = self.attributes.index(attribute)
        
        # Pops the element at index 'attr_pos' from 'self.attributes'.
        self.attributes.pop(attr_pos)
        print(f"<Deleted Attribute>: {attribute} ({self.name})")



# ============================= Class Functions ============================= #

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
<<<<<<< HEAD
        print("<Class Add Error [Invalid Name:1]>\n" + 
=======
        print("<Class Add Error [Invalid Name:1]>: " + 
>>>>>>> 85a6591b49913afd6f27893b56283b25f991bcb9
              "Class name must not be empty.")
        
    # Checks if 'name' already exists as a class name.
    elif name in class_dict:
        # If 'name' already exists as a class name, prints an error.
<<<<<<< HEAD
        print("<Class Add Error [Invalid Name:2]>\n" + 
=======
        print("<Class Add Error [Invalid Name:2]>: " + 
>>>>>>> 85a6591b49913afd6f27893b56283b25f991bcb9
             f"Class named '{name}' already exists.")
    
    else:
        # If all other checks are valid, creates a new UMLCLass object with
        # name 'name' and adds it to the dict of existing classes.
        new_class = UMLClass(name)
        class_dict.update({name : new_class})
        print(f"<Added Class>: {name}")

       
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
        print("<Class Delete Error [Invalid Name]>: " +
              f"Class named '{name}' does not exist.")
    else:
        # If 'name' is the name of an existing class, deconstructs the object,
        # and then removes the listing of the class from the class dict.
        class_dict.pop(name)


def rename_class(old_name : str, 
                 new_name : str) -> None:
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
        print("<Class Rename Error [Invalid Name:1]>: " + 
             f"{old_name} does not exist as the name of a class.")
        
    # If 'old_name' exists, checks the validity of 'new_name'.
    else:
        # Checks if 'new_name' is a valid class name.
        if new_name == "" or new_name == None:
            # If 'new_name' isn't valid, prints an error.
            print("<Class Rename Error [Invalid Name:2]>: " +
                  "New class name must not be empty.")
        
        # Checks if 'new_name' is a unique name.
        elif new_name in class_dict:
            # If 'new_name' is not a unique class name, prints an error.
            print("<Class Rename Error [Invalid Name:3]>: " +
                 f"Class name '{new_name}' alread exists.")
        
        # If 'new_name' is valid and unique, removes the listing for 'old_name'
        # and creates a new listing with the updated UMLClass object.
        else:
            # Temporarily stores the UMLClass object stored in the class dict
            # under 'old_name'.
            uml : UMLClass = class_dict[old_name]
            # Changes the name of the UMLClass object to 'new_name'.
            uml.rename(new_name)
            
            # Removes the listing for 'old_name' from the class dict.
            class_dict.pop(old_name)
            # Creates a new listing for 'uml' in the class dict with the
            # key of 'new_name'.
            class_dict.update({new_name : uml})



# =========================== Attribute Functions =========================== #
    
def add_attribute(class_name : str, 
                  attr_name : str) -> None:
    """
    Adds an attribute to the list of attributes for a given class.
    
    Parameters:/m
    - class_name : str -> the name of the class which will have an attribute
    added to it.
    
    - attr_name : str -> the name of the attribute to be added. Must be a unique
    and valid attribute name. That is, it must not have the same name as an
    attribute already in 'class_name', and it must not be None or the empty
    string.
    """
    
    # Checks if 'class_name' is an existing class in 'class_dict'.
    if class_name not in class_dict:
        # If 'class_name' does not exist in the class dictionary, prints an 
        # error.
        print("<Attribute Add Error [Invalid Class]>: " +
             f"Class named {class_name} does not exist.")
        
    # If 'class_name' does exist as a class name in the class dictionary, checks
    # the validity of 'attr_name' for 'class_name'.
    else:
        # Stores the value of the class dictionary listing for 'class_name' in 
        # a varible to be worked on.
        uml : UMLClass = class_dict[class_name]
        
        #Checks if 'attr_name' is a valid attribute name.
        if attr_name == "" or attr_name == None:
            # If 'attr_name' is invalid, prints an error.
            print("<Attribute Add Error [Invalid Name:1]>: " +
                  "New attribute name must not be empty.")
        
        # Checks if 'attr_name' is unique to 'class_name'.
        elif attr_name in uml.attributes:
            # If 'attr_name' is not unique, prints an error.
            print("<Attribute Add Error [Invalid Name:2]>: " +
                 f"{attr_name} already exists as an attribute of {class_name}.")
        else:
            # If all checks for 'attr_name' are valid, adds 'attr_name' as an
            # attribute to the class with name 'class_name'.
            uml.add_attribute(attr_name)

        
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
                  f"{class_name}.")
        else:
            # If 'attr_name' is valid, removes the attribute from the list of
            # attributes in 'uml'.
            uml.delete_attribute(attr_name)


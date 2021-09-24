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
                  f" {class_name}.")
        else:
            # If 'attr_name' is valid, removes the attribute from the list of
            # attributes in 'uml'.
            uml.delete_attribute(attr_name)
from uml_components.UMLClass import class_dict
from uml_components.UMLRelationship import UMLRelationship, relationship_list

def check_class(cls : str) -> bool:
    """
    Checks if the given class exists in the class dictionary.
    
    Parameters:
    - cls : str -> the name of the class to be checked for.
    
    Returns:
    - found : bool -> True if cls exists, False otherwise.
    """
    
    found : bool = False
    
    # Loops through the class dictionary and sets found to True if 'cls' is in
    # the class dictionary.
    for key in class_dict:
        if cls == key:
            found = True
            
    return found


def check_type(rel_type : str) -> bool:

    """
    Checks to ensure that the relationship type is one of Aggregation, 
    Composition, Inheritance, or Realization.

    - rel_type : str -> the type to be checked.
    """

    # A set of valid relationship types.
    relationship_types = {"aggregation", 
                          "composition", 
                          "inheritance", 
                          "realization"}
    
    if rel_type.lower() in relationship_types:
        return True
    else:
        return False

def find_rel(source : str, dest : str) -> tuple:
    index : int = 0
    
    if check_class(source) and check_class(dest): 
        relationship : UMLRelationship
        for relationship in relationship_list:
            # If source and destination are both valid, iterates through the
            # relationship list until it finds a matching relationship.
            if (source == relationship.source and 
                dest == relationship.destination):
                # If the source and destination match the source and destination
                # of the current iteration, returns True.
                return (True, index)
            else:
                # Increments the index by 1 and checks again.
                index += 1
                
    return (False, index)

def add_relationship(source : str, destination : str, rel_type : str) -> str:

    """
    Adds a new relationship to the relationship list.
    
    Parameters:
    - source : str -> the name of the primary class in the relationship.
    - destination : str -> the name of the secondary class in the relationship.
    - rel_type : str -> the type of relationship to be created. Must be one of 
    ['Aggregation', 'Composition', 'Inheritance', 'Realization'].
    """
    
    err = f"<Added Relationship>: {source} - {destination} ({rel_type})"

    # Checks if the given relationship type is valid.
    if not check_type(rel_type):
        # If invalid, prints an error.
        err = f"{rel_type} is not a valid relationship type."
        print("<Relationship Add Error>: " +
              f"{rel_type} is not a valid relationship type.")
    else:
        # If the type is valid, checks if both source and destination are valid
        # classes.
        if not check_class(source):
            err = f"{source} does not exist as the name of a class."
            print("<Relationship Add Error>: " +
                  f"{source} does not exist as the name of a class.")
        if not check_class(destination):
            err = f"{destination} does not exist as the name of a class."
            print("<Relationship Add Error>: " +
                  f"{destination} does not exist as the name of a class.")
        
        
        if check_class(source) and check_class(destination):
            # If both source and destination are valid, checks if the 
            # relationship already exists.
            for relationship in relationship_list:
                if (source == relationship.source and 
                    destination == relationship.destination):
                    err = f"Relationship {source} - {destination} already " + "exists"
                    print("<Relationship Add Error>: " +
                          f"Relationship {source} - {destination} already " +
                          "exists")
            
            # If the relationship does not already exist, creates a new 
            # UMLRelationship object and adds it to the relationship list.
            rel = UMLRelationship(source, destination, rel_type)
            relationship_list.append(rel)

    return err

def delete_relationship(source : str, dest : str) -> str:

    """
    Deletes an existing relationship of source - dest from the relationship 
    list.

    Parameters:
    - source : str -> the name of the primary class of the relationship.
    - dest : str -> the name of the secondary class of the relationship.
    """
    
    err = f"<Deleted Relationship>: {source} - {dest})"

    # Checks if the given source and destination are valid classes.
    if not check_class(source):
        err = f"{source} does not exist as the name of a class."
        print("<Relationship Delete Error>: " +
              f"{source} does not exist as the name of a class.")
    if not check_class(dest):
        err = f"{dest} does not exist as the name of a class."
        print("<Relationship Delete Error>: " +
              f"{dest} does not exist as the name of a class.")
            
    
    # Checks whether a valid relationship was found.
    found, index = find_rel(source, dest)
    if found:
        # If matching relationship found, deletes the relationship from the
        # list.
        rel = relationship_list.pop(index)
        err = f"<Deleted Relationship>: {source} - {dest} ({rel.type})"
        print(f"<Deleted Relationship>: {source} - {dest} ({rel.type})")
    else:
        # Otherwise, prints an error.
        err = f"Relationship {source} - {dest} does not exist."
        print("<Relationship Delete Error>: " +
                f"Relationship {source} - {dest} does not exist.")

    return err


def rel_cleanup(cls : str) -> None:
    """
    Deletes all relationships that have a source or destination of 'cls'.
    
    Parameter:
    - cls : str -> the name of the class whose relationships will be deleted.
    """
    
    # Checks if the class exists in the class dictionary.
    if cls in class_dict:
        # If cls is the name of the class, iterates through the relationship
        # list and deletes all relationships where cls is source or destination.
        relationship : UMLRelationship
        for relationship in relationship_list:
            # Deletes if cls is source.
            if cls == relationship.source:
                delete_relationship(cls, relationship.destination)
                rel_cleanup(cls)
            # Deletes if cls is destination.
            if cls == relationship.destination:
                delete_relationship(relationship.source, cls)
                rel_cleanup(cls)


def list_relationships() -> None:
    """
    Lists all relationships.
    """

    # Prints '(none)' if no relationships in list.
    if len(relationship_list) < 1:
        print("(none)")
    else:
        # Loops through the relationship list and prints each entry.
        for relationship in relationship_list:
            print(relationship)


def change_type(source : str, dest : str, new_type : str):

    #Checks to ensure that the new relationship type is one of Aggregation,
    #Composition, Inheritance, or Realization and then replaces the old 
    #relationship type of the named relationship with the new relationship type.
    
    #parameters:
    #source- String that is set as the name of a UMLClass object
    #destination- String that is set as the name of a UMLClass object
    #new_type- String of the new relationship type


    #Check to make sure the relationship exists
    found, index = find_rel(source, dest)
    if found == False:
        print("<Relationship Type Error>: " +
              f"{source}-{dest} is not a valid relationship.")
    #Check to make sure the new relationship type exists
    elif check_type(new_type) == False:
        print("<Relationship Type Error>: " +
              f"{new_type} is not a valid relationship type.")
    else:
        #Update the relationship type
        relationship : UMLRelationship = relationship_list[index]
        relationship.change_type(new_type)

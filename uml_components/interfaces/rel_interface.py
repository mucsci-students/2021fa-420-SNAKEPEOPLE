from uml_components.UMLClass import class_dict
from uml_components.UMLRelationship import UMLRelationship, relationship_list

def add_relationship(source : str, destination : str, rel_type : str) -> None:

    """
    Adds a new relationship to the relationship list.
    
    Parameters:
    - source : str -> the name of the primary class in the relationship.
    - destination : str -> the name of the secondary class in the relationship.
    - rel_type : str -> the type of relationship to be created. Must be one of 
    ['Aggregation', 'Composition', 'Inheritance', 'Realization'].
    """
    
    # Checks if the given relationship type is valid.
    if not check_type(rel_type):
        # If invalid, prints an error.
        print("<Relationship Add Error>: " +
              f"{rel_type} is not a valid relationship type.")
    else:
        # If the type is valid, checks if both source and destination are valid
        # classes.
        if not check_class(source):
            print("<Relationship Add Error>: " +
                  f"{source} does not exist as the name of a class.")
        if not check_class(destination):
            print("<Relationship Add Error>: " +
                  f"{destination} does not exist as the name of a class.")
        
        
        if check_class(source) and check_class(destination):
            # If both source and destination are valid, checks if the 
            # relationship already exists.
            for relationship in relationship_list:
                if (source == relationship.source and 
                    destination == relationship.destination):
                    print("<Relationship Add Error>: " +
                          f"Relationship {source} - {destination} already " +
                          "exists")
            
            # If the relationship does not already exist, creates a new 
            # UMLRelationship object and adds it to the relationship list.
            rel = UMLRelationship(source, destination, rel_type)
            relationship_list.append(rel)


def delete_relationship(source : str, dest : str) -> None:

    """
    Delete an existing relationship of source - dest from the relationship list.

    Parameters:
    - source : str -> the name of the primary class of the relationship.
    - dest : str -> the name of the secondary class of the relationship.
    """
    
    # Checks if the given source and destination are valid classes.
    if not check_class(source):
        print("<Relationship Delete Error>: " +
              f"{source} does not exist as the name of a class.")
    if not check_class(dest):
        print("<Relationship Delete Error>: " +
              f"{dest} does not exist as the name of a class.")
        
        
    if check_class(source) and check_class(dest):
        index : int = 0
        found : bool = False
        
        relationship : UMLRelationship
        for relationship in relationship_list:
            # If source and destination are both valid, iterates through the
            # relationship list until it finds a matching relationship.
            if (source == relationship.source and 
                dest == relationship.destination):
                # If the source and destination match the source and destination
                # of the current iteration, set found to True and break the 
                # loop.    
                found = True
                break
            else:
                # Increments the index by 1 and checks again.
                index += 1
        
        # Checks whether a valid relationship was found.
        if found:
            # If matching relationship found, deletes the relationship from the
            # list.
            rel = relationship_list.pop(index)
            print(f"<Deleted Relationship>: {source} - {dest} ({rel.type})")
        else:
            # Otherwise, prints an error.
            print("<Relationship Delete Error>: " +
                  f"Relationship {source} - {dest} does not exist.")

##########################################################################################

def rel_cleanup(cls : str) -> None:

    
    if cls in class_dict:
        relationship : UMLRelationship
        for relationship in relationship_list:
            if cls == relationship.source:
                delete_relationship(cls, relationship.destination)
            if cls == relationship.destination:
                delete_relationship(relationship.source, cls)
        
    

##########################################################################################

def list_relationships() -> None:

    #List all relationships in the form "<source>-<destination>"

    if len(relationship_list) < 1:
        print("(none)")
    else:
        for relationship in relationship_list:
            print(relationship)

##########################################################################################

def Change_reltype(source : str, dest : str, new_type : str):

    #Checks to ensure that the new relationship type is one of Aggregation,
    #Composition, Inheritance, or Realization and then replaces the old 
    #relationship type of the named relationship with the new relationship type.
    
    #parameters:
    #source- String that is set as the name of a UMLClass object
    #destination- String that is set as the name of a UMLClass object
    #new_type- String of the new relationship type

    found = False
    rel_index = 0
    while rel_index < len(relationship_list):
        if ((relationship_list[rel_index].sourceName == source) 
              and (relationship_list[rel_index].destName == dest)):
            found = True
            break
        ++rel_index

    #Check to make sure the relationship exists
    if found == False:
        print(f"<Relationship Type Error>: "+
            f"Relationship {source}-{dest} is an invalid relationship.")
    #Check to make sure the new relationship type exists
    elif check_type(new_type) == False:
        print(f"<Relationship Type Error>: "+
                f"Relationship type {new_type} is an invalid type.")
    else:
        #Update the relationship type
        relationship_list[rel_index].changeType(new_type)

##########################################################################################

def check_class(cls : str) -> bool:
    """
    Checks if the given class exists in the class dictionary.
    
    Parameters:
    - cls : str -> the name of the class to be checked for.
    
    Returns:
    - found : bool -> True if cls exists, False otherwise.
    """
    
    found : bool = False
    
    for key in class_dict:
        if cls == key:
            found = True
            
    return found

##########################################################################################

def check_type(rel_type : str) -> bool:

    #Checks to ensure that the new relationship type is one of Aggregation,
    #Composition, Inheritance, or Realization.

    #new_type- String of the new relationship type

    relationship_types = {"aggregation", 
                          "composition", 
                          "inheritance", 
                          "realization"}
    
    if rel_type.lower() in relationship_types:
        return True
    else:
        return False

##########################################################################################

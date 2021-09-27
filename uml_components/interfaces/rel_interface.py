from uml_components.UMLClass import class_dict
from uml_components.UMLRelationship import UMLRelationship, relationship_list

def add_relationship(source : str, destination : str, rel_type : str) -> None:

    #Add a relationship by creating a new UMLRelationship object containing
    #the uml_class associated with the source string, the uml_class associated 
    #with the destination string, and the type of relationship
    
    #parameters:
    #source- String that is set as the name of a UMLClass object
    #destination- String that is set as the name of a UMLClass object
    #rel_type- String that defines the relationship type to be aggregation, composition,
    #inheritance, or realization
    
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
        
        # If both source and destination are valid, 
        if check_class(source) and check_class(destination):
            
            for relationship in relationship_list:
                if (source == relationship.source and 
                    destination == relationship.destination):
                    print("<Relationship Add Error>: " +
                          f"Relationship {source} - {destination} already " +
                          "exists")
            
            rel = UMLRelationship(source, destination, rel_type)

##########################################################################################

def delete_relationship(source : str, destination : str) -> None:

    #Delete a relationship between source and destination
    
    #parameters:
    #source- String that is set as the name of a UMLClass object
    #destination- String that is set as the name of a UMLClass object

    if check_params(source, destination) == False:
        return
    else:
        #Ensure that the relationship exists
        i = 0;
        while i < len(relationship_list):
            if((relationship_list[i].sourceName == source) and
                 (relationship_list[i].destName == destination)):
                del_rel = relationship_list.pop(i)
                del del_rel
                return
            ++i
        else:
            print(f"ERROR: Relationship {source}-{destination}, does not exist.")

##########################################################################################

def rel_cleanup(source : str) -> None:

    #Delete all relationships involving the UMLClass object
    #associated with source

    #parameters:
    #source- String that is set as the name of a UMLClass object
    i = 0
    while i < len(relationship_list):
        if ((relationship_list[i].sourceName == source) or
             (relationship_list[i].destName == source)):            
            del_rel = relationship_list.pop(i)
            del del_rel
            --i
        ++i

##########################################################################################

def list_relationships() -> None:

    #List all relationships in the form "<source>-<destination>"

    if len(relationship_list) == 0:
        print("(none)")

    for i in relationship_list:
        print("Relationship: " + i.sourceName + "-" + i.destName +  "   Relationship type: " + i.rel_type)

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
    found = False
    
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

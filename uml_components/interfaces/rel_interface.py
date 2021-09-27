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
    

    if check_params(source, destination) == False:
        return
    elif check_reltype(rel_type) == False:
        print(f"<Relationship Add Error>: "+
                f"Relationship type {rel_type} is an invalid type.")
    else:
        #Ensure the relationship does not already exist
        for i in relationship_list:
            if (i.sourceName == source) and (i.destName == destination):
                print("<Relationship Add Error>: "+
                    f"Relationship {source}-{destination} already exists.")
                return
        
        #Create the UMLRelationship and add it to the list
        new_rel = UMLRelationship(class_dict[source],
                                  class_dict[destination], 
                                  rel_type)
        relationship_list.append(new_rel)
        print(f"<Relationship Added>: {source}-{destination}")

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
    elif check_reltype(new_type) == False:
        print(f"<Relationship Type Error>: "+
                f"Relationship type {new_type} is an invalid type.")
    else:
        #Update the relationship type
        relationship_list[rel_index].changeType(new_type)

##########################################################################################

def check_params(source : str, destination : str) -> bool:
    
    #Checks to see if source and destination are valid classes
    #If either source or destination are invalid, print an error
    #and return false

    #parameters:
    #source- String that is set as the name of a UMLClass object
    #destination- String that is set as the name of a UMLClass object

    if source == "" or destination == "":
        print("ERROR: class name cannot be empty")
        return False

    found_source = False
    found_dest = False

    for key in class_dict:
        if key == source:
            found_source = True
        if key == destination:
            found_dest = True

    if found_source == False and found_dest == False:
        print(f"ERROR: {source} and {destination} are invalid, both arguements must be existing classes.")
        return False

    elif found_source == False:
        print(f"ERROR: {source} is invalid, source must be an existing class.")
        return False

    elif found_dest == False:
        print(f"ERROR: {destination} is invalid, destination must be an existing class.")
        return False

    return True

##########################################################################################

def check_reltype(rel_type) -> bool:

    #Checks to ensure that the new relationship type is one of Aggregation,
    #Composition, Inheritance, or Realization.

    #new_type- String of the new relationship type

    relationship_types = {"aggregation", "composition", "inheritance", "realization"}
    if rel_type.lower() in relationship_types:
        return True
    else:
        return False

##########################################################################################

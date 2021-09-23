import uml_class

uml_class.class_dict
relationship_list = []

class UMLRelationship():
    
    #UMLRelationship is an object that models a relationship between two UML classes.
    #The class stores a name in the form "<source>-<destination>", a source object referencing
    #a uml class object, and a destination object also referencing a uml class object.

    def __init__(self, source, destination, rel_type: str):
        self.source = source
        self.destination = destination
        self.sourceName = source.name
        self.destName = destination.name
        self.rel_type = rel_type

    def __del__(self):
        print(f"<Deleted Relationship>: {self.sourceName}-{self.destName}")
    
    def __repr__(self):
        return self.sourceName + "-" + self.destName
        
    def rename(self, new_name : str):
        self.name = new_name

    def changeSource(self, new_source):
        self.source = new_source
        self.sourceName = new_source.name

    def changeDestination(self, new_dest):
        self.destination = new_dest
        self.destName = new_dest.name

    def changeType(self, new_type):
        self.rel_type = new_type


##########################################################################################

def add_relationship(source : str, destination : str, rel_type : str) -> None:

    #Add a relationship by creating a new UMLRelationship object containing
    #the name "<source>-<destination>", uml_class associated with the source 
    #string, and the uml_class associated with the destination string
    
    #parameters:
    #source- String that is set as the name of a UMLClass object
    #destination- String that is set as the name of a UMLClass object
    

    if check_params(source, destination) == False:
        return
    elif check_reltype(rel_type) == False:
        print(f"<Relationship Add Error>: "+
                f"Relationship type {rel_type} is an invalid type.")
    else:
        #if check_reltype(rel_type) == True:
        for i in relationship_list:
            #Ensure the relationship does not already exist
            if (i.sourceName == source) and (i.destName == destination):
                print("<Relationship Add Error>: "+
                    f"Relationship {source}-{destination} already exists.")
                return
            #Create the UMLRelationship and add it to the dictionary

        new_rel = UMLRelationship(uml_class.class_dict[source],
                                    uml_class.class_dict[destination], rel_type)
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
            if(relationship_list[i].sourceName == source) and (relationship_list[i].destName == destination):
                
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
        if (relationship_list[i].sourceName == source) or (relationship_list[i].destName == source):            
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
    found = False
    rel_index = 0
    while rel_index < len(relationship_list):
        if (relationship_list[rel_index].sourceName == source) and (relationship_list[rel_index].destName == dest):
            found = True
            break
        ++rel_index

    if found == False:
        print(f"<Relationship Type Error>: "+
            f"Relationship {source}-{dest} is an invalid relationship.")
    #Takes in a string that is the relationship's name, and the new type of relationship
    elif check_reltype(new_type) == False:
        print(f"<Relationship Type Error>: "+
                f"Relationship type {new_type} is an invalid type.")
    else:
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

    for key in uml_class.class_dict:
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

    if rel_type in {"aggregation", "composition", "inheritance", "realization"}:
        return True
    else:
        return False

##########################################################################################

import uml_class

uml_class.class_dict
relationship_dict = dict()

class UMLRelationship():
    
    #UMLRelationship is an object that models a relationship between two UML classes.
    #The class stores a name in the form "<source>-<destination>", a source object referencing
    #a uml class object, and a destination object also referencing a uml class object.

    def __init__(self, name : str, source, destination):
        self.name = name
        self.source = source
        self.destination = destination
        self.sourceName = source.name
        self.destName = destination.name

    def __del__(self):
        print(f"Deleting UMLRelationship:<{self.name}>...")
    
    def __repr__(self):
        return self.name
        
    def rename(self, new_name : str):
        self.name = new_name

    def changeSource(self, new_source):
        self.source = new_source
        self.sourceName = new_source.name

    def changeDestination(self, new_dest):
        self.destination = new_dest
        self.destName = new_dest.name


##########################################################################################

def add_relationship(source, destination):

    #Add a relationship by creating a new UMLRelationship object containing
    #the name "<source>-<destination>", uml_class associated with the source 
    #string, and the uml_class associated with the destination string
    
    #parameters:
    #source- String that is set as the name of a UMLClass object
    #destination- String that is set as the name of a UMLClass object
    

    if check_params(source, destination) == False:
        return
    else:
        name = source + "-" + destination
        #Ensure the relationship does not already exist
        if name in relationship_dict.keys():
            print(f"ERROR: Relationship {name} already exists")
            return
        #Create the UMLRelationship and add it to the dictionary
        else:
            new_rel = UMLRelationship(source + "-" + destination, 
                uml_class.class_dict[source], uml_class.class_dict[destination])
            relationship_dict.update({name: new_rel})

##########################################################################################

def delete_relationship(source, destination):

    #Delete a relationship between source and destination
    
    #parameters:
    #source- String that is set as the name of a UMLClass object
    #destination- String that is set as the name of a UMLClass object

    name = source + "-" + destination

    if check_params(source, destination) == False:
        return
    else:
        #Ensure that the relationship exists
        if name not in relationship_dict.keys():
            print(f"ERROR: Relationship {name}, does not exist.")
        else:
            del relationship_dict[name]

##########################################################################################

def rel_cleanup(source):

    #Delete all relationships involving the UMLClass object
    #associated with source

    #parameters:
    #source- String that is set as the name of a UMLClass object
    
    if source in uml_class.class_dict.keys():
        for key in list(relationship_dict.keys()):
            #Compare the source attribute of the UMLRelationship object with
            #the UMLClass object associated with source
            if relationship_dict[key].source == uml_class.class_dict[source]:
                del relationship_dict[key]
            #Compare the destination attribute of the UMLRelationship object with
            #the UMLClass object associated with source
            elif relationship_dict[key].destination == uml_class.class_dict[source]:
                del relationship_dict[key]

def list_relationships():

    #List all relationships in the form "<source>-<destination>"

    if len(relationship_dict) == 0:
        print("No relationships exist.")

    for key in relationship_dict:
        print(key)

def rename_relationship(old_name, new_name):

    #Find all relationships with the old name, delete the old relationships
    #then create a new relationship to replace the old one with the updated
    #UMLClass object

    if new_name in uml_class.class_dict.keys():
        for key in list(relationship_dict.keys()):
            #Compare the source name of the UMLRelationship object with
            #the old name to see if the current relationship should be updated
            if relationship_dict[key].sourceName == old_name:
                source = new_name
                destination = relationship_dict[key].destName
                del relationship_dict[key]
                add_relationship(source, destination)                
            #Compare the destination name of the UMLRelationship object with
            #the old name to see if the current relationship should be updated
            elif relationship_dict[key].destination == old_name:
                source = relationship_dict[key].sourceName
                destination = new_name
                del relationship_dict[key]
                add_relationship(source, destination)

def check_params(source, destination):
    
    #Checks to see if source and destination are valid classes
    #If either source or destination are invalid, print an error
    #and return false

    #parameters:
    #source- String that is set as the name of a UMLClass object
    #destination- String that is set as the name of a UMLClass object


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

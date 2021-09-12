import uml_class

uml_class.class_dict
relationship_dict = dict()

def add_relationship(source, destination):
    
    found_source = False
    found_dest = False

    #Ensure both destination and source exist.

    for key in uml_class.class_dict:
        if key == source:
            found_source = True
        if key == destination:
            found_dest = True

    if found_source == False and found_dest == False:
        print("Invalid source and destination, both arguements must be existing classes.")
        return

    if found_source == False:
        print("Invalid source, source must be an existing class.")
        return

    if found_dest == False:
        print("Invalid destination, destination must be an existing class.")
        return

    #Ensure the relationship does not already exist
    
    if (source + "-" + destination) in relationship_dict.keys():
        print("Relationship already exists")
        return

    #Add an element of the relationship dictionary that contains the key:value pair
    # "source-destination" : (obj<sourceName>, obj<destinationName>)
    relationship_dict[source + "-" + destination] = (uml_class.class_dict[source], uml_class.class_dict[destination])


def delete_relationship (source, destination):

    found_source = False
    found_dest = False

    #Ensure both destination and source exist.

    for key in uml_class.class_dict:
        if key == source:
            found_source = True
        if key == destination:
            found_dest = True

    if found_source == False and found_dest == False:
        print("Invalid source and destination, both arguements must be existing classes.")
        return

    if found_source == False:
        print("Invalid source, source must be an existing class.")
        return

    if found_dest == False:
        print("Invalid destination, destination must be an existing class.")
        return

    #Ensure relationship actually exists
    if (source + "-" + destination) not in relationship_dict.keys():
        print("Relationship does not exist")
        return

    del relationship_dict[source + "-" + destination]


def list_relationships():

    if len(relationship_dict) == 0:
        print("No relationships exist.")

    for key in relationship_dict:
        print(key)

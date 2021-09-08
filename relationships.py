def add_relationship(class_dict, source, destination, rel_dict):
    
    found_source = False
    found_dest = False

    #Ensure both destination and source exist.

    for key in class_dict:
        if key == source:
            found_source = True
        if key == found_dest:
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
    
    if (source + "-" + destination) in rel_dict.keys():
        print("Relationship already exists")
        return

    #Add an element of the relationship dictionary that contains the key:value pair
    # "source-destination" : (obj<sourceName>, obj<destinationName>)
    rel_dict[source + "-" + destination] = (class_dict[source], class_dict[destination])

    #return the dictionary with the new relationship included
    return rel_dict

def delete_relationship (class_dict, source, destination, rel_dict):

    found_source = False
    found_dest = False

    #Ensure both destination and source exist.

    for key in class_dict:
        if key == source:
            found_source = True
        if key == found_dest:
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

    del rel_dict[source + "-" + destination]

    #Return the dictionary minus the deleted relationship
    return rel_dict
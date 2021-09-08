def add_relationship(class_dict, source, destination, rel_dict):
    
    found_source = False
    found_dest = False

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

    #relationship checking for sprint 2
    #if rel_type not in {"Aggregation", "Composition", "Inheritance", "Realization"}:
    #    print("Invalid type")

    rel_dict[source + "-" + destination] = (class_dict[source], class_dict[destination])

    return rel_dict

def delete_relationship (class_dict, source, destination, rel_dict):

    found_source = False
    found_dest = False

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

    return rel_dict
def add_relationship(dict, class_list, source, destination):
    
    found_source = False
    found_dest = False

    for key in dict:
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

    #if rel_type not in {"Aggregation", "Composition", "Inheritance", "Realization"}:
    #    print("Invalid type")

    
from uml_components import UMLRelationship

# check a relationship can be added
def add_rel () :
    rel = UMLRelationship ()

# check for adding a relationship with invalid sources
def invalid_source_rel () :
    rel = UMLRelationship ()

# check for adding a relationship with invalid source and destination
def invalid_source_destination_rel () :
    rel = UMLRelationship ()

# check for adding a relationship with an invalid destination
def invalid_destination_rel () :
    rel = UMLRelationship ()

# check for adding a duplicate relationship
def dupl_rel () :
    rel = UMLRelationship ()

# checks for deleting a non-existant relationship
def del_ne_rel () :
    rel = UMLRelationship ()

# checks for deleting a relationship
def del_rel () :
    rel = UMLRelationship ()

# checks for deleting an invalid source
def del_invalid_source () :
    rel = UMLRelationship ()

# checks for deleting a relationship with an invalid and destination
def del_invalid_source_destination () :
    rel = UMLRelationship ()

# checks for deleting a relationship with an invalid destination
def del_invalid_destination () :
    rel = UMLRelationship ()

# checks for an empty relationship dictionary
def empty_rel_dict () :
    rel = UMLRelationship ()

# checks for listing all classes when no classes exist
def list_rel_dict () :
    rel = UMLRelationship ()

# checks for listing a class that does not exist
def list_ne_class_rel () :
    rel = UMLRelationship ()

# checks save error handling when no classes are created
def error_handle_rel () :
    rel = UMLRelationship ()

# checks for testing load abort
def load_abort_rel () :
    rel = UMLRelationship ()
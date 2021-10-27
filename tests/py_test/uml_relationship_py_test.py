from uml_components import UMLRelationship
from uml_components import UMLClass
import io
import sys
import snake_uml

# check a relationship can be added
def test_add_rel () :
    snake_uml.main (sys.argv)
    assert UMLRelationship.relationship_list["class1-class2"].source == UMLClass.class_dict["class1"]
    assert UMLRelationship.relationship_list["class1-class2"].source == UMLClass.class_dict["class2"]
    assert len (UMLRelationship.relationship_list) == 1
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# check for adding a relationship with invalid sources
def test_invalid_source_rel () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "ERROR: class3 is invalid, source must be an existing class.\n" in out.getvalue (), True
    assert len (UMLRelationship.relationship_list) == 0
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# check for adding a relationship with invalid source and destination
def test_invalid_source_destination_rel () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "ERROR: class4 and class3 are invalid, both arguments must be existing classes.\n" in out.getvalue () == True
    assert len(UMLRelationship.relationship_list) == 0
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# check for adding a relationship with an invalid destination
def test_invalid_destination_rel () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Error: class3 is invalid, destination must be an existing class.\n" in out.getvalue (), True
    assert len (UMLRelationship.relationship_list) == 0
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# check for adding a duplicate relationship
def test_dupl_rel () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "<Relationship Add Error>: Relationship class5-class6 already exists." in out.getvalue () == True
    assert len (UMLRelationship.relationship_list) == 1
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# checks for deleting a non-existant relationship
def test_del_ne_rel () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Error: Relationship class1-class2, does not exist.\n" in out.getvalue () == True
    assert len (UMLRelationship.relationship_list) == 0
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# checks for deleting a relationship
def test_del_rel () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert UMLRelationship.relationship_list == {}
    assert len (UMLRelationship.relationship_list) == 0
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# checks for deleting an invalid source
def test_del_invalid_source () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "<Error: class3 is invalid, source must be an existing class.\n" in out.getvalue () == True
    assert len (UMLRelationship.relationship_list) == 0
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# checks for deleting a relationship with an invalid and destination
def test_del_invalid_source_destination () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Error: class4 and class3 are invalid, both arguments must be existing classes.\n" in out.getvalue () == True
    assert len (UMLRelationship.relationship_list) == 0
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# checks for deleting a relationship with an invalid destination
def test_del_invalid_destination () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Error: class3 is invalid, destination must be an existing class.\n" in out.getvalue () == True
    assert len (UMLRelationship.relationship_list) == 0
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# checks for an empty relationship dictionary
def test_empty_rel_dict () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "(none)" in out.getvalue () == True
    assert len (UMLRelationship.relationship_list) == 0
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# checks for listing all classes when no classes exist
def test_list_rel_dict () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "(none)" in out.getvalue () == True
    assert len (UMLClass.class_dict) == 0
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# checks for listing a class that does not exist
def test_list_ne_class_rel () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "<Illegal Argument Error>: class1 does not exist as a class." in out.getvalue () == True
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# checks save error handling when no classes are created
def test_error_handle_rel () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Error: There are no classes in the class dictionary.\nSave failed." in out.getvalue () == True
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# checks for testing load abort
def test_load_abort_rel () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Load cancelled." in out.getvalue () == True
    assert len (UMLRelationship.relationship_list) == 0
    assert len (UMLClass.class_dict) == 0
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}
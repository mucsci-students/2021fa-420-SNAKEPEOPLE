from uml_components import UMLRelationship
from uml_components import UMLClass
from uml_components.interfaces import rel_interface, class_interface
import io
import sys
import snake_uml

# check a relationship can be added
def test_add_rel () :
    class_interface.add_class ("class1")
    rel_interface.add_relationship ("class1")
    rel_interface.add_relationship ("class2")
    snake_uml.main (sys.argv)
    assert rel_interface.find_rel ("class1") == class_interface.__name__
    class_interface.add_class ("class2")
    assert rel_interface.find_rel ("class2") == class_interface.__name__
    assert len (rel_interface.relationship_list) == 1
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# check for adding a relationship with invalid sources
def test_invalid_source_rel () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "ERROR: class is invalid, source must be an existing class.\n" in out.getvalue (), True
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
    assert "ERROR: classes are invalid, both arguments must be existing classes.\n" in out.getvalue () == True
    assert len (rel_interface.relationship_list) == 0
    del out
    class_interface.class_dict = {}
    rel_interface.relationship_list = {}

# check for adding a relationship with an invalid destination
def test_invalid_destination_rel () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Error: class is invalid, destination must be an existing class.\n" in out.getvalue (), True
    assert len (rel_interface.relationship_list) == 0
    del out
    class_interface.class_dict = {}
    rel_interface.relationship_list = {}

# check for adding a duplicate relationship
def test_dupl_rel () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Error: Relationship classes already exists." in out.getvalue () == True
    assert len (rel_interface.relationship_list) == 1
    del out
    class_interface.class_dict = {}
    rel_interface.relationship_list = {}

# checks for deleting a non-existant relationship
def test_del_ne_rel () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Error: Relationship class, does not exist.\n" in out.getvalue () == True
    assert len (rel_interface.relationship_list) == 0
    del out
    class_interface.class_dict = {}
    rel_interface.relationship_list = {}

# checks for deleting a relationship
def test_del_rel () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert rel_interface.relationship_list == {}
    assert len (rel_interface.relationship_list) == 0
    del out
    class_interface.class_dict = {}
    rel_interface.relationship_list = {}

# checks for deleting an invalid source
def test_del_invalid_source () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Error: class is invalid, source must be an existing class.\n" in out.getvalue () == True
    assert len (rel_interface.relationship_list) == 0
    del out
    class_interface.class_dict = {}
    rel_interface.relationship_list = {}

# checks for deleting a relationship with an invalid and destination
def test_del_invalid_source_destination () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Error: classes are invalid, both arguments must be existing classes.\n" in out.getvalue () == True
    assert len (rel_interface.relationship_list) == 0
    del out
    class_interface.class_dict = {}
    rel_interface.relationship_list = {}

# checks for deleting a relationship with an invalid destination
def test_del_invalid_destination () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Error: class is invalid, destination must be an existing class.\n" in out.getvalue () == True
    assert len (rel_interface.relationship_list) == 0
    del out
    class_interface.class_dict = {}
    rel_interface.relationship_list = {}

# checks for an empty relationship dictionary
def test_empty_rel_dict () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "(none)" in out.getvalue () == True
    assert len (rel_interface.relationship_list) == 0
    del out
    class_interface.class_dict = {}
    rel_interface.relationship_list = {}

# checks for listing all classes when no classes exist
def test_list_rel_dict () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "(none)" in out.getvalue () == True
    assert len (UMLClass.class_dict) == 0
    del out
    class_interface.class_dict = {}
    rel_interface.relationship_list = {}

# checks for listing a class that does not exist
def test_list_ne_class_rel () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Error: class does not exist as a class." in out.getvalue () == True
    del out
    class_interface.class_dict = {}
    rel_interface.relationship_list = {}

# checks save error handling when no classes are created
def test_error_handle_rel () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Error: There are no classes in the class dictionary.\nSave failed." in out.getvalue () == True
    del out
    class_interface.class_dict = {}
    rel_interface.relationship_list = {}

# checks for testing load abort
def test_load_abort_rel () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Load cancelled." in out.getvalue () == True
    assert len (rel_interface.relationship_list) == 0
    assert len (class_interface.class_dict) == 0
    del out
    class_interface.class_dict = {}
    rel_interface.relationship_list = {}
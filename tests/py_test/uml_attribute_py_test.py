from uml_components import UMLAttributes
from uml_components import UMLClass
from uml_components import UMLRelationship
import io
import sys
import snake_uml
from uml_components.interfaces import class_interface, attr_interface, rel_interface

# check adding an attribute to a class
def test_add_attr () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert uml.class_dict["class1"].attributes[0] == "stuff"
    assert len (uml.class_dict) == 1
    assert len (uml.class_dict["class1"].attributes) == 1
    del out
    uml.class_dict = {}
    UMLRelationship.relationship_list = {}

# check if an error message appears if a duplicate attribute is added
def test_err_attr () :
    uml = UMLClass ("class1")
    uml.class_dict["class1"].add_attr ("stuff")
    uml.class_dict["class1"].add_attr ("stuff")
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Attribute already exists as an attribute of class1. " in out.getvalue () == True
    assert len (UMLClass.class_dict) == 1
    assert len (UMLClass.class_dict["class1"].attributes) == 1
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# check adding an attribute to a non-existant class
def test_ne_attr_class () :
    uml = UMLClass ()
    uml.class_dict["class1"].add_attr ("stuff")
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Class name does not exist." in out.getvalue () == True
    assert len (UMLRelationship.relationship_list) == 0
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# check renaming an attribute
def test_rename_attr () :
    uml = UMLClass ()
    uml.class_dict.addclass ("class1")
    uml.class_dict["class1"].add_attr ("stuff")
    uml.class_dict["class1"].rename_attr ("stuff", "stuff2")
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert UMLClass.class_dict["class1"].attributes[0] == "stuff2"
    assert UMLClass.class_dict["class1"].attributes == 1
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# check renaming a non-existant attribute
def test_rename_ne_attr () :
    uml = UMLClass ()
    uml.class_dict.add_class ("class1")
    uml.class_dict["class1"].rename_attr ("stuff", "stuff2")
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Attribute does not exist as the name of an attribute in class1" in out.getvalue () == True
    assert len (UMLClass.class_dict["class_1"].attributes) == 0
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# check renaming an attribute of an already existing attrbute
def test_rename_dup_attr () :
    uml = UMLClass ()
    uml.class_dict.addclass ("class1")
    uml.class_dict["class1"].add_attr ("stuff")
    uml.class_dict["class1"].add_attr ("stuff2")
    uml.class_dict["class1"].rename_attr ("stuff", "stuff2")
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "<Attribute Rename Error [Invalid Name: 3]>: stuff2 already exists as an attribute in class1" in out.getvalue () == True
    assert UMLClass.class_dict["class1"].attributes[0] == "stuff"
    assert UMLClass.class_dict["class1"].attributes[1] == "stuff2"
    assert len (UMLClass.class_dict["class1"].attributes) == 2
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# check deleting an attribute
def test_del_attr () :
    uml = UMLClass ()
    uml.class_dict.add_class ("class1")
    uml.class_dict["class1"].add_attr ("stuff")
    uml.class_dict["class1"].del_attr ("stuff")
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert len (UMLClass.class_dict["class1"].attributes) == 0
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}


# check deleting an attribute that does not exist from a class
def test_del_ne_clss_attr () :
    uml = UMLClass ()
    uml.class_dict.add_class ("class1")
    uml.class_dict["class1"].del_attr ("stuff")
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Attribute does not exist as the name of an attribute in class1." in out.getvalue () == True
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# check deleting an attribute from a class that does not exist
def test_del_attr_frm_nothing () :
    uml = UMLClass ()
    uml.class_dict["class1"].del_attr ("stuff")
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Class named class1 does not exist." in out.getvalue () == True
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}
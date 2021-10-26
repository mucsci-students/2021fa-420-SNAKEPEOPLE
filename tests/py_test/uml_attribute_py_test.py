from uml_components import UMLAttributes
from uml_components import UMLClass
from uml_components import UMLRelationship
import io
import sys
import snake_uml

# check adding an attribute to a class
def add_attr () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert UMLClass.class_dict["class1"].attributes[0] == "stuff"
    assert len (UMLClass.class_dict) == 1
    assert len (UMLClass.class_dict["class1"].attributes) == 1
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# check if an error message appears if a duplicate attribute is added
def err_attr () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "<Attribute Add Error [Invalid Name: 2]>: stuff already exists as an attribute of class1." in out.getvalue () == True
    assert len (UMLClass.class_dict) == 1
    assert len (UMLClass.class_dict["class1"].attributes) == 1
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# check adding an attribute to a non-existant class
def ne_attr_class () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "<Attribute Add Error [Invalid Class]>: Class name class1 does not exist." in out.getvalue () == True
    assert len (UMLRelationship.relationship_list) == 0
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# check renaming an attribute
def rename_attr () :
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
def rename_ne_attr () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "<Attribute Rename Error [Invalid Name: 1]>: stuff does not exist as the name of an attribute in class1" in out.getvalue () == True
    assert len (UMLClass.class_dict["class_1"].attributes) == 0
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# check renaming an attribute of an already existing attrbute
def rename_dup_attr () :
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
def del_attr () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert len (UMLClass.class_dict["class1"].attributes) == 0
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}


# check deleting an attribute that does not exist from a class
def del_ne_clss_attr () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "<Attribute Delete Error [Invalid Name]>: stuff does not exist as the name of an attribute in class1." in out.getvalue () == True
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}

# check deleting an attribute from a class that does not exist
def del_attr_frm_nothing () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "<Attribute Delete Error [Invalid Class]>: Class named class1 does not exist." in out.getvalue () == True
    del out
    UMLClass.class_dict = {}
    UMLRelationship.relationship_list = {}
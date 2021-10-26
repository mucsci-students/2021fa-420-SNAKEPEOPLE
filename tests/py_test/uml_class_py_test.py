from uml_components import UMLClass
import py_test
import io
import sys
import snake_uml

# checks for empty uml_class
def empty_uml () :
    uml = UMLClass ()
    assert uml == ()

# check adding two uml classes
def two_uml_class () :
    UMLClass.class_dict["class1"].name, "class1"
    UMLClass.class_dict["class2"].name, "class2"
    UMLClass.class_dict["class1"].attributes, []
    UMLClass.class_dict["class2"].attributes, []
    assert UMLClass.class_dict["class1"].name == "class1"
    assert UMLClass.class_dict["class2"].name == "class2"
    assert UMLClass.class_dict["class1"].attributes == []
    assert UMLClass.class_dict["class2"].attributes == []

# check input for improper argument lengths
def input_length_uml_class () :
    uml = UMLClass ()
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "<Invalid Arguments Error>\n1 arguments expected, 0 arguments received" in out.getvalue () == True
    assert len (UMLClass.class_dict) == 0
    del out

# check invalid input of proper length
def input_invalid_uml_class () :
    uml = UMLClass ()
    uml.class_dict = {}
    out = io.StringIO
    sys.stdout = out 
    snake_uml.main (sys.argv)
    assert "<Invalid Arguments Error>\n1 arguments expected. 0 arguments received." in out.getvalue () == True
    assert len (uml.class_dict) == 0
    del out
    uml.class_dict = {}

# check adding a duplicate uml class
def duplicate_uml_class () :
    UMLClass.class_dict = {}
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "\n<Class Add Error [Invalid Name: 2]>: Class named 'class1' already exists.\n" in out.getvalue () == True
    del out
    UMLClass.class_dict = {}

# check deleting a uml class
def delete_uml_class () :
    snake_uml.main (sys.argv)
    out = io.StringIO ()
    sys.stdout = out
    sys.stdout = sys.__stdout__
    assert UMLClass.class_dict == {}
    assert len (UMLClass.class_dict) == 0
    UMLClass.class_dict = {}

# check deleting a non-existant uml class
def delete_ne_uml_class () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "<Class Delete Error [Invalid Name]>: Class named 'class 1' does not exist." in out.getvalue () == True
    assert len (UMLClass.class_dict) == 0
    del out
    UMLClass.class_dict = {}

# check renaming a uml class
def rename_uml_class () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert UMLClass.class_dict["class2"].name == "class2"
    assert len (UMLClass.class_dict) == 1
    del out
    UMLClass.class_dict = {}

# check renaming a nonexistant uml class
def rename_ne_uml_class () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "<Class Rename Error [Invalid Name: 1]>: class1 does not exist as the name of a class." in out.getvalue () == True
    del out
    UMLClass.class_dict = {}

# check renaming an already existing uml class
def rename_ae_uml_class () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "<Class Rename Error [Invalid Name: 3]>: Class name 'class2' already exists." in out.getvalue () == True
    assert len (UMLClass.class_dict) == 2
    del out
    UMLClass.class_dict = {}
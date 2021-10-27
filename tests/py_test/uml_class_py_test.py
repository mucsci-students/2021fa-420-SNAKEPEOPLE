from uml_components import UMLClass
import py_test
import io
import sys
import snake_uml

# checks for empty uml_class
def test_empty_uml () :
    uml = UMLClass ()
    assert uml == ()

# check adding two uml classes
def test_two_uml_class () :
    uml = UMLClass ()
    uml.class_dict.addclass ("class1")
    uml.class_dict.addclass ("class2")
    assert UMLClass.class_dict["class1"].name == "class1"
    assert UMLClass.class_dict["class2"].name == "class2"

# check input for improper argument lengths
def test_input_length_uml_class () :
    uml = UMLClass ()
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Error: arguments expected, 0 arguments received" in out.getvalue () == True
    assert len (uml.class_dict) == 0
    del out

# check invalid input of proper length
def test_input_invalid_uml_class () :
    uml = UMLClass ()
    uml.class_dict = {}
    out = io.StringIO
    sys.stdout = out 
    snake_uml.main (sys.argv)
    assert "Error: invalid command." in out.getvalue () == True
    assert len (uml.class_dict) == 0
    del out
    uml.class_dict = {}

# check adding a duplicate uml class
def test_duplicate_uml_class () :
    uml = UMLClass ()
    uml.class_dict.addclass ("class1")
    uml.class_dict.addclass ("class1")
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Class named 'class1' already exists.\n" in out.getvalue () == True
    del out
    uml.class_dict = {}

# check deleting a uml class
def test_delete_uml_class () :
    uml = UMLClass ()
    uml.class_dict.addclass ("class1")
    uml.class_dict.delclass ("class1")
    snake_uml.main (sys.argv)
    out = io.StringIO ()
    sys.stdout = out
    sys.stdout = sys.__stdout__
    assert uml.class_dict == {}
    assert len (uml.class_dict) == 0
    uml.class_dict = {}

# check deleting a non-existant uml class
def test_delete_ne_uml_class () :
    uml = UMLClass ()
    uml.class_dict.delclass ("class1")
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Class named 'class 1' does not exist." in out.getvalue () == True
    assert len (uml.class_dict) == 0
    del out
    uml.class_dict = {}

# check renaming a uml class
def test_rename_uml_class () :
    uml = UMLClass ()
    uml.class_dict.addclass ("class1")
    uml.class_dict.Rename ("class1", "class2")
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert uml.class_dict["class2"].name == "class2"
    assert len (uml.class_dict) == 1
    del out
    uml.class_dict = {}

# check renaming a nonexistant uml class
def test_rename_ne_uml_class () :
    uml = UMLClass ()
    uml.class_dict.Rename ("class1", "class2")
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Error: class1 does not exist as the name of a class." in out.getvalue () == True
    del out
    uml.class_dict = {}

# check renaming an already existing uml class
def test_rename_ae_uml_class () :
    uml = UMLClass ()
    uml.class_dict.addclass ("class1")
    uml.class_dict.addclass ("class2")
    uml.class_dict.Rename ("class1", "class2")
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Error: Class name 'class2' already exists." in out.getvalue () == True
    assert len (uml.class_dict) == 2
    del out
    uml.class_dict = {}
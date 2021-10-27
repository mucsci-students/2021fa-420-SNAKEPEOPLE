import py_test
import io
import sys
from uml_components.interfaces import class_interface
import snake_uml

# checks for empty uml_class
def test_empty_uml () :
    #uml = UMLClass ()
    assert class_interface == ()

# check adding two uml classes
def test_two_uml_class () :
    class_interface.add_class ("class1")
    class_interface.add_class ("class2")
    assert class_interface.class_dict["class1"] == "class1"
    assert class_interface.class_dict["class2"] == "class2"

# check input for improper argument lengths
def test_input_length_uml_class () :
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Error: arguments expected, 0 arguments received" in out.getvalue () == True
    assert len (class_interface.class_dict) == 0
    del out

# check invalid input of proper length
def test_input_invalid_uml_class () :
    #class_interface = {}
    out = io.StringIO
    sys.stdout = out 
    snake_uml.main (sys.argv)
    assert "Error: invalid command." in out.getvalue () == True
    assert len (class_interface.class_dict) == 0
    del out
    class_interface.class_dict = {}

# check adding a duplicate uml class
def test_duplicate_uml_class () :
    class_interface.add_class ("class1")
    class_interface.add_class ("class1")
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert class_interface.class_dict["class1"] == "class1"
    assert "Class named 'class1' already exists.\n" in out.getvalue () == True
    del out
    class_interface.class_dict = {}

# check deleting a uml class
def test_delete_uml_class () :
    class_interface.add_class ("class1")
    class_interface.delete_class ("class")
    snake_uml.main (sys.argv)
    out = io.StringIO ()
    sys.stdout = out
    sys.stdout = sys.__stdout__
    assert class_interface.class_dict == {}
    assert len (class_interface.class_dict) == 0

# check deleting a non-existant uml class
def test_delete_ne_uml_class () :
    class_interface.delete_class ("class1")
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Class named 'class 1' does not exist." in out.getvalue () == True
    assert len (class_interface.class_dict) == 0
    del out
    class_interface.class_dict = {}

# check renaming a uml class
def test_rename_uml_class () :
    class_interface.add_class ("class1")
    class_interface.rename_class ("class2")
    # out = io.StringIO ()
    # sys.stdout = out
    # snake_uml.main (sys.argv)
    # sys.stdout = sys.__stdout__
    assert class_interface.class_dict["class2"] == "class2"
    assert len (class_interface.class_dict) == 1
    # del out
    class_interface.class_dict = {}

# check renaming a nonexistant uml class
def test_rename_ne_uml_class () :
    class_interface.rename_class ("class1", "class2")
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Error: class1 does not exist as the name of a class." in out.getvalue () == True
    del out
    class_interface.class_dict = {}

# check renaming an already existing uml class
def test_rename_ae_uml_class () :
    class_interface.add_class ("class1")
    class_interface.add_class ("class2")
    class_interface.rename_class ("class1", "class2")
    out = io.StringIO ()
    sys.stdout = out
    snake_uml.main (sys.argv)
    sys.stdout = sys.__stdout__
    assert "Error: Class name 'class2' already exists." in out.getvalue () == True
    assert len (class_interface.class_dict) == 2
    del out
    class_interface.class_dict = {}
import pytest
from uml_components.UMLAttributes import UMLField, UMLMethod, UMLParameter
from uml_components import UMLClass
from uml_components.interfaces import class_interface, attr_interface, rel_interface

def test_add_field () :
    class_interface.add_class ("class1")
    assert attr_interface.add_field ("class1", "attr1", "type1")[0]

def test_add_method () :
    class_interface.add_class ("class2")
    assert attr_interface.add_method ("class2", "method2", "type2")[0]
    
def test_add_param () :
    class_interface.add_class ("class12")
    uml : UMLClass.UMLClass = UMLClass.class_dict['class12']
    umlM = attr_interface.add_method ("class12", "method12", "int")
    attr_interface.add_param ("class12", "method12", "param12", "int")
    assert attr_interface.find_param (umlM[0], "param12")

def test_rename_field () :
    class_interface.add_class ("class4")
    attr_interface.add_field ("class4", "field4", "type4")
    assert isinstance (attr_interface.rename_field ("class4", "field4", "newfield"), tuple)

def test_rename_method () :
    class_interface.add_class ("class5")
    attr_interface.add_method ("class5", "method5", "type5")
    assert isinstance (attr_interface.rename_method ("class5", "method5", "newmethod"), tuple)

def test_rename_param () :
    class_interface.add_class ("tanner")
    tanner = UMLClass.class_dict["tanner"]
    tanner.add_method ("doHW", "bool")
    tanner.add_method_param (tanner.methods[0], "pp", "int")
    assert attr_interface.rename_param ("tanner", "doHW", "pp", "ppp")

def test_delete_field () :
    class_interface.add_class ("class7")
    attr_interface.add_field ("class7", "field7", "type7")
    assert attr_interface.delete_field ("class7", "field7")

def test_delete_method () :
    class_interface.add_class ("class8")
    attr_interface.add_method ("class8", "method8", "type8")
    assert attr_interface.delete_method ("class8", "method8")

def test_delete_param () :
    class_interface.add_class("beenis")
    beenis = class_interface.class_dict["beenis"]
    beenis.add_method ("quicksort", "int")
    beenis.add_method_param (beenis.methods[0], "p", "double")
    me = beenis.methods[0]
    assert attr_interface.delete_param ("beenis", "quicksort", "p")

def test_find_field () :
    testF = UMLField ("fieldtest", "typetest")
    class_interface.add_class ("class10")
    assert attr_interface.add_field ("class10", "field10", "type10")
    umlT = class_interface.class_dict["class10"]
    assert attr_interface.find_field (umlT, "field10") 

def test_find_method () :
    assert class_interface.add_class ("class11")
    assert attr_interface.add_method ("class11", "method11", "int")
    umlT2 = class_interface.class_dict["class11"]
    assert attr_interface.find_method (umlT2, "method11")

def test_find_param () :
    class_interface.add_class ("sadge")
    sad = class_interface.class_dict["sadge"]
    sad.add_method ("crying", "int")
    sad.add_method_param (sad.methods[0], "p", "double")
    assert attr_interface.find_param (sad.methods[0], "p")

def test_find_field_two () :
    class_interface.add_class ("Super")
    assert isinstance (attr_interface.add_field ("Super", "static", "auto"), tuple)
    umlF2 = class_interface.class_dict["Super"]
    assert attr_interface.find_field (umlF2, "static")

def test_find_method_two () :
    assert class_interface.add_class ("ClassM")
    assert attr_interface.add_method ("ClassM", "BubbleSort", "void")
    umlM2 = class_interface.class_dict["ClassM"]
    assert attr_interface.find_method (umlM2, "BubbleSort")

# Add some tests that fail on invalid input, output
# Have pytest list each test in the terminal

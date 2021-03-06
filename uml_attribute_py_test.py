# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     uml_attribute_py_test.py

# External Imports
import pytest

# Internal Imports
from uml_components.UMLAttributes import UMLField, UMLMethod, UMLParameter
from uml_components import UMLClass
from uml_components.interfaces import class_interface, attr_interface, rel_interface

###################################################################################################

def test_add_field () :
    class_interface.add_class ("class1")
    valid_field = attr_interface.add_field ("class1", "attr1", "type1")[0]
    assert isinstance(valid_field, UMLField)
    UMLClass.class_dict = dict()
    
def test_add_field_duplicate() :
    class_interface.add_class ("class1")
    valid_field = attr_interface.add_field ("class1", "attr1", "type1")[0]
    duplicate = attr_interface.add_field ("class1", "attr1", "type1")[0]
    assert not isinstance(duplicate, UMLField)
    UMLClass.class_dict = dict()
    
def test_add_field_empty_field_name():
    class_interface.add_class("class1")
    empty_field_name = attr_interface.add_field("class1", "", "type")
    assert empty_field_name[1] == "Field name must not be empty."
    UMLClass.class_dict = dict()
    
def test_add_field_invalid_class():
    empty_field_name = attr_interface.add_field("class2", "attr", "type")[0]
    assert not isinstance(empty_field_name, UMLField)
    UMLClass.class_dict = dict()

def test_add_method () :
    class_interface.add_class ("class2")
    assert attr_interface.add_method ("class2", "method2", "type2")[0]
    UMLClass.class_dict = dict()
    
def test_add_method_duplicate() :
    class_interface.add_class ("class1")
    attr_interface.add_method ("class1", "attr1", "type1")[0]
    duplicate = attr_interface.add_method ("class1", "attr1", "type1")[0]
    assert not isinstance(duplicate, UMLMethod)
    UMLClass.class_dict = dict()
    
def test_add_field_empty_method_name():
    class_interface.add_class ("class1")
    empty_field_name = attr_interface.add_method("class1", "", "type")
    assert empty_field_name[1] == "Method name must not be empty."
    UMLClass.class_dict = dict()
    
def test_add_method_invalid_class():
    class_interface.add_class ("class1")
    empty_field_name = attr_interface.add_method("classf", "attr", "type")[0]
    assert not isinstance(empty_field_name, UMLMethod)
    UMLClass.class_dict = dict()

def test_add_param () :
    class_interface.add_class ("class12")
    yikes = UMLClass.class_dict['class12']
    attr_interface.add_method ("class12", "method12", "int")
    benji = attr_interface.add_param ("class12", yikes.methods[0], "param12", "int")[0]
    assert attr_interface.find_param (yikes.methods[0], benji) == True
    UMLClass.class_dict = dict()
    
def test_add_param_invalid_class():
    class_interface.add_class ("class1")
    m = attr_interface.add_method("class1", "test_m", "test_t",[])[0]
    empty_field_name = attr_interface.add_param("classf", m, "p", "t")[0]
    assert not isinstance(empty_field_name, UMLParameter)
    UMLClass.class_dict = dict()
    
def test_add_param_empty_name():
    class_interface.add_class ("class1")
    m = attr_interface.add_method("class1", "test_m", "test_t",[])[0]
    x = attr_interface.add_param("class1", m, "", "t")[0]
    assert not isinstance(x, UMLParameter)
    UMLClass.class_dict = dict()
    
def test_add_duplicate_param():
    class_interface.add_class("class1")
    m = attr_interface.add_method("class1", "test_m", "test_t",[])[0]
    x = attr_interface.add_param("class1", m, "p", "t")[0]
    y = attr_interface.add_param("class1", m, "p", "t")[0]
    assert not isinstance(y, UMLParameter)
    UMLClass.class_dict = dict()
    
def test_add_param_dup_method():
    class_interface.add_class("class1")
    m1 = attr_interface.add_method("class1", "test_m", "test_t",[])[0]
    x = attr_interface.add_param("class1", m1, "p", "t")[0]
    m2 = attr_interface.add_method("class1", "test_m", "test_t")[0]
    y = attr_interface.add_param("class1", m2, "p", "t")[0]
    assert not isinstance(y, UMLParameter)
    UMLClass.class_dict = dict()

def test_add_param_invalid_m():
    class_interface.add_class("class1")
    m = attr_interface.add_method("class1", "test_m", "test_t",[])[0]
    x = attr_interface.add_param("class1", UMLMethod("a", "b"), "p", "t")[0]
    assert not isinstance(x, UMLParameter)
    UMLClass.class_dict = dict()
    
def test_rename_field () :
    class_interface.add_class ("class4")
    keem = attr_interface.add_field ("class4", "field4", "type4")[0]
    assert isinstance (attr_interface.rename_field ("class4", keem, "newfield"), tuple)
    UMLClass.class_dict = dict()
    
def test_rename_field_invcls():
    class_interface.add_class("class1")
    f = attr_interface.add_field("class1", "field_n", "field_t")[0]
    r = attr_interface.rename_field("class2", f, "w")[0]
    assert not isinstance(r, UMLField)
    UMLClass.class_dict = dict()
    
def test_rename_field_emptyn():
    class_interface.add_class("class1")
    f = attr_interface.add_field("class1", "field_n", "field_t")[0]
    r = attr_interface.rename_field("class1", f, "")[0]
    assert not isinstance(r, UMLField)
    UMLClass.class_dict = dict()
    
def test_rename_field_invf():
    class_interface.add_class("class1")
    f = attr_interface.add_field("class1", "field_n", "field_t")[0]
    r = attr_interface.rename_field("class1", UMLField("g", "g"), "w")[0]
    assert not isinstance(r, UMLField)
    UMLClass.class_dict = dict()

def test_rename_method () :
    class_interface.add_class ("class5")
    attr_interface.add_method ("class5", "method5", "type5")
    messy = UMLClass.class_dict["class5"]
    assert isinstance (attr_interface.rename_method ("class5", messy.methods[0], "newmethod"), tuple)
    UMLClass.class_dict = dict()
    
def test_rename_method_invcls():
    class_interface.add_class("class1")
    m = attr_interface.add_method("class1", "m", "t")[0]
    r = attr_interface.rename_method("class2", m, "n")[0]
    assert not isinstance (r, UMLMethod)
    UMLClass.class_dict = dict()
    
def test_rename_method_invnm():
    class_interface.add_class("class1")
    m = attr_interface.add_method("class1", "m", "t")[0]
    r = attr_interface.rename_method("class1", m, "")[0]
    assert not isinstance (r, UMLMethod)
    UMLClass.class_dict = dict()

def test_rename_param () :
    class_interface.add_class ("tanner")
    tanner = UMLClass.class_dict["tanner"]
    tanner.add_method ("doHW", "bool")
    tannerP = tanner.add_method_param (tanner.methods[0], "pp", "int")
    assert attr_interface.rename_param ("tanner", tanner.methods[0], tannerP, "ppp")

###################################################################################################

def test_delete_field () :
    class_interface.add_class ("class7")
    maxy = attr_interface.add_field ("class7", "field7", "type7")[0]
    assert attr_interface.delete_field ("class7", maxy)

def test_delete_method () :
    class_interface.add_class ("class8")
    cultist = attr_interface.add_method ("class8", "method8", "type8")[0]
    assert attr_interface.delete_method ("class8", cultist)

def test_delete_param () :
    class_interface.add_class("beenis")
    beenis : UMLClass.UMLClass = UMLClass.class_dict["beenis"]
    beenis.add_method ("quicksort", "int")
    me : UMLMethod = beenis.methods[0]
    beenisP = beenis.add_method_param (me, "p", "double")
    assert attr_interface.delete_param ("beenis", me, beenisP)

###################################################################################################

def test_find_field () :
    testF = UMLField ("fieldtest", "typetest")
    class_interface.add_class ("class10")
    assert attr_interface.add_field ("class10", "field10", "type10")
    umlT = UMLClass.class_dict["class10"]
    assert attr_interface.find_field (umlT, umlT.fields[0]) == True

def test_find_method () :
    assert class_interface.add_class ("class11")
    assert attr_interface.add_method ("class11", "method11", "int")
    umlT2 = UMLClass.class_dict["class11"]
    assert attr_interface.find_method (umlT2, umlT2.methods[0]) == True

def test_find_param () :
    class_interface.add_class ("sadge")
    sad = UMLClass.class_dict["sadge"]
    sad.add_method ("crying", "int")
    sad.add_method_param (sad.methods[0], "p", "double")
    assert attr_interface.find_param (sad.methods[0], sad.methods[0].params[0]) == True

def test_find_field_two () :
    class_interface.add_class ("Super")
    assert isinstance (attr_interface.add_field ("Super", "static", "auto"), tuple)
    umlF2 = UMLClass.class_dict["Super"]
    assert attr_interface.find_field (umlF2, umlF2.fields[0]) == True

def test_find_method_two () :
    assert class_interface.add_class ("ClassM")
    assert attr_interface.add_method ("ClassM", "BubbleSort", "void")
    umlM2 = UMLClass.class_dict["ClassM"]
    assert attr_interface.find_method (umlM2, umlM2.methods[0]) == True

###################################################################################################

# Add some tests that fail on invalid input, output
# Have pytest list each test in the terminal

###################################################################################################

import pytest
from uml_components.UMLAttributes import UMLMethod, UMLParameter
from uml_components.interfaces import class_interface, attr_interface, rel_interface

def test_add_field () :
    class_interface.add_class ("class1")
    assert attr_interface.add_field ("class1", "attr1", "type1")

def test_add_method () :
    class_interface.add_class ("class2")
    assert attr_interface.add_method ("class2", "method2", "type2")
    
# def test_add_param () :
#     class_interface.add_class ("class3")
#     assert attr_interface.add_param ("class3", "method3", "param3", "type3")

def test_rename_field () :
    class_interface.add_class ("class4")
    attr_interface.add_field ("class4", "field4", "type4")
    assert attr_interface.rename_field ("class4", "field4", "newfield")

def test_rename_method () :
    class_interface.add_class ("class5")
    attr_interface.add_method ("class5", "method5", "type5")
    assert attr_interface.rename_method ("class5", "method5", "newmethod")

# def test_rename_param () :
#     class_interface.add_class ("class6")
#     attr_interface.add_param ("class6", "method6", "param6", "type6")
#     assert attr_interface.rename_param ("class6", "method6", "param6", "newparam")

def test_delete_field () :
    class_interface.add_class ("class7")
    attr_interface.add_field ("class7", "field7", "type7")
    assert attr_interface.delete_field ("class7", "field7")

def test_delete_method () :
    class_interface.add_class ("class8")
    attr_interface.add_method ("class8", "method8", "type8")
    assert attr_interface.delete_method ("class8", "method8")

# def test_delete_param () :
#     class_interface.add_class ("class9")
#     attr_interface.add_param ("class9", "method9", "param9", "type9")
#     assert attr_interface.delete_param ("class9", "method9", "param9")

def test_find_field () :
    class_interface.add_class ("class10")
    assert attr_interface.add_field ("class10", "field10", "type10")

# def test_find_method () :
#     class_interface.add_class ("class11")
#     assert attr_interface.add_method ("class11", "method11", "type11")

# def test_find_param () :
#     class_interface.add_class ("class12")
#     assert attr_interface.add_param ("class12", "method12", "param12", "type12")

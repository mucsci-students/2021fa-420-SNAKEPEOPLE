from uml_components import UMLAttributes
from uml_components import UMLClass
from uml_components import UMLRelationship
import io
import sys
import snake_uml
from uml_components.interfaces import class_interface, attr_interface, rel_interface

def test_add_field () :
    class_interface.add_class ("class1")
    attr_interface.add_field ("class1", "attr1", "type1")
    #assert attr_interface.class_dict["class1"].__getattribute__ == "attr1"
    assert attr_interface.find_field ("class1", "attr1") == True

def test_add_method () :
    class_interface.add_class ("class2")
    attr_interface.add_method ("class2", "method2", "type2")
    assert attr_interface.find_method ("class2", "method2") == True

def test_add_param () :
    class_interface.add_class ("class3")
    attr_interface.add_param ("class3", "method3", "param3", "type3")
    attr_interface.find_param ("method3", "param3") == True

def test_rename_field () :
    class_interface.add_class ("class4")
    attr_interface.add_field ("class4", "field4", "type4")
    attr_interface.rename_field ("class4", "field4", "newfield")
    assert attr_interface.find_field ("class4", "newfield") == True

def test_rename_method () :
    class_interface.add_class ("class5")
    attr_interface.add_method ("class5", "method5", "type5")
    attr_interface.rename_method ("class5", "method5", "newmethod")
    attr_interface.find_method ("class5", "newmethod") == True

def test_rename_param () :
    class_interface.add_class ("class6")
    attr_interface.add_param ("class6", "method6", "param6", "type6")
    attr_interface.rename_param ("class6", "method6", "param6", "newparam")
    assert attr_interface.find_param ("method6", "newparam") == True

def test_delete_field () :
    class_interface.add_class ("class7")
    attr_interface.add_field ("class7", "field7", "type7")
    attr_interface.delete_field ("class7", "field7")
    assert attr_interface.find_field ("class7", "field7") == False

def test_delete_method () :
    class_interface.add_class ("class8")
    attr_interface.add_method ("class8", "method8", "type8")
    attr_interface.delete_method ("class8", "method8")
    assert attr_interface.find_method ("class8", "method8") == False

def test_delete_param () :
    class_interface.add_class ("class9")
    attr_interface.add_param ("class9", "method9", "param9", "type9")
    attr_interface.delete_param ("class9", "method9", "param9")
    attr_interface.find_param ("method9", "param9") == False

def test_find_field () :
    class_interface.add_class ("class10")
    attr_interface.add_field ("class10", "field10")
    assert attr_interface.find_field ("class10", "field10") == True

def test_find_method () :
    class_interface.add_class ("class11")
    attr_interface.add_method ("class11", "method11", "type11")
    attr_interface.find_method ("class11", "method11") == True

def test_find_param () :
    class_interface.add_class ("class12")
    attr_interface.add_param ("class12", "method12", "param12", "type12")
    attr_interface.find_param ("method12", "param12")

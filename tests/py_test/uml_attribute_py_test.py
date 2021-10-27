from uml_components import UMLAttributes
from uml_components import UMLClass
from uml_components import UMLRelationship
import io
import sys
import snake_uml
from uml_components.interfaces import class_interface, attr_interface, rel_interface

def test_add_field () :
    attr_interface.add_field (class_name, field_name, field_type)

def test_add_method () :
    attr_interface.add_method (class_name, method_name, method_type)

def test_add_param () :
    attr_interface.add_param (class_name, method_name, param_name, param_type)

def test_rename_field () :
    attr_interface.rename_field (class_name, field_name, new_name)

def test_rename_method () :
    attr_interface.rename_method (class_name, method_name, new_name)

def test_rename_param () :
    attr_interface.rename_param (class_name, method_name, param_name, new_name)

def test_delete_field () :
    attr_interface.delete_field (class_name, field_name)

def test_delete_method () :
    attr_interface.delete_method (class_name, method_name)

def test_delete_param () :
    attr_interface.delete_param (class_name, method_name, param_name)

def test_find_field () :
    attr_interface.find_field (uml, field_name)

def test_find_method () :
    attr_interface.find_method (uml, method_name)

def test_find_param () :
    attr_interface.find_param (method, param_name)

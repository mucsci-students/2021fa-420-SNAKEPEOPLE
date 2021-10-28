from uml_components import UMLRelationship
from uml_components import UMLClass
from uml_components.interfaces import rel_interface, class_interface
import pytest

# check a relationship can be added
# def test_add_rel () :
#     index = 0
#     class_interface.add_class ("source1")
#     class_interface.add_class ("destination1")
#     rel_interface.add_relationship ("source1", "destination1", "compostition")
#     assert rel_interface.find_rel ("source1", "destination1") == (True, index)

def test_del_rel () :
    index = 0
    class_interface.add_class ("source2")
    class_interface.add_class ("destination2")
    rel_interface.add_relationship ("source2", "destination2", "composition")
    rel_interface.delete_relationship ("source2", "destination2")
    assert rel_interface.find_rel ("source2", "destination2") == (False, index)

def test_check_type () :
    class_interface.add_class ("source3")
    class_interface.add_class ("destination3")
    rel_interface.add_relationship ("source3", "destination3", "composition")
    rel_interface.change_type ("source3", "destination3", "aggregation")
    assert rel_interface.check_type ("aggregation") == True

def test_find_rel () :
    index = 1
    class_interface.add_class ("source4")
    class_interface.add_class ("destination4")
    rel_interface.add_relationship ("source4", "destination4", "aggregation")
    assert rel_interface.find_rel ("source4", "destination4") == (True, index)

def test_rel_cleanup () :
    index = 2
    class_interface.add_class ("source5")
    class_interface.add_class ("destination5")
    rel_interface.add_relationship ("source5", "destination5", "aggregation")
    rel_interface.rel_cleanup ("source5")
    assert rel_interface.find_rel ("source5", "destination5") == (False, index)

def test_change_type () :
    rel_interface.add_relationship ("source6", "destination6", "aggregation")
    rel_interface.change_type ("source6", "destination6", "composition")
    assert rel_interface.check_type ("composition") == True

def test_check_class () :
    class_interface.add_class ("classChk")
    assert rel_interface.check_class ("classChk") == True
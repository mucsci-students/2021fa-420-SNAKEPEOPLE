import pytest
from uml_components.interfaces import class_interface

def test_add_class () :
    assert class_interface.add_class ("class09")

def test_rename_class () :
    assert class_interface.rename_class ("class09", "class10")

def test_delete_class () :
    assert class_interface.delete_class ("class09")

def test_add_empty_class () :
    assert class_interface.add_class ("")

def test_add_empty_rename () :
    assert class_interface.add_class ("class10")
    assert class_interface.rename_class ("class10", "")

def test_delete_empty_class () :
    assert class_interface.add_class ("class11")
    assert class_interface.delete_class (" ")

def test_delete_ne_class () :
    assert class_interface.delete_class ("class11")
    assert class_interface.delete_class ("class15")
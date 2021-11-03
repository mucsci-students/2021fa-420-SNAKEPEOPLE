import pytest
from uml_components.interfaces import class_interface

def test_add_class () :
    assert class_interface.add_class ("class09")
    assert isinstance (class_interface.add_class ("class2"), tuple)

def test_rename_class () :
    assert class_interface.rename_class ("class09", "class10")
    assert isinstance (class_interface.rename_class ("class10", "class1"), tuple)

def test_delete_class () :
    assert class_interface.add_class ("class69")
    assert isinstance (class_interface.delete_class("class69"), tuple)

def test_add_empty_class () :
    assert class_interface.add_class ("")
    assert isinstance (class_interface.add_class (""), tuple)

def test_add_empty_rename () :
    assert class_interface.add_class ("class10")
    assert class_interface.rename_class ("class10", "")
    assert isinstance (class_interface.rename_class ("", "class20"), tuple)

def test_delete_empty_class () :
    assert class_interface.add_class ("class11")
    assert class_interface.delete_class (" ")
    assert class_interface.add_class ("emptyclass")
    assert isinstance (class_interface.delete_class ("emptyclass"), tuple)

def test_delete_ne_class () :
    assert class_interface.delete_class ("class11")
    assert isinstance (class_interface.delete_class ("class15"), tuple)

import pytest
from uml_components.interfaces import class_interface

def test_add_class () :
    assert class_interface.add_class ("class09")
    assert type (class_interface.add_class ("class2")) is str

def test_rename_class () :
    assert class_interface.rename_class ("class09", "class10")
    assert type (class_interface.rename_class ("class10", "class1")) is str

def test_delete_class () :
    assert class_interface.delete_class ("class09")
    assert class_interface.add_class ("class69")
    assert type(class_interface.delete_class ("class69")) is str

def test_add_empty_class () :
    assert class_interface.add_class ("")
    assert type(class_interface.add_class ("")) is str

def test_add_empty_rename () :
    assert class_interface.add_class ("class10")
    assert class_interface.rename_class ("class10", "")
    assert type (class_interface.rename_class ("", "class20")) is str

def test_delete_empty_class () :
    assert class_interface.add_class ("class11")
    assert class_interface.delete_class (" ")
    assert class_interface.add_class ("emptyclass")
    assert type(class_interface.delete_class ("emptyclass")) is str

def test_delete_ne_class () :
    assert class_interface.delete_class ("class11")
    assert type(class_interface.delete_class ("class15")) is str
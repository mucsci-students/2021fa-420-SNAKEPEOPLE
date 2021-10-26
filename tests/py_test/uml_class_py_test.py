from uml_components import UMLClass
import py_test

# checks for empty uml_class
def empty_uml () :
    uml = UMLClass ()
    assert uml == ()

# check adding two uml classes
def two_uml_class () :
    uml1 = UMLClass ()
    uml2 = UMLClass ()
    assert uml1 == ()
    assert uml2 == ()

# check input for improper argument lengths
def input_length_uml_class () :
    uml = UMLClass ()

# check invalid input of proper length
def input_invalid_uml_class () :
    uml = UMLClass ()

# check adding a duplicate uml class
def duplicate_uml_class () :
    uml1 = UMLClass (1)
    uml2 = UMLClass (2)
    assert uml1 == uml2

# check deleting a uml class
def delete_uml_class () :
    uml = UMLClass ()

# check deleting a non-existant uml class
def delete_ne_uml_class () :
    uml = UMLClass ()

# check renaming a uml class
def rename_uml_class () :
    uml = UMLClass ()

# check renaming a nonexistant uml class
def rename_ne_uml_class () :
    uml = UMLClass ()

# check renaming an already existing uml class
def rename_ae_uml_class () :
    uml = UMLClass ()
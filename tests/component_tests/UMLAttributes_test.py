import unittest
import io
import sys
from unittest import mock

import snake_uml

from uml_components import UMLClass
from uml_components import UMLRelationship
from uml_components import UMLAttributes
from uml_components.interfaces import attr_interface

class UMLAttributes_test (unittest.TestCase) :

    # Tests adding an attribute
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addattr class1 stuff", "exit"])
    def test_addAtr(self, mock):
        snake_uml.main(sys.argv)
        out = io.StringIO()
        sys.stdout = out
        sys.stdout = sys.__stdout__
        self.assertEqual(UMLClass.class_dict["class1"].attributes[0], "stuff")
        self.assertEqual(len(UMLClass.class_dict), 1)
        self.assertEqual(len(UMLClass.class_dict["class1"].attributes), 1)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    # Tests to see if adding a duplicate attribute results in an error message
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addattr class1 stuff", "addattr class1 stuff", "exit"])
    def test_addDupAtr(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Attribute Add Error [Invalid Name:2]>: stuff already exists as an attribute of class1." in out.getvalue(), True)
        self.assertEqual(len(UMLClass.class_dict), 1)
        self.assertEqual(len(UMLClass.class_dict["class1"].attributes), 1)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    # Tests adding an attribute to a non-existant class
    @unittest.mock.patch('builtins.input', side_effect=["addattr class1 stuff", "exit"])
    def test_addAtrToNothing(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Attribute Add Error [Invalid Class]>: Class named class1 does not exist." in out.getvalue(), True)
        self.assertEqual(len(UMLRelationship.relationship_dict), 0)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    # Tests renaming an attribute
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addattr class1 stuff", "renattr class1 stuff stuff2", "exit"])
    def test_renameAtr(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual(UMLClass.class_dict["class1"].attributes[0], "stuff2")
        self.assertEqual(len(UMLClass.class_dict["class1"].attributes), 1)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    # Tests renaming a non-existant attribute
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "renattr class1 stuff stuff2", "exit"])
    def test_renameNothingAtr(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Attribute Rename Error [Invalid Name:1]>: stuff does not exist as the name of an attribute in class1" in out.getvalue(), True)
        self.assertEqual(len(UMLClass.class_dict["class1"].attributes), 0)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    # Tests renaming an attribute to the name of an already existing attribute
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addattr class1 stuff", "addattr class1 stuff2", "renattr class1 stuff stuff2", "exit"])
    def test_renameDupAtr(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Attribute Rename Error [Invalid Name:3]>: stuff2 already exists as an attribute in class1" in out.getvalue(), True)
        self.assertEqual(UMLClass.class_dict["class1"].attributes[0], "stuff")
        self.assertEqual(UMLClass.class_dict["class1"].attributes[1], "stuff2")
        self.assertEqual(len(UMLClass.class_dict["class1"].attributes), 2)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    # Tests deleting a legitimate attribute
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addattr class1 stuff", "delattr class1 stuff", "exit"])
    def test_deleteAtr(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual(len(UMLClass.class_dict["class1"].attributes), 0)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    # Tests deleting an attribute that does not exist from a class
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "delattr class1 stuff", "exit"])
    def test_deleteFalseAtr(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Attribute Delete Error [Invalid Name]>: stuff does not exist as the name of an attribute in class1." in out.getvalue(), True)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    # Tests deleting an attribute from a class that does not exist
    @unittest.mock.patch('builtins.input', side_effect=["delattr class1 stuff", "exit"])
    def test_deleteAtrFromNothing(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Attribute Delete Error [Invalid Class]>: Class named class1 does not exist." in out.getvalue(), True)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    
import unittest
import io
import sys
from unittest import mock

import snake_uml

from uml_components import UMLClass, UMLAttributes
from uml_components.interfaces import class_interface

# An assortment of tests for the UMLClass and its components

class UMLClass_test (unittest.TestCase) :

    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addclass class2", "exit"])
    def test_addClass(self, mock):   
        snake_uml.main(sys.argv)
        self.assertEqual(UMLClass.class_dict["class1"].name, "class1")
        self.assertEqual(UMLClass.class_dict["class2"].name, "class2")
        self.assertEqual(UMLClass.class_dict["class1"].attributes, [])
        self.assertEqual(UMLClass.class_dict["class2"].attributes, [])
        self.assertEqual(len(UMLClass.class_dict), 2)
        UMLClass.class_dict = {}

    @unittest.mock.patch('builtins.input', side_effect=["poggers class2", "exit"])
    def test_inputCheckValidity(self, mock):   
        UMLClass.class_dict = {}
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Invalid Command Error>: 'poggers' is not a valid command.\nType 'help' for a list of valid commands." in out.getvalue(), True)
        self.assertEqual(len(UMLClass.class_dict), 0)
        del out
        UMLClass.class_dict = {}

    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addclass class1", "exit"])
    def test_addDupClass(self, mock):
        UMLClass.class_dict = {}
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("\n<Class Add Error [Invalid Name:2]>: Class named 'class1' already exists.\n" in out.getvalue(), True)
        self.assertEqual(len(UMLClass.class_dict), 1)
        del out
        UMLClass.class_dict = {}
    
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "delclass class1", "exit"])
    def test_deleteClass(self, mock): 
        snake_uml.main(sys.argv)
        out = io.StringIO()
        sys.stdout = out
        sys.stdout = sys.__stdout__
        self.assertEqual(UMLClass.class_dict, {})
        self.assertEqual(len(UMLClass.class_dict), 0)
        del out
        UMLClass.class_dict = {}

    @unittest.mock.patch('builtins.input', side_effect=["delclass class1", "exit"])
    def test_deleteNothingClass(self, mock): 
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Class Delete Error [Invalid Name]>: Class named 'class1' does not exist." in out.getvalue(), True)
        self.assertEqual(len(UMLClass.class_dict), 0)
        del out
        UMLClass.class_dict = {}

    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "renclass class1 class2", "exit"])
    def test_renameClass(self, mock): 
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual(UMLClass.class_dict["class2"].name, "class2")
        self.assertEqual(len(UMLClass.class_dict), 1)
        del out
        UMLClass.class_dict = {}

    @unittest.mock.patch('builtins.input', side_effect=["renclass class1 class2", "exit"])
    def test_renameNothingClass(self, mock): 
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Class Rename Error [Invalid Name:1]>: class1 does not exist as the name of a class." in out.getvalue(), True)
        self.assertEqual(len(UMLClass.class_dict), 0)
        del out
        UMLClass.class_dict = {}

    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addclass class2", "renclass class1 class2", "exit"])
    def test_renameClassToExisting(self, mock): 
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Class Rename Error [Invalid Name:3]>: Class name 'class2' alread exists." in out.getvalue(), True)
        self.assertEqual(len(UMLClass.class_dict), 2)
        del out
        UMLClass.class_dict = {}
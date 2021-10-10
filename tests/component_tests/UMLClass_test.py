import unittest
import io
import sys
from unittest import mock

import snake_uml

from uml_components import UMLClass, UMLAttributes
from uml_components.interfaces import class_interface

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


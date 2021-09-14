import unittest
import io
import sys
from unittest import mock
import uml_class
import relationships
import snake_uml


class test(unittest.TestCase):

    #Test adding a single class
    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "add class class1", "exit"])
    def test_addClass(self, mock):   
        snake_uml.main(sys.argv)
        out = io.StringIO()
        sys.stdout = out
        print(uml_class.class_dict)
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "{'class1': \n\tClass Name: class1\n\tAttributes:\n}\n")                                                                                                                                             
        self.assertEqual(len(uml_class.class_dict), 1)

    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "exit"])
    def test_addDupClass(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue()[0:72], "\n<Class Add Error [Invalid Name:2]>\nClass named 'class1' already exists.")
        self.assertEqual(len(uml_class.class_dict), 1)

    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "exit"])
    def test_addDupClass(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue()[0:72], "\n<Class Add Error [Invalid Name:2]>\nClass named 'class1' already exists.")
        self.assertEqual(len(uml_class.class_dict), 1)



if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
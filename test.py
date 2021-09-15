import unittest
import io
import sys
from unittest import mock
import uml_class
import relationships
import snake_uml

class test(unittest.TestCase):

    #Test adding two class
    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "add class class2", "exit"])
    def test_addClass(self, mock):   
        snake_uml.main(sys.argv)
        self.assertEqual(uml_class.class_dict["class1"].name, "class1")
        self.assertEqual(uml_class.class_dict["class2"].name, "class2")
        self.assertEqual(uml_class.class_dict["class1"].attributes, [])
        self.assertEqual(uml_class.class_dict["class1"].attributes, [])
        self.assertEqual(len(uml_class.class_dict), 2)
    
    #Test adding a duplicate class
    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "exit"])
    def test_addDupClass(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        print(out.getvalue())
        self.assertEqual(out.getvalue(), "\n<Class Add Error [Invalid Name:2]>\nClass named 'class1' already exists.")
        self.assertEqual(len(uml_class.class_dict), 2)
        del out

    #Test deleting a class
    @unittest.mock.patch('builtins.input', side_effect=["delete class class1", "exit"])
    def test_deleteClass(self, mock): 
        snake_uml.main(sys.argv)
        out = io.StringIO()
        sys.stdout = out
        print(uml_class.class_dict)
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "{'class2': \n\tClass Name: class2\n\tAttributes:\n}\n")
        del out

    @unittest.mock.patch('builtins.input', side_effect=["delete class class1", "exit"])
    def test_deleteClass(self, mock): 
        snake_uml.main(sys.argv)
        out = io.StringIO()
        sys.stdout = out
        print(uml_class.class_dict)
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "{'class2': \n\tClass Name: class2\n\tAttributes:\n}\n")
        del out


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
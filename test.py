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
        self.assertEqual(out.getvalue(), "\n<Class Add Error [Invalid Name:2]>\nClass named 'class1' already exists.\n")
        self.assertEqual(len(uml_class.class_dict), 2)
        del out

    #Test deleting a class
    @unittest.mock.patch('builtins.input', side_effect=["delete class class1", "delete class class2", "exit"])
    def test_deleteClass(self, mock): 
        snake_uml.main(sys.argv)
        out = io.StringIO()
        sys.stdout = out
        print(uml_class.class_dict)
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "{}\n")
        del out

    #Test deleting a non-existent class
    @unittest.mock.patch('builtins.input', side_effect=["delete class class1", "exit"])
    def test_deleteNothingClass(self, mock): 
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "<Class Delete Error [Invalid Name]>\nClass named 'class1' does not exist.\n")
        del out

    #Test adding a relationship : SOMEHOW class1 and class2 already exist here
    @unittest.mock.patch('builtins.input', side_effect=["add relationship class1 class2", "exit"])
    def test_addRel(self, mock):   
        snake_uml.main(sys.argv)
        self.assertEqual(relationships.relationship_dict["class1-class2"].source, uml_class.class_dict["class1"])
        self.assertEqual(relationships.relationship_dict["class1-class2"].destination, uml_class.class_dict["class2"])
        self.assertEqual(len(relationships.relationship_dict), 1)

    #Test adding an invalid source
    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "add class class2", "add relationship class3 class2", "exit"])
    def test_falseSource(self, mock):   
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue()[74:], "ERROR: class3 is invalid, source must be an existing class.\n")
        del out

    #Test adding an invalid destination and source
    @unittest.mock.patch('builtins.input', side_effect=["add relationship class4 class3", "exit"])
    def test_falseBoth(self, mock):   
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "ERROR: class4 and class3 are invalid, both arguements must be existing classes.\n")
        del out

    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "add relationship class1 class3", "exit"])
    def test_falseDest(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "ERROR: class1 are invalid, both arguements must be existing classes.\n")
        del out

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
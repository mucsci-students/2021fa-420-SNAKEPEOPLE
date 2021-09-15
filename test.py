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
        uml_class.class_dict = {}
    
    #Test adding a duplicate class
    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "add class class1", "exit"])
    def test_addDupClass(self, mock):
        uml_class.class_dict = {}
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("\n<Class Add Error [Invalid Name:2]>\nClass named 'class1' already exists.\n" in out.getvalue(), True)
        self.assertEqual(len(uml_class.class_dict), 1)
        del out
        uml_class.class_dict = {}

    #Test deleting a class
    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "delete class class1", "exit"])
    def test_deleteClass(self, mock): 
        snake_uml.main(sys.argv)
        out = io.StringIO()
        sys.stdout = out
        sys.stdout = sys.__stdout__
        self.assertEqual(uml_class.class_dict, {})
        del out
        uml_class.class_dict = {}

    #Test deleting a non-existent class
    @unittest.mock.patch('builtins.input', side_effect=["delete class class1", "exit"])
    def test_deleteNothingClass(self, mock): 
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Class Delete Error [Invalid Name]>\nClass named 'class1' does not exist.\n" in out.getvalue(), True)
        del out
        uml_class.class_dict = {}

    #Test renaming a class
    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "rename class class1 class2", "exit"])
    def test_rename(self, mock): 
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual(uml_class.class_dict["class2"].name, "class2")
        self.assertEqual(len(uml_class.class_dict), 1)
        del out
        uml_class.class_dict = {}

    #Test renaming a non-existant class
    @unittest.mock.patch('builtins.input', side_effect=["rename class class1 class2", "exit"])
    def test_renameNothing(self, mock): 
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Class Rename Error [Invalid Name:1]>\nclass1 does not exist as the name of a class." in out.getvalue(), True)
        del out
        uml_class.class_dict = {}

    #Test renaming a class to an already existing class
    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "add class class2", "rename class class1 class2", "exit"])
    def test_renameToExisting(self, mock): 
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Class Rename Error [Invalid Name:3]>\nClass name 'class2' alread exists." in out.getvalue(), True)
        del out
        uml_class.class_dict = {}

    #Test adding an attribute
    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "add attribute class1 stuff", "exit"])
    def test_addAtr(self, mock):
        snake_uml.main(sys.argv)
        out = io.StringIO()
        sys.stdout = out
        sys.stdout = sys.__stdout__
        self.assertEqual(uml_class.class_dict["class1"].attributes[0], "stuff")
        self.assertEqual(len(relationships.relationship_dict), 0)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test to see if adding a duplicate attribute results in an error message
    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "add attribute class1 stuff", "add attribute class1 stuff", "exit"])
    def test_addDupAtr(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Attribute Add Error [Invalid Name:2]>\nstuff already exists as an attribute of class1." in out.getvalue(), True)
        self.assertEqual(len(relationships.relationship_dict), 0)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test adding an attribute to a non-existant class
    @unittest.mock.patch('builtins.input', side_effect=["add attribute class1 stuff", "exit"])
    def test_addAtrToNothing(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Attribute Add Error [Invalid Class]>\nClass named class1 does not exist." in out.getvalue(), True)
        self.assertEqual(len(relationships.relationship_dict), 0)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test renaming an attribute
    # @unittest.mock.patch('builtins.input', side_effect=["add class class1", "add attribute class1 stuff", "rename attribute class1 stuff stuff2", "exit"])
    # def test_renameAtr(self, mock):
    #     out = io.StringIO()
    #     sys.stdout = out
    #     snake_uml.main(sys.argv)
    #     sys.stdout = sys.__stdout__
    #     self.assertEqual(uml_class.class_dict["class1"].attributes[0], "stuff2")
    #     del out
    #     uml_class.class_dict = {}
    #     relationships.relationship_dict = {}

    #Test renaming a non-existant attribute
    #@unittest.mock.patch('builtins.input', side_effect=["add class class1", "rename attribute class1 stuff stuff2", "exit"])
    # def test_renameNothingAtr(self, mock):
    #     out = io.StringIO()
    #     sys.stdout = out
    #     snake_uml.main(sys.argv)
    #     sys.stdout = sys.__stdout__
    #     self.assertEqual("<Attribute Rename Error [Invalid Name:1]>\nstuff1 does not exist as the name of an attribute inclass1" in out.getvalue(), True)
    #     del out
    #     uml_class.class_dict = {}
    #     relationships.relationship_dict = {}

    #Test renaming an attribute to the name of an already existing attribute
    # @unittest.mock.patch('builtins.input', side_effect=["add class class1", "add attribute class1 stuff", "add attribute class1 stuff2", "add attribute class1 stuff stuff2", "exit"])
    # def test_renameAtr(self, mock):
    #     out = io.StringIO()
    #     sys.stdout = out
    #     snake_uml.main(sys.argv)
    #     sys.stdout = sys.__stdout__
    #     self.assertEqual("<Attribute Rename Error [Invalid Name:3]>\nstuff2 already exists as an attribute in class1" in out.getvalue(), True)
    #     del out
    #     uml_class.class_dict = {}
    #     relationships.relationship_dict = {}

    #Test deleting a legitamate attribute
    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "add attribute class1 stuff", "delete attribute class1 stuff", "exit"])
    def test_deleteAtr(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual(len(uml_class.class_dict["class1"].attributes), 0)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test deleting an attribute that does not exist from a class
    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "delete attribute class1 stuff", "exit"])
    def test_deleteFalseAtr(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Attribute Delete Error [Invalid Name]>\nstuff does not exist as the name of an attribute in class1." in out.getvalue(), True)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test deleting an attribute from a class that does not exist
    @unittest.mock.patch('builtins.input', side_effect=["delete attribute class1 stuff", "exit"])
    def test_deleteAtrFromNothing(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Attribute Delete Error [Invalid Class]>\nClass named class1 does not exist." in out.getvalue(), True)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test adding a relationship
    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "add class class2", "add relationship class1 class2", "exit"])
    def test_addRel(self, mock):   
        snake_uml.main(sys.argv)
        self.assertEqual(relationships.relationship_dict["class1-class2"].source, uml_class.class_dict["class1"])
        self.assertEqual(relationships.relationship_dict["class1-class2"].destination, uml_class.class_dict["class2"])
        self.assertEqual(len(relationships.relationship_dict), 1)
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test adding an invalid source
    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "add class class2", "add relationship class3 class2", "exit"])
    def test_falseSource(self, mock):   
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("ERROR: class3 is invalid, source must be an existing class.\n" in out.getvalue(), True)
        self.assertEqual(len(relationships.relationship_dict), 0)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test adding a relationship with an invalid destination and source
    @unittest.mock.patch('builtins.input', side_effect=["add relationship class4 class3", "exit"])
    def test_falseBoth(self, mock):   
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("ERROR: class4 and class3 are invalid, both arguements must be existing classes.\n" in out.getvalue(), True)
        self.assertEqual(len(relationships.relationship_dict), 0)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test addind a relationship with an invalid destination
    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "add relationship class1 class3", "exit"])
    def test_falseDest(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("ERROR: class3 is invalid, destination must be an existing class.\n" in out.getvalue(), True)
        self.assertEqual(len(relationships.relationship_dict), 0)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test adding a duplicate relationship
    @unittest.mock.patch('builtins.input', side_effect=["add class class5", "add class class6", "add relationship class5 class6", "add relationship class5 class6", "exit"])
    def test_dupRel(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("ERROR: Relationship class5-class6 already exists\n" in out.getvalue(), True)
        self.assertEqual(len(relationships.relationship_dict), 1)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test deleting a non-existant relationship
    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "add class class2", "delete relationship class1 class2", "exit"])
    def test_deleteNothingRel(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("ERROR: Relationship class1-class2, does not exist.\n" in out.getvalue(), True)
        self.assertEqual(len(relationships.relationship_dict), 0)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test deleting a legitimate relationship
    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "add class class2", "add relationship class1 class2", "delete relationship class1 class2", "exit"])
    def test_deleteRel(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual(relationships.relationship_dict, {})
        self.assertEqual(len(relationships.relationship_dict), 0)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test deleting an invalid source
    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "delete relationship class3 class1", "exit"])
    def test_DelfalseSource(self, mock):   
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("ERROR: class3 is invalid, source must be an existing class.\n" in out.getvalue(), True)
        self.assertEqual(len(relationships.relationship_dict), 0)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test deleting a relationship with an invalid destination and source
    @unittest.mock.patch('builtins.input', side_effect=["delete relationship class4 class3", "exit"])
    def test_DelfalseBoth(self, mock):   
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("ERROR: class4 and class3 are invalid, both arguements must be existing classes.\n" in out.getvalue(), True)
        self.assertEqual(len(relationships.relationship_dict), 0)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test deleting a relationship with an invalid destination
    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "delete relationship class1 class3", "exit"])
    def test_DelfalseDest(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("ERROR: class3 is invalid, destination must be an existing class.\n" in out.getvalue(), True)
        self.assertEqual(len(relationships.relationship_dict), 0)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test listing an empty relationship dictionary
    @unittest.mock.patch('builtins.input', side_effect=["list relations", "exit"])
    def test_listNothingRel(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("No relationships exist.\n" in out.getvalue(), True)
        self.assertEqual(len(relationships.relationship_dict), 0)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}
        
    #Test listing all classes while no classes exist   
    @unittest.mock.patch('builtins.input', side_effect=["list classes", "exit"])
    def test_listNothingclasses(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("No classes exist.\n" in out.getvalue(), True)
        self.assertEqual(len(relationships.relationship_dict), 0)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test listing a class that does not exist
    @unittest.mock.patch('builtins.input', side_effect=["list class class1", "exit"])
    def test_listNothing(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("The requested class does not exist.\n" in out.getvalue(), True)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
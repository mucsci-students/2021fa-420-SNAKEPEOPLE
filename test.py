import unittest
import io
import sys
from unittest import mock
import uml_class
import relationships
import snake_uml
import filecmp

class test(unittest.TestCase):

    #Test adding two class
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addclass class2", "exit"])
    def test_addClass(self, mock):   
        snake_uml.main(sys.argv)
        self.assertEqual(uml_class.class_dict["class1"].name, "class1")
        self.assertEqual(uml_class.class_dict["class2"].name, "class2")
        self.assertEqual(uml_class.class_dict["class1"].attributes, [])
        self.assertEqual(uml_class.class_dict["class2"].attributes, [])
        self.assertEqual(len(uml_class.class_dict), 2)
        uml_class.class_dict = {}

    #Test input checker for proper argument lengths
    @unittest.mock.patch('builtins.input', side_effect=["addclass ", "exit"])
    def test_inputCheckLength(self, mock):   
        uml_class.class_dict = {}
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Invalid Arguments Error>\n1 arguments expected. 0 arguments received." in out.getvalue(), True)
        self.assertEqual(len(uml_class.class_dict), 0)
        del out
        uml_class.class_dict = {}

    #Test invalid input of the correct length
    @unittest.mock.patch('builtins.input', side_effect=["poggers class2", "exit"])
    def test_inputCheckValidity(self, mock):   
        uml_class.class_dict = {}
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Invalid Command Error>: 'poggers' is not a valid command.\nType 'help' for a list of valid commands." in out.getvalue(), True)
        self.assertEqual(len(uml_class.class_dict), 0)
        del out
        uml_class.class_dict = {}

    
    #Test adding a duplicate class
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addclass class1", "exit"])
    def test_addDupClass(self, mock):
        uml_class.class_dict = {}
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("\n<Class Add Error [Invalid Name:2]>: Class named 'class1' already exists.\n" in out.getvalue(), True)
        self.assertEqual(len(uml_class.class_dict), 1)
        del out
        uml_class.class_dict = {}

    #Test deleting a class
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "delclass class1", "exit"])
    def test_deleteClass(self, mock): 
        snake_uml.main(sys.argv)
        out = io.StringIO()
        sys.stdout = out
        sys.stdout = sys.__stdout__
        self.assertEqual(uml_class.class_dict, {})
        self.assertEqual(len(uml_class.class_dict), 0)
        del out
        uml_class.class_dict = {}

    #Test deleting a non-existent class
    @unittest.mock.patch('builtins.input', side_effect=["delclass class1", "exit"])
    def test_deleteNothingClass(self, mock): 
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Class Delete Error [Invalid Name]>: Class named 'class1' does not exist." in out.getvalue(), True)
        self.assertEqual(len(uml_class.class_dict), 0)
        del out
        uml_class.class_dict = {}

    #Test renaming a class
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "renclass class1 class2", "exit"])
    def test_renameClass(self, mock): 
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual(uml_class.class_dict["class2"].name, "class2")
        self.assertEqual(len(uml_class.class_dict), 1)
        del out
        uml_class.class_dict = {}

    #Test renaming a non-existant class
    @unittest.mock.patch('builtins.input', side_effect=["renclass class1 class2", "exit"])
    def test_renameNothingClass(self, mock): 
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Class Rename Error [Invalid Name:1]>: class1 does not exist as the name of a class." in out.getvalue(), True)
        self.assertEqual(len(uml_class.class_dict), 0)
        del out
        uml_class.class_dict = {}

    #Test renaming a class to an already existing class
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addclass class2", "renclass class1 class2", "exit"])
    def test_renameClassToExisting(self, mock): 
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Class Rename Error [Invalid Name:3]>: Class name 'class2' alread exists." in out.getvalue(), True)
        self.assertEqual(len(uml_class.class_dict), 2)
        del out
        uml_class.class_dict = {}

    #Test adding an attribute
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addattr class1 stuff", "exit"])
    def test_addAtr(self, mock):
        snake_uml.main(sys.argv)
        out = io.StringIO()
        sys.stdout = out
        sys.stdout = sys.__stdout__
        self.assertEqual(uml_class.class_dict["class1"].attributes[0], "stuff")
        self.assertEqual(len(uml_class.class_dict), 1)
        self.assertEqual(len(uml_class.class_dict["class1"].attributes), 1)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test to see if adding a duplicate attribute results in an error message
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addattr class1 stuff", "addattr class1 stuff", "exit"])
    def test_addDupAtr(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Attribute Add Error [Invalid Name:2]>: stuff already exists as an attribute of class1." in out.getvalue(), True)
        self.assertEqual(len(uml_class.class_dict), 1)
        self.assertEqual(len(uml_class.class_dict["class1"].attributes), 1)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test adding an attribute to a non-existant class
    @unittest.mock.patch('builtins.input', side_effect=["addattr class1 stuff", "exit"])
    def test_addAtrToNothing(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Attribute Add Error [Invalid Class]>: Class named class1 does not exist." in out.getvalue(), True)
        self.assertEqual(len(relationships.relationship_dict), 0)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test renaming an attribute
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addattr class1 stuff", "renattr class1 stuff stuff2", "exit"])
    def test_renameAtr(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual(uml_class.class_dict["class1"].attributes[0], "stuff2")
        self.assertEqual(len(uml_class.class_dict["class1"].attributes), 1)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test renaming a non-existant attribute
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "renattr class1 stuff stuff2", "exit"])
    def test_renameNothingAtr(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Attribute Rename Error [Invalid Name:1]>: stuff does not exist as the name of an attribute in class1" in out.getvalue(), True)
        self.assertEqual(len(uml_class.class_dict["class1"].attributes), 0)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test renaming an attribute to the name of an already existing attribute
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addattr class1 stuff", "addattr class1 stuff2", "renattr class1 stuff stuff2", "exit"])
    def test_renameDupAtr(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Attribute Rename Error [Invalid Name:3]>: stuff2 already exists as an attribute in class1" in out.getvalue(), True)
        self.assertEqual(uml_class.class_dict["class1"].attributes[0], "stuff")
        self.assertEqual(uml_class.class_dict["class1"].attributes[1], "stuff2")
        self.assertEqual(len(uml_class.class_dict["class1"].attributes), 2)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test deleting a legitamate attribute
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addattr class1 stuff", "delattr class1 stuff", "exit"])
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
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "delattr class1 stuff", "exit"])
    def test_deleteFalseAtr(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Attribute Delete Error [Invalid Name]>: stuff does not exist as the name of an attribute in class1." in out.getvalue(), True)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test deleting an attribute from a class that does not exist
    @unittest.mock.patch('builtins.input', side_effect=["delattr class1 stuff", "exit"])
    def test_deleteAtrFromNothing(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Attribute Delete Error [Invalid Class]>: Class named class1 does not exist." in out.getvalue(), True)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test adding a relationship
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addclass class2", "addrel class1 class2", "exit"])
    def test_addRel(self, mock):   
        snake_uml.main(sys.argv)
        self.assertEqual(relationships.relationship_dict["class1-class2"].source, uml_class.class_dict["class1"])
        self.assertEqual(relationships.relationship_dict["class1-class2"].destination, uml_class.class_dict["class2"])
        self.assertEqual(len(relationships.relationship_dict), 1)
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test adding an invalid source
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addclass class2", "addrel class3 class2", "exit"])
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
    @unittest.mock.patch('builtins.input', side_effect=["addrel class4 class3", "exit"])
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
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addrel class1 class3", "exit"])
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
    @unittest.mock.patch('builtins.input', side_effect=["addclass class5", "addclass class6", "addrel class5 class6", "addrel class5 class6", "exit"])
    def test_dupRel(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Relationship Add Error>: Relationship class5-class6 already exists." in out.getvalue(), True)
        self.assertEqual(len(relationships.relationship_dict), 1)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test deleting a non-existant relationship
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addclass class2", "delrel class1 class2", "exit"])
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
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addclass class2", "addrel class1 class2", "delrel class1 class2", "exit"])
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
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "delrel class3 class1", "exit"])
    def test_DelFalseSource(self, mock):   
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
    @unittest.mock.patch('builtins.input', side_effect=["delrel class4 class3", "exit"])
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
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "delrel class1 class3", "exit"])
    def test_DelFalseDest(self, mock):
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
    @unittest.mock.patch('builtins.input', side_effect=["listrel", "exit"])
    def test_listNothingRel(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("(none)" in out.getvalue(), True)
        self.assertEqual(len(relationships.relationship_dict), 0)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}
        
    #Test listing all classes while no classes exist   
    @unittest.mock.patch('builtins.input', side_effect=["listclass all", "exit"])
    def test_listNothingClasses(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("(none)" in out.getvalue(), True)
        self.assertEqual(len(uml_class.class_dict), 0)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test listing a class that does not exist
    @unittest.mock.patch('builtins.input', side_effect=["listclass class1", "exit"])
    def test_listNothingClass(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Illegal Argument Error>: class1 does not exist as a class." in out.getvalue(), True)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test save error handling when no classes are created
    @unittest.mock.patch('builtins.input', side_effect=["save", "exit"])
    def test_saveEmpty(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("Error: There are no classes in the class dictionary.\nSave failed." in out.getvalue(), True)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

    #Test load abort
    @unittest.mock.patch('builtins.input', side_effect=["load", "n", "exit"])
    def test_loadAbort(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("Load cancelled." in out.getvalue(), True)
        self.assertEqual(len(relationships.relationship_dict), 0)
        self.assertEqual(len(uml_class.class_dict), 0)
        del out
        uml_class.class_dict = {}
        relationships.relationship_dict = {}

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
import unittest
import io
import sys
from unittest import mock

import snake_uml

from uml_components import UMLClass, UMLRelationship
from uml_components.interfaces import rel_interface


class UMLRelationship_test (unittest.TestCase) :

    #Test adding a relationship
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addclass class2", "addrel class1 class2", "exit"])
    def test_addRel(self, mock):   
        snake_uml.main(sys.argv)
        self.assertEqual(UMLRelationship.relationship_dict["class1-class2"].source, UMLClass.class_dict["class1"])
        self.assertEqual(UMLRelationship.relationship_dict["class1-class2"].destination, UMLClass.class_dict["class2"])
        self.assertEqual(len(UMLRelationship.relationship_dict), 1)
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    #Test adding an invalid source
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addclass class2", "addrel class3 class2", "exit"])
    def test_falseSource(self, mock):   
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("ERROR: class3 is invalid, source must be an existing class.\n" in out.getvalue(), True)
        self.assertEqual(len(UMLRelationship.relationship_dict), 0)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    #Test adding a relationship with an invalid destination and source
    @unittest.mock.patch('builtins.input', side_effect=["addrel class4 class3", "exit"])
    def test_falseBoth(self, mock):   
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("ERROR: class4 and class3 are invalid, both arguements must be existing classes.\n" in out.getvalue(), True)
        self.assertEqual(len(UMLRelationship.relationship_dict), 0)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    #Test addind a relationship with an invalid destination
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addrel class1 class3", "exit"])
    def test_falseDest(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("ERROR: class3 is invalid, destination must be an existing class.\n" in out.getvalue(), True)
        self.assertEqual(len(UMLRelationship.relationship_dict), 0)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    #Test adding a duplicate relationship
    @unittest.mock.patch('builtins.input', side_effect=["addclass class5", "addclass class6", "addrel class5 class6", "addrel class5 class6", "exit"])
    def test_dupRel(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Relationship Add Error>: Relationship class5-class6 already exists." in out.getvalue(), True)
        self.assertEqual(len(UMLRelationship.relationship_dict), 1)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    #Test deleting a non-existant relationship
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addclass class2", "delrel class1 class2", "exit"])
    def test_deleteNothingRel(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("ERROR: Relationship class1-class2, does not exist.\n" in out.getvalue(), True)
        self.assertEqual(len(UMLRelationship.relationship_dict), 0)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    #Test deleting a legitimate relationship
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "addclass class2", "addrel class1 class2", "delrel class1 class2", "exit"])
    def test_deleteRel(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual(UMLRelationship.relationship_dict, {})
        self.assertEqual(len(UMLRelationship.relationship_dict), 0)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    #Test deleting an invalid source
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "delrel class3 class1", "exit"])
    def test_DelFalseSource(self, mock):   
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("ERROR: class3 is invalid, source must be an existing class.\n" in out.getvalue(), True)
        self.assertEqual(len(UMLRelationship.relationship_dict), 0)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    #Test deleting a relationship with an invalid destination and source
    @unittest.mock.patch('builtins.input', side_effect=["delrel class4 class3", "exit"])
    def test_DelfalseBoth(self, mock):   
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("ERROR: class4 and class3 are invalid, both arguements must be existing classes.\n" in out.getvalue(), True)
        self.assertEqual(len(UMLRelationship.relationship_dict), 0)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    #Test deleting a relationship with an invalid destination
    @unittest.mock.patch('builtins.input', side_effect=["addclass class1", "delrel class1 class3", "exit"])
    def test_DelFalseDest(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("ERROR: class3 is invalid, destination must be an existing class.\n" in out.getvalue(), True)
        self.assertEqual(len(UMLRelationship.relationship_dict), 0)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    #Test listing an empty relationship dictionary
    @unittest.mock.patch('builtins.input', side_effect=["listrel", "exit"])
    def test_listNothingRel(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("(none)" in out.getvalue(), True)
        self.assertEqual(len(UMLRelationship.relationship_dict), 0)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}
        
    #Test listing all classes while no classes exist   
    @unittest.mock.patch('builtins.input', side_effect=["listclass all", "exit"])
    def test_listNothingClasses(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("(none)" in out.getvalue(), True)
        self.assertEqual(len(UMLClass.class_dict), 0)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    #Test listing a class that does not exist
    @unittest.mock.patch('builtins.input', side_effect=["listclass class1", "exit"])
    def test_listNothingClass(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("<Illegal Argument Error>: class1 does not exist as a class." in out.getvalue(), True)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    #Test save error handling when no classes are created
    @unittest.mock.patch('builtins.input', side_effect=["save testfile", "exit"])
    def test_saveEmpty(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("Error: There are no classes in the class dictionary.\nSave failed." in out.getvalue(), True)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}

    #Test load abort
    @unittest.mock.patch('builtins.input', side_effect=["load testfile", "n", "exit"])
    def test_loadAbort(self, mock):
        out = io.StringIO()
        sys.stdout = out
        snake_uml.main(sys.argv)
        sys.stdout = sys.__stdout__
        self.assertEqual("Load cancelled." in out.getvalue(), True)
        self.assertEqual(len(UMLRelationship.relationship_dict), 0)
        self.assertEqual(len(UMLClass.class_dict), 0)
        del out
        UMLClass.class_dict = {}
        UMLRelationship.relationship_dict = {}
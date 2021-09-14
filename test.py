import unittest
import io
import sys
from unittest import mock
import uml_class
import relationships
import snake_uml


class test(unittest.TestCase):

    #def test_addClass(self):

    @unittest.mock.patch('builtins.input', side_effect=["add class class1", "add class class1", "exit"])                                                                                                                          
    def test_addClass(self, mock):   
        snake_uml.main(sys.argv)
        out = io.StringIO()
        sys.stdout = out
        print(uml_class.class_dict)
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "{'class1': \n\tClass Name: class1\n\tAttributes:\n}\n")                                                                                                                                             
        self.assertEqual(len(uml_class.class_dict), 1)



        # with mock.patch('builtins.input', side_affect=["add class class1", "exit"]):
        #     snake_uml.main(sys.argv)
        #     print(uml_class.class_dict)
        #     self.assertTrue(len(uml_class.class_dict), 1)
        
        # #Check that adding a duplicate class will print an error message.
        # out = io.StringIO()
        # sys.stdout = out
        # uml_class.add_class("class2")
        # sys.stdout = sys.__stdout__
        # self.assertEqual(out.getvalue(), "\n<Class Add Error [Invalid Name:2]>\nClass named 'class2' already exists.\n")



    # #Check that deleting a non-existant class will result in a printed error.
    #     out = io.StringIO()
    #     sys.stdout = out
    #     uml_class.delete_class("class1")
    #     sys.stdout = sys.__stdout__
    #     self.assertEqual(out.getvalue(), "Error: class1 does not exist as the name of a class.\n")

    # def test_addClass(self):
    #     uml_class.add_class("class1")
    #     uml_class.add_class("class2")
    #     class1 = uml_class.UMLClass("class1")
    #     class2 = uml_class.UMLClass("class2")

    #     self.assertEqual(len(uml_class.class_dict), 2)

    #     relationships.add_relationship("class1", "class2")

    #     self.assertEqual(len(relationships.relationship_dict), 1)

    #     self.assertEqual(relationships.relationship_dict["class1-class2"], 
    #                 (uml_class.class_dict["class1"], uml_class.class_dict["class2"]))

    #     relationships.delete_relationship("class1", "class2")

    #     self.assertEqual(len(relationships.relationship_dict), 0)

    #     uml_class.delete_class("class1")

    #     self.assertEqual(len(uml_class.class_dict), 1)

    #     #Check that deleting a non-existant class will result in a printed error.
    #     out = io.StringIO()
    #     sys.stdout = out
    #     uml_class.delete_class("class1")
    #     sys.stdout = sys.__stdout__
    #     self.assertEqual(out.getvalue(), "Error: class1 does not exist as the name of a class.\n")

    #     #Check that adding a duplicate class will print an error message.
    #     out = io.StringIO()
    #     sys.stdout = out
    #     uml_class.add_class("class2")
    #     sys.stdout = sys.__stdout__
    #     self.assertEqual(out.getvalue(), "Error: class2 is already the name of an existing class.\n")

    #     #Check that adding a relationship without a source will print the appropriate message
    #     out = io.StringIO()
    #     sys.stdout = out
    #     relationships.add_relationship("class1", "class2")
    #     sys.stdout = sys.__stdout__
    #     self.assertEqual(out.getvalue(), "Invalid source, source must be an existing class.\n")

    #     uml_class.add_class("class1")
    #     uml_class.delete_class("class2")

    #     #Check that adding a relationship without a valid destination will fail
    #     out = io.StringIO()
    #     sys.stdout = out
    #     relationships.add_relationship("class1", "class2")
    #     sys.stdout = sys.__stdout__
    #     self.assertEqual(out.getvalue(), "Invalid destination, destination must be an existing class.\n")

    #     uml_class.delete_class("class1")

    #     #Check that adding a relationship without a valid source and destination will result
    #     #in an appropriate error message
    #     out = io.StringIO()
    #     sys.stdout = out
    #     relationships.add_relationship("class1", "class2")
    #     sys.stdout = sys.__stdout__
    #     self.assertEqual(out.getvalue(), "Invalid source and destination, both arguements must be existing classes.\n")

    #     #Check that deleting a relationship without a valid source and destination will result
    #     #in an appropriate error message
    #     out = io.StringIO()
    #     sys.stdout = out
    #     relationships.delete_relationship("class1", "class2")
    #     sys.stdout = sys.__stdout__
    #     self.assertEqual(out.getvalue(), "Invalid source and destination, both arguements must be existing classes.\n")

    #     uml_class.add_class("class1")

    #     #Check that deleting a relationship without a valid destination will result
    #     #in an appropriate error message
    #     out = io.StringIO()
    #     sys.stdout = out
    #     relationships.delete_relationship("class1", "class2")
    #     sys.stdout = sys.__stdout__
    #     self.assertEqual(out.getvalue(), "Invalid destination, destination must be an existing class.\n")

    #     uml_class.add_class("class2")

    #     print(uml_class.class_dict)
    #     #Check that deleting a relationship without a valid source and destination will result
    #     #in an appropriate error message
    #     out = io.StringIO()
    #     sys.stdout = out
    #     relationships.delete_relationship("class3", "class2")
    #     sys.stdout = sys.__stdout__
    #     self.assertEqual(out.getvalue(), "Invalid source, source must be an existing class.\n")


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
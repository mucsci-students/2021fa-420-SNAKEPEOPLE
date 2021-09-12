import unittest
import io
import sys
import unittest.mock
import uml_class
import relationships



class test(unittest.TestCase):

    def test_addClass(self):
        uml_class.add_class("class1")
        uml_class.add_class("class2")
        class1 = uml_class.UMLClass("class1")
        class2 = uml_class.UMLClass("class2")

        self.assertEqual(len(uml_class.class_dict), 2)

        relationships.add_relationship("class1", "class2")

        self.assertEqual(len(relationships.relationship_dict), 1)

        self.assertEqual(relationships.relationship_dict["class1-class2"], 
                    (uml_class.class_dict["class1"], uml_class.class_dict["class2"]))

        relationships.delete_relationship("class1", "class2")

        self.assertEqual(len(relationships.relationship_dict), 0)

        uml_class.delete_class("class1")

        self.assertEqual(len(uml_class.class_dict), 1)

        #Check that deleting a non-existant class will result in a printed error.
        out = io.StringIO()
        sys.stdout = out
        uml_class.delete_class("class1")
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "Error: class1 does not exist as the name of a class.\n")

        #Check that adding a duplicate class will print an error message.
        out = io.StringIO()
        sys.stdout = out
        uml_class.add_class("class2")
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "Error: class2 is already the name of an existing class.\n")

        #Check that adding a relationship without a source will print the appropriate message
        out = io.StringIO()
        sys.stdout = out
        relationships.add_relationship("class1", "class2")
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "Invalid source, source must be an existing class.\n")

        uml_class.add_class("class1")
        uml_class.delete_class("class2")

        #Check that adding a relationship without a valid destination will fail
        out = io.StringIO()
        sys.stdout = out
        relationships.add_relationship("class1", "class2")
        sys.stdout = sys.__stdout__
        self.assertEqual(out.getvalue(), "Invalid destination, destination must be an existing class.\n")

        uml_class.delete_class("class1")

        #Check that adding a relationship without a valid source and destination will result
        #in an appropriate 


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
import unittest
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
        
        self.assertEqual(relationships.relationship_dict["class1-class2"][1], 
                                uml_class.class_dict["class2"])

        

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
import unittest
import uml_class
import relationships



class test(unittest.TestCase):

    def test_addClass(self):
        uml_class.add_class("class1")
        uml_class.add_class("class2")
        class1 = uml_class.UMLClass("class1")
        class2 = uml_class.UMLClass("class2")

        #self.assertEqual(dict.cmp(uml_class.class_dict, testdict), 0)



        relationships.add_relationship("class1", "class2")

        print(relationships.relationship_dict)

        self.assertEqual(relationships.relationship_dict["class1-class2"], (class1, class2))



if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
import json
import uml_class

#json.load (open ('UMLJson.txt'))

json_dict = uml_class.class_dict

# Temporary class for experimentation with UML JSon interaction
class UML_To_Json:

    def __init__(self, name : str, attr : list = []) :
        self.name = name
        self.attr = attr

    def __del__ (self) :
        print (f"Deleting UMLClass:<{self.name}>...")

    def __repr__ (self):
        return self.name

    def rename (self, new_name : str) :
        self.name = new_name

    def toJson (self) :
        return json.dumps (self, default=lambda o: o.__dict__,
            sort_keys=True, indent = 4)

class_convert_1 = UML_To_Json ("UML Test 1", ["Attr1", "Attr2", "Attr3"])

class_convert_2 = UML_To_Json ("UML Test 2", ["Attr4", "Attr5", "Attr6"])

class File_Convert:
    def write_file (self):
        # writes uml dict to a json file
        # opens file and writes encoded json file to UMLJson.json
            with open ('UMLJson.json', 'w') as jf:

            # dumps function encodes class object/dictionary 
                prep_json_obj = json.dumps (class_convert_1.toJson ())

                prep_json_uml_dict = json.dumps (json_dict)

            # writes takes encoded info from dumps to json file 
                jf.write (prep_json_obj)

            # \n is necessary to create a new line. write does not start a new line
                jf.write ("\n")

                jf.write (prep_json_uml_dict)

                jf.close ()

# TODO
# create load json file function
# make save/write a new function

# converts json file to array data and prints array
uml_data = [json.loads(line) for line in open('UMLJson.json', 'r')]

print (uml_data)
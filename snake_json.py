import json
# key = name_of_class, value representation is class instance

#json.load (open ('UMLJson.txt'))

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

# dict_json = {
#     "UML Class" : "UML",
#     "Attribute" : "Attr1",
#     "ID" : 1922
# }

with open ('UMLJson.json', 'w') as jf:
    prep_json_obj = json.dumps (class_convert_1.toJson ())
    #prep_json_dict = json.dumps (dict_json)

    jf.write (prep_json_obj)
    jf.write ("\n")
    #jf.write (prep_json_dict)
    jf.close ()

uml_data = [json.loads(line) for line in open('UMLJson.json', 'r')]

print (uml_data)
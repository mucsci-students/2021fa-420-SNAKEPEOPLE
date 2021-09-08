import json
# key = name_of_class, value representation is class instance

#json.load (open ('UMLJson.txt'))

class JsonTest:
    def __init__(self, name, num, id):
        self.name = name
        self.num = num
        self.id = id
    def toJson (self) :
        return json.dumps (self, default=lambda o: o.__dict__,
            sort_keys=True, indent = 4)

test = JsonTest ("uml", 123, 456)

dict_json = {
    "UML Class" : "UML",
    "" : "Manager",
    "Task" : "Manage",
    "ID" : 1922
}

with open ('UMLJson.json', 'w') as jf:
    prep_json_obj = json.dumps (test.toJson ())
    prep_json_dict = json.dumps (dict_json)

    jf.write (prep_json_obj)
    jf.write ("\n")
    jf.write (prep_json_dict)
    jf.close ()

uml_data = [json.loads(line) for line in open('UMLJson.json', 'r')]

print (uml_data)
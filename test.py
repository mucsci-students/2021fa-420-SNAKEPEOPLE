import uml_class
import json
import jsonpickle

uml_class.add_class("Test")
a = jsonpickle.encode(uml_class.class_dict["Test"])
uml_class.add_class("Object")
b = jsonpickle.encode(uml_class.class_dict["Object"])

temp = {"Test" : a,
        "Object" : b}

with open("save_files/classes.json", "w") as outfile:
    json.dump(temp, outfile)
        
load_dict = {}
with open("save_files/classes.json") as infile:
    load_dict = json.load(infile)
    
print(load_dict)
x = jsonpickle.decode(load_dict["Test"])

print(x)
    

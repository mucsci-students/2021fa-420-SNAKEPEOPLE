import json
# key = name_of_class, value representation is class instance
dict_json = {
    "Name" : "Evan",
    "Role" : "Manager",
    "Task" : "Manage",
    "ID" : 1922
}

prep_json = json.dumps (dict_json)

print (prep_json)

unpack_json = json.loads (prep_json)

#print (dict_json)
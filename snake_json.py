import json
dict_json = {
    "Name" : "Evan",
    "Role" : "Manager",
    "Task" : "Manage",
    "ID" : 1922
}

prep_json = json.dumps (dict_json)

print (dict_json)
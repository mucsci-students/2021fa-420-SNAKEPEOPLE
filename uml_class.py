# Project Name: SNAKE PEOPLE UML Editor
# File Name:    uml_class.py

import json
from types import new_class

class_dict = dict()

class UMLClass():
    
    def __init__(self, name : str, attr : list = []):
        self.name = name
        self.attr = attr
        
    def __del__(self):
        print(f"Deleting UMLCLass:<{self.name}>...")
    
    def __repr__(self):
        return self.name
    
    def rename(self, new_name : str):
        self.name = new_name

    def toJson (self) :
        return json.dumps (self, default=lambda o: o.__dict__,
            sort_keys=True, indent = 4)

    def write_file (self):
        # writes/saves uml dict to a json file
        # opens file and writes encoded json file to UMLJson.json
            with open ('UMLJson.json', 'w') as jf:

                # dumps function encodes class object/dictionary 
                prep_json_obj = json.dumps (self.toJson ())

                # writes takes encoded info from dumps to json file 
                jf.write (prep_json_obj)

                # \n is necessary to create a new line. write does not start a new line
                jf.write ("\n")

                jf.close ()

    def load_file () :
                # converts json file to array data and prints array

                # creates an empty dict with json file decoded and assigned to it 
                # through the load function

                class_dict = {}

                with open ('UMLJson.json', "r") as f :
                    class_dict = json.load (f)

                #test by printing data received from file
                print (class_dict)

def add_class(name : str) -> None:
    # Checks if 'name' is a key in the dict of existing classes.
    if name not in class_dict:
        # If 'name' does not already exist in the class dict, create a new class
        # with that name, and add it to the dict.
        new_class = UMLClass(name)
        class_dict.update({name : new_class})
    else:
        # If 'name' already exists, prints an error.
        print(f"Error: {name} is already the name of an existing class.")
        
def delete_class(name : str) -> None:
    # Checks if 'name is a key in the dict of existing classes.
    if name in class_dict:
        # If 'name' already exists in the class dict, removes the entry with the
        # key equal to 'name'.
        class_dict.pop(name)
    else:
        # If 'name' does not exist, prints an error.
        print(f"Error: {name} does not exist as the name of a class.")

def rename_class(uml_class : UMLClass, new_name : str) -> None:
    uml_class.rename(new_name)

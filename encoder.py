from json import JSONEncoder
from typing import Union
from UMLClass import UMLClass
from UMLAttributes import *
from relationships import UMLRelationship

class UMLEncoder(JSONEncoder):
    '''
    A child class of json.JSONEncoder. Used to overwrite JSONEncoder.default()
    for use with UMLClass and UMLRelationship objects.
    '''
    
    def default(self, o: Union[UMLClass, UMLRelationship]) -> dict:
        return o.__dict__
    
def decode_classes(json_dict : dict) -> dict:
    '''
    Parses class information from JSON data. Instantiates UMLClass objects from
    the data, and adds them to a dict.
    
    Parameters:\n
        - json_dict : dict -> a dict containing the data read in from a .json 
        file.
    
    Returns: 
        - decode_dict : dict -> a dict structured like the class_dict from
        uml_class.py. The class_dict should be made to point to the return value
        of the function.
    '''
    
    decode_dict = {}
    
    for object in json_dict:
        if 'obj_type' in object and object['obj_type'] == 'class':
            decode_dict.update({object['name'] : UMLClass(**object)})
            
    return decode_dict
            
def decode_relationships(json_dict : dict) -> dict:
    '''
    Parses relationship information from JSON data. Instantiates UMLRelationship 
    objects from the data, and adds them to a dict.
    
    Parameters:\n
        - json_dict : dict -> a dict containing the data read in from a .json 
        file.
    
    Returns: 
        - decode_dict : dict -> a dict structured like the relationship_dict 
        from relationships.py. The relationship_dict should be made to point to 
        the return value of the function.
    '''
    
    decode_dict = {}
    
    for object in json_dict:
        if 'obj_type' in object and object['obj_type'] == 'relationship':
            decode_dict.update({object['name'] : UMLRelationship(**object)})
            
    return decode_dict

if __name__ == "__main__":
    import json
    
    method = Method("test", "null")
    method.add_param(Parameter("index", "int"))
    _class = UMLClass("name")
    _class.add_method("g", "null")
    a = json.dumps(_class, cls=UMLEncoder)
    z = json.loads(a)
    x = decode_classes(z) 
    print(x)  
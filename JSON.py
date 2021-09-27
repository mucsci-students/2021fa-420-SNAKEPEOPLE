import json
from uml_components.UMLAttributes import Field, Method
from uml_components.UMLRelationship import UMLRelationship
from uml_components.UMLClass import UMLClass
from typing import Union

class ComplexEncoder(json.JSONEncoder):
    """
    A complex json encoder for encoding nested objects.
    """
    
    def default(self, obj: Union[UMLClass or UMLRelationship]) -> dict:
        if hasattr(obj, 'toJson'):
            return obj.toJson()
        else:
            return json.JSONEncoder.default(self, obj)
        
def encode(classes : list, relationships : list) -> str:
    objects = {"classes" : classes,
               "relationships" : relationships}
    
    return json.dumps(objects, indent= 4, cls= ComplexEncoder)

def decode_classes(classes : dict) -> dict:
    cls_dict = {}
    
    for cls in classes:
        fields = []
        methods = []
    
        for field in cls['fields']:
            fields.append(Field(**field))
        for method in cls['methods']:
            methods.append(Method(**method))
            
        obj : UMLClass = UMLClass(**cls)
        obj.fields = fields
        obj.methods = methods
        
        cls_dict.update({obj.name : obj})
        
    return cls_dict

def decode_relationships(relationships : dict) -> list:
    rel_list = []
    
    for rel in relationships:
        obj : UMLRelationship = UMLRelationship(**rel)
        rel_list.append(obj)
    
    return rel_list

def decode(json_str : str) -> tuple[dict,list]:
    json_dict = json.loads(json_str)
    
    classes = json_dict['classes']
    relationships = json_dict['relationships']
    
    return (decode_classes(classes), decode_relationships(relationships))
        
if __name__ == "__main__":
    
    from uml_components.interfaces import (class_interface as cif, 
                                           attr_interface as aif,
                                           rel_interface as rif)
    from uml_components.UMLClass import class_dict
    from uml_components.UMLRelationship import relationship_list
        
    cif.add_class("Apple")
    clsa : UMLClass = class_dict["Apple"]
    aif.add_field("Apple", "variety", "String")
    aif.add_field("Apple", "height", "int")
    aif.add_method("Apple", "getObj", "Object")
    
    cif.add_class("Banana")
    clsb : UMLClass = class_dict["Banana"]
    aif.add_field("Banana", "color", "String")
    aif.add_field("Banana", "weight", "int")
    aif.add_method("Banana", "getObj", "Object")
    
    rif.add_relationship(clsa.name, clsb.name, "inheritance")
    rela : UMLRelationship = relationship_list[0]
    
    
    cls_list = [clsa.toJson(), clsb.toJson()]
    rel_list = [rela.toJson()]
    
    xmp = encode(cls_list, rel_list)
    print(xmp)
    input()
    json_dict = json.loads(xmp)
    class_json = json_dict['classes']
    rel_json = json_dict['relationships']
    
    input()
    old_cd = class_dict
    class_dict, rel_list = decode(xmp)
    print(class_dict)
    print (rel_list)
    
    
    
    
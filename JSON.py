import json
from uml_components.UMLAttributes import UMLField, UMLMethod, UMLParameter
from uml_components.UMLRelationship import UMLRelationship
from uml_components.UMLClass import UMLClass
from typing import Union

class ComplexEncoder(json.JSONEncoder):
    """
    A complex json encoder for encoding nested objects.
    """
    
    # Overwrites json.JSONEncoder.default() to account for custom python
    def default(self, 
                obj: Union[UMLClass or UMLRelationship]) -> dict:
        if hasattr(obj, 'toJson'):
            return obj.toJson()
        else:
            return json.JSONEncoder.default(self, obj)
        
def encode(classes : list, 
           relationships : list) -> str:
    """
    Encodes lists of classes and relationships into JSON.
    
    Parameters:
    - classes : list[dict] -> all classes to be encoded into JSON.
    - relationships : list[dict] -> all relationships to be encoded
    into JSON.
    
    return : str -> JSON representation of a dictionary of the parameter lists. 
    """
    
    # Dictionary containing lists of classes and relationships.
    objects = {"classes" : classes,
               "relationships" : relationships}
    
    # Returns the result of the json.dumps() method, which is a string.
    return json.dumps(objects, indent= 4, cls= ComplexEncoder)


def decode_classes(classes : list) -> dict:
    """
    Decodes JSON into python objects representing a UMLClass and it's fields and
    methods, including method paramters.
    
    Parameters:
    - classes : list -> the list of classes derived from the dictionary returned
    by json.loads().
    
    returns : dict -> a dictionary of UMLClasses where the key is the name of 
    the UMLClass. The internally stored class dictionary should point to this
    value.
    """
    
    # Function's nternal class dictionary.
    cls_dict = {}
    
    # Loops through the list of classes.
    for cls in classes:
        
        # Lists of UMLAttribute Field and Method objects that exist in the 
        # class.
        fields = []
        methods = []
    
        # Loops through the list of JSON representaions of fields and creating
        # UMLAttribute Field objects.
        for field in cls['fields']:
            fields.append(UMLField(**field))
        
        # Loops through the list of JSON representations of methods and creating
        # UMLAttribute Method objects and their parameters (if they exist). Then
        # appends the Method objects to the list 'methods'.
        for method in cls['methods']:
            
            # List of UMLAttribute Parameter objects
            params = []
            m_obj = UMLMethod(**method)
            
            # Loops through the list of JSON representations of parameters
            # creating UMLAttribute Parameter objects and appending them to
            # 'params'.
            for param in method['params']:
                p_obj = UMLParameter(**param)
                params.append(p_obj)
            
            m_obj.params = params    
            methods.append(m_obj)
            
        # Constructs a new UMLClass object with paramters derived from 'cls'
        obj : UMLClass = UMLClass(**cls)
        # Assigns the list of fields and methods to the UMLClass objects fields
        # of the same name.
        obj.fields = fields
        obj.methods = methods
        
        # Adds the object to the internal class dictionary.
        cls_dict.update({obj.name : obj})
        
    return cls_dict


def decode_relationships(relationships : list) -> list:
    """
    Decodes JSON into python objects representing a UMLRelationship.
    
    Parameters:
    - relationships : list -> the list of relationships derived from the 
    dictionary returned by json.loads().
    
    return : list -> a list containing UMLRelationship objects. The internal
    relationship list should point to this value.
    """
    
    # Function's internal relationship list.
    rel_list = []
    
    # Loops through the list of JSON representations of relationships, creating
    # UMLRelationship objects and appending those objects to the function's
    # internal relationship list.
    for rel in relationships:
        obj : UMLRelationship = UMLRelationship(**rel)
        rel_list.append(obj)
    
    return rel_list


def decode(json_str : str) -> tuple:
    """
    Decodes JSON into the respective UML components objects.
    
    Parameters:
    - json_str : str -> the encoded json string of UML component objects.
    
    return : tuple[dict,list] -> a tuple of the class dictionary returned by 
    'decode_classes' and the relationship list returned by 
    'decode_relationships'.
    """
    

    json_dict = json.loads(json_str)
    
    # Pulls the lists of classes and relationships from json_dict.
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
    
    old_cd = class_dict
    class_dict, rel_list = decode(xmp)
    print (class_dict)
    print (rel_list)
    
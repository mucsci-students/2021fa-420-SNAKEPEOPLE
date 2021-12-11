# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     UMLClass.py

# External Imports
from typing import Dict, List, Union

# Internal Imports
from uml_components.UMLAttributes import (
    UMLField,
    UMLMethod,
    UMLParameter)

###################################################################################################

class UMLClass():
    """
    A representation of a class for a UML class diagram.
    
    Fields:
    - name : str -> the name of the class. Given during object construction.
    attributes : list -> a list of attributes of the class. Is intialized
    as an empty list.
    """
    
    def __init__(self, 
                 name : str,
                 fields : List[UMLField] = None,
                 methods : List[UMLMethod] = None,
                 position_x : int = None,
                 position_y : int = None,
                 **kwargs):
        
        self.name = name
            
        self.fields = fields if fields else list()
        self.methods = methods if methods else list()
        
        self.position_x = position_x if position_x else -1
        self.position_y = position_y if position_y else -1

    def __repr__(self) -> str:
        
        name = f"\nClass Name: {self.name}"
        fields = "\n    Fields: (none)"
        methods = "\n    Methods: (none)"
        
        if self.fields != []:
            fields = f"\n    Fields:"
            for field in self.fields:
                fields += f"\n    - {field}"
        
        if self.methods != []:
            methods = f"\n    Methods:"
            for method in self.methods:
                methods += f"\n    - {method}"
            
            
        return name + fields + methods

    def rename(self, 
               new_name : str):
        
        # Sets 'self.name' to be equal to 'new_name'.
        print(f"<Renamed Class>: {self.name} -> {new_name}")
        self.name = new_name

    def add_field(self,
                  name : str,
                  type : str) -> UMLField:
        
        # Adds a new field object to the built-in list of fields.
        new_field = UMLField(name, type)

        self.fields.append(new_field)
        print(f"<Added Field ({self.name})>: {type} {name}")
        
        return new_field

    def add_method(self,
                   name : str,
                   return_type : str,
                   parameters : Union[List[UMLParameter], None] = None
                   ) -> UMLMethod:
        
        param_list = parameters if parameters else list()
        new_method = UMLMethod(name, return_type, param_list)
        
        self.methods.append(new_method)
        print(f"<Added Method ({self.name})>: {new_method}")
        
        return new_method

    def add_method_param(self,
                         method : UMLMethod,
                         param_name : str,
                         param_type : str) -> UMLParameter:
        
        param = method.add_param(param_name, param_type)
        
        print(f"<Added Method Parameter ({self.name}.{method})>: {param}")
        
        return param

    def delete_field(self,
                     field : UMLField) -> UMLField:
        idx = self.fields.index(field)
        self.fields.pop(idx)
        print(f"<Deleted Field ({self.name})>: {field}")
        
        return field

    def delete_method(self,
                      method : UMLMethod) -> None:
        method.clear()
        idx = self.methods.index(method)
        self.methods.pop(idx)
        print(f"<Deleted Method ({self.name})>: {method}")
        
    def delete_param(self,
                     method : UMLMethod,
                     param : UMLParameter) -> None:
        idx = method.params.index(param)
        method.params.pop(idx)
        print(f"<Deleted Method Parameter ({self.name}.{method})>: {param}")
        
    def get_field(self,
                  field_name : str) -> Union[UMLField, None]:
        field : UMLField
        for field in self.fields:
            if field_name == field.name:
                return field
        
        return None

    def toJson(self) -> dict:
        return self.__dict__

###################################################################################################

class_dict: Dict[str, UMLClass] = dict()

###################################################################################################
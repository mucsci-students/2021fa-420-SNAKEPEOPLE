# Project Name: SNAKE PEOPLE UML Editor
# File Name:    uml_class.py

from uml_components.UMLAttributes import (UMLField,
                                          UMLMethod,
                                          UMLParameter)
from typing import Union

from uml_components.interfaces.attr_interface import delete_field

class_dict = dict()

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
                 fields : list = None,
                 methods : list = None,
                 **kwargs):
        
        self.name = name
            
        self.fields = fields if fields else list()
        self.methods = methods if methods else list()
        
        print(f"<Added Class>: {name}")
        

    def __repr__(self):
        
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
                  type : str):
        
        # Adds a new field object to the built-in list of fields.
        new_field = UMLField(name, type)

        self.fields.append(new_field)
        print(f"<Added Field ({self.name})>: {type} {name}")
        
        
    def add_method(self,
                   name : str,
                   return_type : str,
                   parameters : Union[list[UMLParameter], None] = None) -> None:
        
        param_list = parameters if parameters else list()
        new_method = UMLMethod(name, return_type, param_list)
        
        self.methods.append(new_method)
        print(f"<Added Method ({self.name})>: {return_type} " +
              f"{name}({param_list})")
    
    
    def add_method_param(self,
                         method : UMLMethod,
                         param_name : str,
                         param_type : str) -> None:
        
        method.add_param(param_name, param_type)
        
        print(f"<Added Method Parameter ({self.name}.{method.name}())>: " +
              f"{param_type} {param_name}")
        
    def delete_field(self,
                     field : UMLField) -> None:
        idx = self.fields.index(field)
        self.fields.pop(idx)
        
    def delete_method(self,
                      method : UMLMethod) -> None:
        method.clear()
        idx = self.methods.index(method)
        self.methods.pop(idx)
        
    def delete_param(self,
                     method : UMLMethod,
                     param : UMLParameter) -> None:
        idx = method.params.index(param)
        method.params.pop(idx)
            
    
    def toJson(self) -> dict:
        return self.__dict__

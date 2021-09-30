# Project Name: SNAKE PEOPLE UML Editor
# File Name:    uml_class.py

from . import UMLAttributes

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
        new_field = UMLAttributes.Field(name, type)

        self.fields.append(new_field)
        print(f"<Added Field ({self.name})>: {type} {name}")
        
        
    def add_method(self,
                   name : str,
                   return_type : str,
                   parameters = None):
        
        param_list = parameters if parameters else list()
        new_method = UMLAttributes.Method(name, return_type, param_list)
        
        self.methods.append(new_method)
        print(f"<Added Method ({self.name})>: {return_type} " +
              f"{name}({param_list})")
    
    
    def add_method_param(self,
                         method : UMLAttributes.Method,
                         param_name : str,
                         param_type : str):
        
        new_param = UMLAttributes.Parameter(param_name, param_type)
        method.add_param(new_param)
        
        print(f"<Added Method Parameter ({self.name}.{method.name}())>: " +
              f"{param_type} {param_name}")
        

    def delete_attr(self,
                    attr : UMLAttributes.UMLAttribute):
        
        attr_pos : int
        
        if isinstance(attr, UMLAttributes.Field):
            attr_pos = self.fields.index(attr)
            field_n : str = self.fields[attr_pos].name
            
            self.fields.pop(attr_pos)
            
            print(f"<Deleted Field>: {field_n} ({self.name})")
        
        if isinstance(attr, UMLAttributes.Method):
            attr_pos = self.methods.index(attr)
            method_n : str = self.fields[attr_pos].name
            
            self.methods.pop(attr_pos)
            
            print(f"<Deleted Method>: {method_n} ({self.name})")
            
    
    def toJson(self) -> dict:
        return self.__dict__

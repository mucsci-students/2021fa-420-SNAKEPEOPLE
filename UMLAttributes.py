from dataclasses import dataclass, field

@dataclass
class UMLAttribute:
    pass
    
@dataclass
class Parameter:
    name : str
    type : str
    
@dataclass
class Field (UMLAttribute):
    name : str
    type : str
    
    def rename(self, 
               new_name : str):
        self.name = new_name
    
@dataclass
class Method (UMLAttribute):
    name : str
    return_type : str
    parameters : list = field(default_factory=list)
        
    def rename(self, 
               new_name : str) -> None:
        self.name = new_name
        
    def add_param(self, 
                  param : Parameter) -> None:
        self.parameters.append(param)
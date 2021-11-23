from dataclasses import dataclass, field
from typing import List, Union

@dataclass
class UMLAttribute:
    name : str
    
    def toJson(self) -> dict:
        return self.__dict__

@dataclass
class UMLParameter (UMLAttribute):
    type : str
    
    def __eq__(self, 
               other):
        if isinstance(other, UMLParameter):
            return (self.name == other.name and
                    self.type == other.type)
            
    def __hash__(self) -> int:
        return hash(self.type)
    
    def __repr__(self) -> str:
        output = f"{self.type} {self.name}"
        return output
    
    def rename(self, 
               new_name : str) -> None:
        self.name = new_name

@dataclass
class UMLField (UMLAttribute):
    type : str
    
    def __eq__(self, 
               other):
        if isinstance(other, UMLField):
            return (self.name == other.name and
                    self.type == other.type)
            
    def __hash__(self) -> int:
        return hash(self.type)
    
    def __repr__(self):
        output = f"{self.type} {self.name}"
        return output
        
    def rename(self, 
               new_name : str) -> None:
        self.name = new_name

@dataclass
class UMLMethod (UMLAttribute):
    return_type : str
    params : List[UMLParameter] = field(default_factory=list)
            
    def __eq__(self, 
               other):
        if isinstance(other, UMLMethod):
            return (self.name == other.name and
                    self.return_type == other.return_type and
                    set(self.params) == set(other.params))
            
    def __hash__(self) -> int:
        return hash(self.return_type)
            
    def __repr__(self):
        output = f"{self.return_type} {self.name}("
        output += ", ".join([str(e) for e in self.params])
        return output + ")"
                
    def rename(self, 
               new_name : str) -> None:
        self.name = new_name
        
    def add_param(self, 
                  param_name : str,
                  param_type : str) -> UMLParameter:
        
        param = UMLParameter(param_name, param_type)
        self.params.append(param)
        
        return param
    
    def get_param(self,
                  param_name) -> Union[UMLParameter, None]:
        p:UMLParameter
        for p in self.params:
            if p.name == param_name:
                return p
        
    def clear(self) -> None:
        self.params = []
        
    
from dataclasses import dataclass, field

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
    
    def __repr__(self):
        output = f"{self.type} {self.name}"
        return output
        
    def rename(self, 
               new_name : str) -> None:
        self.name = new_name
    
@dataclass
class UMLMethod (UMLAttribute):
    return_type : str
    params : list = field(default_factory=list)
            
    def __eq__(self, 
               other):
        if isinstance(other, UMLMethod):
            return (self.name == other.name and
                    self.return_type == other.return_type and
                    self.params == other.params)
            
    def __repr__(self):
        output = f"{self.return_type} {self.name}("
        for param in self.params:
            if param == self.params[len(self.params) - 1]:
                output += f"{param}"
            else:
                output += f"{param}, "
        
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
        
    def clear(self) -> None:
        self.params = []
        
    
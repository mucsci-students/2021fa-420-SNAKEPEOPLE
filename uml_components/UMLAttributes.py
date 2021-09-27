from dataclasses import dataclass, field

@dataclass
class UMLAttribute:
    name : str
    
@dataclass
class Parameter:
    name : str
    type : str
    
    def __repr__(self):
        output = f"{self.type} {self.name}"
        return output
    
@dataclass
class Field (UMLAttribute):
    type : str
    
    def __repr__(self):
        output = f"{self.type} {self.name}"
        return output
        
    def rename(self, 
               new_name : str):
        self.name = new_name
    
@dataclass
class Method (UMLAttribute):
    return_type : str
    parameters : list[Parameter] = field(default_factory=list)
            
    def __repr__(self):
        output = f"{self.return_type} {self.name}("
        for param in self.parameters:
            if param == self.parameters[len(self.parameters) - 1]:
                output += f"{param}"
            else:
                output += f"{param}, "
        
        return output + ")"
                
    def rename(self, 
               new_name : str) -> None:
        self.name = new_name
        
    def add_param(self, 
                  param : Parameter) -> None:
        self.parameters.append(param)

if __name__ == "__main__":       
    method = Method("get_attr", "UMLAttribute")
    method.add_param(Parameter("index", "int"))
    method.add_param(Parameter("count", "int"))
    print(method)
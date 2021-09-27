from dataclasses import dataclass, field

@dataclass
class UMLAttribute:
    name : str
    
    def toJson(self) -> dict:
        return self.__dict__

    
@dataclass
class Parameter (UMLAttribute):
    type : str
    
    def __repr__(self) -> str:
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
    params : list[Parameter] = field(default_factory=list)
            
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
                  param : Parameter) -> None:
        self.params.append(param)

if __name__ == "__main__":       
    method = Method("get_attr", "UMLAttribute")
    method.add_param(Parameter("index", "int"))
    method.add_param(Parameter("count", "int"))
    print(method)
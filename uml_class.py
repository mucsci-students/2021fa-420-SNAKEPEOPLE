# Project Name: SNAKE PEOPLE UML Editor
# File Name:    uml_class.py

class UMLClass():
    
    def __init__(self, name : str, attr : list = []):
        self.name = name
        self.attr = attr
        
    def __del__(self):
        print(f"Deleting UMLCLass:<{self.name}>...")
    
    def __repr__(self):
        return self.name
    
    def rename(self, new_name : str):
        self.name = new_name
        
my_class = UMLClass("car")
print(my_class)
my_class.rename("rav4")
print(my_class)
del my_class
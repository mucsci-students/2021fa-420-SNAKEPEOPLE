relationship_list = []

class UMLRelationship():
    
    #UMLRelationship is an object that models a relationship between two UML classes.
    #The class stores a name in the form a source object referencing a uml class object,
    #and a destination object also referencing a uml class object.

    def __init__(self, source, destination, rel_type: str):
        self.source = source
        self.destination = destination
        self.sourceName = source.name
        self.destName = destination.name
        self.rel_type = rel_type

    def __del__(self):
        print(f"<Deleted Relationship>: {self.sourceName}-{self.destName}")
    
    def __repr__(self):
        return self.sourceName + "-" + self.destName
        
    def rename(self, new_name : str):
        self.name = new_name

    def changeSource(self, new_source):
        self.source = new_source
        self.sourceName = new_source.name

    def changeDestination(self, new_dest):
        self.destination = new_dest
        self.destName = new_dest.name

    def changeType(self, new_type):
        self.rel_type = new_type
        
    def toJson(self):
        return self.__dict__

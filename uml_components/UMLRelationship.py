relationship_list = []

class UMLRelationship():
    
    """
    A representation of a relationship for a UML class diagram.
    
    Fields:
    - source : str -> the name of primary object of the relationship.
    - destination : str -> the name of the secondary object of the relationship.
    - type : str -> the type of relationship. Can be one of ['Aggregation', 
    'Composition', 'Inheritance', 'Realization'].
    """

    def __init__(self, 
                 source : str, 
                 destination : str, 
                 type : str,
                 **kwargs):
        
        self.source = source
        self.destination = destination
        self.type = type
    
    def __repr__(self):
        return f"{self.source} - {self.destination} ({self.type})"

    def change_source(self, 
                      new_source : str):
        self.source = new_source

    def change_destination(self, 
                           new_destination : str):
        self.destination = new_destination

    def change_type(self, new_type : str):
        self.rel_type = new_type
        
    def toJson(self):
        return self.__dict__

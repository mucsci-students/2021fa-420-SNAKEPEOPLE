from types import new_class
from typing import Text
from uml_components.UMLClass import UMLClass, class_dict
from uml_components.UMLRelationship import UMLRelationship, relationship_list
from uml_components.interfaces import (attr_interface as ai,
                                       class_interface as ci,
                                       rel_interface as ri)
from uml_components import UMLAttributes

from . import UMLBox
from . import UMLField
from . import UMLLine
from . import UMLMethod
import queue

undo_stack = queue.LifoQueue()
redo_stack = queue.LifoQueue()

class UMLSavepoint():

    def __init__(self):

        dup_dict = dict()
        coord_list = []
        dup_fields = []
        dup_methods = []
        dup_rel = []
        dup_params = []

        for name, value in class_dict.items():

            #For each class, make a copy of the methods list
            for method in value.methods:
                #For each method, make a copy of the parameter list
                for param in method.params:
                    #add the most recently duplicated parameter object to the duplicate parameter list
                    dup_params.append(UMLAttributes.UMLParameter(param.name, param.type))
                #Add the most recently duplicated method object to the duplicate method list
                dup_methods.append(UMLAttributes.UMLMethod(method.name, method.return_type, dup_params.copy()))
                dup_params = []

            #For each class duplicate the fields list
            for field in value.fields:
                #Add the most recently duplicated field object to the duplicate field list
                dup_fields.append(UMLAttributes.UMLField(field.name, field.type)) 
            #Create a duplicate class object containing the duplicated fields and methods
            new_class = UMLClass(name, dup_fields, dup_methods)
            #Add the current state of the class to the duplicate dictionary
            dup_dict.update({name : new_class})
            #Add coordinates for each canvas box
            coord_list.append(UMLBox.get_coords(name))
            dup_methods = []
            dup_fields = []

        self.coords_list = coord_list
        self.class_dict = dup_dict

        #Duplicate the relationship list
        for i in relationship_list:
            #Add the most recently duplicated relationship object 
            #to the duplicate relationship list
            dup_rel.append(UMLRelationship(i.source, i.destination, i.type))
        self.relationship_list = dup_rel


def save_point():
    #Add the current state to the undo stack
    undo_stack.put(UMLSavepoint())

def undo():
    #Add the current state to the redo stack
    redo_stack.put(UMLSavepoint())

    last_state : UMLSavepoint
    last_state = undo_stack.get()

    #Clear the relationship list
    while len(relationship_list) > 0:
        ri.delete_relationship(relationship_list[0].source, relationship_list[0].destination)

    #Roll back the class dictionary to the previous state
    class_dict.clear()
    class_dict.update(last_state.class_dict)

    #Clear the canvas
    UMLBox.test_canvas.delete("all")
    UMLBox.class_list = []

    populate_canvas(last_state)

def redo():
    #Place the current state on the undo stack
    undo_stack.put(UMLSavepoint())

    last_state : UMLSavepoint
    last_state = redo_stack.get()

    #Clear the relationhsip list
    while len(relationship_list) > 0:
        ri.delete_relationship(relationship_list[0].source, relationship_list[0].destination)

    #Roll back the class dictionary to the previous state (forward state)
    class_dict.clear()
    class_dict.update(last_state.class_dict)
        
    #clear the canvas
    UMLBox.test_canvas.delete("all")
    UMLBox.class_list = []

    populate_canvas(last_state)

def populate_canvas(last_state):
    index = 0

    #Create a canvas element for each dictionary item
    for name, value in class_dict.items():
        UMLBox.create_box_with_coords(value.name, last_state.coords_list[index][0], last_state.coords_list[index][1],
                            last_state.coords_list[index][2], last_state.coords_list[index][3])
        UMLField.update_fields(name)
        UMLMethod.update_methods(name)
        index += 1

    #Add any relationships back into the relationship list
    for i in last_state.relationship_list:
        ri.add_relationship(i.source, i.destination, i.type)
        UMLLine.add_line(i.source, i.destination, i.type)

#Clear the redo_stack
#Used only when undos occur and a new action is taken other than redo
def clear_stack():
    while(redo_stack.empty() == False):
        redo_stack.get()
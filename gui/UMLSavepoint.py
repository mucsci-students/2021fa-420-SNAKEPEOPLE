# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     UMLSavepoint.py

from gui import ViewChange
from uml_components import UMLClass
from uml_components import UMLRelationship
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

    def __init__(self, mode):

        dup_dict = dict()
        coord_list = []
        dup_fields = []
        dup_methods = []
        dup_rel = []
        dup_params = []

        for name, value in UMLClass.class_dict.items():

            #For each class, make a copy of the methods list
            for method in value.methods:
                #For each method, make a copy of the parameter list
                for param in method.params:
                    #add the most recently duplicated parameter object to the duplicate parameter list
                    dup_params.append(UMLAttributes.UMLParameter(param.name, param.type))
                #Add the most recently duplicated method object to the duplicate method list
                dup_methods.append(UMLAttributes.UMLMethod(method.name, 
                method.return_type, dup_params.copy()))
                dup_params = []

            #For each class duplicate the fields list
            for field in value.fields:
                #Add the most recently duplicated field object to the duplicate field list
                dup_fields.append(UMLAttributes.UMLField(field.name, field.type)) 
            #Add coordinates for each canvas box
            if mode == "gui":
                coords = UMLBox.get_xy(name)
                x = coords[0]
                y = coords[1]
            else:
                x = value.position_x
                y = value.position_y
            #Create a duplicate class object containing the duplicated fields and methods
            new_class = UMLClass.UMLClass(name, dup_fields, dup_methods, x, y)
            #Add the current state of the class to the duplicate dictionary
            dup_dict.update({name : new_class})

            dup_methods = []
            dup_fields = []

        self.coords_list = coord_list
        self.class_dict = dup_dict

        #Duplicate the relationship list
        for i in UMLRelationship.relationship_list:
            #Add the most recently duplicated relationship object 
            #to the duplicate relationship list
            dup_rel.append(UMLRelationship.UMLRelationship(i.source, i.destination, i.type))
        self.relationship_list = dup_rel


def save_point(mode = "gui"):
    #Add the current state to the undo stack
    undo_stack.put(UMLSavepoint(mode))

def undo(mode = "gui"):
    #Add the current state to the redo stack
    redo_stack.put(UMLSavepoint(mode))

    last_state : UMLSavepoint
    last_state = undo_stack.get()

    #Clear the relationship list
    while len(UMLRelationship.relationship_list) > 0:
        ri.delete_relationship(UMLRelationship.relationship_list[0].source, 
        UMLRelationship.relationship_list[0].destination)
    #Recreate the previous state's relationship list
    for i in last_state.relationship_list:
        ri.add_relationship(i.source, i.destination, i.type)

    #Roll back the class dictionary to the previous state
    UMLClass.class_dict.clear()
    UMLClass.class_dict.update(last_state.class_dict)

    if mode == "gui": 
        #clear the canvas
        UMLBox.test_canvas.delete("all")
        UMLBox.class_list = []

        populate_canvas(last_state)

def redo(mode = "gui"):
    #Place the current state on the undo stack
    undo_stack.put(UMLSavepoint(mode))

    last_state : UMLSavepoint
    last_state = redo_stack.get()

    #Clear the relationhsip list
    while len(UMLRelationship.relationship_list) > 0:
        ri.delete_relationship(UMLRelationship.relationship_list[0].source,
         UMLRelationship.relationship_list[0].destination)
    #Recreate the previous state of the relationship list
    for i in last_state.relationship_list:
        ri.add_relationship(i.source, i.destination, i.type)

    #Roll back the class dictionary to the previous state (forward state)
    UMLClass.class_dict.clear()
    UMLClass.class_dict.update(last_state.class_dict)

    if mode == "gui": 
        #clear the canvas
        UMLBox.test_canvas.delete("all")
        UMLBox.class_list = []

        populate_canvas(last_state)

def populate_canvas(last_state):
    index = 0

    #Create a canvas element for each dictionary item
    for name, value in UMLClass.class_dict.items():
        x1, y1, x2, y2 = make_coords(name, value.position_x, value.position_y)
        UMLBox.create_box_with_coords(name, x1, y1, x2, y2)
        ViewChange.bring_all_front(UMLBox.class_list[len(UMLBox.class_list) - 1])
        UMLField.update_fields(name)
        UMLMethod.update_methods(name)
        index += 1

    #Add any relationships back into the canvas
    for i in UMLRelationship.relationship_list:
        UMLLine.add_line(i.source, i.destination, i.type)

#Clear the redo_stack
#Used only when undos occur and a new action is taken other than redo
def clear_stack():
    while(redo_stack.empty() == False):
        redo_stack.get()

def make_coords(class_name : str, x : int, y : int):
    """Get horizontal size of box"""
    longest_name = 3.5 * len(class_name)
    i = 0
    #Check class name against field and method labels
    if(len("Fields:") * 3.5 > longest_name):
        longest_name = len("Fields:") * 3.5
    if(len("Methods:") * 3.5 > longest_name):
        longest_name = len("Methods:") * 3.5
    uml : UMLClass = UMLClass.class_dict[class_name]
    #Check to see if the longest name is in fields
    for fields in uml.fields:
        name = "-" + fields.type + " " + fields.name
        if len(name) * 3.5 > longest_name:
            longest_name = len(name) * 3.5
    uml : UMLClass = UMLClass.class_dict[class_name]
    method : ai.UMLMethod
    param : ai.UMLParameter
    #find if the longest name is within methods
    for method in uml.methods:
        name = method.name + " " + method.return_type + "("
        if len(name) * 3.5 > longest_name:
            longest_name = len(name) * 3.5
        for param in method.params:
            name = "  -" + param.type + " " + method.name
            if len(name) * 3.5 > longest_name:
                longest_name = len(name) * 3.5
    x1 = x - 40 - longest_name
    x2 = x + 40 + longest_name
    """Get Vertical size of box"""
    yinc = 30
    #Add 15 to the vertical size of the box for each field
    for fields in uml.fields:
        yinc += 15
    method : ai.UMLMethod
    param : ai.UMLParameter
    #Add 45 to the vertical increment for each method and 15 for each parameter
    for method in uml.methods:
        yinc += 45
        for param in method.params:
            yinc += 15
    y1 = y
    y2 = y + yinc
    return (x1, y1, x2, y2)
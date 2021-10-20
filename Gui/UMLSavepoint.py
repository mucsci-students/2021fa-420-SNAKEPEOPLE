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
            for method in value.methods:
                for param in method.params:
                    dup_params.append(UMLAttributes.UMLParameter(param.name, param.type))
                dup_methods.append(UMLAttributes.UMLMethod(method.name, method.return_type, dup_params.copy()))
                dup_params = []
            for field in value.fields:
                dup_fields.append(UMLAttributes.UMLField(field.name, field.type)) 
            new_class = UMLClass(name, dup_fields, dup_methods)
            dup_dict.update({name : new_class})
            coord_list.append(UMLBox.get_coords(name))
            dup_methods = []
            dup_fields = []
        self.coords_list = coord_list
        self.class_dict = dup_dict

        for i in relationship_list:
            dup_rel.append(UMLRelationship(i.source, i.destination, i.type))
        self.relationship_list = dup_rel


def save_point():
    undo_stack.put(UMLSavepoint())

def undo():
    redo_stack.put(UMLSavepoint())
    last_state : UMLSavepoint
    last_state = undo_stack.get()
    class_dict.clear()
    class_dict.update(last_state.class_dict)

    while len(relationship_list) > 0:
        ri.delete_relationship(relationship_list[0].source, relationship_list[0].destination)

    undo_class = False
    if len(UMLBox.class_list) > len(class_dict):
        undo_class = True


    UMLBox.test_canvas.delete("all")
    UMLBox.class_list = []

    populate_canvas(last_state)

    if(undo_class):
        if len(UMLBox.class_list) == 0:
            UMLBox.UMLsquare.y1 = 40
            UMLBox.UMLsquare.y2 = 65
            UMLBox.UMLsquare.x1 = 120
            UMLBox.UMLsquare.x2 = 200
        else:
            textspace = UMLBox.class_list[(len(UMLBox.class_list) - 1)].textspace
            if len(UMLBox.class_list) % 2 == 1:
                UMLBox.UMLsquare.y1 -= 100
                UMLBox.UMLsquare.y2 -= 100
                UMLBox.UMLsquare.x1 += 200 + textspace
                UMLBox.UMLsquare.x2 += 200 + textspace
            else:
                UMLBox.UMLsquare.x1 = 120
                UMLBox.UMLsquare.x2 = 200
        UMLBox.UMLsquare.tracker = len(UMLBox.class_list)

def redo():
    undo_stack.put(UMLSavepoint())
    last_state : UMLSavepoint
    last_state = redo_stack.get()
    class_dict.clear()
    class_dict.update(last_state.class_dict)

    while len(relationship_list) > 0:
        ri.delete_relationship(relationship_list[0].source, relationship_list[0].destination)

    redo_class = False
    if len(UMLBox.class_list) < len(class_dict):
        redo_class = True


    UMLBox.test_canvas.delete("all")
    UMLBox.class_list = []

    populate_canvas(last_state)

    if(redo_class):
        textspace = UMLBox.class_list[(len(UMLBox.class_list) - 1)].textspace
        if len(UMLBox.class_list) % 2 == 1:
            UMLBox.UMLsquare.x1 += 200 + textspace
            UMLBox.UMLsquare.x2 += 200 + textspace
        else:
            UMLBox.UMLsquare.y1 += 100
            UMLBox.UMLsquare.y2 += 100
            UMLBox.UMLsquare.x1 = 120
            UMLBox.UMLsquare.x2 = 200
        UMLBox.UMLsquare.tracker = len(UMLBox.class_list)

def populate_canvas(last_state):
    index = 0
    for name, value in class_dict.items():
        UMLBox.create_box_with_coords(value.name, last_state.coords_list[index][0], last_state.coords_list[index][1],
                            last_state.coords_list[index][2], last_state.coords_list[index][3])
        UMLField.update_fields(name)
        UMLMethod.update_methods(name)
        index += 1

    for i in last_state.relationship_list:
        ri.add_relationship(i.source, i.destination, i.type)
        UMLLine.add_line(i.source, i.destination, i.type)
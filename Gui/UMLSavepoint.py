from types import new_class
from uml_components.UMLClass import UMLClass, class_dict
from uml_components.UMLRelationship import UMLRelationship, relationship_list
from uml_components import UMLAttributes
from . import UMLBox
from . import UMLField
from . import UMLLine
from . import UMLMethod
import queue

action_stack = queue.LifoQueue()

class UMLSavepoint():

    def __init__(self):
        dup_dict = dict()
        coord_list = []
        dup_methods = []
        for name, value in class_dict.items():
            for method in value.methods:
                dup_methods.append(UMLAttributes.UMLMethod(method.name, method.return_type, method.params.copy()))
            new_class = UMLClass(name, value.fields.copy(), dup_methods)
            dup_dict.update({name : new_class})
            coord_list.append(UMLBox.get_coords(name))
        self.coords_list = coord_list
        self.class_dict = dup_dict
        self.relationship_list = relationship_list.copy()

def save_point():
    action_stack.put(UMLSavepoint())

def undo():
    last_state : UMLSavepoint
    last_state = action_stack.get()
    class_dict.clear()
    class_dict.update(last_state.class_dict)
    relationship_list = last_state.relationship_list
    UMLBox.test_canvas.delete("all")
    UMLBox.class_list = []
    index = 0
    for name, value in class_dict.items():
        UMLBox.create_box_with_coords(value.name, last_state.coords_list[index][0], last_state.coords_list[index][1],
                            last_state.coords_list[index][2], last_state.coords_list[index][3])
        UMLField.update_fields(value.name)
        UMLMethod.update_methods(value.name)
        index += 1
    for rel in last_state.relationship_list:
        UMLLine.add_line(rel.source, rel.destination, rel.type)
        
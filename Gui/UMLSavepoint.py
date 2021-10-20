from types import new_class
from uml_components.UMLClass import UMLClass, class_dict
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
        for name, value in class_dict.items():
            new_class = UMLClass(name, value.fields.copy(), value.methods.copy())
            dup_dict.update({name : new_class})
            coord_list.append(UMLBox.get_coords(name))
        self.coords_list = coord_list
        self.class_dict = dup_dict

def save_point():
    action_stack.put(UMLSavepoint())

def undo():
    last_state : UMLSavepoint
    last_state = action_stack.get()
    class_dict.clear()
    class_dict.update(last_state.class_dict)
    print(last_state.class_dict)
    UMLBox.test_canvas.delete("all")
    UMLBox.class_list = []
    index = 0
    for name, value in class_dict.items():
        UMLBox.create_box_with_coords(value.name, last_state.coords_list[index][0], last_state.coords_list[index][1],
                            last_state.coords_list[index][2], last_state.coords_list[index][3])
        UMLField.update_fields(value.name)
        UMLMethod.update_methods(value.name)
        index += 1
    
        
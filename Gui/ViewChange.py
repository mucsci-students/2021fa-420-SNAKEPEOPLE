"""THIS FILE ACTS AS THE VIEW CHANGER ALL OTHER METHODS USE THIS FILE TO UPDATE THE CANVAS"""
from gui import UMLBox

def del_item(name):
    UMLBox.test_canvas.delete(name)

def bring_front(item):
    UMLBox.test_canvas.tag_raise(item)

def push_back(item):
    UMLBox.test_canvas.tag_lower(item)

def set_rec(item, x1, y1, x2, y2):
    UMLBox.test_canvas.coords(item, x1, y1, x2, y2)

def set_text(item, x, y):
    UMLBox.test_canvas.coords(item, x, y)

def set_line(item, x1, y1, x2, y2):
    UMLBox.test_canvas.coords(item, x1, y1, x2, y2)

def item_config(item, text, justify, state):
    if(justify == None and state == None):
        UMLBox.test_canvas.itemconfigure(item, text = text)
    else:
        UMLBox.test_canvas.itemconfigure(item, text = text, justify = justify, state = state)

def bring_all_front(obj):
    bring_front(obj.rec)
    bring_front(obj.methodlabel)
    bring_front(obj.methodtext)
    bring_front(obj.fieldlabel)
    bring_front(obj.fieldtext)
    bring_front(obj.label)
        

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
        
"""DESIGN PATTERNS WITHIN CANVAS
    Iterators - Python for loops are iterative by design
    Memento - I create copies of the current state of the
              canvas and use that to undo/redo anthing
    Bridge - relationships within UMLSquare are subject to 
             change in quantity, so rather than change the the 
             lines connecting boxes within the box object, I 
             create a list that references all lines connected
             to the box.
    Facade - In UMLBox I call another method which I created
             to hide the details of bringing every canvas element
             to the front for a given box.
    Command - Within the UMLFields and UMLMethods class, I
              have a general update fields and update methods function
              which relies on the implementation details of the model
              to help produce an output on the canvas. Any button that
              modifes a field or methods invokes the same command, either
              update_fields() or update_methods()
    Observer - Within the update_fields() and update_methods() I
               shift around boxes to fit the canvas better, but in
               doing so may lose some realtionship representations.
               Because I have a list of all relationships displayed, 
               I make a call to fix_lines() which goes through the
               'subscriber' list for relationships within each class
               and updates them to reconnect themselves to the correct
               boxes.
    State - Each canvas element can be designated as having three states,
            Normal, Disabled, or Hidden. These states make the object appear
            to be different, but its the same type of object. I use this
            specifically when dealing with method and field textboxes. Initially
            I want them hidden, but when the text box is populated I want them
            visible.
    Template Method - We loosely use this in the canvas by instantiating all
                      necessary parts of the box at the start and modify them
                      later when the specific data is applied to each box
    """
    
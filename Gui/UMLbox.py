import tkinter as tk
from UMLLine import deleteline
import EventHandler
import ViewChange

class_list = []

def setCanvas(can):
    global canvas
    canvas = can

def find_pos_from_name(name : str):
    pos = 0
    while pos < len(class_list):
        if class_list[pos][0] == name:
            return pos
        pos += 1

class UMLsquare():

    """the list tracks the name, the square element, the class name label,
    how much padding to account for lengthy text, lines, fields, yincrement due to fields,
    field header, method header, methods text element, fields and methods, and vertical increment
    due to methods and parametes"""
    tracker = 0
    x1 = 120
    x2 = 200
    y1 = 40
    y2 = 65
    xspace = 0
    def __init__(self, canvas, x1 : int, y1 : int, x2 : int, y2 : int, name : str):
        x1 = x1 + UMLsquare.xspace
        x2 = x2 + UMLsquare.xspace
        label = canvas.create_text(x1 + 40, y1 + 12, text = name, state=tk.DISABLED, tags=name)
        textspace =3.5 * len(name)
        rec = canvas.create_rectangle(x1 - textspace, y1, x2 + textspace, y2 + 40, fill="#D1FF65", tags=name)
        fieldlabel = canvas.create_text(x1 + 10, y1 + 30, text = "Field(s):", state=tk.DISABLED)
        fieldtext = canvas.create_text(x1 + 40, y1 + 25, text = "", state=tk.HIDDEN, anchor=tk.N)
        yincrement = 30
        methodlabel = canvas.create_text(x1 + 18, y1 + 50, text = "Method(s):", state=tk.DISABLED)
        methodText = canvas.create_text(x1 + 40, y1 + 60, text = "", state=tk.HIDDEN, anchor=tk.N)
        canvas.tag_lower(rec)
        method_increment = 0
        self.info = [name, rec, label, textspace, [], fieldtext, [], yincrement, fieldlabel, methodlabel, methodText, [], method_increment]
        class_list.append(self.info)
        EventHandler.can_drag(rec)
    
"""add a box to the canvas"""        
def create_box(canvas, name : str):
    obj = UMLsquare(canvas, UMLsquare.x1, UMLsquare.y1, UMLsquare.x2, UMLsquare.y2, name)
    """shift everything right after the first box in a row and then shift down after the second"""
    if(UMLsquare.tracker % 2 == 0):
        UMLsquare.x1 += 400
        UMLsquare.x2 += 400
    else:
        UMLsquare.x1 -= 400
        UMLsquare.x2 -= 400
        UMLsquare.y1 += 300
        UMLsquare.y2 += 300
        UMLsquare.xspace = 0
    UMLsquare.tracker += 1

"""Remove the box with the text = name"""
def delete_box(name : str):
    pos = find_pos_from_name(name)
    subpos = 0
    """remove any lines connecting the box to any other boxes"""
    while subpos < len(class_list[pos][4]):
        if(class_list[pos][4][subpos][0] == "source"):
            deleteline(canvas, class_list[pos][1], class_list[pos][4][subpos][2])
            subpos -= 1
        else:
            deleteline(canvas, class_list[pos][4][subpos][2], class_list[pos][1])
            subpos -= 1
        subpos += 1
    """delete everything associated with the box"""
    ViewChange.del_item(class_list[pos][5])
    ViewChange.del_item(class_list[pos][8])
    ViewChange.del_item(class_list[pos][9])
    ViewChange.del_item(class_list[pos][10])
    class_list.pop(pos)
    ViewChange.del_item(name)

"""rename a box with the name = oldname"""
def rename_box(oldname : str, newname : str):
    pos = 0
    """Find the position of the box with the old name"""
    while pos < len(class_list):
        if oldname == class_list[pos][0]:
            """save the box and text values"""
            x1,y1,x2,y2 = canvas.coords(class_list[pos][1])
            class_list[pos][0] = newname
            class_list[pos][3] = len(newname) *3.5
            canvas.coords(class_list[pos][1], x1 - len(newname) *3.5, y1, x2 + len(newname) *3.5, y2)
            break
        else:
            pos += 1
    """Change the text of the circle to the updated name"""
    ViewChange.item_config(class_list[pos][2], newname, None, None)


"""update the width of the box according to the length of the contained text"""
def update_size(pos : int):
    old_longest =3.5 * len(class_list[pos][0])
    longest_name =3.5 * len(class_list[pos][0])
    i = 0
    """find the longest text entry in the box"""
    for i in class_list[pos][6]:
        if len(i) *3.5 > longest_name:
            longest_name = len(i) *3.5
    for i in class_list[pos][11]:
        for k in i:
            if len(k) *3.5 > longest_name:
                longest_name = len(k) *3.5
    class_list[pos][3] = longest_name
    """find the center and build off of it left and right using the 
    length of the longest text entry"""
    x1,y1,x2,y2 = canvas.coords(class_list[pos][1])
    center = ((x2 - x1) / 2) + x1
    x1 = center - 40 - longest_name
    x2 = center + 40 + longest_name
    """update the box size, and shift header text elements"""
    ViewChange.set_rec(class_list[pos][1], x1, y1, x2, y2)
    x,y = canvas.coords(class_list[pos][8])
    ViewChange.set_text(class_list[pos][8], x1 + 25, y)
    x,y = canvas.coords(class_list[pos][9])
    ViewChange.set_text(class_list[pos][9], x1 + 35, y)
    return center
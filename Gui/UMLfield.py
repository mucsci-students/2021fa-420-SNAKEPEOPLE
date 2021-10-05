import tkinter as tk
import UMLbox
import ViewChange

"""add a field and update the vertical length of the box"""
def add_field(name : str, field : str):
    pos = UMLbox.find_pos_from_name(name)
    """add field to list of fields"""
    UMLbox.class_list[pos][6].append(field)
    """update the height of the box"""
    x1, y1, x2, y2 = UMLbox.canvas.coords(UMLbox.class_list[pos][1])
    ViewChange.set_rec(UMLbox.class_list[pos][1], x1, y1, x2, y2 + 15)
    """increase the running count of the height of the box"""
    UMLbox.class_list[pos][7] += 15
    newtext = new_fieldText(pos)
    """update the text of the field text element"""
    ViewChange.item_config(UMLbox.class_list[pos][5], text = newtext, justify = tk.CENTER, state=tk.DISABLED)
    """move everything below the field downward"""
    x,y = UMLbox.canvas.coords(UMLbox.class_list[pos][9])
    ViewChange.set_text(UMLbox.class_list[pos][9], x, y + 15)
    x,y = UMLbox.canvas.coords(UMLbox.class_list[pos][10])
    ViewChange.set_text(UMLbox.class_list[pos][10], x, y + 15)
    """adjust width of the box"""
    UMLbox.update_size(pos)

"""delete a field and update the vertical length of the box"""
def del_field(name : str, field : str):
    pos = UMLbox.find_pos_from_name(name)
    fieldpos = 0
    """find the fields position in the field list"""
    while fieldpos < len(UMLbox.class_list[pos][6]):
        if UMLbox.class_list[pos][6][fieldpos] == field:
            UMLbox.class_list[pos][6].pop(fieldpos)
            break
        fieldpos += 1
    """update the running count of the height of the box"""
    UMLbox.class_list[pos][7] -= 15
    """update the shape of the box"""
    x1, y1, x2, y2 = UMLbox.canvas.coords(UMLbox.class_list[pos][1])
    ViewChange.set_rec(UMLbox.class_list[pos][1], x1, y1, x2, y2 - 15)
    newtext = new_fieldText(pos)
    """update the text of the field text element"""
    ViewChange.item_config(UMLbox.class_list[pos][5], text = newtext, justify = tk.CENTER, state=tk.DISABLED)
    """shift everything below the field section upward"""
    x,y = UMLbox.canvas.coords(UMLbox.class_list[pos][9])
    ViewChange.set_text(UMLbox.class_list[pos][9], x, y - 15)
    """adjust the width of the box"""
    UMLbox.update_size(pos)

"""rename a field and update the vertical length of the box"""
def rename_field(name : str, oldname : str, newname : str):
    pos = UMLbox.find_pos_from_name(name)
    fieldpos = 0
    """find the field's location in the list"""
    while fieldpos < len(UMLbox.class_list[pos][6]):
        if UMLbox.class_list[pos][6][fieldpos] == oldname:
            UMLbox.class_list[pos][6][fieldpos] = newname
            break
        fieldpos += 1
    newtext = new_fieldText(pos)
    """update the text"""
    ViewChange.item_config(UMLbox.class_list[pos][5], text = newtext, justify = tk.CENTER, state=tk.DISABLED)
    """adjust the width of the box"""
    UMLbox.update_size(pos)

"""create a new block of text conaining the formated parameters"""
def new_fieldText(pos):
    newtext = ""
    for i in UMLbox.class_list[pos][6]:
        newtext = newtext + "\n-" + i
    return newtext
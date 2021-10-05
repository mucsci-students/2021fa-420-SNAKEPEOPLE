import tkinter as tk
from UMLbox import class_list
import UMLbox
import ViewChange

"""add a method and paramters and increment the vertical length of the box"""
def add_method(classname : str, methodname : str, parameters : list):
    i = 0
    """tried a for loop here to begin with, didn't work. Basically adding padding
        every parameter"""
    while i < len(parameters):
        parameters[i] = "    -" + parameters[i]
        i += 1
    parameters.insert(0, methodname)
    pos = UMLbox.find_pos_from_name(classname)
    class_list[pos][11].append(parameters)
    """increment yincrement so the box can resize with the length of the method list"""
    UMLbox.class_list[pos][12] += 10 + len(parameters) * 20
    x1, y1, x2, y2 = UMLbox.canvas.coords(UMLbox.class_list[pos][1])
    """increase the size of the containing box"""
    ViewChange.set_rec(UMLbox.class_list[pos][1], x1, y1, x2, y2 + 10 + len(parameters)*20)
    newtext = block_text(pos)
    """update the text block"""
    ViewChange.item_config(UMLbox.class_list[pos][10], text = newtext, justify = tk.LEFT, state=tk.DISABLED)
    newspot = UMLbox.update_size(pos)

"""delete a method and paramters and increment the vertical length of the box"""
def del_method(classname : str, methodname : str):
    pos = UMLbox.find_pos_from_name(classname)
    del_list = []
    i = 0
    """find the method within the box association and remove it"""
    while i < len(UMLbox.class_list[pos][11]):
        if UMLbox.class_list[pos][11][i][0] == methodname:
            del_list = UMLbox.class_list[pos][11].pop(i)
            break
        i += 1
    """decrement size of the box"""
    UMLbox.class_list[pos][12] -= 10 + len(del_list) * 20
    x1, y1, x2, y2 = UMLbox.canvas.coords(UMLbox.class_list[pos][1])
    """update the size of the box"""
    ViewChange.set_rec(UMLbox.class_list[pos][1], x1, y1, x2, y2 - (10 + len(del_list)*20))
    newtext = block_text(pos)
    """update the method text element"""
    ViewChange.item_config(UMLbox.class_list[pos][10], text = newtext, justify = tk.LEFT, state=tk.DISABLED)

"""change the paramters of a method and increment the vertical length of the box"""
def change_params(classname : str, methodname : str, new_params : list):
    pos = UMLbox.find_pos_from_name(classname)
    i = 0
    """find the position of the method before it is moved"""
    while i < len(UMLbox.class_list[pos][11]):
        if UMLbox.class_list[pos][11][i][0] == methodname:
            break
        i += 1
    del_method(classname, methodname)
    add_method(classname, methodname, new_params)
    k = 0
    """find the position of the method after it is re-inserted with new parameters"""
    while k < len(UMLbox.class_list[pos][11]):
        if UMLbox.class_list[pos][11][k][0] == methodname:
            break
        k += 1
    """move the method back to its original place in the list"""
    save = UMLbox.class_list[pos][11].pop(k)
    UMLbox.class_list[pos][11].insert(i, save)
    newtext = block_text(pos)
    """update the text element of method text"""
    ViewChange.item_config(UMLbox.class_list[pos][10], text = newtext, justify = tk.LEFT, state=tk.DISABLED)


"""create a new block of text that contains the formatted method list"""
def block_text(pos):
    newtext = ""
    index = 0
    subindex = 0
    while index < len(UMLbox.class_list[pos][11]):
        subindex = 0
        while subindex < len(UMLbox.class_list[pos][11][index]):
            if subindex == 0:
                newtext = newtext + "" + UMLbox.class_list[pos][11][index][subindex] + ":\n"
            else:
                newtext = newtext + "" + UMLbox.class_list[pos][11][index][subindex] + "\n"
            subindex += 1
            if(subindex == len(UMLbox.class_list[pos][11][index])):
                newtext = newtext + "\n"
        index += 1
    return newtext
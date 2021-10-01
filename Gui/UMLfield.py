import tkinter as tk
import UMLbox

def add_field(name : str, field : str):
    pos = UMLbox.find_pos_from_name(name)
    UMLbox.class_list[pos][6].append(field)
    newtext = ""
    x1, y1, x2, y2 = UMLbox.canvas.coords(UMLbox.class_list[pos][1])
    UMLbox.canvas.coords(UMLbox.class_list[pos][1], x1, y1, x2, y2 + 15)
    UMLbox.class_list[pos][7] += 15
    for i in UMLbox.class_list[pos][6]:
        newtext = newtext + "\n-" + i
    UMLbox.canvas.itemconfigure(UMLbox.class_list[pos][5], text = newtext, justify = tk.CENTER, state=tk.DISABLED)
    x,y = UMLbox.canvas.coords(UMLbox.class_list[pos][9])
    UMLbox.canvas.coords(UMLbox.class_list[pos][9], x, y + 15)
    x,y = UMLbox.canvas.coords(UMLbox.class_list[pos][10])
    UMLbox.canvas.coords(UMLbox.class_list[pos][10], x, y + 15)
    UMLbox.update_size(pos)


def del_field(name : str, field : str):
    pos = UMLbox.find_pos_from_name(name)
    fieldpos = 0
    while fieldpos < len(UMLbox.class_list[pos][6]):
        if UMLbox.class_list[pos][6][fieldpos] == field:
            UMLbox.class_list[pos][6].pop(fieldpos)
            break
        fieldpos += 1
    UMLbox.class_list[pos][7] -= 15
    newtext = ""
    x1, y1, x2, y2 = UMLbox.canvas.coords(UMLbox.class_list[pos][1])
    y2 = y2
    UMLbox.canvas.coords(UMLbox.class_list[pos][1], x1, y1, x2, y2 - 15)
    for i in UMLbox.class_list[pos][6]:
        newtext = newtext + "\n-" + i
    UMLbox.canvas.itemconfigure(UMLbox.class_list[pos][5], text = newtext, justify = tk.CENTER, state=tk.DISABLED)
    x,y = UMLbox.canvas.coords(UMLbox.class_list[pos][9])
    UMLbox.canvas.coords(UMLbox.class_list[pos][9], x, y - 15)
    UMLbox.update_size(pos)


def rename_field(name : str, oldname : str, newname : str):
    pos = UMLbox.find_pos_from_name(name)
    fieldpos = 0
    while fieldpos < len(UMLbox.class_list[pos][6]):
        if UMLbox.class_list[pos][6][fieldpos] == oldname:
            UMLbox.class_list[pos][6][fieldpos] = newname
            break
        fieldpos += 1
    newtext = ""
    for i in UMLbox.class_list[pos][6]:
        newtext = newtext + "\n-" + i
    UMLbox.canvas.itemconfigure(UMLbox.class_list[pos][5], text = newtext, justify = tk.CENTER, state=tk.DISABLED)
    UMLbox.update_size(pos)
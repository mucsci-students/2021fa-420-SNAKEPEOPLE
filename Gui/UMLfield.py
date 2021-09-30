import tkinter as tk
import UMLbox

def add_field(name : str, field : str):
    pos = UMLbox.find_pos_from_name(name)
    while pos < len(UMLbox.circle_list):
        if UMLbox.circle_list[pos][0] == name:
            break
        pos += 1
    UMLbox.circle_list[pos][6].append(field)
    newtext = ""
    x1, y1, x2, y2 = UMLbox.DndCanvas.coords(UMLbox.circle_list[pos][1])
    y2 = y2
    UMLbox.DndCanvas.coords(UMLbox.circle_list[pos][1], x1, y1, x2, y2 + 15)
    UMLbox.circle_list[pos][7] += 15
    for i in UMLbox.circle_list[pos][6]:
        newtext = newtext + "\n" + i
    UMLbox.DndCanvas.itemconfigure(UMLbox.circle_list[pos][5], text = newtext, justify = tk.LEFT, state=tk.DISABLED)

def del_field(name : str, field : str):
    pos = UMLbox.find_pos_from_name(name)
    fieldpos = 0
    while fieldpos < len(UMLbox.circle_list[pos][6]):
        if UMLbox.circle_list[pos][6][fieldpos] == field:
            UMLbox.circle_list[pos][6].pop(fieldpos)
            break
        fieldpos += 1
    UMLbox.circle_list[pos][7] -= 15
    newtext = ""
    x1, y1, x2, y2 = UMLbox.DndCanvas.coords(UMLbox.circle_list[pos][1])
    y2 = y2
    UMLbox.DndCanvas.coords(UMLbox.circle_list[pos][1], x1, y1, x2, y2 - 15)
    for i in UMLbox.circle_list[pos][6]:
        newtext = newtext + "\n" + i
    UMLbox.DndCanvas.itemconfigure(UMLbox.circle_list[pos][5], text = newtext, justify = tk.LEFT, state=tk.DISABLED)

def rename_field(name : str, oldname : str, newname : str):
    pos = UMLbox.find_pos_from_name(name)
    fieldpos = 0
    while fieldpos < len(UMLbox.circle_list[pos][6]):
        if UMLbox.circle_list[pos][6][fieldpos] == oldname:
            UMLbox.circle_list[pos][6][fieldpos] = newname
            break
        fieldpos += 1
    newtext = ""
    for i in UMLbox.circle_list[pos][6]:
        newtext = newtext + "\n" + i
    UMLbox.DndCanvas.itemconfigure(UMLbox.circle_list[pos][5], text = newtext, justify = tk.LEFT, state=tk.DISABLED)
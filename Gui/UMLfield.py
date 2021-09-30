import tkinter as tk
import UMLbox

def add_field(name : str, field : str):
    pos = UMLbox.find_pos_from_name(name)
    UMLbox.class_list[pos][6].append(field)
    newtext = ""
    UMLbox.update_size(pos, field)
    x1, y1, x2, y2 = UMLbox.DndCanvas.coords(UMLbox.class_list[pos][1])
    UMLbox.DndCanvas.coords(UMLbox.class_list[pos][1], x1, y1, x2, y2 + 15)
    UMLbox.class_list[pos][7] += 15
    for i in UMLbox.class_list[pos][6]:
        newtext = newtext + "\n" + i
    UMLbox.DndCanvas.itemconfigure(UMLbox.class_list[pos][5], text = newtext, justify = tk.CENTER, state=tk.DISABLED)
    x,y = UMLbox.DndCanvas.coords(UMLbox.class_list[pos][9])
    UMLbox.DndCanvas.coords(UMLbox.class_list[pos][9], x, y + 15)


def del_field(name : str, field : str):
    pos = UMLbox.find_pos_from_name(name)
    fieldpos = 0
    while fieldpos < len(UMLbox.class_list[pos][6]):
        if UMLbox.class_list[pos][6][fieldpos] == field:
            UMLbox.class_list[pos][6].pop(fieldpos)
            break
        fieldpos += 1
    if len(field) * 2.5 == UMLbox.class_list[pos][3]:
        UMLbox.update_size(pos, field)
    UMLbox.class_list[pos][7] -= 15
    newtext = ""
    x1, y1, x2, y2 = UMLbox.DndCanvas.coords(UMLbox.class_list[pos][1])
    y2 = y2
    UMLbox.DndCanvas.coords(UMLbox.class_list[pos][1], x1, y1, x2, y2 - 15)
    for i in UMLbox.class_list[pos][6]:
        newtext = newtext + "\n" + i
    UMLbox.DndCanvas.itemconfigure(UMLbox.class_list[pos][5], text = newtext, justify = tk.CENTER, state=tk.DISABLED)
    x,y = UMLbox.DndCanvas.coords(UMLbox.class_list[pos][9])
    UMLbox.DndCanvas.coords(UMLbox.class_list[pos][9], x, y - 15)


def rename_field(name : str, oldname : str, newname : str):
    pos = UMLbox.find_pos_from_name(name)
    fieldpos = 0
    while fieldpos < len(UMLbox.class_list[pos][6]):
        if UMLbox.class_list[pos][6][fieldpos] == oldname:
            UMLbox.class_list[pos][6][fieldpos] = newname
            break
        fieldpos += 1
    if len(newname) * 2.5 > UMLbox.class_list[pos][3]:
        UMLbox.update_size(pos, newname)
    if len(oldname) * 2.5 == UMLbox.class_list[pos][3]:
        UMLbox.update_size(pos, oldname)
    newtext = ""
    for i in UMLbox.class_list[pos][6]:
        newtext = newtext + "\n" + i
    UMLbox.DndCanvas.itemconfigure(UMLbox.class_list[pos][5], text = newtext, justify = tk.CENTER, state=tk.DISABLED)
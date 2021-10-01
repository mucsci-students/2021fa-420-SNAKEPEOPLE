import tkinter as tk
from UMLbox import class_list
import UMLbox

def find_longest(paramlist):
    longest = paramlist[0]
    for i in paramlist:
        if len(i) > len(longest):
            longest = i
    return i

def add_method(classname : str, methodname : str, parameters : list):
    i = 0
    while i < len(parameters):
        parameters[i] = "    -" + parameters[i]
        i += 1
    parameters.insert(0, methodname)
    pos = UMLbox.find_pos_from_name(classname)
    class_list[pos][11].append(parameters)
    print(class_list[pos][11])
    UMLbox.class_list[pos][12] += 10 + len(parameters) * 20
    x1, y1, x2, y2 = UMLbox.canvas.coords(UMLbox.class_list[pos][1])
    UMLbox.canvas.coords(UMLbox.class_list[pos][1], x1, y1, x2, y2 + 10 + len(parameters)*20)
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
    UMLbox.canvas.itemconfigure(UMLbox.class_list[pos][10], text = newtext, justify = tk.LEFT, state=tk.DISABLED)
    newspot = UMLbox.update_size(pos)
    x,y = UMLbox.canvas.coords(UMLbox.class_list[pos][9])
    UMLbox.canvas.coords(UMLbox.class_list[pos][10], newspot, y + 10)

def del_method(classname : str, methodname : str):
    pos = UMLbox.find_pos_from_name(classname)
    del_list = []
    i = 0
    while i < len(UMLbox.class_list[pos][11]):
        if UMLbox.class_list[pos][11][i][0] == methodname:
            del_list = UMLbox.class_list[pos][11].pop(i)
            break
        i += 1
    UMLbox.class_list[pos][12] -= 10 + len(del_list) * 20
    x1, y1, x2, y2 = UMLbox.canvas.coords(UMLbox.class_list[pos][1])
    UMLbox.canvas.coords(UMLbox.class_list[pos][1], x1, y1, x2, y2 - (10 + len(del_list)*20))
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
    UMLbox.canvas.itemconfigure(UMLbox.class_list[pos][10], text = newtext, justify = tk.LEFT, state=tk.DISABLED)
    x,y = UMLbox.canvas.coords(UMLbox.class_list[pos][9])
    UMLbox.canvas.coords(UMLbox.class_list[pos][10], x, y + 10)
    newspot = UMLbox.update_size(pos)
    x,y = UMLbox.canvas.coords(UMLbox.class_list[pos][9])
    UMLbox.canvas.coords(UMLbox.class_list[pos][10], newspot, y + 10)

def change_params(classname : str, methodname : str, new_params : list):
    pos = UMLbox.find_pos_from_name(classname)
    i = 0
    while i < len(UMLbox.class_list[pos][11]):
        if UMLbox.class_list[pos][11][i][0] == methodname:
            break
        i += 1
    del_method(classname, methodname)
    add_method(classname, methodname, new_params)
    k = 0
    while k < len(UMLbox.class_list[pos][11]):
        if UMLbox.class_list[pos][11][k][0] == methodname:
            break
        k += 1
    save = UMLbox.class_list[pos][11].pop(k)
    UMLbox.class_list[pos][11].insert(i, save)
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
    UMLbox.canvas.itemconfigure(UMLbox.class_list[pos][10], text = newtext, justify = tk.LEFT, state=tk.DISABLED)
    x,y = UMLbox.canvas.coords(UMLbox.class_list[pos][9])
    UMLbox.canvas.coords(UMLbox.class_list[pos][10], x, y + 10)
    newspot = UMLbox.update_size(pos)
    x,y = UMLbox.canvas.coords(UMLbox.class_list[pos][9])
    UMLbox.canvas.coords(UMLbox.class_list[pos][10], newspot, y + 10)
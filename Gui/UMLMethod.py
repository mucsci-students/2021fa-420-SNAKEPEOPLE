import tkinter as tk
from gui import UMLBox
from gui import ViewChange
from uml_components.UMLClass import UMLClass

"""add a method and paramters and increment the vertical length of the box"""
def add_method(classname : str, methodname : str, parameters : list):
    add_meth = True
    pos = UMLBox.find_pos_from_name(classname)
    for i in UMLBox.class_list[pos][11]:
        if i[0].split(' ')[0] == methodname.split(' ')[0]:
            add_meth = False
    if(add_meth):
        i = 0
        parameters.insert(0, methodname)
        UMLBox.class_list[pos][11].append(parameters)
        newtext = block_text(pos)
        """update the text block"""
        ViewChange.item_config(UMLBox.class_list[pos][10], text = newtext, justify = tk.LEFT, state=tk.DISABLED)
        UMLBox.update_size(pos)
        update_vertical(pos)

"""delete a method and paramters and increment the vertical length of the box"""
def del_method(classname : str, methodname : str):
    pos = UMLBox.find_pos_from_name(classname)
    del_list = []
    i = 0
    """find the method within the box association and remove it"""
    while i < len(UMLBox.class_list[pos][11]):
        if UMLBox.class_list[pos][11][i][0].split(' ')[0] == methodname:
            del_list = UMLBox.class_list[pos][11].pop(i)
            break
        i += 1
    newtext = block_text(pos)
    """update the method text element"""
    ViewChange.item_config(UMLBox.class_list[pos][10], text = newtext, justify = tk.LEFT, state=tk.DISABLED)
    UMLBox.update_size(pos)
    update_vertical(pos)

"""change the paramters of a method and increment the vertical length of the box"""
def change_params(classname : str, methodname : str, new_params : list):
    pos = UMLBox.find_pos_from_name(classname)
    i = 0
    """find the position of the method before it is moved"""
    while i < len(UMLBox.class_list[pos][11]):
        if UMLBox.class_list[pos][11][i][0].split(' ')[0] == methodname:
            break
        i += 1
    del_method(classname, methodname)
    add_method(classname, methodname, new_params)
    k = 0
    """find the position of the method after it is re-inserted with new parameters"""
    while k < len(UMLBox.class_list[pos][11]):
        if UMLBox.class_list[pos][11][k][0] == methodname:
            break
        k += 1
    """move the method back to its original place in the list"""
    save = UMLBox.class_list[pos][11].pop(k)
    UMLBox.class_list[pos][11].insert(i, save)
    newtext = block_text(pos)
    """update the text element of method text"""
    ViewChange.item_config(UMLBox.class_list[pos][10], text = newtext, justify = tk.LEFT, state=tk.DISABLED)
    UMLBox.update_size(pos)
    update_vertical(pos)


"""create a new block of text that contains the formatted method list"""
def block_text(pos):
    newtext = ""
    index = 0
    subindex = 0
    while index < len(UMLBox.class_list[pos][11]):
        subindex = 0
        while subindex < len(UMLBox.class_list[pos][11][index]):
            if subindex == 0:
                newtext = newtext + "" + UMLBox.class_list[pos][11][index][subindex] + " (\n"
            else:
                newtext = newtext + "    " + UMLBox.class_list[pos][11][index][subindex] + ",\n"
            subindex += 1
            if(subindex == len(UMLBox.class_list[pos][11][index])):
                newtext = newtext + ")\n"
        index += 1
    return newtext

def del_param(classname: str, methodname : str, del_params: str):
    pos = UMLBox.find_pos_from_name(classname)
    ind = 0
    param_i = 1
    """Find the method/parameter location within the method/param list of the box"""
    while ind < len(UMLBox.class_list[pos][11]):
        if methodname == UMLBox.class_list[pos][11][ind][0].split(' ')[0]:
            break
        ind += 1
    """remove del_param from the method/parameter list of the box"""
    while param_i < len(UMLBox.class_list[pos][11][ind]):
        if UMLBox.class_list[pos][11][ind][param_i].split(' ')[1] == del_params.split(' ')[0]:
            UMLBox.class_list[pos][11][ind].pop(param_i)
        param_i += 1
    param_i = 1
    """update the parameter list and view using already created methods"""
    change_params(classname, UMLBox.class_list[pos][11][ind][0], UMLBox.class_list[pos][11][ind][1:])
    x1, y1, x2, y2 = UMLBox.test_canvas.coords(UMLBox.class_list[pos][1])
    ViewChange.set_rec(UMLBox.class_list[pos][1], x1, y1, x2, y2 - 5)
    UMLBox.update_size(pos)
    update_vertical(pos)

def rename_method(classname : str, oldname : str, newname : str):
    ren_meth = True
    pos = UMLBox.find_pos_from_name(classname)
    for i in UMLBox.class_list[pos][11]:
        print(i[0].split(' ')[0])
        if i[0].split(' ')[0] == newname:
            ren_meth = False
    if(ren_meth):
        pos = UMLBox.find_pos_from_name(classname)
        i = 0
        while i < len(UMLBox.class_list[pos][11]):
            if UMLBox.class_list[pos][11][i][0].split(' ')[0] == oldname:
                break
            i += 1
        param_list = UMLBox.class_list[pos][11][i]
        ret_type = UMLBox.class_list[pos][11][i][0].split(' ')[1]
        del_method(classname, oldname)
        param_list.pop(0)
        add_method(classname, newname + " " + ret_type, param_list)
        UMLBox.update_size(pos)
        update_vertical(pos)

def add_param(classname : str, methodname : str, paramname : str):
    pos = UMLBox.find_pos_from_name(classname)
    ind = 0
    param_i = 1
    add = True
    """Find the method/parameter location within the method/param list of the box"""
    while ind < len(UMLBox.class_list[pos][11]):
        if methodname == UMLBox.class_list[pos][11][ind][0].split(' ')[0]:
            break
        ind += 1
    while param_i < len(UMLBox.class_list[pos][11][ind]):
        if UMLBox.class_list[pos][11][ind][param_i].split(' ')[1] == paramname.split(' ')[1]:
            add = False
        param_i += 1
    if(add):
        """normalize parameters in the method/parameter list of the box"""
        UMLBox.class_list[pos][11][ind].append(paramname)
        """update the parameter list and view using already created methods"""
        change_params(classname, UMLBox.class_list[pos][11][ind][0], UMLBox.class_list[pos][11][ind][1:])
        UMLBox.update_size(pos)
        update_vertical(pos)

def rename_param(classname : str, methodname : str, old_param : str, new_param : str):
    pos = UMLBox.find_pos_from_name(classname)
    ind = 0
    param_i = 1
    rename = True
    """Find the method/parameter location within the method/param list of the box"""
    while ind < len(UMLBox.class_list[pos][11]):
        if methodname == UMLBox.class_list[pos][11][ind][0].split(' ')[0]:
            break
        ind += 1
    while param_i < len(UMLBox.class_list[pos][11][ind]):
        if UMLBox.class_list[pos][11][ind][param_i].split(' ')[1] == new_param:
            rename = False
        param_i += 1
    if(rename):
        param_i = 1
        while param_i < len(UMLBox.class_list[pos][11][ind]):
            if UMLBox.class_list[pos][11][ind][param_i].split(' ')[1] == old_param:
                UMLBox.class_list[pos][11][ind][param_i] = UMLBox.class_list[pos][11][ind][param_i].split(' ')[0] + " " + new_param
            param_i += 1
        newtext = block_text(pos)
        """update the text block"""
        ViewChange.item_config(UMLBox.class_list[pos][10], text = newtext, justify = tk.LEFT, state=tk.DISABLED)
        UMLBox.update_size(pos)
        update_vertical(pos)

def delete_method(classname : str, methodname : str):
    pos = UMLBox.find_pos_from_name(classname)
    del_list = []
    i = 0
    """find the method within the box association and remove it"""
    while i < len(UMLBox.class_list[pos][11]):
        if UMLBox.class_list[pos][11][i][0].split(' ')[0] == methodname:
            del_list = UMLBox.class_list[pos][11]
            break
        i += 1
    index = 1
    while index < len(del_list):
        del_param(classname, methodname, del_list[i])
        index += 1
    if len(UMLBox.class_list[pos][11]) > 0:
        UMLBox.class_list[pos][11].pop(i)
    newtext = block_text(pos)
    """update the method text element"""
    ViewChange.item_config(UMLBox.class_list[pos][10], text = newtext, justify = tk.LEFT, state=tk.DISABLED)
    UMLBox.update_size(pos)
    update_vertical(pos)

def update_vertical(pos):
    UMLBox.class_list[pos][12] = 0
    for i in UMLBox.class_list[pos][11]:
        UMLBox.class_list[pos][12] += 10
        for k in i:
            UMLBox.class_list[pos][12] += 25
    x1,y1,x2,y2 = UMLBox.test_canvas.coords(UMLBox.class_list[pos][1])
    ViewChange.set_rec(UMLBox.class_list[pos][1], x1, y1, x2, y1 + 35 + UMLBox.class_list[pos][7] + UMLBox.class_list[pos][12])
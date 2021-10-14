import tkinter as tk
from gui import UMLBox
from gui import ViewChange

#add a method and paramters#
def add_method(classname : str, methodname : str, parameters : list):
    add_meth = True
    pos = UMLBox.find_pos_from_name(classname)
    #Check for duplicate method names#
    for i in UMLBox.class_list[pos][11]:
        if i[0].split(' ')[0] == methodname.split(' ')[0]:
            add_meth = False
    if(add_meth):
        i = 0
        #Add the method to the list that contains fields#
        parameters.insert(0, methodname)
        #Add the method and parameters to the list of methods and parameters#
        UMLBox.class_list[pos][11].append(parameters)
        #update the text block#
        newtext = block_text(pos)
        ViewChange.item_config(UMLBox.class_list[pos][10], text = newtext, justify = tk.LEFT, state=tk.DISABLED)
        #Update the box shape#
        UMLBox.update_size(pos)
        update_vertical(pos)

#delete a method and paramters#
def del_method(classname : str, methodname : str):
    pos = UMLBox.find_pos_from_name(classname)
    del_list = []
    ind = 0
    #find the method within the box association and remove it#
    for i in UMLBox.class_list[pos][11]:
        if i[0].split(' ')[0] == methodname:
            del_list = UMLBox.class_list[pos][11].pop(ind)
            break
        ind += 1
    newtext = block_text(pos)
    #update the method text element#
    ViewChange.item_config(UMLBox.class_list[pos][10], text = newtext, justify = tk.LEFT, state=tk.DISABLED)
    #Update the shape of the box#
    UMLBox.update_size(pos)
    update_vertical(pos)

#change the paramters of a method and increment the vertical length of the box#
def change_params(classname : str, methodname : str, new_params : list):
    pos = UMLBox.find_pos_from_name(classname)
    ind = 0
    #find the position of the method before it is moved#
    for i in UMLBox.class_list[pos][11]:
        if i[0].split(' ')[0] == methodname:
            break
        ind += 1
    del_method(classname, methodname)
    add_method(classname, methodname, new_params)
    k = 0
    #find the position of the method after it is re-inserted with new parameters#
    for i in UMLBox.class_list[pos][11]:
        if i[0] == methodname:
            break
        k += 1
    #move the method back to its original place in the list#
    save = UMLBox.class_list[pos][11].pop(k)
    UMLBox.class_list[pos][11].insert(ind, save)
    #update the text element of method text#
    newtext = block_text(pos)
    ViewChange.item_config(UMLBox.class_list[pos][10], text = newtext, justify = tk.LEFT, state=tk.DISABLED)
    #Update the size of the box#
    UMLBox.update_size(pos)
    update_vertical(pos)


#create a new block of text that contains the formatted method list#
def block_text(pos):
    newtext = ""
    index = 0
    subindex = 0
    for i in UMLBox.class_list[pos][11]:
        subindex = 0
        for k in i:
            if subindex == 0:
                newtext = newtext + "" + k + " (\n"
            else:
                newtext = newtext + "    " + k + ",\n"
            subindex += 1
            if(subindex == len(i)):
                newtext = newtext + ")\n\n"
        index += 1
    return newtext

#Delete a parameter from the list#
def del_param(classname: str, methodname : str, del_params: str):
    pos = UMLBox.find_pos_from_name(classname)
    ind = 0
    param_i = 1
    #Find the method location within the method/param list of the box#
    for i in UMLBox.class_list[pos][11]:
        if methodname == i[0].split(' ')[0]:
            break
        ind += 1
    #remove del_param from the method/parameter list of the box#
    for i in UMLBox.class_list[pos][11][ind][1:]:
        if i.split(' ')[1] == del_params.split(' ')[0]:
            UMLBox.class_list[pos][11][ind].pop(param_i)
        param_i += 1
    param_i = 1
    #update the parameter list and view using already created methods#
    change_params(classname, UMLBox.class_list[pos][11][ind][0], UMLBox.class_list[pos][11][ind][1:])
    #Update the shape of the box#
    UMLBox.update_size(pos)
    update_vertical(pos)

#Rename a method to a unique name#
def rename_method(classname : str, oldname : str, newname : str):
    ren_meth = True
    pos = UMLBox.find_pos_from_name(classname)
    #Check for duplicate methods#
    for i in UMLBox.class_list[pos][11]:
        print(i[0].split(' ')[0])
        if i[0].split(' ')[0] == newname:
            ren_meth = False
    if(ren_meth):
        pos = UMLBox.find_pos_from_name(classname)
        i = 0
        #Find the position of the method cooresponding to oldname#
        for k in UMLBox.class_list[pos][11]:
            if k[0].split(' ')[0] == oldname:
                break
            i += 1
        param_list = UMLBox.class_list[pos][11][i]
        #Save the return type of the method being updated#
        ret_type = UMLBox.class_list[pos][11][i][0].split(' ')[1]
        #delete the method with oldname#
        del_method(classname, oldname)
        param_list.pop(0)
        #Create the method with newname and same parameters as oldname#
        add_method(classname, newname + " " + ret_type, param_list)
        #Update the shape of the box#
        UMLBox.update_size(pos)
        update_vertical(pos)

#Add a parameter to a method#
def add_param(classname : str, methodname : str, paramname : str):
    pos = UMLBox.find_pos_from_name(classname)
    ind = 0
    param_i = 1
    add = True
    #Find the method location within the method/param list of the box#
    for i in UMLBox.class_list[pos][11]:
        if methodname == UMLBox.class_list[pos][11][ind][0].split(' ')[0]:
            break
        ind += 1
    #Check for duplicate parameter names#
    for i in UMLBox.class_list[pos][11][ind][1:]:
        if i.split(' ')[1] == paramname.split(' ')[1]:
            add = False
        param_i += 1
    if(add):
        #Add the new parameter to the list of parameters#
        UMLBox.class_list[pos][11][ind].append(paramname)
        #update the parameter list and view using already created methods#
        change_params(classname, UMLBox.class_list[pos][11][ind][0], UMLBox.class_list[pos][11][ind][1:])
        #Update the size of the box#
        UMLBox.update_size(pos)
        update_vertical(pos)

#Rename a parameter#
def rename_param(classname : str, methodname : str, old_param : str, new_param : str):
    pos = UMLBox.find_pos_from_name(classname)
    ind = 0
    param_i = 1
    rename = True
    #Find the method location within the method/param list of the box#
    for i in UMLBox.class_list[pos][11]:
        if methodname == i[0].split(' ')[0]:
            break
        ind += 1
    #Check for duplicate parameter names#
    for i in UMLBox.class_list[pos][11][ind][1:]:
        if UMLBox.class_list[pos][11][ind][param_i].split(' ')[1] == new_param:
            rename = False
        param_i += 1
    if(rename):
        param_i = 1
        #Find the location of the old parameter name#
        for i in UMLBox.class_list[pos][11][ind][1:]:
            if i.split(' ')[1] == old_param:
                UMLBox.class_list[pos][11][ind][param_i] = i.split(' ')[0] + " " + new_param
            param_i += 1
        #update the text block#
        newtext = block_text(pos)
        ViewChange.item_config(UMLBox.class_list[pos][10], text = newtext, justify = tk.LEFT, state=tk.DISABLED)
        #Update the shape of the box#
        UMLBox.update_size(pos)
        update_vertical(pos)

#Update the vertical size of the box according to method and paramaters#
def update_vertical(pos):
    UMLBox.class_list[pos][12] = 0
    #Find an appropriate vertical spacing to contain the methods and parameters#
    for i in UMLBox.class_list[pos][11]:
        UMLBox.class_list[pos][12] += 25
        for k in i:
            UMLBox.class_list[pos][12] += 25
    #Update the view#
    x1,y1,x2,y2 = UMLBox.test_canvas.coords(UMLBox.class_list[pos][1])
    ViewChange.set_rec(UMLBox.class_list[pos][1], x1, y1, x2, y1 + 35 + UMLBox.class_list[pos][7] + UMLBox.class_list[pos][12])
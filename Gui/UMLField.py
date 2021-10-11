import tkinter as tk
from gui import UMLBox
from gui import ViewChange

#add a field#
def add_field(name : str, field : str):
    pos = UMLBox.find_pos_from_name(name)
    addfield = True
    #Check the list for duplicate field names#
    for i in UMLBox.class_list[pos][6]:
        if i.split(' ')[1] == field.split(' ')[1]:
            addfield = False
    if(addfield):
        #add field to list of fields#
        UMLBox.class_list[pos][6].append(field)
        #update the height of the box#
        x1, y1, x2, y2 = UMLBox.test_canvas.coords(UMLBox.class_list[pos][1])
        ViewChange.set_rec(UMLBox.class_list[pos][1], x1, y1, x2, y2 + 15)
        #increase the running count of the height of the box#
        UMLBox.class_list[pos][7] += 15
        newtext = new_fieldText(pos)
        #update the text of the field text element#
        ViewChange.item_config(UMLBox.class_list[pos][5], text = newtext, justify = tk.CENTER, state=tk.DISABLED)
        #move everything below the field downward#
        x,y = UMLBox.test_canvas.coords(UMLBox.class_list[pos][9])
        ViewChange.set_text(UMLBox.class_list[pos][9], x, y + 15)
        x,y = UMLBox.test_canvas.coords(UMLBox.class_list[pos][10])
        ViewChange.set_text(UMLBox.class_list[pos][10], x, y + 15)
        #adjust width of the box#
        UMLBox.update_size(pos)

#delete a field#
def del_field(name : str, field : str):
    pos = UMLBox.find_pos_from_name(name)
    fieldpos = 0
    #find the fields position in the field list#
    while fieldpos < len(UMLBox.class_list[pos][6]):
        if UMLBox.class_list[pos][6][fieldpos].split(' ')[1] == field:
            UMLBox.class_list[pos][6].pop(fieldpos)
            break
        fieldpos += 1
    #update the running count of the height of the box#
    UMLBox.class_list[pos][7] -= 15
    #update the shape of the box#
    x1, y1, x2, y2 = UMLBox.test_canvas.coords(UMLBox.class_list[pos][1])
    ViewChange.set_rec(UMLBox.class_list[pos][1], x1, y1, x2, y2 - 15)
    newtext = new_fieldText(pos)
    #update the text of the field text element#
    ViewChange.item_config(UMLBox.class_list[pos][5], text = newtext, justify = tk.CENTER, state=tk.DISABLED)
    #shift everything below the field section upward#
    x,y = UMLBox.test_canvas.coords(UMLBox.class_list[pos][9])
    ViewChange.set_text(UMLBox.class_list[pos][9], x, y - 15)
    #adjust the width of the box#
    UMLBox.update_size(pos)

#rename a field#
def rename_field(name : str, oldname : str, newname : str):
    pos = UMLBox.find_pos_from_name(name)
    fieldpos = 0
    addfield = True
    #find the field's location in the list#
    while fieldpos < len(UMLBox.class_list[pos][6]):
        var_type = UMLBox.class_list[pos][6][fieldpos].split(' ')[0]
        if UMLBox.class_list[pos][6][fieldpos].split(' ')[1] == oldname:
            newname = var_type + " " + newname
            #Check for duplicate field names#
            for i in UMLBox.class_list[pos][6]:
                if i == newname:
                    addfield = False
            #Update the old fieldname#
            if(addfield):
                UMLBox.class_list[pos][6][fieldpos] = newname
            break
        fieldpos += 1
    if(addfield):
        #update the text#
        newtext = new_fieldText(pos)
        ViewChange.item_config(UMLBox.class_list[pos][5], text = newtext, justify = tk.CENTER, state=tk.DISABLED)
        #adjust the width of the box#
        UMLBox.update_size(pos)

#create a new block of text conaining the formated parameters#
def new_fieldText(pos):
    newtext = ""
    for i in UMLBox.class_list[pos][6]:
        newtext = newtext + "\n-" + i
    return newtext

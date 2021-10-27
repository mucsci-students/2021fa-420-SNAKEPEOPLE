from gui import UMLBox
from gui import ViewChange
from uml_components.UMLAttributes import UMLField
from uml_components.interfaces import (attr_interface as ai,
                                       class_interface as ci,
                                       rel_interface as ri)
from uml_components.UMLClass import UMLClass, class_dict
from . import UMLField
from . import UMLMethod
from . import UMLSavepoint

global moved
moved = False
global saved
saved = True

#bind clicking and dragging to functions
def can_drag(rec):
    UMLBox.test_canvas.tag_bind(rec, "<Button-1>", on_click)
    UMLBox.test_canvas.tag_bind(rec, "<B1-Motion>", can_dragMotion)
    UMLBox.test_canvas.tag_bind(rec, "<ButtonRelease-1>", on_unclick)

#find the closest element to the click
def on_click(event):
    global crec
    crec = UMLBox.test_canvas.find_closest(event.x, event.y)
    #Save the current position of all boxes
    global saved
    saved = False
    global save
    pos = 0
    #Make all borders black
    clear_border()
    for i in UMLBox.class_list:
        if crec[0] in {i.rec, i.label, i.methodlabel, i.methodtext, i.fieldtext, i.fieldlabel}:
            label = i.label
            rec = i.rec
            break
        pos += 1
    #Update the current clicked rectangle to have a red outline
    UMLBox.test_canvas.itemconfig(rec, outline="red")
    #Save the current state of the canvas
    save = UMLSavepoint.UMLSavepoint("gui")

#line up vriables so that whatever you click on within
#a box results in the dragging of the box
def can_dragMotion(event):
    global moved
    moved = True
    #get the index in the class_list of the current rectangle being clicked
    pos = 0
    for i in UMLBox.class_list:
        if crec[0] in {i.rec, i.label, i.methodlabel, i.methodtext, i.fieldtext, i.fieldlabel}:
            label = i.label
            rec = i.rec
            break
        pos += 1

    #Bring all currently selected items from the clicked box to front of view#
    ViewChange.bring_front(rec)
    ViewChange.bring_front(label)
    ViewChange.bring_front(UMLBox.class_list[pos].fieldtext)
    ViewChange.bring_front(UMLBox.class_list[pos].fieldlabel)
    ViewChange.bring_front(UMLBox.class_list[pos].methodlabel)
    ViewChange.bring_front(UMLBox.class_list[pos].methodtext)

    #get coordinates and modify them to maintain the shape of the box as you move it around#
    new_x1 = event.x - 20 - UMLBox.class_list[pos].textspace
    new_y1 = event.y - 15 
    new_x2 = event.x + 60 + UMLBox.class_list[pos].textspace
    new_y2 = event.y + UMLBox.class_list[pos].yinc

    #Bind the new coordinates so that the square cannot go outside#
    #of the canvas#
    uml : UMLClass = class_dict[UMLBox.class_list[pos].name]
    if len(uml.fields) == 0:
        spacer = 20
    else:
        spacer = 10
    if(new_x2 > UMLBox.test_canvas.winfo_width()):
        new_x1 = UMLBox.test_canvas.winfo_width() - 80 - 2 * UMLBox.class_list[pos].textspace
        new_x2 = UMLBox.test_canvas.winfo_width()
    if(new_y2 > UMLBox.test_canvas.winfo_height()):
        new_y1 = UMLBox.test_canvas.winfo_height() - UMLBox.class_list[pos].yinc - 15 - spacer
        new_y2 = UMLBox.test_canvas.winfo_height()
    if(new_x1 < 0):
        new_x1 = 0
        new_x2 = 80 + 2 * UMLBox.class_list[pos].textspace 
    if(new_y1 < 0):
        new_y1 = 0
        new_y2 = 15 + UMLBox.class_list[pos].yinc

    #find the center of the box#
    x1, y1, x2, y2 = UMLBox.test_canvas.coords(UMLBox.class_list[pos].rec)
    center = ((x2 - x1) / 2) + x1

    #move the elements#
    ViewChange.set_rec(rec, new_x1, new_y1, new_x2, new_y2 + spacer)
    ViewChange.set_text(label, new_x1 + 40 + UMLBox.class_list[pos].textspace, new_y1 + 12)
    ViewChange.set_text(UMLBox.class_list[pos].fieldlabel, x1 + 25, new_y1 + 30)
    fx,fy = UMLBox.test_canvas.coords(UMLBox.class_list[pos].fieldlabel)
    ViewChange.set_text(UMLBox.class_list[pos].fieldtext, center, fy + 5)
    ViewChange.set_text(UMLBox.class_list[pos].methodlabel, x1 + 35, fy + spacer + 15 * len(uml.fields))
    mx,my = UMLBox.test_canvas.coords(UMLBox.class_list[pos].methodlabel)
    ViewChange.set_text(UMLBox.class_list[pos].methodtext, center, my + 10)

    #Move any lines connected to the box#
    if(len(UMLBox.class_list[pos].rels) > 0):
        for i in UMLBox.class_list[pos].rels:
            if i[0] == "source":
                x1, y1, x2, y2 = UMLBox.test_canvas.coords(i[1])
                ViewChange.set_line(i[1], new_x1, new_y1, x2, y2)
            if i[0] == "dest":
                x1, y1, x2, y2 = UMLBox.test_canvas.coords(i[1])
                ViewChange.set_line(i[1], x1, y1, new_x1, new_y1)

def on_unclick(event):
    #Add to the undo stack if the box moved
    if saved == False and moved == True:
        UMLSavepoint.undo_stack.put(save)
        UMLSavepoint.clear_stack()
    pos = 0
    for i in UMLBox.class_list:
        if crec[0] in {i.rec, i.label, i.methodlabel, i.methodtext, i.fieldtext, i.fieldlabel}:
            label = i.label
            rec = i.rec
            break
        pos += 1
    UMLBox.update_size(pos)

def clear_border():
    #Change all outlines to be black
    for i in UMLBox.class_list:
        UMLBox.test_canvas.itemconfig(i.rec, outline="black")
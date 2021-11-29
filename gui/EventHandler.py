# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     EventHandler.py

import tkinter as tk

from gui import UMLBox
from gui import ViewChange
from uml_components.interfaces import (attr_interface as ai,
                                       class_interface as ci,
                                       rel_interface as ri)
from uml_components import UMLClass
from . import UMLField
from . import UMLMethod
from . import UMLSavepoint
from . import gui_main

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
    canvas = event.widget
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    global crec
    crec = UMLBox.test_canvas.find_closest(x, y)
    #Save the current position of all boxes
    global saved
    saved = False
    global save
    pos = 0
    #Make all borders black
    clear_border()
    for i in UMLBox.class_list:
        if crec[0] in {i.rec, i.label, i.methodlabel, i.methodtext, i.fieldtext, i.fieldlabel, i.ftop, i.mtop}:
            label = i.label
            rec = i.rec
            break
        pos += 1
    #Save the current state of the canvas
    save = UMLSavepoint.UMLSavepoint("gui")
    ViewChange.bring_all_front(UMLBox.class_list[pos])

#line up vriables so that whatever you click on within
#a box results in the dragging of the box
def can_dragMotion(event):
    global moved
    moved = True
    #get the index in the class_list of the current rectangle being clicked
    pos = 0
    for i in UMLBox.class_list:
        if crec[0] in {i.rec, i.label, i.methodlabel, i.methodtext, i.fieldtext, i.fieldlabel, i.ftop, i.mtop}:
            label = i.label
            rec = i.rec
            break
        pos += 1

    #Bring all currently selected items from the clicked box to front of view#
    ViewChange.bring_all_front(UMLBox.class_list[pos])

    canvas = event.widget
    #Get the absolute coordinates of the canvas
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    #Get the absolute max width and height of the canvas
    cx = canvas.canvasx(canvas.winfo_width())
    cy = canvas.canvasy(canvas.winfo_height())
    #get coordinates and modify them to maintain the shape of the box as you move it around#
    new_x1 = x - 20 - UMLBox.class_list[pos].textspace
    new_y1 = y - 15 
    new_x2 = x + 60 + UMLBox.class_list[pos].textspace
    new_y2 = y + UMLBox.class_list[pos].yinc

    #Store some variables to account for if fields exist
    #These are used to add padding when necessary
    uml : UMLClass = UMLClass.class_dict[UMLBox.class_list[pos].name]
    if len(uml.fields) == 0:
        spacer = 20
        spacer2 = 0
    else:
        spacer = 10
        spacer2 = 15

    #If box is pulled right enough beyond the current view of the canvas, scroll right
    if new_x2 > cx - 1:
        #Check to see if pull is far enough, scroll if it is
        if new_x2 > cx + 50:
            UMLBox.test_canvas.xview_scroll(1, 'units')
            new_x1 = cx - 80 - 2 * UMLBox.class_list[pos].textspace + 71
            new_x2 = cx + 71
        #Otherwise confine the box to the right side of the view of the canvas
        else:
            new_x1 = cx - 80 - 2 * UMLBox.class_list[pos].textspace
            new_x2 = cx
        #Stop the box from going past the end of the canvas
        if new_x2 >= UMLBox.maxx - 1:
            UMLBox.update_global(1000, 0)
            UMLBox.test_canvas.config(scrollregion=(0,0,UMLBox.maxx,UMLBox.maxy))
        scroll_helper(rec, pos, new_x1, new_x2, new_y1, new_y2, spacer, label)

    #If box is pulled down enough beyond the current view of the canvas, scroll down
    if new_y2 > cy - 27 + spacer2*(2/3):
        #Check to see if pull is far enough, scroll if it is
        if new_y2 > cy + 75:
            UMLBox.test_canvas.yview_scroll(1, 'units')
            new_y1 = cy - UMLBox.class_list[pos].yinc - 42 + (spacer2*(2/3)) + 60
            new_y2 = cy - 27 + (spacer2*(2/3)) + 60
        #Otherwise confine the box to the bottom side of the view of the canvas
        else:
            new_y1 = cy - UMLBox.class_list[pos].yinc - 42 + (spacer2*(2/3))
            new_y2 = cy - 27 + (spacer2*(2/3))
        #Stop the box from going past the end of the canvas
        if new_y2 > UMLBox.maxy:
            UMLBox.update_global(0, 1000)
            UMLBox.test_canvas.config(scrollregion=(0,0,UMLBox.maxx,UMLBox.maxy))
        scroll_helper(rec, pos, new_x1, new_x2, new_y1, new_y2, spacer, label)

    #If box is pulled left enough beyond the current view of the canvas, scroll left
    if event.x < 20 + UMLBox.class_list[pos].textspace + 5:
        new_x1 = x - event.x + 5
        new_x2 = x - event.x + 2*UMLBox.class_list[pos].textspace + 80 + 5
        #Check to see if the pull is far enough, scroll if it is
        if event.x < 0:
            UMLBox.test_canvas.xview_scroll(-1, 'units')
            new_x1 -= 78
            new_x2 -= 78
        #Stop the box from going past the end of the canvas
        if x < 5:
            new_x1 = canvas.canvasx(5)
            new_x2 = canvas.canvasx(5) + 2*UMLBox.class_list[pos].textspace + 80
        scroll_helper(rec, pos, new_x1, new_x2, new_y1, new_y2, spacer, label)

    #If box is pulled up enough beyond the current view of the canvas, scroll up    
    if event.y < 20:
        new_y1 = y - event.y + 5
        new_y2 = y - event.y + UMLBox.class_list[pos].yinc + 15 + 5
        #Check to see if the pull is far enough, scroll if it is
        if event.y < -10:
            UMLBox.test_canvas.yview_scroll(-1, 'units')
            new_y1 -= 60
            new_y2 -= 60
        #Stop the box from going past the end of the canvas
        if canvas.canvasy(event.y) <= canvas.canvasy(5):
            new_y1 = canvas.canvasy(5)
            new_y2 = canvas.canvasy(5) + 15 + UMLBox.class_list[pos].yinc
        scroll_helper(rec, pos, new_x1, new_x2, new_y1, new_y2, spacer, label)

    #find the center of the box#
    x1, y1, x2, y2 = UMLBox.test_canvas.coords(UMLBox.class_list[pos].rec)
    center = ((x2 - x1) / 2) + x1

    #move the elements#
    ViewChange.set_rec(rec, new_x1, new_y1, new_x2, new_y2 + spacer - 5)
    ViewChange.set_text(label, new_x1 + 40 + UMLBox.class_list[pos].textspace, new_y1 + 12)
    ViewChange.set_line(UMLBox.class_list[pos].ftop, new_x1, new_y1 + 22, new_x2, new_y1 + 22)
    ViewChange.set_text(UMLBox.class_list[pos].fieldlabel, x1 + 25, new_y1 + 30)
    fx,fy = UMLBox.test_canvas.coords(UMLBox.class_list[pos].fieldlabel)
    ViewChange.set_text(UMLBox.class_list[pos].fieldtext, x1 + 22, fy + 10)
    ViewChange.set_text(UMLBox.class_list[pos].methodlabel, x1 + 35, fy + 10 + spacer + 15 * len(uml.fields))
    mx,my = UMLBox.test_canvas.coords(UMLBox.class_list[pos].methodlabel)
    ViewChange.set_line(UMLBox.class_list[pos].mtop, new_x1, my - 8, new_x2, my - 8)
    ViewChange.set_text(UMLBox.class_list[pos].methodtext, new_x1 + 22, my + 10)

    #Move any lines connected to the box#
    if(len(UMLBox.class_list[pos].rels) > 0):
        for i in UMLBox.class_list[pos].rels:
            if i[0] == "source":
                x1, y1, x2, y2 = UMLBox.test_canvas.coords(i[1])

                b1x1, b1y1, b1x2, b1y2 = UMLBox.get_coords(UMLBox.class_list[pos].name)
                b2x1, b2y1, b2x2, b2y2 = UMLBox.test_canvas.coords(i[2])

                #Get the center for the source and destination boxes
                lx1 = b1x1 + abs(b1x1-b1x2)/2
                lx2 = b2x1 + abs(b2x1-b2x2)/2
                ly1 = b1y1 + abs(b1y1-b1y2)/2
                ly2 = b2y1 + abs(b2y1-b2y2)/2

                #Move sequence for the diamonds
                if len(UMLBox.test_canvas.coords(i[3])) == 8:
                    if lx2 > lx1:
                        #Move the diamond to the top
                        if b2y2 <= b1y1:
                            UMLBox.test_canvas.coords(i[3], lx1, b1y1, lx1 - 10, 
                                b1y1 - 10, lx1, b1y1 - 20, x1 + 10, b1y1 - 10)
                            ly1 = b1y1 - 20
                        #Move the diamond to the bottom
                        elif b2y1 >= b1y2:
                            UMLBox.test_canvas.coords(i[3], lx1, b1y2, lx1 - 10, 
                                b1y2 + 10, lx1, b1y2 + 20, lx1 + 10, b1y2 + 10)
                            ly1 = b1y2 + 20
                        #Move the diamond to the right
                        else:
                            UMLBox.test_canvas.coords(i[3], b1x2, ly1, b1x2 + 10, 
                                ly1 - 10, b1x2 + 20, ly1, b1x2 + 10, ly1 + 10)
                            lx1 = b1x2 + 20
                    else:
                        #Move the diamond to the top
                        if b2y2 <= b1y1:
                            UMLBox.test_canvas.coords(i[3], lx1, b1y1, lx1 - 10, 
                                b1y1 - 10, lx1, b1y1 - 20, lx1 + 10, b1y1 - 10)
                            ly1 = b1y1 - 20
                        #Move the diamond to the bottom
                        elif b2y1 >= b1y2:
                            UMLBox.test_canvas.coords(i[3], lx1, b1y2, lx1 - 10, 
                                b1y2 + 10, lx1, b1y2 + 20, lx1 + 10, b1y2 + 10)
                            ly1 = b1y2 + 20
                        #Move the diamond to the left
                        else:
                            UMLBox.test_canvas.coords(i[3], b1x1, ly1, b1x1 - 10, 
                                ly1 - 10, b1x1 - 20, ly1, b1x1 - 10, ly1 + 10)
                            lx1 = b1x1 - 20
                #Move sequence for the triangles
                else:
                    if lx2 > lx1:
                        #Move the triangle to the top
                        if b2y2 <= b1y1:
                            UMLBox.test_canvas.coords(i[3], lx1, b1y1, lx1 - 10, 
                                b1y1 - 20, lx1 + 10, b1y1 - 20)
                            ly1 = b1y1 - 20
                        #Move the triangle to the bottom
                        elif b2y1 >= b1y2:
                            UMLBox.test_canvas.coords(i[3], lx1, b1y2, lx1 - 10, 
                                b1y2 + 20, lx1 + 10, b1y2 + 20)
                            ly1 = b1y2 + 20
                        #Move the triangle to the right
                        else:
                            UMLBox.test_canvas.coords(i[3], b1x2, ly1, b1x2 + 20, 
                                ly1 - 10, b1x2 + 20, ly1 + 10)
                            lx1 = b1x2 + 20
                    else:
                        #Move the triangle to the top
                        if b2y2 <= b1y1:
                            UMLBox.test_canvas.coords(i[3], lx1, b1y1, lx1 - 10, 
                                b1y1 - 20, lx1 + 10, b1y1 - 20)
                            ly1 = b1y1 - 20
                        #Move the triangle to the bottom
                        elif b2y1 >= b1y2:
                            UMLBox.test_canvas.coords(i[3], lx1, b1y2, lx1 - 10, 
                                b1y2 + 20, lx1 + 10, b1y2 + 20)
                            ly1 = b1y2 + 20
                        #Move the triangle to the left
                        else:
                            UMLBox.test_canvas.coords(i[3], b1x1, ly1, b1x1 - 20, 
                                ly1 - 10, b1x1 - 20, ly1 + 10)
                            lx1 = b1x1 - 20
                ViewChange.set_line(i[1], lx1, ly1, lx2, ly2)
            if i[0] == "dest":
                x1, y1, x2, y2 = UMLBox.test_canvas.coords(i[1])
                b2x1, b2y1, b2x2, b2y2 = UMLBox.get_coords(UMLBox.class_list[pos].name)
                b1x1, b1y1, b1x2, b1y2 = UMLBox.test_canvas.coords(i[2])

                lx1 = b1x1 + abs(b1x1-b1x2)/2
                lx2 = b2x1 + abs(b2x1-b2x2)/2
                ly1 = b1y1 + abs(b1y1-b1y2)/2
                ly2 = b2y1 + abs(b2y1-b2y2)/2

                #Move sequence for the diamond
                if len(UMLBox.test_canvas.coords(i[3])) == 8:
                    if lx2 > lx1:
                        #Move the diamond to the top
                        if b2y2 <= b1y1:
                            UMLBox.test_canvas.coords(i[3], lx1, b1y1, lx1 - 10, 
                                b1y1 - 10, lx1, b1y1 - 20, lx1 + 10, b1y1 - 10)
                            ly1 = b1y1 - 20
                        #Move the diamond to the bottom
                        elif b2y1 >= b1y2:
                            UMLBox.test_canvas.coords(i[3], lx1, b1y2, lx1 - 10, 
                                b1y2 + 10, lx1, b1y2 + 20, lx1 + 10, b1y2 + 10)
                            ly1 = b1y2 + 20
                        #Move the diamond to the right
                        else:
                            UMLBox.test_canvas.coords(i[3], b1x2, ly1, b1x2 + 10, 
                                ly1 - 10, b1x2 + 20, ly1, b1x2 + 10, ly1 + 10)
                            lx1 = b1x2 + 20
                    else:
                        #Move the diamond to the top
                        if b2y2 <= b1y1:
                            UMLBox.test_canvas.coords(i[3], lx1, b1y1, lx1 - 10, 
                                b1y1 - 10, lx1, b1y1 - 20, lx1 + 10, b1y1 - 10)
                            ly1 = b1y1 - 20
                        #Move the diamond to the botttom
                        elif b2y1 >= b1y2:
                            UMLBox.test_canvas.coords(i[3], lx1, b1y2, lx1 - 10, 
                                b1y2 + 10, lx1, b1y2 + 20, lx1 + 10, b1y2 + 10)
                            ly1 = b1y2 + 20
                        #Move the diamond to the left
                        else:
                            UMLBox.test_canvas.coords(i[3], b1x1, ly1, b1x1 - 10, 
                                ly1 - 10, b1x1 - 20, ly1, b1x1 - 10, ly1 + 10)
                            lx1 = b1x1 - 20
                #Move sequence for the triangle
                else:
                    if lx2 > lx1:
                        #Move the triangle to the top
                        if b2y2 <= b1y1:
                            UMLBox.test_canvas.coords(i[3], lx1, b1y1, lx1 - 10, 
                                b1y1 - 20, lx1 + 10, b1y1 - 20)
                            ly1 = b1y1 - 20
                        #Move the triangle to the bottom
                        elif b2y1 >= b1y2:
                            UMLBox.test_canvas.coords(i[3], lx1, b1y2, lx1 - 10, 
                                b1y2 + 20, lx1 + 10, b1y2 + 20)
                            ly1 = b1y2 + 20
                        #Move the triangle to the right
                        else:
                            UMLBox.test_canvas.coords(i[3], b1x2, ly1, b1x2 + 20, 
                                ly1 - 10, b1x2 + 20, ly1 + 10)
                            lx1 = b1x2 + 20
                    else:
                        #Move the triangle to the bottom
                        if b2y2 <= b1y1:
                            UMLBox.test_canvas.coords(i[3], lx1, b1y1, lx1 - 10, 
                                b1y1 - 20, lx1 + 10, b1y1 - 20)
                            ly1 = b1y1 - 20
                        #Move the triangle to the top
                        elif b2y1 >= b1y2:
                            UMLBox.test_canvas.coords(i[3], lx1, b1y2, lx1 - 10, 
                                b1y2 + 20, lx1 + 10, b1y2 + 20)
                            ly1 = b1y2 + 20
                        #Move the triangle to the left
                        else:
                            UMLBox.test_canvas.coords(i[3], b1x1, ly1, b1x1 - 20, 
                                ly1 - 10, b1x1 - 20, ly1 + 10)
                            lx1 = b1x1 - 20
                ViewChange.set_line(i[1], lx2, ly2, lx1, ly1)

def on_unclick(event):
    #Add to the undo stack if the box moved
    if saved == False and moved == True:
        UMLSavepoint.undo_stack.put(save)
        UMLSavepoint.clear_stack()
        set_moved()
    pos = 0
    for i in UMLBox.class_list:
        if crec[0] in {i.rec, i.label, i.methodlabel, i.methodtext, i.fieldtext, i.fieldlabel}:
            label = i.label
            rec = i.rec
            break
        pos += 1
    UMLBox.update_size(pos)
    UMLField.update_vertical(pos)
    x, y = UMLBox.get_xy(UMLBox.class_list[pos].name)
    UMLClass.class_dict[UMLBox.class_list[pos].name].position_x = x
    UMLClass.class_dict[UMLBox.class_list[pos].name].position_y = y

def clear_border():
    #Change all outlines to be black
    for i in UMLBox.class_list:
        UMLBox.test_canvas.itemconfig(i.rec, outline="black")

def set_moved():
    global moved
    moved = False

#This function helps to maintain the shape of the UMLBox object and its contents.
def scroll_helper(rec, pos, new_x1, new_x2, new_y1, new_y2, spacer, label):
    #Account for presence of UMLFields
    #These are used later to add padding
    uml : UMLClass = UMLClass.class_dict[UMLBox.class_list[pos].name]
    if len(uml.fields) == 0:
        spacer = 20
    else:
        spacer = 10

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

def crop():
    if UMLBox.class_list != []:
        bounds = UMLBox.test_canvas.bbox("all")
        UMLBox.test_canvas.config(scrollregion=(0,0,bounds[2],bounds[3]))
        xinc = bounds[2] - UMLBox.maxx
        yinc = bounds[3] - UMLBox.maxy
        UMLBox.update_global(xinc, yinc)
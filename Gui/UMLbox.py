import tkinter as tk
from UMLline import delete_line
import EventHandler
import ViewChange

class_list = []

def setCanvas(canvas):
    global DndCanvas
    DndCanvas = canvas

def find_pos_from_name(name):
    pos = 0
    while pos < len(class_list):
        if class_list[pos][0] == name:
            return pos
        pos += 1

class UMLsquare():

    #tracker keeps the circles from being created on top of each other
    #create a new oval on the graph and enable movement
    #add each new circle to the list in a tuple consisting of
    #(name, creat_oval return, create_text return)

    tracker = 0
    x1 = 40
    x2 = 120
    y1 = 40
    y2 = 65
    def __init__(self, canvas, x1 : int, y1 : int, x2 : int, y2 : int, name : str):
        label = canvas.create_text(x1 + 40, y1 + 12, text = name, state=tk.DISABLED, tags=name)
        textspace = 2.5 * len(name)
        rec = canvas.create_rectangle(x1 - textspace, y1, x2 + textspace, y2 + 15, fill="red", tags=name)
        fieldlabel = canvas.create_text(x1 + 10, y1 + 30, text = "Field(s):", state=tk.DISABLED)
        fieldtext = canvas.create_text(x1 + 30, y1 + 25, text = "", state=tk.HIDDEN, anchor=tk.N)
        yincrement = 15
        DndCanvas.tag_lower(rec)
        class_list.append([name, rec, label, textspace, [], fieldtext, [], yincrement, fieldlabel])
        EventHandler.can_drag(rec)
    
        
def create_class(canvas, name : str):
    UMLsquare(canvas, UMLsquare.x1, UMLsquare.y1, UMLsquare.x2, UMLsquare.y2, name)
    if(UMLsquare.tracker % 2 == 0):
        UMLsquare.x1 += 300
        UMLsquare.x2 += 300
    else:
        UMLsquare.x1 -= 300
        UMLsquare.x2 -= 300
        UMLsquare.y1 += 300
        UMLsquare.y2 += 300
    UMLsquare.tracker += 1

#Remove the circle with the text = name
def delete_circle(name : str):
    pos = find_pos_from_name(name)
    subpos = 0
    while subpos < len(class_list[pos][4]):
        if(class_list[pos][4][subpos][0] == "source"):
            delete_line(DndCanvas, class_list[pos][1], class_list[pos][4][subpos][2])
            subpos -= 1
        else:
            delete_line(DndCanvas, class_list[pos][4][subpos][2], class_list[pos][1])
            subpos -= 1
        subpos += 1
    ViewChange.del_item(class_list[pos][5])
    ViewChange.del_item(class_list[pos][8])
    class_list.pop(pos)
    ViewChange.del_item(name)
    print(class_list)

def rename_circle(oldname : str, newname : str):
    pos = 0
    #Find the position of the circle with the old name
    while pos < len(class_list):
        if oldname == class_list[pos][0]:
            #save the circle and text values
            x1,y1,x2,y2 = DndCanvas.coords(class_list[pos][1])
            class_list[pos][0] = newname
            class_list[pos][3] = len(newname) * 2.5
            DndCanvas.coords(class_list[pos][1], x1 - len(newname) * 2.5, y1, x2 + len(newname) * 2.5, y2)
            break
        else:
            pos += 1
    #Change the text of the circle to the updated name
    ViewChange.item_config(class_list[pos][2], newname, None, None)
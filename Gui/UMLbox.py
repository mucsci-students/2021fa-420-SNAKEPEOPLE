import tkinter as tk
from UMLline import delete_line

circle_list = []

def setCanvas(canvas):
    global DndCanvas
    DndCanvas = canvas

def find_pos_from_name(name):
    pos = 0
    while pos < len(circle_list):
        if circle_list[pos][0] == name:
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
        circle_list.append([name, rec, label, textspace, [], fieldtext, [], yincrement, fieldlabel])
        can_drag(rec)
    
        
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

#bind clicking and dragging to functions
def can_drag(rec):
    DndCanvas.tag_bind(rec, "<Button-1>", on_click)
    DndCanvas.tag_bind(rec, "<B1-Motion>", can_dragMotion)

#find the closest element to the click
def on_click(event):
    global crec
    crec = DndCanvas.find_closest(event.x, event.y)

#line up variables so that circle equals the circle element
#and label refers to the text element within the circle
#Bring current circle to front
def can_dragMotion(event):
    pos = 0
    while pos < len(circle_list):
        if crec[0] in circle_list[pos]:
            label = circle_list[pos][2]
            circle = circle_list[pos][1]
            break
        pos += 1

    DndCanvas.tag_raise(circle)
    DndCanvas.tag_raise(label)
    DndCanvas.tag_raise(circle_list[pos][5])
    DndCanvas.tag_raise(circle_list[pos][8])
    x1, y1, x2, y2 = DndCanvas.coords(circle_list[pos][1])
    new_x1 = event.x - 20 - circle_list[pos][3]
    new_y1 = event.y - 15 
    new_x2 = event.x + 60 + circle_list[pos][3]
    new_y2 = event.y + 10 + circle_list[pos][7]

    #Bind the new coordinates so that the circle cannot go outside
    #of the canvas
    if(new_x2 > DndCanvas.winfo_width()):
        new_x1 = DndCanvas.winfo_width() - 80 - 2.5 * circle_list[pos][3]
        new_x2 = DndCanvas.winfo_width()
    if(new_y2 > DndCanvas.winfo_height()):
        new_y1 = DndCanvas.winfo_height() - 25
        new_y2 = DndCanvas.winfo_height()
    if(new_x1 < 0):
        new_x1 = 0
        new_x2 = 80 + 2 * circle_list[pos][3]
    if(new_y1 < 0):
        new_y1 = 0
        new_y2 = 25


    #move the elements
    DndCanvas.coords(circle, new_x1, new_y1, new_x2, new_y2)
    DndCanvas.coords(label, new_x1 + 40 + circle_list[pos][3], new_y1 + 12.5)
    DndCanvas.coords(circle_list[pos][8], new_x1 + circle_list[pos][3] + 10, new_y1 + 30)
    DndCanvas.coords(circle_list[pos][5], new_x1 + circle_list[pos][3] + 30, new_y1 + 25)
    if(len(circle_list[pos][4]) > 0):
        for i in circle_list[pos][4]:
            if i[0] == "source":
                x1, y1, x2, y2 = DndCanvas.coords(i[1])
                DndCanvas.coords(i[1], new_x1 + 40 + circle_list[pos][3], new_y1 + 12.5, x2, y2)
            if i[0] == "dest":
                x1, y1, x2, y2 = DndCanvas.coords(i[1])
                DndCanvas.coords(i[1], x1, y1, new_x2 - 95 - circle_list[pos][3], new_y2 - 25)

#Remove the circle with the text = name
def delete_circle(name : str):
    pos = find_pos_from_name(name)
    subpos = 0
    while subpos < len(circle_list[pos][4]):
        if(circle_list[pos][4][subpos][0] == "source"):
            delete_line(DndCanvas, circle_list[pos][1], circle_list[pos][4][subpos][2])
            subpos -= 1
        else:
            delete_line(DndCanvas, circle_list[pos][4][subpos][2], circle_list[pos][1])
            subpos -= 1
        subpos += 1
    DndCanvas.delete(circle_list[pos][5])
    DndCanvas.delete(circle_list[pos][8])
    circle_list.pop(pos)
    DndCanvas.delete(name)
    print(circle_list)

def rename_circle(oldname : str, newname : str):
    pos = 0
    #Find the position of the circle with the old name
    while pos < len(circle_list):
        if oldname == circle_list[pos][0]:
            #save the circle and text values
            x1,y1,x2,y2 = DndCanvas.coords(circle_list[pos][1])
            circle_list[pos][0] = newname
            circle_list[pos][3] = len(newname) * 2.5
            DndCanvas.coords(circle_list[pos][1], x1 - len(newname) * 2.5, y1, x2 + len(newname) * 2.5, y2)
            break
        else:
            pos += 1
    #Change the text of the circle to the updated name
    DndCanvas.itemconfigure(circle_list[pos][2], text = newname)
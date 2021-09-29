import tkinter as tk

square_list = []

def setCanvas(canvas):
    global DndCanvas
    DndCanvas = canvas

class UMLsquare():

    tracker = 0
    x1 = 20
    x2 = 70
    y1 = 20
    y2 = 70
    def __init__(self, canvas, x1, y1, x2, y2, name):
        rec = canvas.create_oval(x1, y1, x2, y2, fill="red")
        label = canvas.create_text(x1 + 25, y1 + 25, text = name, state=tk.DISABLED)
        square_list.append((name, rec, label))
        can_drag(rec)
    
        
def create_class(canvas, name):
    UMLsquare(canvas, UMLsquare.x1, UMLsquare.y1, UMLsquare.x2, UMLsquare.y2, name)
    if(UMLsquare.tracker % 2 == 0):
        UMLsquare.x1 += 100
        UMLsquare.x2 += 100
    else:
        UMLsquare.x1 -= 100
        UMLsquare.x2 -= 100
        UMLsquare.y1 += 100
        UMLsquare.y2 += 100
    UMLsquare.tracker += 1

def can_drag(rec):
    DndCanvas.tag_bind(rec, "<Button-1>", on_click)
    DndCanvas.tag_bind(rec, "<B1-Motion>", can_dragMotion)

def on_click(event):
    global crec
    crec = DndCanvas.find_closest(event.x, event.y)

def findpos(crec):
    i = 0
    while i < len(square_list):
        if crec[0] in square_list[i]:
            return i
        else:
            i += 1

def can_dragMotion(event):
    pos = findpos(crec)
    if(DndCanvas.type(crec) == "oval"):
        circle = crec
        label = square_list[pos][2]
    elif(DndCanvas.type(crec) == "text"):
        label = crec
        circle = square_list[pos][1]     
    new_x1 = event.x - 25
    new_y1 = event.y - 25
    new_x2 = event.x + 25
    new_y2 = event.y + 25
    if(new_x2 > DndCanvas.winfo_width()):
        new_x1 = DndCanvas.winfo_width() - 50
        new_x2 = DndCanvas.winfo_width()
    if(new_y2 > DndCanvas.winfo_height()):
        new_y1 = DndCanvas.winfo_height() - 50
        new_y2 = DndCanvas.winfo_height()
    if(new_x1 < 0):
        new_x1 = 0
        new_x2 = 50
    if(new_y1 < 0):
        new_y1 = 0
        new_y2 = 50
    DndCanvas.coords(circle, new_x1, new_y1, new_x2, new_y2)
    DndCanvas.coords(label, new_x1 + 25, new_y1 + 25)
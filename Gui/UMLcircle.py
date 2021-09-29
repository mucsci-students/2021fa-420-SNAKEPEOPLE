import tkinter as tk

circle_list = []

def setCanvas(canvas):
    global DndCanvas
    DndCanvas = canvas

class UMLsquare():

    #tracker keeps the circles from being created on top of each other
    #create a new oval on the graph and enable movement
    #add each new circle to the list in a tuple consisting of
    #(name, creat_oval return, create_text return)

    tracker = 0
    x1 = 20
    x2 = 70
    y1 = 20
    y2 = 70
    def __init__(self, canvas, x1, y1, x2, y2, name):
        rec = canvas.create_oval(x1, y1, x2, y2, fill="red")
        label = canvas.create_text(x1 + 25, y1 + 25, text = name, state=tk.DISABLED)
        circle_list.append((name, rec, label))
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

#bind clicking on an object to collect what element was clicked
def can_drag(rec):
    DndCanvas.tag_bind(rec, "<Button-1>", on_click)
    DndCanvas.tag_bind(rec, "<B1-Motion>", can_dragMotion)

#find the closest element to the click
def on_click(event):
    global crec
    crec = DndCanvas.find_closest(event.x, event.y)

#find the position within the circle list of the found element
def findpos():
    i = 0
    while i < len(circle_list):
        if crec[0] in circle_list[i]:
            return i
        else:
            i += 1

#line up variables so that circle equals the circle element
#and label refers to the text element within the circle
def can_dragMotion(event):
    pos = findpos()
    if(DndCanvas.type(crec) == "oval"):
        circle = crec
        label = circle_list[pos][2]
    elif(DndCanvas.type(crec) == "text"):
        label = crec
        circle = circle_list[pos][1]     
    new_x1 = event.x - 25
    new_y1 = event.y - 25
    new_x2 = event.x + 25
    new_y2 = event.y + 25

    #Bind the new coordinates so that the circle cannot go outside
    #of the canvas
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

    #move the elements
    DndCanvas.coords(circle, new_x1, new_y1, new_x2, new_y2)
    DndCanvas.coords(label, new_x1 + 25, new_y1 + 25)
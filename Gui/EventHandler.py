import UMLbox
import ViewChange
#bind clicking and dragging to functions
def can_drag(rec):
    UMLbox.DndCanvas.tag_bind(rec, "<Button-1>", on_click)
    UMLbox.DndCanvas.tag_bind(rec, "<B1-Motion>", can_dragMotion)

#find the closest element to the click
def on_click(event):
    global crec
    crec = UMLbox.DndCanvas.find_closest(event.x, event.y)

#line up variables so that circle equals the circle element
#and label refers to the text element within the circle
#Bring current circle to front
def can_dragMotion(event):
    pos = 0
    while pos < len(UMLbox.class_list):
        if crec[0] in UMLbox.class_list[pos]:
            label = UMLbox.class_list[pos][2]
            circle = UMLbox.class_list[pos][1]
            break
        pos += 1

    ViewChange.bring_front(circle)
    ViewChange.bring_front(label)
    ViewChange.bring_front(UMLbox.class_list[pos][5])
    ViewChange.bring_front(UMLbox.class_list[pos][8])
    x1, y1, x2, y2 = UMLbox.DndCanvas.coords(UMLbox.class_list[pos][1])
    new_x1 = event.x - 20 - UMLbox.class_list[pos][3]
    new_y1 = event.y - 15 
    new_x2 = event.x + 60 + UMLbox.class_list[pos][3]
    new_y2 = event.y + 10 + UMLbox.class_list[pos][7]

    #Bind the new coordinates so that the circle cannot go outside
    #of the canvas
    if(new_x2 > UMLbox.DndCanvas.winfo_width()):
        new_x1 = UMLbox.DndCanvas.winfo_width() - 75 - 2.5 * UMLbox.class_list[pos][3]
        new_x2 = UMLbox.DndCanvas.winfo_width()
    if(new_y2 > UMLbox.DndCanvas.winfo_height()):
        new_y1 = UMLbox.DndCanvas.winfo_height() - 25 - UMLbox.class_list[pos][7]
        new_y2 = UMLbox.DndCanvas.winfo_height()
    if(new_x1 < 0):
        new_x1 = 0
        new_x2 = 80 + 2 * UMLbox.class_list[pos][3]
    if(new_y1 < 0):
        new_y1 = 0
        new_y2 = 25 + UMLbox.class_list[pos][7]


    #move the elements
    ViewChange.set_rec(circle, new_x1, new_y1, new_x2, new_y2)
    ViewChange.set_text(label, new_x1 + 40 + UMLbox.class_list[pos][3], new_y1 + 12.5)
    ViewChange.set_text(UMLbox.class_list[pos][8], new_x1 + UMLbox.class_list[pos][3] + 10, new_y1 + 30)
    ViewChange.set_text(UMLbox.class_list[pos][5], new_x1 + UMLbox.class_list[pos][3] + 30, new_y1 + 25)
    if(len(UMLbox.class_list[pos][4]) > 0):
        for i in UMLbox.class_list[pos][4]:
            if i[0] == "source":
                x1, y1, x2, y2 = UMLbox.DndCanvas.coords(i[1])
                ViewChange.set_line(i[1], new_x1 + 40 + UMLbox.class_list[pos][3], new_y1 + 12.5, x2, y2)
            if i[0] == "dest":
                x1, y1, x2, y2 = UMLbox.DndCanvas.coords(i[1])
                ViewChange.set_line(i[1], x1, y1, new_x2 - 95 - UMLbox.class_list[pos][3], new_y2 - 25)

import UMLBox
import ViewChange

#bind clicking and dragging to functions
def can_drag(rec):
    UMLBox.canvas.tag_bind(rec, "<Button-1>", on_click)
    UMLBox.canvas.tag_bind(rec, "<B1-Motion>", can_dragMotion)

#find the closest element to the click
def on_click(event):
    global crec
    crec = UMLBox.canvas.find_closest(event.x, event.y)

"""line up vriables so that whatever you click on within
    a box results in the dragging of the box"""
def can_dragMotion(event):
    """get the index in the class_list of the current rectangle being clicked"""
    pos = 0
    while pos < len(UMLBox.class_list):
        if crec[0] in UMLBox.class_list[pos]:
            label = UMLBox.class_list[pos][2]
            circle = UMLBox.class_list[pos][1]
            break
        pos += 1

    """Bring all currently selected items from the clicked box to front of view"""
    ViewChange.bring_front(circle)
    ViewChange.bring_front(label)
    ViewChange.bring_front(UMLBox.class_list[pos][5])
    ViewChange.bring_front(UMLBox.class_list[pos][8])
    ViewChange.bring_front(UMLBox.class_list[pos][9])
    ViewChange.bring_front(UMLBox.class_list[pos][10])

    """get coordinates and modify them to maintain the shape of the box as you move it around"""
    x1, y1, x2, y2 = UMLBox.canvas.coords(UMLBox.class_list[pos][1])
    new_x1 = event.x - 20 - UMLBox.class_list[pos][3]
    new_y1 = event.y - 15 
    new_x2 = event.x + 60 + UMLBox.class_list[pos][3]
    new_y2 = event.y + 20 + UMLBox.class_list[pos][7] + UMLBox.class_list[pos][12]

    """Bind the new coordinates so that the square cannot go outside
    of the canvas"""
    if(new_x2 > UMLBox.canvas.winfo_width()):
        new_x1 = UMLBox.canvas.winfo_width() - 80 - 2 * UMLBox.class_list[pos][3]
        new_x2 = UMLBox.canvas.winfo_width()
    if(new_y2 > UMLBox.canvas.winfo_height()):
        new_y1 = UMLBox.canvas.winfo_height() - 35 - UMLBox.class_list[pos][7] - UMLBox.class_list[pos][12]
        new_y2 = UMLBox.canvas.winfo_height()
    if(new_x1 < 0):
        new_x1 = 0
        new_x2 = 80 + 2 * UMLBox.class_list[pos][3] 
    if(new_y1 < 0):
        new_y1 = 0
        new_y2 = 35 + UMLBox.class_list[pos][7] + UMLBox.class_list[pos][12]

    """find the center of the box"""
    center = ((x2 - x1) / 2) + x1

    """move the elements"""
    ViewChange.set_rec(circle, new_x1, new_y1, new_x2, new_y2)
    ViewChange.set_text(label, new_x1 + 40 + UMLBox.class_list[pos][3], new_y1 + 12.5)
    ViewChange.set_text(UMLBox.class_list[pos][8], new_x1 + 25, new_y1 + 30)
    ViewChange.set_text(UMLBox.class_list[pos][5], new_x1 + UMLBox.class_list[pos][3] + 40, new_y1 + 25)
    ViewChange.set_text(UMLBox.class_list[pos][9], new_x1 + 35, new_y2 - 15 - UMLBox.class_list[pos][12])
    ViewChange.set_text(UMLBox.class_list[pos][10], center, new_y2 - 5 - UMLBox.class_list[pos][12])


    if(len(UMLBox.class_list[pos][4]) > 0):
        for i in UMLBox.class_list[pos][4]:
            if i[0] == "source":
                x1, y1, x2, y2 = UMLBox.canvas.coords(i[1])
                ViewChange.set_line(i[1], new_x1 + 40 + UMLBox.class_list[pos][3], new_y1 + 12.5, x2, y2)
            if i[0] == "dest":
                x1, y1, x2, y2 = UMLBox.canvas.coords(i[1])
                ViewChange.set_line(i[1], x1, y1, new_x2 + 15 - 3 * UMLBox.class_list[pos][3], new_y2 - 20 - UMLBox.class_list[pos][7] - UMLBox.class_list[pos][12])
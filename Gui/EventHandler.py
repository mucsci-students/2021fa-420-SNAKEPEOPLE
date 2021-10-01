import UMLbox
import ViewChange
#bind clicking and dragging to functions
def can_drag(rec):
    UMLbox.canvas.tag_bind(rec, "<Button-1>", on_click)
    UMLbox.canvas.tag_bind(rec, "<B1-Motion>", can_dragMotion)

#find the closest element to the click
def on_click(event):
    global crec
    crec = UMLbox.canvas.find_closest(event.x, event.y)

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
    ViewChange.bring_front(UMLbox.class_list[pos][9])
    ViewChange.bring_front(UMLbox.class_list[pos][10])
    x1, y1, x2, y2 = UMLbox.canvas.coords(UMLbox.class_list[pos][1])
    new_x1 = event.x - 20 - UMLbox.class_list[pos][3]
    new_y1 = event.y - 15 
    new_x2 = event.x + 60 + UMLbox.class_list[pos][3]
    new_y2 = event.y + 20 + UMLbox.class_list[pos][7] + UMLbox.class_list[pos][12]
    #Bind the new coordinates so that the circle cannot go outside
    #of the canvas
    if(new_x2 > UMLbox.canvas.winfo_width()):
        new_x1 = UMLbox.canvas.winfo_width() - 75 - 2.5 * UMLbox.class_list[pos][3]
        new_x2 = UMLbox.canvas.winfo_width()
    if(new_y2 > UMLbox.canvas.winfo_height()):
        new_y1 = UMLbox.canvas.winfo_height() - 25 - UMLbox.class_list[pos][7] - UMLbox.class_list[pos][12]
        new_y2 = UMLbox.canvas.winfo_height()
    if(new_x1 < 0):
        new_x1 = 0
        new_x2 = 80 + 2 * UMLbox.class_list[pos][3]
    if(new_y1 < 0):
        new_y1 = 0
        new_y2 = 25 + UMLbox.class_list[pos][7] + UMLbox.class_list[pos][12]

    p1,l1,p2,l2 = UMLbox.canvas.coords(UMLbox.class_list[pos][1])
    center = ((x2 - x1) / 2) + x1
    #move the elements
    ViewChange.set_rec(circle, new_x1, new_y1, new_x2, new_y2)
    ViewChange.set_text(label, new_x1 + 40 + UMLbox.class_list[pos][3], new_y1 + 12.5)
    ViewChange.set_text(UMLbox.class_list[pos][8], new_x1 + 25, new_y1 + 30)
    ViewChange.set_text(UMLbox.class_list[pos][5], new_x1 + UMLbox.class_list[pos][3] + 40, new_y1 + 25)
    ViewChange.set_text(UMLbox.class_list[pos][9], new_x1 + 35, new_y2 - 15 - UMLbox.class_list[pos][12])
    ViewChange.set_text(UMLbox.class_list[pos][10], center, new_y2 - 5 - UMLbox.class_list[pos][12])
    if(len(UMLbox.class_list[pos][4]) > 0):
        for i in UMLbox.class_list[pos][4]:
            if i[0] == "source":
                x1, y1, x2, y2 = UMLbox.canvas.coords(i[1])
                ViewChange.set_line(i[1], new_x1 + 40 + UMLbox.class_list[pos][3], new_y1 + 12.5, x2, y2)
            if i[0] == "dest":
                x1, y1, x2, y2 = UMLbox.canvas.coords(i[1])
                ViewChange.set_line(i[1], x1, y1, new_x2 - 95 - UMLbox.class_list[pos][3], new_y2 - 25)
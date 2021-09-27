import tkinter as tk

#Bind button click and drag to actions
def add_drag(widget):
    widget.bind("<Button-1>", start_drag)
    widget.bind("<B1-Motion>", drag_motion)

#Find the position of the widget when you click on it
def start_drag(event):
    widget = event.widget
    widget.startx = event.x
    widget.starty = event.y

#Move the position of the widget with the cursor, but keep it within the frame
def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startx + event.x - 202
    y = widget.winfo_y() - widget.starty + event.y - 218
    if(x > 200):
        x = 200
    if(x < -205):
        x = -205
    if(y > 200):
        y = 200
    if(y < -210):
        y = -210
    widget.place(x = x, y = y)

# label = tk.Label(frame, image=img, width="100", height = "100", text = "class1")

# label2 = tk.Label(frame, image=img, width= "100", height = "100", text = "class2")

# label.grid(row=0, column=0)

# label2.grid(row=1, column=1)

# add_drag(label)
# add_drag(label2)

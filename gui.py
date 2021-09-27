import tkinter as tk

app = tk.Tk()

canvas = tk.Canvas(app, bg="white", height = "300", width = "300")

canvas.grid(row = 1, column = 2)

coord = 10, 10, 300, 300

arc = canvas.create_arc(coord, start = 45, extent = 300, fill = "yellow")

oval = canvas.create_oval(160, 30, 125, 150, fill="black")

text = canvas.create_text(200, 270, text="pucman")

draginfo = {"Widget":canvas, "xCoord":20, "yCoord":30}

element = text

def make_draggable(canvas):
    canvas.bind("<Button-1>", element = on_drag_start())
    canvas.bind("<B1-Motion>", on_drag_motion())

def on_drag_start(event):
    canvas = event.canvas
    canvas._drag_start_x = event.x
    canvas._drag_start_y = event.y
    element = canvas.find_closest(event.x, event.y)

def on_drag_motion(event, element):
    x = canvas.winfo_x() - canvas._drag_start_x + event.x
    y = canvas.winfo_y() - canvas._drag_start_y + event.y
    canvas.move(element, x, y)

app.mainloop()
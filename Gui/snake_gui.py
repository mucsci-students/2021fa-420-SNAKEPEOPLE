import tkinter as tk
from typing import ValuesView
import UMLbox
import UMLline
import UMLfield
import ViewChange

#Create Window
snake_app = tk.Tk()


snake_app.geometry("1200x1200")

#create the canvas
canvas = tk.Canvas(snake_app, bg="grey", width="1000", height="1000")

#put the canvas in the window
canvas.pack()

#tell the class creator what canvas to use in UMLbox
UMLbox.setCanvas(canvas)
ViewChange.set_canvas(canvas)

#Some test classes to add to the screen
UMLbox.create_class(canvas, "class1")
UMLbox.create_class(canvas, "class2")
UMLbox.create_class(canvas, "class3")
UMLbox.create_class(canvas, "class4")

#some example relationship lines
UMLline.add_line(canvas, UMLbox.class_list[0][1], UMLbox.class_list[1][1])
UMLline.add_line(canvas, UMLbox.class_list[2][1], UMLbox.class_list[3][1])
UMLline.add_line(canvas, UMLbox.class_list[0][1], UMLbox.class_list[3][1])

#UMLbox.rename_circle("class1", "fuckery")

UMLfield.add_field("class1", "fuckery")
UMLfield.add_field("class1", "tomfoolery")
UMLfield.add_field("class1", "twas")

UMLfield.rename_field("class1", "fuckery", "fookary")

#UMLbox.delete_circle("class1")
UMLline.delete_line(canvas, UMLbox.class_list[0][1], UMLbox.class_list[3][1])

snake_app.mainloop()
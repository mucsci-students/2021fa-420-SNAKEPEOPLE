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
UMLbox.create_class(canvas, "class5")

#some example relationship lines
UMLline.add_line(canvas, "class1", "class2")
UMLline.add_line(canvas, "class1", "class3")
#UMLline.add_line(canvas, "class1", "class4")

# UMLfield.add_field("class1", "box")
# UMLfield.add_field("class1", "tomfoolery")
# UMLfield.add_field("class1", "twas")
# UMLfield.add_field("class1", "boo")
UMLfield.add_field("class2", "sadasdasdsadsaasdasdsa")
UMLfield.add_field("class2", "asf")
UMLfield.add_field("class2", "twas")
UMLfield.add_field("class2", "boo")

#UMLfield.del_field("class1", "malarcky")

UMLfield.del_field("class2", "sadasdasdsadsaasdasdsa")
#UMLbox.delete_circle("class1")
#UMLline.delete_line(canvas, "class1", "class2")

snake_app.mainloop()
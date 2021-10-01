import tkinter as tk
from typing import ValuesView
import UMLbox
import UMLline
import UMLfield
import ViewChange
import UMLMethod

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
UMLbox.create_box(canvas, "class1")


UMLMethod.add_method("class1", "poggers int2", ["int somethin1", "int Somethin2"])

UMLfield.add_field("class1", "boo")

UMLfield.rename_field("class1", "boo", "ssadasasdaaaaaaaaaasdasdadassd")
UMLbox.create_box(canvas, "class2")


UMLMethod.add_method("class2", "poggers int2", ["int somethin1", "int Somethin2"])

UMLfield.add_field("class2", "boo")

UMLfield.rename_field("class2", "boo", "asdasdasdadasasdasdsadasdasd")

#UMLMethod.add_method("class1", "poggers int", ["int somethin1", "int Somethin2"])
#UMLMethod.add_method("class1", "poggers int3", ["int somethin1", "int Somethin2"])

#UMLMethod.del_method("class1", "poggers int")
#UMLMethod.del_method("class1", "poggers int2")

#UMLMethod.change_params("class1", "poggers int3", ["int asdasd", "kjasdj"])

#UMLbox.create_box(canvas, "class2")

# UMLMethod.add_method("class2", "poggers int2", ["int somethin1", "int Somethin2"])
# UMLMethod.add_method("class2", "poggers int", ["int somethin1", "int Somethin2"])

# UMLMethod.add_method("class2", "poggers int", ["int somethin1", "int Somethin2"])
# #UMLMethod.add_method("class2", "poggers int", ["int somethin1", "int Somethin2"])

# # UMLMethod.add_method("class2", "poggers int", ["int somethin1", "int Somethin2"])

# UMLfield.add_field("class2", "box")
# UMLfield.add_field("class2", "tomfasasdasdadasdasdoolery")
# UMLfield.add_field("class2", "twas")
# UMLfield.add_field("class2", "boo")


#some example relationship lines
#UMLline.add_line(canvas, "class1", "class2")
# UMLline.add_line(canvas, "class1", "class3")
#UMLline.add_line(canvas, "class1", "class4")


#UMLfield.add_field("class2", "sadasdasdsadsaasdasdsa")
# UMLfield.add_field("class2", "asf")
# UMLfield.add_field("class2", "twas")
# UMLfield.add_field("class2", "boo")

#UMLfield.del_field("class1", "malarcky")

#UMLfield.del_field("class2", "sadasdasdsadsaasdasdsa")
#UMLbox.delete_box("class1")
#UMLline.delete_line(canvas, "class1", "class2")

snake_app.mainloop()
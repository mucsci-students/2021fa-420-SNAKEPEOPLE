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
UMLbox.create_box(canvas, "class2")


UMLMethod.add_method("class2", "poggers int3", ["int somethin1", "int asd"])
UMLMethod.add_method("class2", "poggers int4", ["int somethin1", "int Somethin2"])
UMLfield.add_field("class2", "boo")


UMLfield.rename_field("class2", "boo", "a")

UMLbox.create_box(canvas, "class1")


UMLMethod.add_method("class1", "poggers int2", ["int somethin1", "int ssadahaasdasdadsdjadjahjsahaa"])
UMLMethod.add_method("class1", "poggers int3", ["int somethin1", "int asd"])
UMLMethod.add_method("class1", "poggers int4", ["int somethin1", "int Somethin2"])
UMLfield.add_field("class1", "boo")

UMLMethod.del_method("class2", "poggers int2")

UMLMethod.change_params("class2", "poggers int3", ["int asdsadasddsaasdasdsa", "in tasda"])

#UMLfield.rename_field("class1", "boo", "a")

snake_app.mainloop()
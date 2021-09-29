import tkinter as tk
import UMLsquare
import UMLline

#Create Window
snake_app = tk.Tk()

snake_app.geometry("400x400")

canvas = tk.Canvas(snake_app, bg="grey")

canvas.pack()

UMLsquare.setCanvas(canvas)

UMLsquare.create_class(canvas, "class1")
UMLsquare.create_class(canvas, "class2")
UMLsquare.create_class(canvas, "class3")


#UMLline.add_line(canvas, UMLsquare.square_list[0], UMLsquare.square_list[2])

snake_app.mainloop()
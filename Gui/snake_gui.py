import tkinter as tk
import UMLcircle
import UMLline

#Create Window
snake_app = tk.Tk()


snake_app.geometry("400x400")

#create the canvas
canvas = tk.Canvas(snake_app, bg="grey")

#put the canvas in the window
canvas.pack()

#tell the class creator what canvas to use in UMLcircle
UMLcircle.setCanvas(canvas)

#Some test classes to add to the screen
UMLcircle.create_class(canvas, "class1")
UMLcircle.create_class(canvas, "class2")
UMLcircle.create_class(canvas, "class3")
UMLcircle.create_class(canvas, "class4")

#some example relationship lines
UMLline.add_line(canvas, UMLcircle.circle_list[0][1], UMLcircle.circle_list[1][1])
UMLline.add_line(canvas, UMLcircle.circle_list[2][1], UMLcircle.circle_list[3][1])
UMLline.add_line(canvas, UMLcircle.circle_list[0][1], UMLcircle.circle_list[3][1])

snake_app.mainloop()
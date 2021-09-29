import tkinter as tk
import UMLcircle
import UMLline

#Create Window
snake_app = tk.Tk()


snake_app.geometry("1200x1200")

#create the canvas
canvas = tk.Canvas(snake_app, bg="grey", width="1000", height="1000")

#put the canvas in the window
canvas.pack()

#tell the class creator what canvas to use in UMLcircle
UMLcircle.setCanvas(canvas)

#Some test classes to add to the screen
UMLcircle.create_class(canvas, "class1")
UMLcircle.create_class(canvas, "stupidstuff.extralosadasdasdasddasdsadngnasdasdasdamebecauseiamanidiot")
UMLcircle.create_class(canvas, "mmmmmmmmmm")
UMLcircle.create_class(canvas, "class4")

UMLcircle.rename_circle("class1", "monkeyvibesbemonky")

#some example relationship lines
UMLline.add_line(canvas, UMLcircle.circle_list[0][1], UMLcircle.circle_list[1][1])
UMLline.add_line(canvas, UMLcircle.circle_list[2][1], UMLcircle.circle_list[3][1])
UMLline.add_line(canvas, UMLcircle.circle_list[0][1], UMLcircle.circle_list[3][1])

UMLline.delete_line(canvas, UMLcircle.circle_list[0][1], UMLcircle.circle_list[3][1])

snake_app.mainloop()
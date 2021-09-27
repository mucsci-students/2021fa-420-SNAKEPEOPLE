import tkinter as tk
import UMLwidget

#Create Window
snake_app = tk.Tk()

#Create frame within window to hold all labels
frame = tk.LabelFrame(snake_app, text="Frame", padx=200, pady=200, cursor="plus")

#Put frame in window
frame.pack()

#Evan's face

#test class to show adding works, in the future we will probably
#remove evan's face or move the text 
UMLwidget.add_widget("class1", frame)
UMLwidget.add_widget("class2", frame)

snake_app.mainloop()
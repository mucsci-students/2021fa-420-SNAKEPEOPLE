import tkinter as tk
import UMLBox
import UMLLine
import UMLField
import ViewChange
import UMLMethod
#Create Window
snake_app = tk.Tk()


snake_app.geometry("1200x1200")

#create the canvas
canvas = tk.Canvas(snake_app, bg="grey", width="1000", height="1000")

#put the canvas in the window
canvas.pack()

#tell the class creator what canvas to use in UMLBox
UMLBox.setCanvas(canvas)
ViewChange.set_canvas(canvas)

UMLBox.create_box(canvas, "class1")

'''methods include:
        add_field(classname:str field:str)
        del_field(classname:str field:str)
        rename_field(classname:str oldname:str, newname:str)
        add_method(classname : str, methodname : str, parameters : list)
        del_method(classname : str, methodname : str)
        rename_params(classname : str, methodname : str, new_parameters : list)
        create_box(canvas, name:str)
        delete_box(name : str)
        rename_box(oldname : str, newname : str)
        add_line(canvas, source : str, dest : str)
        delete_line(canvas, source : str, dest : str)
        
        **FOR LINES**
        aggregation = blue
        composition = green
        inheritance = red
        realization = black
        '''


snake_app.mainloop()
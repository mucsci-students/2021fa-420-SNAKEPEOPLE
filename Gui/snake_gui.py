import tkinter as tk
import EventHandler
import UMLMethod
import UMLBox
import UMLField
import UMLLine
import ViewChange

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

UMLBox.create_box(canvas, "class1asdadsasdasdasdasd")
UMLBox.create_box(canvas, "class2")
UMLBox.create_box(canvas, "class3")
UMLBox.create_box(canvas, "class4")

UMLLine.add_line(canvas, "class1asdadsasdasdasdasd", "class2", "composition")
# UMLMethod.add_method("class1","int method1",["stuff1"])
# UMLMethod.add_method("class2","int method1",["stuff1", "asdasdasdadasdsadasdadasdsad"])

#UMLMethod.del_params("class2", "int method1", ["asdasdasdadasdsadasdadasdsad"])


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
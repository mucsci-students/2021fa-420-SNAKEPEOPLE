import tkinter as tk
import DnD

label_list = []
currentx = 0
currenty = 0

class UMLwidget():

    #create a new label with the name provided and pack it into the frame
    def __init__(self, name : str, frame):
        self.name = name
        self.label = tk.Label(frame, bg="#10f", width="10", height = "5", text = name)
        if(currentx == currenty):
            ++currentx
        elif(currentx > currenty):
            ++currenty  
        self.label.grid(row=currentx, column=currenty)      

#Add the UMLwidget object to the frame and to the list
#Then call upon drag and drop (DnD) to allow it to move within the frame
def add_widget(name : str, frame):
    new_widget = UMLwidget(name, frame)
    label_list.append(new_widget)
    DnD.add_drag(new_widget.label)

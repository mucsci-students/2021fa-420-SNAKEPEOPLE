import tkinter as tk
from tkinter.constants import CURRENT
import DnD

label_list = []

class UMLwidget():

    currentx = 0
    currenty = 0
    #create a new label with the name provided and pack it into the frame
    def __init__(self, name : str, frame):
        self.name = name
        self.label = tk.Label(frame, bg="#10f", width="10", height = "5", text = name)
        self.label.grid(row=UMLwidget.currentx, column=UMLwidget.currenty)      

#Add the UMLwidget object to the frame and to the list
#Then call upon drag and drop (DnD) to allow it to move within the frame
def add_widget(name : str, frame):
    if(UMLwidget.currentx == UMLwidget.currenty):
        UMLwidget.currentx = UMLwidget.currentx + 1
    elif(UMLwidget.currentx > UMLwidget.currenty):
        UMLwidget.currenty = UMLwidget.currenty + 1
    new_widget = UMLwidget(name, frame)
    label_list.append(new_widget)
    DnD.add_drag(new_widget.label)

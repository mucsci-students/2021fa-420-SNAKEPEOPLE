import tkinter as tk
import DnD

label_list = []

#Create Window
app = tk.Tk()

#Create frame within window to hold all labels
frame = tk.LabelFrame(app, text="Frame", padx=200, pady=200, cursor="plus")

#Put frame in window
frame.pack()

img = tk.PhotoImage(file="Evan.png")

def insert_widget(name):
    name = tk.Label(frame, image=img, width="100", height = "100", text = "class1")
    label_list.append(name)
    name.pack()
    DnD.add_drag(name)

insert_widget("class1")

app.mainloop()
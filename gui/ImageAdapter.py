import tkinter as tk
from typing import Text
from PIL import Image, ImageDraw, ImageFont
import math
from gui import UMLMethod
from snake_uml import save
from uml_components import UMLClass
from . import UMLBox
from . import UMLField
from . import UMLMethod
from . import UMLLine

class ImageAdapter():

    #Setup a tk window and place a canvas in it
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("800x627")
        self.main_frame = tk.Frame(self.window, width=627, height=800)
        self.main_panel = UMLBox.init_canvas(self.main_frame)

    #Populate the canvas, save a snapshot of it,
    #then delete the window.
    def export(self, file_name):
        self.main_frame.pack(fill="both")
        self.main_panel.pack(fill="both")
        UMLBox.class_mediator()
        UMLLine.line_mediator()
        save_as_png(file_name)
        UMLBox.test_canvas.update()
        UMLBox.class_list = []
        self.window.destroy()

def save_as_png(file_name):
    # try:
        UMLBox.test_canvas.update()
        bounds = UMLBox.test_canvas.bbox('all')
        #Create a new image to draw on
        image = Image.new("RGB", (bounds[2] + 30, bounds[3] + 30), 
                            color="#D0D0D0")
        draw = ImageDraw.Draw(image)
        #Set the font of the pillow image
        font = ImageFont.truetype(font="Font/arial.ttf", size=12)
        for i in UMLBox.class_list:
            uml : UMLClass = UMLClass.class_dict[i.name]
            if len(uml.fields) == 0:
                spacer = 7
            else:
                spacer = 0
            coords = UMLBox.get_coords(i.name)
            #Set all the relationship arrows
            for k in i.rels:
                if k[0] == "source":
                    pos = UMLLine.findpos(k[2])
                    #Get coords of the destination box
                    dx1, dy1, dx2, dy2 = UMLBox.get_coords(UMLBox.class_list[pos].name)
                    #Get the dimensions of the source and destination box.
                    b1x1, b1y1, b1x2, b1y2 = UMLBox.test_canvas.coords(i.name)
                    b2x1, b2y1, b2x2, b2y2 = UMLBox.test_canvas.coords(k[2])

                    x1 = b1x1 + abs(b1x1-b1x2)/2
                    x2 = b2x1 + abs(b2x1-b2x2)/2
                    y1 = b1y1 + abs(b1y1-b1y2)/2
                    y2 = b2y1 + abs(b2y1-b2y2)/2

                    if(k[4] == "aggregation"):
                        color = 'blue'
                        add_dash = False
                        if x2 > x1:
                            if b2y2 <= b1y1:
                                draw.polygon(xy=([(x1, b1y1), (x1 - 10, 
                                    b1y1 - 10), (x1, b1y1 - 20), (x1 + 10, b1y1 - 10)]), outline=color, fill="#D0D0D0")
                                y1 = b1y1 - 20
                            elif b2y1 >= b1y2:
                                draw.polygon(xy=([(x1, b1y2), (x1 - 10, 
                                    b1y2 + 10), (x1, b1y2 + 20), (x1 + 10, b1y2 + 10)]), outline=color, fill="#D0D0D0")
                                y1 = b1y2 + 20
                            else:
                                draw.polygon(xy=([(b1x2, y1), (b1x2 + 10, 
                                    y1 - 10), (b1x2 + 20, y1), (b1x2 + 10, y1 + 10)]), outline=color, fill="#D0D0D0")
                                x1 = b1x2 + 20
                        else:
                            if b2y2 <= b1y1:
                                draw.polygon(xy=([(x1, b1y1), (x1 - 10, 
                                    b1y1 - 10), (x1, b1y1 - 20), (x1 + 10, b1y1 - 10)]), outline=color, fill="#D0D0D0")
                                y1 = b1y1 - 20
                            elif b2y1 >= b1y2:
                                draw.polygon(xy=([(x1, b1y2), (x1 - 10, 
                                    b1y2 + 10), (x1, b1y2 + 20), (x1 + 10, b1y2 + 10)]), outline=color, fill="#D0D0D0")
                                y1 = b1y2 + 20
                            else:
                                draw.polygon(xy=([(b1x1, y1), (b1x1 - 10, 
                                    y1 - 10), (b1x1 - 20, y1), (b1x1 - 10, y1 + 10)]), outline=color, fill="#D0D0D0")
                                x1 = b1x2 - 20
                    elif(k[4] == "composition"):
                        color = 'green'
                        add_dash = False
                        if x2 > x1:
                            if b2y2 <= b1y1:
                                draw.polygon(xy=([(x1, b1y1), (x1 - 10, 
                                    b1y1 - 10), (x1, b1y1 - 20), (x1 + 10), (b1y1 - 10)]), fill="black", outline=color)
                                y1 = b1y1 - 20
                            elif b2y1 >= b1y2:
                                draw.polygon(xy=([(x1, b1y2), (x1 - 10, 
                                    b1y2 + 10), (x1, b1y2 + 20), (x1 + 10, b1y2 + 10)]), fill="black", outline=color)
                                y1 = b1y2 + 20
                            else:
                                draw.polygon(xy=([(b1x2, y1), (b1x2 + 10, 
                                    y1 - 10), (b1x2 + 20, y1), (b1x2 + 10, y1 + 10)]), fill="black", outline=color)
                                x1 = b1x2 + 20
                        else:
                            if b2y2 <= b1y1:
                                draw.polygon(xy=([(x1, b1y1), (x1 - 10, 
                                    b1y1 - 10), (x1, b1y1 - 20), (x1 + 10, b1y1 - 10)]), fill="black", outline=color)
                                y1 = b1y1 - 20
                            elif b2y1 >= b1y2:
                                draw.polygon(xy=([(x1, b1y2), (x1 - 10, 
                                    b1y2 + 10), (x1, b1y2 + 20), (x1 + 10, b1y2 + 10)]), fill="black", outline=color)
                                y1 = b1y2 + 20
                            else:
                                draw.polygon(xy=([(b1x1, y1), (b1x1 - 10, 
                                    y1 - 10), (b1x1 - 20, y1), (b1x1 - 10, y1 + 10)]), fill="black", outline=color)
                                x1 = b1x2 - 20
                    elif(k[4] == "inheritance"):
                        color = 'red'
                        add_dash = False
                        if x2 > x1:
                            if b2y2 <= b1y1:
                                draw.polygon(xy=([(x1, b1y1), (x1 - 10, 
                                    b1y1 - 20), (x1 + 10, b1y1 - 20)]), outline=color, fill="#D0D0D0")
                                y1 = b1y1 - 20
                            elif b2y1 >= b1y2:
                                draw.polygon(xy=([(x1, b1y2), (x1 - 10, 
                                    b1y2 + 20), (x1 + 10, b1y2 + 20)]), outline=color, fill="#D0D0D0")
                                y1 = b1y2 + 20
                            else:
                                draw.polygon(xy=([(b1x2, y1), (b1x2 + 20, 
                                    y1 - 10), (b1x2 + 20, y1 + 10)]), outline=color, fill="#D0D0D0")
                                x1 = b1x2 + 20
                        else:
                            if b2y2 <= b1y1:
                                draw.polygon(xy=([(x1, b1y1), (x1 - 10, 
                                    b1y1 - 20), (x1 + 10, b1y1 - 20)]), outline=color, fill="#D0D0D0")
                                y1 = b1y1 - 20
                            elif b2y1 >= b1y2:
                                draw.polygon(xy=([(x1, b1y2), (x1 - 10, 
                                    b1y2 + 20), (x1 + 10, b1y2 + 20)]), outline=color, fill="#D0D0D0")
                                y1 = b1y2 + 20
                            else:
                                draw.polygon(xy=([(b1x1, y1), (b1x1 - 20, 
                                    y1 - 10), (b1x1 - 20, y1 + 10)]), outline=color, fill="#D0D0D0")
                                x1 = b1x1 - 20
                    else:
                        color = 'black'
                        add_dash = True
                        if x2 > x1:
                            if b2y2 <= b1y1:
                                draw.polygon(xy=([(x1, b1y1), (x1 - 10, 
                                    b1y1 - 20), (x1 + 10, b1y1 - 20)]), outline=color, fill="#D0D0D0")
                                y1 = b1y1 - 20
                            elif b2y1 >= b1y2:
                                draw.polygon(xy=([(x1, b1y2), (x1 - 10, 
                                    b1y2 + 20), (x1 + 10, b1y2 + 20)]), outline=color, fill="#D0D0D0")
                                y1 = b1y2 + 20
                            else:
                                draw.polygon(xy=([(b1x2, y1), (b1x2 + 20, 
                                    y1 - 10), (b1x2 + 20, y1 + 10)]), outline=color, fill="#D0D0D0")
                                x1 = b1x2 + 20
                        else:
                            if b2y2 <= b1y1:
                                draw.polygon(xy=([(x1, b1y1), (x1 - 10, 
                                    b1y1 - 20), (x1 + 10, b1y1 - 20)]), outline=color, fill="#D0D0D0")
                                y1 = b1y1 - 20
                            elif b2y1 >= b1y2:
                                draw.polygon(xy=([(x1, b1y2), (x1 - 10, 
                                    b1y2 + 20), (x1 + 10, b1y2 + 20)]), outline=color, fill="#D0D0D0")
                                y1 = b1y2 + 20
                            else:
                                draw.polygon(xy=([(b1x1, y1), (b1x1 - 20, 
                                    y1 - 10), (b1x1 - 20, y1 + 10)]), outline=color, fill="#D0D0D0")
                                x1 = b1x1 - 20
                draw.line(xy=((x1, y1), (x2,y2)), fill=UMLBox.test_canvas.itemcget(k[1], "fill"), width=2)
            #Draw the box
            draw.rectangle(xy=(coords), fill="#D1FF65", outline="black")
            center = (coords[2]-coords[0])/2 + coords[0]
            #Draw the name
            draw.text(xy=(center, coords[1] + 12), text=i.name, fill="black", font=font, anchor="mm")
            #Draw the field label
            draw.text(xy=(coords[0] + 5, coords[1] + 25), text="Field(s):", fill="black", font=font)
            fx,fy = UMLBox.test_canvas.coords(i.fieldlabel)
            #Draw the field text
            draw.text(xy=(center, fy + 10), text=UMLField.new_fieldText(i.name), fill="black", font=font, anchor="ma")
            #Draw the method label
            draw.text(xy=(coords[0] + 5, fy + spacer + 8 + 15*len(uml.fields)), text="Method(s):", fill="black", font=font)
            mx,my = UMLBox.test_canvas.coords(i.methodlabel)
            #Draw the method/parameter text
            draw.text(xy=(center, my + 12), text=UMLMethod.block_text(i.name), fill="black", font=font, anchor="ma")
        #crop the image
        cropped_image = image.crop((bounds[0] - 50, bounds[1] - 50, bounds[2] + 50, bounds[3] + 50))
        #Save the file as a png
        cropped_image.save(file_name + '.png')
        return "Exported png successfully."
    # except:
    #     return "Failed to export."


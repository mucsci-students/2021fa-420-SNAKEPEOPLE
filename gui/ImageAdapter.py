import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
import os
import platform

from gui import UMLMethod
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

def save_as_png(file_path):
    try:
        UMLBox.test_canvas.update()
        bounds = UMLBox.test_canvas.bbox('all')
        #Create a new image to draw on
        image = Image.new("RGB", (bounds[2] + 30, bounds[3] + 30), 
                            color="#D0D0D0")
        draw = ImageDraw.Draw(image)
        #Set the font of the pillow image
        if platform.system() == "Darwin":
            font = ImageFont.truetype(font="/Library/Fonts/Arial.ttf", size=12)
        elif platform.system() == "Windows":
            font = ImageFont.truetype(font="C:\WINDOWS\FONTS\ARIAL.TTF", size=12)
        elif platform.system() == "Linux":
            font = ImageFont.truetype(font="/usr/share/fonts/liberation/LiberationSans-Regular.ttf", size=12)
        else:
            font = ImageFont.load_default()
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

                    #Add a hollow diamond for the relationship type aggregation
                    if(k[4] == "aggregation"):
                        color = 'blue'
                        add_dash = False
                        if x2 > x1:
                            #Draw a diamond on the top of the box
                            if b2y2 <= b1y1:
                                draw.polygon(xy=([(x1, b1y1), (x1 - 10, 
                                    b1y1 - 10), (x1, b1y1 - 20), (x1 + 10, b1y1 - 10)]), outline=color, fill="#D0D0D0")
                                y1 = b1y1 - 20
                            #Draw a diamond on the bottom of the box
                            elif b2y1 >= b1y2:
                                draw.polygon(xy=([(x1, b1y2), (x1 - 10, 
                                    b1y2 + 10), (x1, b1y2 + 20), (x1 + 10, b1y2 + 10)]), outline=color, fill="#D0D0D0")
                                y1 = b1y2 + 20
                            #Draw a diamond on the right of the box
                            else:
                                draw.polygon(xy=([(b1x2, y1), (b1x2 + 10, 
                                    y1 - 10), (b1x2 + 20, y1), (b1x2 + 10, y1 + 10)]), outline=color, fill="#D0D0D0")
                                x1 = b1x2 + 20
                        else:
                            #Draw a diamond on the top of the box
                            if b2y2 <= b1y1:
                                draw.polygon(xy=([(x1, b1y1), (x1 - 10, 
                                    b1y1 - 10), (x1, b1y1 - 20), (x1 + 10, b1y1 - 10)]), outline=color, fill="#D0D0D0")
                                y1 = b1y1 - 20
                            #Draw a diamond on the bottom of the box
                            elif b2y1 >= b1y2:
                                draw.polygon(xy=([(x1, b1y2), (x1 - 10, 
                                    b1y2 + 10), (x1, b1y2 + 20), (x1 + 10, b1y2 + 10)]), outline=color, fill="#D0D0D0")
                                y1 = b1y2 + 20
                            #Draw a diamond on the left of the box
                            else:
                                draw.polygon(xy=([(b1x1, y1), (b1x1 - 10, 
                                    y1 - 10), (b1x1 - 20, y1), (b1x1 - 10, y1 + 10)]), outline=color, fill="#D0D0D0")
                                x1 = b1x1 - 20
                    #Add a filled diamond for the relationship type aggregation
                    elif(k[4] == "composition"):
                        color = 'green'
                        add_dash = False
                        if x2 > x1:
                            #Draw a triangle on the top of the box
                            if b2y2 <= b1y1:
                                draw.polygon(xy=([(x1, b1y1), (x1 - 10, 
                                    b1y1 - 10), (x1, b1y1 - 20), (x1 + 10), (b1y1 - 10)]), fill="black", outline=color)
                                y1 = b1y1 - 20
                            #Draw a triangle on the bottom of the box
                            elif b2y1 >= b1y2:
                                draw.polygon(xy=([(x1, b1y2), (x1 - 10, 
                                    b1y2 + 10), (x1, b1y2 + 20), (x1 + 10, b1y2 + 10)]), fill="black", outline=color)
                                y1 = b1y2 + 20
                            #Draw a triangle on the right of the box
                            else:
                                draw.polygon(xy=([(b1x2, y1), (b1x2 + 10, 
                                    y1 - 10), (b1x2 + 20, y1), (b1x2 + 10, y1 + 10)]), fill="black", outline=color)
                                x1 = b1x2 + 20
                        else:
                            #Draw a triangle on the top of the box
                            if b2y2 <= b1y1:
                                draw.polygon(xy=([(x1, b1y1), (x1 - 10, 
                                    b1y1 - 10), (x1, b1y1 - 20), (x1 + 10, b1y1 - 10)]), fill="black", outline=color)
                                y1 = b1y1 - 20
                            #Draw a triangle on the top of the box
                            elif b2y1 >= b1y2:
                                draw.polygon(xy=([(x1, b1y2), (x1 - 10, 
                                    b1y2 + 10), (x1, b1y2 + 20), (x1 + 10, b1y2 + 10)]), fill="black", outline=color)
                                y1 = b1y2 + 20
                            #Draw a triangle on the left of the box
                            else:
                                draw.polygon(xy=([(b1x1, y1), (b1x1 - 10, 
                                    y1 - 10), (b1x1 - 20, y1), (b1x1 - 10, y1 + 10)]), fill="black", outline=color)
                                x1 = b1x1 - 20
                    #Add a hollow triangle for the relationship type aggregation
                    elif(k[4] == "inheritance"):
                        color = 'red'
                        add_dash = False
                        if x2 > x1:
                            #Draw a triangle on the top of the box
                            if b2y2 <= b1y1:
                                draw.polygon(xy=([(x1, b1y1), (x1 - 10, 
                                    b1y1 - 20), (x1 + 10, b1y1 - 20)]), outline=color, fill="#D0D0D0")
                                y1 = b1y1 - 20
                            #Draw a triangle on the top of the box
                            elif b2y1 >= b1y2:
                                draw.polygon(xy=([(x1, b1y2), (x1 - 10, 
                                    b1y2 + 20), (x1 + 10, b1y2 + 20)]), outline=color, fill="#D0D0D0")
                                y1 = b1y2 + 20
                            #Draw a triangle on the right of the box
                            else:
                                draw.polygon(xy=([(b1x2, y1), (b1x2 + 20, 
                                    y1 - 10), (b1x2 + 20, y1 + 10)]), outline=color, fill="#D0D0D0")
                                x1 = b1x2 + 20
                        else:
                            #Draw a triangle on the top of the box
                            if b2y2 <= b1y1:
                                draw.polygon(xy=([(x1, b1y1), (x1 - 10, 
                                    b1y1 - 20), (x1 + 10, b1y1 - 20)]), outline=color, fill="#D0D0D0")
                                y1 = b1y1 - 20
                            #Draw a triangle on the bottom of the box
                            elif b2y1 >= b1y2:
                                draw.polygon(xy=([(x1, b1y2), (x1 - 10, 
                                    b1y2 + 20), (x1 + 10, b1y2 + 20)]), outline=color, fill="#D0D0D0")
                                y1 = b1y2 + 20
                            #Draw a triangle on the right of the box
                            else:
                                draw.polygon(xy=([(b1x1, y1), (b1x1 - 20, 
                                    y1 - 10), (b1x1 - 20, y1 + 10)]), outline=color, fill="#D0D0D0")
                                x1 = b1x1 - 20
                    #Add a hollow triangle for the relationship type aggregation
                    else:
                        color = 'black'
                        add_dash = True
                        if x2 > x1:
                            #Draw a triangle on the top of the box
                            if b2y2 <= b1y1:
                                draw.polygon(xy=([(x1, b1y1), (x1 - 10, 
                                    b1y1 - 20), (x1 + 10, b1y1 - 20)]), outline=color, fill="#D0D0D0")
                                y1 = b1y1 - 20
                            #Draw a triangle on the bottom of the box
                            elif b2y1 >= b1y2:
                                draw.polygon(xy=([(x1, b1y2), (x1 - 10, 
                                    b1y2 + 20), (x1 + 10, b1y2 + 20)]), outline=color, fill="#D0D0D0")
                                y1 = b1y2 + 20
                            #Draw a triangle on the right of the box
                            else:
                                draw.polygon(xy=([(b1x2, y1), (b1x2 + 20, 
                                    y1 - 10), (b1x2 + 20, y1 + 10)]), outline=color, fill="#D0D0D0")
                                x1 = b1x2 + 20
                        else:
                            #Draw a triangle on the top of the box
                            if b2y2 <= b1y1:
                                draw.polygon(xy=([(x1, b1y1), (x1 - 10, 
                                    b1y1 - 20), (x1 + 10, b1y1 - 20)]), outline=color, fill="#D0D0D0")
                                y1 = b1y1 - 20
                            #Draw a triangle on the bottom of the box
                            elif b2y1 >= b1y2:
                                draw.polygon(xy=([(x1, b1y2), (x1 - 10, 
                                    b1y2 + 20), (x1 + 10, b1y2 + 20)]), outline=color, fill="#D0D0D0")
                                y1 = b1y2 + 20
                            #Draw a triangle on the left of the box
                            else:
                                draw.polygon(xy=([(b1x1, y1), (b1x1 - 20, 
                                    y1 - 10), (b1x1 - 20, y1 + 10)]), outline=color, fill="#D0D0D0")
                                x1 = b1x1 - 20
                    #Add a solid line if the relationship type is not realization
                    if not add_dash:
                        draw.line(xy=((x1, y1), (x2,y2)), fill=UMLBox.test_canvas.itemcget(k[1], "fill"), width=2)
                    else:
                        #Get start and end points of the line
                        lx1, ly1, lx2, ly2 = UMLBox.test_canvas.coords(k[1])
                        #Find the slope of the current line
                        slope = (ly2-ly1)/(lx2-lx1)
                        #Get the y intercept of the line
                        b = ly2 - slope*lx2
                        var = 0
                        if abs(x2-x1) > abs(y2-y1):
                            #create a dash lne along the line equation incrementing along the x axis
                            if x1 < x2:
                                #Increment from right to left
                                while x1 < x2:
                                    #Add a dash
                                    if var % 2 == 0:
                                        var = var + 1
                                        x1 = x1 + 3
                                        temp_y2 = slope * x1 + b
                                        draw.line(xy=((x1 - 3, y1), (x1,temp_y2)), fill=UMLBox.test_canvas.itemcget(k[1], "fill"), width=2)
                                        y1 = temp_y2
                                    #Leave some empty space
                                    else:
                                        var = var + 1
                                        x1 = x1 + 3
                                        temp_y2 = slope * x1 + b
                                        y1 = temp_y2
                            else:
                                #Increment from left to right
                                while x1 > x2:
                                    #Add a dash
                                    if var % 2 == 0:
                                        var = var + 1
                                        x1 = x1 - 3
                                        temp_y2 = slope * x1 + b
                                        draw.line(xy=((x1 + 3, y1), (x1,temp_y2)), fill=UMLBox.test_canvas.itemcget(k[1], "fill"), width=2)
                                        y1 = temp_y2
                                    #Leave some empty space
                                    else:
                                        var = var + 1
                                        x1 = x1 - 3
                                        temp_y2 = slope * x1 + b
                                        y1 = temp_y2
                        else:
                            #create a dash lne along the line equation incrementing along the y axis
                            if y1 < y2:
                                #Increment from bottom to top
                                while y1 < y2:
                                    #Add a dash
                                    if var % 2 == 0:
                                        var = var + 1
                                        y1 = y1 + 3
                                        temp_x2 = (y1 - b) / slope
                                        draw.line(xy=((x1, y1 - 3), (temp_x2, y1)), fill=UMLBox.test_canvas.itemcget(k[1], "fill"), width=2)
                                        x1 = temp_x2
                                    #Leave some empty space
                                    else:
                                        var = var + 1
                                        y1 = y1 + 3
                                        temp_x2 = (y1 - b) / slope
                                        x1 = temp_x2
                            else:
                                #Increment from top to bottom
                                while y1 > y2:
                                    #Add a dash
                                    if var % 2 == 0:
                                        var = var + 1
                                        y1 = y1 - 3
                                        temp_x2 = (y1 - b) / slope
                                        draw.line(xy=((x1, y1 + 3), (temp_x2, y1)), fill=UMLBox.test_canvas.itemcget(k[1], "fill"), width=2)
                                        x1 = temp_x2
                                    #Leave some empty space
                                    else:
                                        var = var + 1
                                        y1 = y1 - 3
                                        temp_x2 = (y1 - b) / slope
                                        x1 = temp_x2
        for i in UMLBox.class_list:
            uml : UMLClass = UMLClass.class_dict[i.name]
            if len(uml.fields) == 0:
                spacer = 7
            else:
                spacer = 0
            coords = UMLBox.get_coords(i.name)
            #Draw the box
            draw.rectangle(xy=(coords[0], coords[1], coords[2], coords[3] + 2), fill="#D1FF65", outline="black", width=2)
            center = (coords[2]-coords[0])/2 + coords[0]
            #Draw the name
            draw.text(xy=(center, coords[1] + 12), text=i.name, fill="black", anchor="mm", font=font)
            #Draw the field label
            draw.text(xy=(coords[0] + 5, coords[1] + 25), text="Field(s):", fill="black", font=font)
            fx,fy = UMLBox.test_canvas.coords(i.fieldlabel)
            #Draw the field text
            draw.text(xy=(fx - 4, fy + 20 + (15*len(uml.fields)/2)), text=UMLField.new_fieldText(i.name), fill="black", font=font, anchor="lm")
            #Draw the method label
            draw.text(xy=(coords[0] + 5, fy + spacer + 18 + 15*len(uml.fields)), text="Method(s):", fill="black", font=font)
            mx,my = UMLBox.test_canvas.coords(i.methodlabel)
            #Draw the method/parameter text
            draw.text(xy=(coords[0] + 20, my + 24), text=UMLMethod.block_text(i.name), fill="black", font=font, anchor="ls")
            lx1, ly1, lx2, ly2 = UMLBox.test_canvas.coords(i.ftop)
            draw.line(xy=((lx1, ly1), (lx2, ly2)), fill="black", width=2)
            lx1, ly1, lx2, ly2 = UMLBox.test_canvas.coords(i.mtop)
            draw.line(xy=((lx1, ly1), (lx2, ly2)), fill="black", width=2)
        #crop the image
        cropped_image = image.crop((bounds[0] - 10, bounds[1] - 10, bounds[2] + 10, bounds[3] + 10))
        #Save the file as a png
        cropped_image.save(file_path)
        return "Exported png successfully."
    except:
        return "Failed to export"

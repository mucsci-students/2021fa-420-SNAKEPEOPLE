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
    try:
        UMLBox.test_canvas.update()
        bounds = UMLBox.test_canvas.bbox('all')
        #Create a new image to draw on
        image1 = Image.new("RGB", (bounds[2] + 30, bounds[3] + 30), 
                            color="#D0D0D0")
        draw = ImageDraw.Draw(image1)
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
                    draw.line(xy=((coords[0], coords[1]), (dx1, dy1)), fill=UMLBox.test_canvas.itemcget(k[1], "fill"), width=4)
                    #Get start and end points of the line
                    lx1, ly1, lx2, ly2 = UMLBox.test_canvas.coords(k[1])
                    #Find the slope of the current line
                    slope = (ly2-ly1)/(lx2-lx1)
                    #Get the y intercept of the line
                    b = ly2 - slope*lx2
                    #Aquire the base vertices for the arrowhead
                    v1, v2 = get_vals(lx2, lx1, ly2, ly1, b, slope)
                    # Check if line is vertical
                    if lx1 == lx2:
                        vtx1 = (v1-5, v2)
                        vtx2 = (v1+5, v2)
                    # Check if line is horizontal
                    elif ly1==ly2:
                        vtx1 = (v1, v2+5)
                        vtx2 = (v1, v2-5)
                    else:
                        alpha = math.atan2(ly2-ly1,lx2-lx1)-90*math.pi/180
                        a = 4*math.cos(alpha)
                        b = 4*math.sin(alpha)
                        vtx1 = (v1+a, v2+b)
                        vtx2 = (v1-a, v2-b)
                    #Draw the triangle at the end of the line
                    draw.polygon([vtx1, vtx2, (lx2, ly2)], fill=UMLBox.test_canvas.itemcget(k[1], "fill"))
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
        #Save the file as a png
        image1.save(file_name + '.png')
        return "Exported png successfully."
    except:
        return "Failed to export."

#Recursively get the y coordinate that is
#less than 10 units away from the endpoint
def get_v2(val, slope, ly2, ly1, b):
    #Get a triangle base y if the line goes
    #from top to bottom
    if ly2 > ly1:
        v2 = ly2 - val
        v1 = (v2 - b)/slope
    #Get a triangle base y if the line goes
    #from bottom to top
    else:
        v2 = ly2 + val
        v1 = (v2 - b)/slope
    #Return if the base y is less than 10 units
    #away from the endpoint
    if abs(v2 - ly2) < 10:
        return v2
    #Recurse if the base y is not less than 10
    #units away from the endpoint
    else:
        return get_v2(val - 1, slope, ly2, ly1, b)

#Recursively get the x coordinate that is
#less than 10 units away from the endpoint
def get_v1(val, slope, lx2, lx1, b):
    #Get a triangle base x if the line goes
    #from right to left
    if lx2 > lx1:
        v1 = lx2 - val
        v2 = slope*(v1) + b
    #Get a triangle base x if the line goes
    #from left to right
    else:
        v1 = lx2 + val
        v2 = slope*(v1) + b
    #Return if the base x is less than 10 units
    #away from the endpoint
    if abs(v1 - lx2) < 10:
        return v1
    #Recurse if the base x is not less than 10
    #units away from the endpoint
    else:
        return get_v1(val - 1, slope, lx2, lx1, b)

#Get the base x and y for the triangle that goes
#at the end of the line
def get_vals(lx2, lx1, ly2, ly1, b, slope):
    #Get the base x
    v1 = get_v1(10, slope, lx2, lx1, b)
    #Get the base y
    v2 = get_v2(10, slope, ly2, ly1, b)
    #If delta x is greater than delta y
    #define the arrowhead to be based off
    #the x coordinate on the line
    if abs(lx2 - lx1) > abs(ly2 - ly1):
        v2 = slope*(v1) + b
    #If delta y is greater than delta x
    #define the arrowhead to be based off
    #the y coordinate on the line
    else:
        v1 = (v2 - b)/slope
    return v1, v2
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


    def __init__(file_name):
        window = tk.Tk()
        window.geometry('800x627')
        main_frame = tk.Frame(window, width=627, height=800)
        main_panel = UMLBox.init_canvas(main_frame)
        main_frame.pack(fill="both")
        main_panel.pack(fill="both")
        UMLBox.class_mediator()
        UMLLine.line_mediator()
        save_as_png(file_name)
        UMLBox.test_canvas.update()
        window.destroy()

def save_as_png(file_name):
    UMLBox.test_canvas.update()
    #Create a new image to draw on
    image1 = Image.new("RGB", (UMLBox.test_canvas.winfo_width(), UMLBox.test_canvas.winfo_height()), 
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
                v1 = 0.98*(lx2-lx1)+lx1
                v2 = 0.98*(ly2-ly1)+ly1
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
                draw.polygon([vtx1, vtx2, lx2, ly2], fill=UMLBox.test_canvas.itemcget(k[1], "fill"))
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

# Project Name:  SNAKE PEOPLE UML Editor
# File Name:     UMLLine.py

# Internal Imports
from gui import ViewChange, UMLBox
from uml_components import UMLRelationship

###################################################################################################

# Object for a line representing a relationship between two classes.
class UMLLine():
    # Create a line from one box to another.
    def __init__(self, x1, y1, x2, y2, source, dest, line_type):
        sourcepos = findpos(source)
        destpos = findpos(dest)
        b1x1, b1y1, b1x2, b1y2 = UMLBox.test_canvas.coords(source)
        b2x1, b2y1, b2x2, b2y2 = UMLBox.test_canvas.coords(dest)

        # Get the center coords of the source and destination box.
        x1 = b1x1 + abs(b1x1-b1x2)/2
        x2 = b2x1 + abs(b2x1-b2x2)/2
        y1 = b1y1 + abs(b1y1-b1y2)/2
        y2 = b2y1 + abs(b2y1-b2y2)/2

        # Create a relationship identifier for aggregation (empty diamond)
        #   and place it along the border of the box.
        if(line_type == "aggregation"):
            color = 'blue'
            add_dash = False
            if x2 > x1:
                # Place relationship identifier on the top of the box.
                if b2y2 <= b1y1:
                    shape = UMLBox.test_canvas.create_polygon(x1, b1y1, x1 - 10, 
                        b1y1 - 10, x1, b1y1 - 20, x1 + 10, b1y1 - 10, outline = color, fill = "#D0D0D0", width = 2)
                    y1 = b1y1 - 20

                # Place relationship identifier on the bottom of the box.
                elif b2y1 >= b1y2:
                    shape = UMLBox.test_canvas.create_polygon(x1, b1y2, x1 - 10, 
                        b1y2 + 10, x1, b1y2 + 20, x1 + 10, b1y2 + 10, outline = color, fill = "#D0D0D0", width = 2)
                    y1 = b1y2 + 20

                # Place relationship identifier on the right of the box.
                else:
                    shape = UMLBox.test_canvas.create_polygon(b1x2, y1, b1x2 + 10, 
                        y1 - 10, b1x2 + 20, y1, b1x2 + 10, y1 + 10, outline = color, fill = "#D0D0D0", width = 2)
                    x1 = b1x2 + 20

            else:
                # Place relationship identifier on the top of the box.
                if b2y2 <= b1y1:
                    shape = UMLBox.test_canvas.create_polygon(x1, b1y1, x1 - 10, 
                        b1y1 - 10, x1, b1y1 - 20, x1 + 10, b1y1 - 10, outline = color, fill = "#D0D0D0", width = 2)
                    y1 = b1y1 - 20

                # Place relationship identifier on the bottom of the box.
                elif b2y1 >= b1y2:
                    shape = UMLBox.test_canvas.create_polygon(x1, b1y2, x1 - 10, 
                        b1y2 + 10, x1, b1y2 + 20, x1 + 10, b1y2 + 10, outline = color, fill = "#D0D0D0", width = 2)
                    y1 = b1y2 + 20

                # Place relationship identifier on the left of the box.
                else:
                    shape = UMLBox.test_canvas.create_polygon(b1x1, y1, b1x1 - 10, 
                        y1 - 10, b1x1 - 20, y1, b1x1 - 10, y1 + 10, outline = color, fill = "#D0D0D0", width = 2)
                    x1 = b1x1 - 20

        # Create a relationship identifier for composition (filled diamond)
        #   and place it along the border of the box.
        elif(line_type == "composition"):
            color = 'green'
            add_dash = False
            if x2 > x1:
                # Place relationship identifier on the top of the box.
                if b2y2 <= b1y1:
                    shape = UMLBox.test_canvas.create_polygon(x1, b1y1, x1 - 10, 
                        b1y1 - 10, x1, b1y1 - 20, x1 + 10, b1y1 - 10, fill = "black", outline = color)
                    y1 = b1y1 - 20

                # Place relationship identifier on the bottom of the box.
                elif b2y1 >= b1y2:
                    shape = UMLBox.test_canvas.create_polygon(x1, b1y2, x1 - 10, 
                        b1y2 + 10, x1, b1y2 + 20, x1 + 10, b1y2 + 10, fill = "black", outline = color)
                    y1 = b1y2 + 20

                # Place relationship identifier on the right of the box.
                else:
                    shape = UMLBox.test_canvas.create_polygon(b1x2, y1, b1x2 + 10, 
                        y1 - 10, b1x2 + 20, y1, b1x2 + 10, y1 + 10, fill = "black", outline = color)
                    x1 = b1x2 + 20

            else:
                # Place relationship identifier on the top of the box.
                if b2y2 <= b1y1:
                    shape = UMLBox.test_canvas.create_polygon(x1, b1y1, x1 - 10, 
                        b1y1 - 10, x1, b1y1 - 20, x1 + 10, b1y1 - 10, fill = "black", outline = color)
                    y1 = b1y1 - 20

                # Place relationship identifier on the bottom of the box.
                elif b2y1 >= b1y2:
                    shape = UMLBox.test_canvas.create_polygon(x1, b1y2, x1 - 10, 
                        b1y2 + 10, x1, b1y2 + 20, x1 + 10, b1y2 + 10, fill = "black", outline = color)
                    y1 = b1y2 + 20

                # Place relationship identifier on the left of the box.
                else:
                    shape = UMLBox.test_canvas.create_polygon(b1x1, y1, b1x1 - 10, 
                        y1 - 10, b1x1 - 20, y1, b1x1 - 10, y1 + 10, fill = "black", outline = color)
                    x1 = b1x1 - 20

        # Create a relationship identifier for inheritance (empty triangle)
        #   and place it along the border of the box.
        elif(line_type == "inheritance"):
            color = 'red'
            add_dash = False
            if x2 > x1:
                # Place relationship identifier on the top of the box.
                if b2y2 <= b1y1:
                    shape = UMLBox.test_canvas.create_polygon(x1, b1y1, x1 - 10, 
                        b1y1 - 20, x1 + 10, b1y1 - 20, outline = color, fill = "#D0D0D0")
                    y1 = b1y1 - 20

                # Place relationship identifier on the bottom of the box.
                elif b2y1 >= b1y2:
                    shape = UMLBox.test_canvas.create_polygon(x1, b1y2, x1 - 10, 
                        b1y2 + 20, x1 + 10, b1y2 + 20, outline = color, fill = "#D0D0D0")
                    y1 = b1y2 + 20

                # Place relationship identifier on the right of the box.
                else:
                    shape = UMLBox.test_canvas.create_polygon(b1x2, y1, b1x2 + 20, 
                        y1 - 10, b1x2 + 20, y1 + 10, outline = color, fill = "#D0D0D0")
                    x1 = b1x2 + 20

            else:
                # Place relationship identifier on the top of the box.
                if b2y2 <= b1y1:
                    shape = UMLBox.test_canvas.create_polygon(x1, b1y1, x1 - 10, 
                        b1y1 - 20, x1 + 10, b1y1 - 20, outline = color, fill = "#D0D0D0")
                    y1 = b1y1 - 20

                # Place relationship identifier on the bottom of the box.
                elif b2y1 >= b1y2:
                    shape = UMLBox.test_canvas.create_polygon(x1, b1y2, x1 - 10, 
                        b1y2 + 20, x1 + 10, b1y2 + 20, outline = color, fill = "#D0D0D0")
                    y1 = b1y2 + 20

                # Place relationship identifier on the left of the box.
                else:
                    shape = UMLBox.test_canvas.create_polygon(b1x1, y1, b1x1 - 20, 
                        y1 - 10, b1x1 - 20, y1 + 10, outline = color, fill = "#D0D0D0")
                    x1 = b1x1 - 20

        # Create a relationship identifier for Realization (empty triangle, dashed line)
        #   and place it along the border of the box.
        else:
            color = 'black'
            add_dash = True
            if x2 > x1:
                # Place relationship identifier on the top of the box.
                if b2y2 <= b1y1:
                    shape = UMLBox.test_canvas.create_polygon(x1, b1y1, x1 - 10, 
                        b1y1 - 20, x1 + 10, b1y1 - 20, outline = color, fill = "#D0D0D0")
                    y1 = b1y1 - 20

                # Place relationship identifier on the bottom of the box.
                elif b2y1 >= b1y2:
                    shape = UMLBox.test_canvas.create_polygon(x1, b1y2, x1 - 10, 
                        b1y2 + 20, x1 + 10, b1y2 + 20, outline = color, fill = "#D0D0D0")
                    y1 = b1y2 + 20

                # Place relationship identifier on the right of the box.
                else:
                    shape = UMLBox.test_canvas.create_polygon(b1x2, y1, b1x2 + 20, 
                        y1 - 10, b1x2 + 20, y1 + 10, outline = color, fill = "#D0D0D0")
                    x1 = b1x2 + 20

            else:
                # Place relationship identifier on the top of the box.
                if b2y2 <= b1y1:
                    shape = UMLBox.test_canvas.create_polygon(x1, b1y1, x1 - 10, 
                        b1y1 - 20, x1 + 10, b1y1 - 20, outline = color, fill = "#D0D0D0")
                    y1 = b1y1 - 20

                # Place relationship identifier on the bottom of the box.
                elif b2y1 >= b1y2:
                    shape = UMLBox.test_canvas.create_polygon(x1, b1y2, x1 - 10, 
                        b1y2 + 20, x1 + 10, b1y2 + 20, outline = color, fill = "#D0D0D0")
                    y1 = b1y2 + 20

                # Place relationship identifier on the left of the box.
                else:
                    shape= UMLBox.test_canvas.create_polygon(b1x1, y1, b1x1 - 20, 
                        y1 - 10, b1x1 - 20, y1 + 10, outline = color, fill = "#D0D0D0")
                    x1 = b1x1 - 20

        # If not realization, create a line of the specified color.
        if not add_dash:    
            line = UMLBox.test_canvas.create_line(x1, y1, x2, y2, fill = color, width = 3)

        # If Realization, create a dashed line.
        else:
            line = UMLBox.test_canvas.create_line(x1, y1, x2, y2, fill = color, width = 3, dash = (255, 255))
        UMLBox.test_canvas.tag_lower(line)

        # Store entries for source and dest boxes that tell whether the box is the source
        #   or destination of a relationship.
        UMLBox.class_list[sourcepos].rels.append(("source", line, dest, shape, line_type))
        UMLBox.class_list[destpos].rels.append(("dest", line, source, shape, line_type))

###################################################################################################

# Add a line connecting two classes by name, source and dest.
def add_line(source : str, dest : str, line_type : str):
    sourcepos = UMLBox.find_pos_from_name(source)
    destpos = UMLBox.find_pos_from_name(dest)
    sourceItem = UMLBox.class_list[UMLBox.find_pos_from_name(source)].rec
    destItem = UMLBox.class_list[UMLBox.find_pos_from_name(dest)].rec
    midsourcex = UMLBox.test_canvas.coords(sourceItem)[0]
    midsourcey = UMLBox.test_canvas.coords(sourceItem)[1]
    middestx = UMLBox.test_canvas.coords(destItem)[0]
    middesty = UMLBox.test_canvas.coords(destItem)[1]
    UMLLine(midsourcex, midsourcey, middestx, middesty, sourceItem, destItem, line_type)

# Find the position of the class_list of the source.
def findpos(source):
    pos = 0
    while(pos < len(UMLBox.class_list)):
        if source == UMLBox.class_list[pos].rec:
            return pos
        else:
            pos += 1

###################################################################################################

# Fine the correct box elements of the source and dest within the class_list.
def delete_line(source : str, dest : str):
    sourcepos = UMLBox.find_pos_from_name(source)
    destpos = UMLBox.find_pos_from_name(dest)
    deleteline(UMLBox.class_list[sourcepos].rec, UMLBox.class_list[destpos].rec)

# Remove a line from the class_list storage. 
#   Line is stored both ways, so two deletes must occur.
def deleteline(source, dest):
    sourcepos = findpos(source)
    destpos = findpos(dest)
    subpos = 0

    # Delete all line entries for a box that involve source
    while subpos < len(UMLBox.class_list[sourcepos].rels):
        if (UMLBox.class_list[sourcepos].rels[subpos][0] == "source" 
            and UMLBox.class_list[sourcepos].rels[subpos][2] == dest):
            line = UMLBox.class_list[sourcepos].rels[subpos][1]
            ViewChange.del_item(UMLBox.class_list[sourcepos].rels[subpos][3])
            UMLBox.class_list[sourcepos].rels.pop(subpos)
        subpos += 1
    subpos = 0

    # Delete all line entries for a box that involve dest
    while subpos < len(UMLBox.class_list[destpos].rels):
        if (UMLBox.class_list[destpos].rels[subpos][0] == "dest" 
            and UMLBox.class_list[destpos].rels[subpos][2] == source):
            ViewChange.del_item(UMLBox.class_list[sourcepos].rels[subpos][3])
            UMLBox.class_list[destpos].rels.pop(subpos)
        subpos += 1

    # Delete the line element itself
    ViewChange.del_item(line)
    
###################################################################################################

def line_mediator():
    # Delete all existing relationships on the canvas.
    for i in UMLBox.class_list:
        while len(i.rels) > 0:
            ViewChange.del_item(i.rels[0][1])
            ViewChange.del_item(i.rels[0][3])
            i.rels.pop(0)
        i.rels = []

    # Add any relationships back to the list, if both boxes exist in the canvas.
    for i in UMLRelationship.relationship_list:
        if UMLBox.find_pos_from_name(i.source) != None and UMLBox.find_pos_from_name(i.destination) != None:
            add_line(i.source, i.destination, i.type)

###################################################################################################
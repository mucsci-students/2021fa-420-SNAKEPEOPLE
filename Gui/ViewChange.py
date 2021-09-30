def set_canvas(can):
    global canvas
    canvas = can

def del_item(name):
    canvas.delete(name)

def bring_front(item):
    canvas.tag_raise(item)

def set_rec(item, x1, y1, x2, y2):
    canvas.coords(item, x1, y1, x2, y2)

def set_text(item, x, y):
    canvas.coords(item, x, y)

def set_line(item, x1, y1, x2, y2):
    canvas.coords(item, x1, y1, x2, y2)

def item_config(item, text, justify, state):
    if(justify == None and state == None):
        canvas.itemconfigure(item, text = text)
    else:
        canvas.itemconfigure(item, text = text, justify = justify, state = state)

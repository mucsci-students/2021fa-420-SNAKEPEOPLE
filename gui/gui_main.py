import tkinter as tk
from tkinter import font

def run(class_dict : dict):
    
    window = tk.Tk()
    window.title("Snake People UML Editor")
    window.grid_rowconfigure(0,weight=1)
    window.grid_columnconfigure(1,weight=1)
    
    menubar = build_menu(window)
    
    my_font = font.Font(size=12)
    
    # Element Construction
    selector_frame = tk.Frame(window, bg="#700")
    display_frame = tk.Frame(window, bg="#070")
    control_frame = tk.Frame(window)
    
    class_box = tk.Listbox(selector_frame, 
                        #    width=20, 
                           font=my_font,
                           bd=3)
    
    test_canvas = tk.Canvas(display_frame, 
                            width=600, 
                            height=600,
                            bg="#888",
                            bd=3)
    
    populate_listbox(class_box, ["str(x) for x in range(8000000000000000)"])
    
    # Element placement in window.
    selector_frame.grid(row=0, column=0, sticky="nsw")
    selector_frame.columnconfigure(0, weight=1)
    selector_frame.rowconfigure(0, weight=1)
    
    display_frame.grid(row=0, column=1, sticky="nsew")
    display_frame.columnconfigure(1, weight=1)
    display_frame.rowconfigure(0,weight=1)
    
    control_frame.grid(row=0, column=2, sticky="nse")
    control_frame.columnconfigure(2, weight=1)
    control_frame.rowconfigure(0, weight=1)
    
    class_box.grid(row=0, column=0, sticky="nsw")
    test_canvas.grid(row=0, column=1, sticky="nsew")
    
    buttons(control_frame, [])
    window.config(menu=menubar)
    window.mainloop()
    
def populate_listbox(box : tk.Listbox, values : list):
    """
    Fills a Tk Listbox with values.
    """
    idx = 0
    for x in values:
        box.insert(idx, x)
        
def buttons(cf : tk.Frame, btn_list : list):
    for x in range(6):
        btn = tk.Button(cf, text=str(x), width=22, bd=3)
        btn.pack()
        
def build_menu(window : tk.Tk) -> tk.Menu:
    menubar = tk.Menu(window)
    menu_file = tk.Menu(menubar, tearoff=0)
    menu_file.add_command(label="Save")
    menu_file.add_command(label="Load")
    menu_file.add_separator()
    menu_file.add_command(label="Exit")
    menubar.add_cascade(label="File", menu=menu_file)
    
    return menubar

if __name__ == "__main__":
    run({})
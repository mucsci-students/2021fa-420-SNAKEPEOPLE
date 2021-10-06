import tkinter as tk
from tkinter import font

from gui import gui_buttons
from uml_components import UMLClass, UMLRelationship
from gui.UMLBox import class_list

def run():
    
    window = tk.Tk()
    window.title("Snake People UML Editor")
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1,weight=1)
    window.grid_columnconfigure(1,weight=1)
    
    menubar = build_menu(window)
    
    title_font = font.Font(size=12)
    list_font = font.Font(size=11)
    
    # Element Construction
    classes_frame = tk.LabelFrame(window, 
                                   labelanchor='nw', 
                                   text="Classes", 
                                   font=title_font)
    
    relationship_frame = tk.LabelFrame(window, 
                                   labelanchor='nw', 
                                   text="Relationships", 
                                   font=title_font)
    
    display_frame = tk.Frame(window)
    control_frame = tk.Frame(window)
    
    class_box = tk.Listbox(classes_frame, 
                           font=list_font,
                           width=30,
                           bd=3)
    
    rel_box = tk.Listbox(relationship_frame,
                         font=list_font,
                         width=30,
                         bd=3)
    
    test_canvas = tk.Canvas(display_frame, 
                            width=600, 
                            height=600,
                            bg="#888",
                            bd=3)
    
    def update_classes():
        if class_box.get(0, tk.END) != tuple(UMLClass.class_dict.keys()):
            class_box.delete(0, tk.END)
            for key in UMLClass.class_dict:
                class_box.insert(tk.END, UMLClass.class_dict[key].name)
        window.after(10, update_classes)
        
    def update_rels():
        if rel_box.get(0, tk.END) != tuple(UMLRelationship.relationship_list):
            rel_box.delete(0, tk.END)
            for rel in UMLRelationship.relationship_list:
                rel_box.insert(tk.END, rel)
        window.after(10, update_rels)
        
    test_canvas.update_idletasks()        
    update_classes()
    update_rels()
    
    
    # Element placement in window.
    classes_frame.grid(row=0, column=0, sticky="nsw")
    classes_frame.columnconfigure(0, weight=1)
    classes_frame.rowconfigure(0, weight=1)
    
    relationship_frame.grid(row=1, column=0, sticky="nsw")
    relationship_frame.columnconfigure(0, weight=1)
    relationship_frame.rowconfigure(1, weight=1)
    
    display_frame.grid(row=0, column=1, sticky="nsew", rowspan=2)
    display_frame.columnconfigure(1, weight=1)
    display_frame.rowconfigure(0,weight=1)
    
    control_frame.grid(row=0, column=2, sticky="nse", rowspan=2)
    control_frame.columnconfigure(2, weight=1)
    control_frame.rowconfigure(0, weight=1)
    
    class_box.grid(row=0, column=0, sticky="nsw")
    rel_box.grid(row=1, column=0, sticky="nsw")
    test_canvas.grid(row=0, column=1, sticky="nsew", rowspan=2)
    
    btn_list = gui_buttons.make_buttons(control_frame)
    buttons(btn_list)
    
    window.config(menu=menubar)
    
    window.mainloop()
    
        
def buttons(btn_list : list):
    for btn in btn_list:
        btn.pack()
     
def clear_dict():
    UMLClass.class_dict = dict()
        
def build_menu(window : tk.Tk) -> tk.Menu:
    menubar = tk.Menu(window)
    menu_file = tk.Menu(menubar, tearoff=0)
    menu_file.add_command(label="New", command=clear_dict)
    menu_file.add_command(label="Save")
    menu_file.add_command(label="Load")
    menu_file.add_separator()
    menu_file.add_command(label="Exit", command=exit)
    menubar.add_cascade(label="File", menu=menu_file)
    
    return menubar

if __name__ == "__main__":
    run()
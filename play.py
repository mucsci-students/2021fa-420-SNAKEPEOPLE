import tkinter as tk

class Main(tk.Tk):
    def __init__(self): 
        super().__init__()
        self.canvas = tk.Canvas(self, width=500, height=300)
        self.canvas.grid(row=0,column=0)
        self.label = tk.Label(self.canvas, text='Hello World', bg='blue')
        self.canvas.find_closest(0,0)
        self.label.bind("<Button-1>", self.getelement)
        self.id_label = self.canvas.create_window(100,100, window=self.element,    tags="motion_bound")
        self.update()
        self.label.bind("<B1-Motion>", self.relocate)

    def relocate(self, event):
        print(self.canvas.winfo_pointerxy())
        x0,y0 = self.canvas.winfo_pointerxy()
        x0 -= self.canvas.winfo_rootx()
        y0 -= self.canvas.winfo_rooty()
        self.canvas.coords(self.id_label,x0,y0)

    def getelement(self, event):
        self.element = self.canvas.find_closest(event.x, event.y)

if __name__ == "__main__":
    main = Main()
    main.mainloop()
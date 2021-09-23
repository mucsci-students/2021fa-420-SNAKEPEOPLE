import tkinter as tk
import tkinter.font as tk_font

app = tk.Tk()
app.title("UML Editor")

ab = "#707070"
af = "#f0f0f0"

canvas = tk.Canvas(app, bg="red", height = "200", width = "200")

canvas.grid(row=2, column=2)

button_addclass = tk.Button(app,
                            text="addclass",
                            width="20",
                            height="5",
                            activebackground=ab,
                            activeforeground=af,)

button_addclass.grid(row = 3, column = 3)

app.mainloop()
import sys, os, string, time
import tkinter as tk

def setCanvas(can):
    global canvas
    canvas = can

class CanvasDnD (tk.Frame):
  def __init__ (self, master):
    self.master =master
    self.loc =self.dragged =0
    self.name = "clas1"
    canvas.pack ()
    canvas.tag_bind (self.name, "<ButtonPress-1>", self.down)
    canvas.tag_bind (self.name, "<ButtonRelease-1>", self.chkup)
    canvas.tag_bind (self.name, "<Enter>", self.enter)
    canvas.tag_bind (self.name, "<Leave>", self.leave)

  def down (self, event):
    self.loc =1
    self.dragged =0
    event.widget.bind ("<Motion>", self.motion)

  def motion (self, event):
    root.config (cursor ="exchange")
    cnv = event.widget
    cnv.itemconfigure (tk.CURRENT, fill ="blue")
    x,y = cnv.canvasx(event.x), cnv.canvasy(event.y)
    got = event.widget.coords (tk.CURRENT, x, y)
  
  def leave (self, event):
    self.loc =0

  def enter (self, event):
    self.loc =1
    if self.dragged ==event.time:
      self.up (event)

  def chkup (self, event):
    event.widget.unbind ("<Motion>")
    root.config (cursor ="")
    self.target =event.widget.find_withtag (tk.CURRENT)
    event.widget.itemconfigure (tk.CURRENT, fill =self.defaultcolor)
    if self.loc: # is button released in same widget as pressed?
      self.up (event)
    else:
      self.dragged =event.time

  def up (self, event):
    event.widget.unbind ("<Motion>")

root =tk.Tk()
canvas = tk.Canvas(root)
setCanvas(canvas)
CanvasDnD (root).pack()
root.mainloop()
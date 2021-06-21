import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import tkinter

app = Tk()
canvas=Canvas(master=app)
app.title="Rat in a fucking maze"
app.geometry("600x600")
bk_image=tk.PhotoImage(file="pyprograms\GUIwork\Maze.png")
bk_label=tk.Label(app,image=bk_image)
bk_label.place(x=0,y=0)
image = ImageTk.PhotoImage(Image.open("D:\demo\pyprograms\GUIwork\here.png"))

canvas.create_image(50,50,anchor=NW,image=image)

canvas.pack()

app.mainloop()
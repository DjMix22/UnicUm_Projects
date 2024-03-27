import tkinter as tk
from random import randint


class Circles:
    def __init__(self, win):
        self.canvas = tk.Canvas(win, width=400, height=400)
        self.canvas.pack()
        win.bind("<Button-1>", self.create_circle)

    def create_circle(self, trash):
        x0 = randint(20, 380)
        y0 = randint(20, 380)
        x1 = x0 + 20
        y1 = y0 + 20
        self.canvas.create_oval(x0, y0, x1, y1, fill="#FFD700")


win = tk.Tk()
win.geometry("400x400")
win.title("Создание круга по клику мыши")

circle_creator = Circles(win)

win.mainloop()

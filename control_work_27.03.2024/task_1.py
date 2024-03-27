import tkinter as tk
from tkinter import ttk, messagebox


class HelloWorld:
    def __init__(self, win):
        self.button = None

        self.frame = tk.Frame(win)
        self.frame.pack(expand=True)

        self.create_buttons()

    @staticmethod
    def print_hello_world():
        messagebox.showinfo(title="Вывод", message="Hello Word!")

    def create_buttons(self):
        self.button = ttk.Button(self.frame, command=self.print_hello_world, text="Enter")
        self.button.pack(pady=10)


win = tk.Tk()
win.title("Окно")
win.geometry("400x400")
hello_world = HelloWorld(win)

hello_world.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
win.mainloop()

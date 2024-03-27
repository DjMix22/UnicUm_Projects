import tkinter as tk
from tkinter import ttk, messagebox

win = tk.Tk()
win.title("Окно")
win.geometry("400x400")

style = ttk.Style()
style.configure("BW.TLabel", font=("Arial", 12))

frame = tk.Frame(win)
frame.pack(expand=True)


def create_entry(text):
    label = tk.Label(frame, text=text)
    label.pack()
    entry = tk.Entry(frame)
    entry.pack()
    return entry


entry_x1 = create_entry("x1")
entry_x2 = create_entry("x2")


def add():
    global result
    try:
        x1 = int(entry_x1.get())
        x2 = int(entry_x2.get())
        if x1 is not None and x2 is not None:
            result = x1 + x2
        else:
            messagebox.showinfo(title="Ошибка!!!", message="Вы не ввели какое-либо число!!!")
    except ValueError:
        messagebox.showinfo(title="Ошибка!!!", message="Неверные числа!")


def sub():
    global result
    try:
        x1 = int(entry_x1.get())
        x2 = int(entry_x2.get())
        if x1 is not None and x2 is not None:
            result = x1 - x2
        else:
            messagebox.showinfo(title="Ошибка!!!", message="Вы не ввели какое-либо число!!!")
    except ValueError:
        messagebox.showinfo(title="Ошибка!!!", message="Неверные числа!")


def equals():
    messagebox.showinfo(title="Вывод", message=result)


result = "Вы не нажали кнопку сложения или вычитания"

btn_add = ttk.Button(frame, text="+", command=add)
btn_add.pack(pady=10)

btn_sub = ttk.Button(frame, text="-", command=sub)
btn_sub.pack(pady=10)

btn_equals = ttk.Button(frame, text="=", command=equals)
btn_equals.pack(pady=10)

frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
win.mainloop()

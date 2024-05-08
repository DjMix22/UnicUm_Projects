import math
import tkinter as tk


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self):
        self.__x = None
        self.__y = None
        self.__r = None

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, r):
        self.__r = r

    def area(self):
        return math.pi * self.__r ** 2

    def print_circle(self):
        x = self.__x
        y = self.__y
        r = self.__r
        root = tk.Tk()

        canvas = tk.Canvas(root, width=500 + r, height=500 + r)
        canvas.pack()

        canvas.create_oval(250 - r // 2, 250 - r // 2, 250 + r // 2, 250 + r // 2, outline="green", width=1, fill="green")
        canvas.create_text(250, 250, text=f"{round(self.area(), 1)}", fill="black")

        root.mainloop()

        print(f"{self} нарисован!")

    def __str__(self):
        return f"Круг с координатами ({self.__x}, {self.__y}) радиусом {self.__r}"


class Rect(Shape):
    def __init__(self):
        self.__length = None
        self.__width = None

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __str__(self):
        return f"Прямоугольник с длиной {self.__length}, шириной {self.__width}"


def main_circle():
    circle_1 = Circle()
    circle_1.x = 10
    circle_1.y = 20
    circle_1.r = 50

    circle_2 = Circle()
    circle_2.x = 80
    circle_2.y = 90
    circle_2.r = 10

    print(f"{circle_1} площадью {circle_1.area()}")
    print(f"{circle_2} площадью {circle_2.area()}")

    circle_1.print_circle()
    circle_2.print_circle()


def main_rectangle():
    print("Введите стороны прямоугольника для нахождения площади!")
    rectangle = Rect()
    rectangle.length = int(input("Длина: "))
    rectangle.width = int(input("Ширина: "))
    print(f"{rectangle} с площадью {rectangle.area()}")


if __name__ == '__main__':
    main_circle()
    try:
        main_rectangle()
    except ValueError:
        main_rectangle()

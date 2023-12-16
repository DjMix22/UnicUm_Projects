class Calculator():
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def add(self, num_1, num_2):
        print(num_1 + num_2)

    def sub(self, num_1, num_2):
        print(num_1 - num_2)

    def multiply(self, num_1, num_2):
        print(num_1 * num_2)

    def division(self, num_1, num_2):
        try:
            print(num_1 / num_2)
        except ZeroDivisionError:
            print("Не дели на ноль!")


class AreaCalculator():
    def circle(self, radius):
        print(3.14 * radius ** 2)

    def square(self, line):
        print(line ** 2)

    def triangle(self, a, b, c):
        p = (a + b + c) / 2
        area = p * (p - a) * (p - b) * (p - c)
        print(area ** 0.5)


while True:
    AC = AreaCalculator
    OperationNumber = int(input("1) Сложение\n2) Вычитание\n3) Умножение\n4) Деление"
                                "\n5) Площадь круга\n6) Площадь квадрата\n7) Площадь треугольника"
                                "\n8) Выйти из программы\nВведите номер операции: "))

    try:
        if 1 <= OperationNumber <= 4:
            first_number = int(input("Введите первое число: "))
            second_number = int(input("Введите второе число: "))
            expression = Calculator(first_number, second_number)
        if OperationNumber == 1:
            expression.add(expression.num_1, expression.num_2)
        elif OperationNumber == 2:
            expression.sub(expression.num_1, expression.num_2)
        elif OperationNumber == 3:
            expression.multiply(expression.num_1, expression.num_2)
        elif OperationNumber == 4:
            expression.division(expression.num_1, expression.num_2)
        elif OperationNumber == 5:
            AreaCalculator.circle(self=AC, radius=float(input("Введите радиус: ")))
        elif OperationNumber == 6:
            AreaCalculator.square(self=AC, line=float(input("Введите длину стороны: ")))
        elif OperationNumber == 7:
            AreaCalculator.triangle(self=AC, a=float(input("1-ая сторона: ")), b=float(input("2-ая сторона: ")), c=float(input("3-ая сторона: ")))
        elif OperationNumber == 8:
            break
        else:
            print("Не верное значение!")
    except ValueError:
        print("Не верное значение!")

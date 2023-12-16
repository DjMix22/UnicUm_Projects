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
        print(num_1 / num_2)


first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

expression = Calculator(first_number, second_number)

expression.add(expression.num_1, expression.num_2)
expression.sub(expression.num_1, expression.num_2)
expression.multiply(expression.num_1, expression.num_2)
expression.division(expression.num_1, expression.num_2)

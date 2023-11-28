from random import *


def random_password(len_password):
    letters_small = "abcdefghijklmnopqrstuvwxyz"
    letters_big = "ABCDEGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_symbols = "!@#$%^&*()-_=+[]{}\|;:‘,<>/?`~"

    matrix = [letters_small, letters_big, numbers, special_symbols]

    password = ""

    for i in range(len_password):
            random_list = matrix[randint(0, 3)]
            password += random_list[randint(0, len(random_list) - 1)]

    return password


len_password = int(input("Введите длину пароля: "))
print(random_password(len_password))

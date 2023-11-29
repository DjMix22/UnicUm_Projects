# # 1 задание
#
# def my_decorator(multiply):
#     def wrapper(n_1, n_2):
#         return multiply(n_1,n_2)*2
#     return  wrapper
#
# @my_decorator
# def multiply(n_1,n_2):
#     return   n_1+n_2
#
# n_1 = int(input("Введите первое число: "))
# n_2 = int(input("Введите второе число: "))
#
# print(multiply(n_1, n_2))


# # 2 задание
# 
# def my_decorator(multiply):
#     def wrapper(*args, **kwargs):
#         print(f'Вызываю функцию {multiply.__name__} с аргументами {args}')
#         result = multiply(*args, **kwargs)
#     return  wrapper
# 
# @my_decorator
# def multiply(*args, **kwargs):
#     return  args * kwargs
# 
# 
# n_1 = int(input("Введите первое число: "))
# n_2 = int(input("Введите второе число: "))

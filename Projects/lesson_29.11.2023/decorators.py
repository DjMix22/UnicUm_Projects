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


# # 2 задача

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f'Вызываю функцию {func.__name__} с аргументами {args=} {kwargs=}')
#         return func(*args, **kwargs) * 2
#     return wrapper
# 
# 
# @my_decorator
# def summ(num_1, num_2):
#     return num_1 + num_2
# 
# 
# n_1 = int(input("Введите первое число: "))
# n_2 = int(input("Введите второе число: "))
# 
# print(summ(n_1, n_2))

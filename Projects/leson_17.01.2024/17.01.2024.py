import math
import time


def timer_func(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        string = f"Время выполнения функции: {end - start}"
        return [result, string]
    return wrapper


@timer_func
def stirling_factorial(n):
    return math.sqrt(2 * math.pi * n) * ((n / math.e) ** n)


def recursion_factorial(n):
    if n < 1:
        return 1
    else:
        num = n * recursion_factorial(n - 1)
        return num


@timer_func
def recursion_factorial_2(n):
    return recursion_factorial(n)


@timer_func
def cycle_factorial(n):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans


number = int(input())

recursion = recursion_factorial_2(number)
print(f"Факториал рекурсией:\n{recursion[0]}\n{recursion[1]}\n")

stirling = stirling_factorial(number)
print(f"Факториал алгоритмом стирлинга:\n{stirling[0]}\n{stirling[1]}\n")

cycle = cycle_factorial(number)
print(f"Факториал циклом:\n{cycle[0]}\n{cycle[1]}")

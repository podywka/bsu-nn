import math
import random
import os

# ---------------- a ----------------

def log2_value(x):
    """Вычисляет логарифм по основанию 2"""
    return math.log2(x)

# пример использования
x = 15
print("a - log2(15) =", log2_value(x))


# ---------------- b ----------------

def repeat_random(n=4):
    """Генерирует одно случайное число и повторяет его n раз"""
    val = random.random()
    return [val]*n

# пример использования
print("b - 4 одинаковых случайных числа:", repeat_random(4))


# ---------------- c ----------------

def current_defined_names():
    """Возвращает список текущих имен в глобальном пространстве"""
    return list(globals().keys())

# пример использования
print("c - текущие имена:", current_defined_names())


# ---------------- d ----------------

def create_and_use_module():
    from module import greet 
    return greet("Иван")

# пример использования
print("d - использование собственного модуля:", create_and_use_module())

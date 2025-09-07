import math

# ---------------- a ----------------

def distance(x1, y1, x2, y2):
    """Вычисляет расстояние между точками (x1,y1) и (x2,y2)"""
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

# пример использования
x1, y1, x2, y2 = 1.0, 2.0, 4.0, 6.0
print("1a:", distance(x1, y1, x2, y2))  # 5.0


# ---------------- b ----------------

def power(a, n):
    """Возводит число a в степень n без использования **"""
    result = 1
    for _ in range(abs(n)):
        result *= a
    if n < 0:
        result = 1 / result
    return result

# пример использования
a, n = 2.0, 3
print("1b:", power(a, n))  # 8.0

# ---------------- c ----------------

def capitalize(word):
    """Меняет первую букву слова на заглавную"""
    if not word:
        return ""
    first = chr(ord(word[0]) - 32) if 'a' <= word[0] <= 'z' else word[0]
    return first + word[1:]

# пример использования на строке
text = "hello world python"
capitalized_text = ' '.join(capitalize(w) for w in text.split())
print("1c:", capitalized_text)  # Hello World Python


# ---------------- d ----------------

def my_max(*args):
    """Возвращает максимум из переменного числа аргументов"""
    if not args:
        raise ValueError("Нет аргументов для сравнения")
    max_val = args[0]
    for val in args[1:]:
        if val > max_val:
            max_val = val
    return max_val

# пример
print("1d:", my_max(3, 7, 2, 5))  # 7


# ---------------- e ----------------

def distance_safe(x1, y1, x2, y2):
    """Вычисляет расстояние с обработкой исключений"""
    try:
        # проверка, что все входные данные можно преобразовать к float
        x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    except ValueError:
        print("Ошибка: введены не числовые значения")
    except TypeError:
        print("Ошибка: неверный тип данных")
    except Exception as e:
        print("Другая ошибка:", e)

# пример использования
print("1e:", distance_safe(1, 2, "a", 6))  # Ошибка: введены не числовые значения

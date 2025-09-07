# a) Сколько чисел одновременно в двух списках
list1 = [1,2,3,4]
list2 = [3,4,5,6]
common_count = len(set(list1) & set(list2))
print("2a:", common_count)

# b) Для последовательности чисел выводим YES/NO
def seen_numbers(sequence):
    seen = set()
    result = []
    for num in sequence:
        if num in seen:
            result.append("YES")
        else:
            result.append("NO")
            seen.add(num)
    return result

seq = [1,2,3,2,1,4]
print("2b:", seen_numbers(seq))

# c) Цвета кубиков Ани и Бори
def cube_colors(ana, borya):
    ana_set = set(ana)
    borya_set = set(borya)
    both = sorted(ana_set & borya_set)
    only_ana = sorted(ana_set - borya_set)
    only_borya = sorted(borya_set - ana_set)
    return (len(both), both, len(only_ana), only_ana, len(only_borya), only_borya)

ana = [1,2,3,4]
borya = [3,4,5,6]
print("2c:", cube_colors(ana, borya))

# d) Возможные числа Августа
def possible_numbers(n, queries):
    possible = set(range(1, n+1))
    for numbers, answer in queries:
        numbers_set = set(numbers)
        if answer == "YES":
            possible &= numbers_set
        else:
            possible -= numbers_set
    return sorted(possible)

n = 10
queries = [
    ([1,2,3], "NO"),
    ([2,3,4], "YES"),
    ([4,5,6], "YES")
]
print("2d:", possible_numbers(n, queries))

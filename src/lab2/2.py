def smallest_divisor(n):
    i = 2
    while i <= n:
        if n % i == 0:
            return i
        i += 1


def calculate_day(x, y):
    distance = x
    day = 1
    while distance < y:
        distance += distance * 0.1
        day += 1

    return day


def calculate_years(x, p, y):
    years = 0

    while x < y:
        x += x * (p / 100)
        x = int(x * 100) / 100
        years += 1

    return years


def fibonacci_number_index(a):
    if a == 0:
        return 0

    fib_prev = 0
    fib_curr = 1
    index = 1

    while fib_curr < a:
        fib_temp = fib_curr
        fib_curr += fib_prev
        fib_prev = fib_temp
        index += 1

    if fib_curr == a:
        return index
    else:
        return -1

print("Smallest divisor:", str(smallest_divisor(55)))   

print("Days need:", str(calculate_day(100, 200)))

print("Years need:", str(calculate_years(10, 11, 100)))

print("Index:", str(fibonacci_number_index(55)))

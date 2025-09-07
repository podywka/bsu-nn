def maxOf3(a, b, c):
    return max(a, b, c)


def equalsNumbers(a, b, c):
    if a == b == c:
        return 3
    elif a == b or a == c or b == c:
        return 2
    else:
        return 0


def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def canRookMove(start_col, start_row, end_col, end_row):
    if start_col == end_col or start_row == end_row:
        return "YES"
    else:
        return "NO"
    
a, b, c = list(map(int, input("ВВЕДИТЕ a,b,c: ").split()))
print("max of 3:", maxOf3(a,b,c))

print("count of equals numbers:", equalsNumbers(a,b,c))

y = int(input("ВВЕДИТЕ y: "))
print("is year leap:", isLeapYear(y))

x1, y1, x2, y2 = list(map(int, input("ВВЕДИТЕ x1,y1,x2,y2: ").split()))
print("the rook:", canRookMove(x1, y1, x2, y2))

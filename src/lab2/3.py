def getLastDigit(number):
    return number % 10

def getFractionalPart(x):
    return x%1

def getFirstDecimalDigit(x):
    fractional_part = x - int(x)
    return int(fractional_part * 10)

def round(x):
    fractional_part = x - int(x)

    if fractional_part < 0.5:
        return int(x)
    else:
        return int(x) + 1

print("Last digit:", getLastDigit(1213136))

print("Fractional part:", getFractionalPart(12.312321312))

print("First decimal Digit:", getFirstDecimalDigit(12.312321312))

print("Rounded:", round(12.412321312))

import random

# Выведите все элементы списка с четными индексами
def getEvenIndex(A):
    return A[::2]

# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
def swapMinMax(numbers):
    minIndex = numbers.index(min(numbers))
    maxIndex = numbers.index(max(numbers))
    numbers[minIndex], numbers[maxIndex] = numbers[maxIndex], numbers[minIndex]

# Дан список-массив, заполненный случайным образом нулями и единицами (сформируйте его). 
# Найдите самую длинную непрерывную последовательность единиц и определите индексы первого и последнего элементов в ней.
def findLongestSequenceIndexes(array):
    maxLength = 0
    maxStart = 0
    maxEnd = 0

    currLength = 0
    currStart = 0

    for i in range(len(array)):
        if array[i] == 1:
            currLength += 1
            if currLength == 1:
                currStart = i
            if currLength > maxLength:
                maxLength = currLength
                maxStart = currStart
                maxEnd = i
        else:
            currLength = 0

    return maxStart, maxEnd


print("Even index numbers: ", getEvenIndex([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

numbers = [1, 2, 3, 4, 5, 6, 7]
swapMinMax(numbers)
print("Swapped min max elements in array: ", numbers)

arr = [random.choice([0, 1]) for _ in range(10)]
print(arr)
start, end = findLongestSequenceIndexes(arr)
print("First index:", start, "Last index:", end)

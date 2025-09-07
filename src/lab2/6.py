import random

# Определите: сколько гласных и сколько согласных букв в строке.
def count_vowels_consonants(string):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowelCount = 0
    consonantCount = 0

    for char in string.lower():
        if char in vowels:
            vowelCount += 1
        elif char in consonants:
            consonantCount += 1

    return vowelCount, consonantCount

# Дано предложение, слова которого отделены пробелами, в конце предложения точка. Напишите каждое слово, начиная его с большой буквы и заканчивая точкой.
def divideWordsFromSentence(sentence):
    return sentence.title().replace(' ', '. ')

# Дана строка. Определите частоту, с которой входят разные буквы в эту строку.
def letterFrequency(string):
    frequency = {}

    for letter in string:
        if letter.isalpha():
            if letter in frequency:
                frequency[letter] += 1
            else:
                frequency[letter] = 1

    return frequency

# Дана строка. Группы символов между пробелами считаются словами. Определите сколько слов начинается и заканчивается одной и той же буквой.
def wordsWithSameStartEnd(string):
    words = string.split()
    count = 0

    for word in words:
        if word[0].lower() == word[-1].lower():
            count += 1

    return count

# В списке перепишите все ненулевые элементы в начало списка (сохраняя порядок), а нулевые - в конец.
def rearrangeList(lst):
    noZeros = [x for x in lst if x != 0]
    zeros = [x for x in lst if x == 0]
    result = noZeros + zeros
    return result

# Получите список из положительных элементов другого списка, стоящих на четных местах.
def getPositiveElemAtEvenPos(lst):
    result = [x for i, x in enumerate(lst) if i % 2 == 0 and x > 0]
    return result

print("Task a")
vowels, consonants = count_vowels_consonants("Hello, world")
print("Hello, world")
print("Vowels:", vowels, "Consonants:", consonants)

print("Task b")
sentence = "hello my world."
print(sentence)
print(divideWordsFromSentence(sentence))

print("Task c")
string = "Hello, World!"
print(string)
frequency = letterFrequency(string)
for letter, count in frequency.items():
    print(f"{letter}: {count}")

print("Task d")
string = "aunt pop lol bob man"
print(string)
count = wordsWithSameStartEnd(string)
print("Words that starts and ends with same letter:", count)

print("Task f")
myList = [4, 0, 2, 0, 1, 0, 3, 0, 5]
print("List:", myList)
rearrangeList = rearrangeList(myList)
print("Rearranged List:", rearrangeList)

print("Task g")
myList = [1, 2, 0, 5, -3, 7, 9]
print("List:", myList)
print("Positive elements at even positions:", getPositiveElemAtEvenPos(myList))

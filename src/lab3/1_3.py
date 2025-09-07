from collections import defaultdict, Counter

# a) Подсчет повторов слов
def word_repeats(text):
    words = text.split()
    counts = defaultdict(int)
    result = []
    for w in words:
        result.append(counts[w])
        counts[w] += 1
    return result

text = "hi hi what is hi"
print("3a:", word_repeats(text))

# b) Синонимы
def find_synonym(pairs, word):
    d = {}
    for w1, w2 in pairs:
        d[w1] = w2
        d[w2] = w1
    return d[word]

pairs = [("big","large"),("small","tiny")]
print("3b:", find_synonym(pairs, "big"))

# c) Слово с максимальной частотой
def most_common_word(lines):
    words = []
    for line in lines:
        words.extend(line.split())
    c = Counter(words)
    max_count = max(c.values())
    max_words = [w for w in c if c[w]==max_count]
    return min(max_words)

lines = ["hi hi what", "is hi"]
print("3c:", most_common_word(lines))

# d) Все слова с частотами, сортировка по убыванию и лексикографически
def all_words_sorted(lines):
    words = []
    for line in lines:
        words.extend(line.split())
    c = Counter(words)
    lst = [(-freq, word) for word, freq in c.items()]
    lst.sort()
    return [word for freq, word in lst]

lines = ["hi hi what", "is hi"]
print("3d:", all_words_sorted(lines))

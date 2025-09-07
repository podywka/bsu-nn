import os

# ---------------- a ----------------

def write_surnames(filename, surnames):
    """Записывает список фамилий в текстовый файл"""
    with open(filename, "w", encoding="utf-8") as f:
        for s in surnames:
            f.write(s + "\n")

def read_file(filename):
    """Считывает весь файл и возвращает список строк"""
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]

# пример использования
surnames = ["Иванов", "Петров", "Сидоров", "Кузнецов"]
filename_surnames = "surnames.txt"
write_surnames(filename_surnames, surnames)
print("a - содержимое файла surnames.txt:")
print("\n".join(read_file(filename_surnames)))


# ---------------- b ----------------

def print_surnames_numbered(filename):
    """Выводит фамилии из файла с порядковым номером"""
    lines = read_file(filename)
    for i, line in enumerate(lines, 1):
        print(f"{i}. {line}")

# пример использования
print("b - фамилии с номерами:")
print_surnames_numbered(filename_surnames)


# ---------------- c ----------------

def write_fullnames(filename, fullnames):
    """Записывает список полных имён в файл"""
    with open(filename, "w", encoding="utf-8") as f:
        for name in fullnames:
            f.write(name + "\n")

def print_file_lines(filename):
    """Выводит строки файла построчно"""
    for line in read_file(filename):
        print(line)

# пример использования
fullnames = ["Иван Иванов", "Петр Петров", "Сидор Сидоров", "Кузьма Кузнецов"]
filename_fullnames = "fullnames.txt"
write_fullnames(filename_fullnames, fullnames)
print("c - полные имена:")
print_file_lines(filename_fullnames)


# ---------------- d ----------------

def print_surname_initial(filename):
    """Выводит фамилию и первую букву имени"""
    for line in read_file(filename):
        parts = line.split()
        if len(parts) >= 2:
            print(f"{parts[1][0]}. {parts[0]}")  # I. Иванов

# пример использования
print("d - фамилия и первая буква имени:")
print_surname_initial(filename_fullnames)

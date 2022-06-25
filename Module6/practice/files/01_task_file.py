# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле.
# Пробельные символы: " " - пробел, "\n" - перенос строки, "\t" - табуляция
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется ровно одной пустой строкой от предыдущего и после последнего нет пустой строки

path = "files/limericks.txt"  # вместо dir подставь название папки с файлом.
# Или удалите dir, если limericks.txt в той же папке, что и текущий файл

# Открываем файл на чтение
f = open(path, "r", encoding="utf-8")
# В переменную line считываем строку за стройкой из файла(f)
n = 0
count = 0
for line in f:
    print(line.rstrip())
    count = count + len(line) - line.count("\n") - line.count(" ")
    if line == "\n":
        n += 1
print("Количество непробельных символов: ", count)
print("Количество стихотворений: ", n)

# Подсказка: пустые строки выглядят так "\n". Помните? Строка считывается вместе с символом переноса!
# Применение метода "\n".rstrip() --> "" вернет вам пустую строку, строку из НУЛЯ символов.

# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

import random
n = int(input("Введите n: "))
list = []
summa = 0
num = 0
for _ in range(n):
    num = random.randint(-10, 10)
    list.append(num)
    summa += num
print(list)
print(summa)


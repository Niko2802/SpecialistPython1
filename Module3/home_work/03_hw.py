# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

numbers = []
n = int(input("Введите n: "))
a = 0
s = 0
while a < n:
    numbers.append(random.randint(-100, 100))
    a += 1
print(numbers)
for item in numbers:
    if item > 0 and (item % 2 == 0):
        s = s + item
print(s)

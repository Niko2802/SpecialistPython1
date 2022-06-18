# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("first number - "))     # Первое число
second_number = int(input("second number - "))    # Второе число
numbers = []
numbers3 = []
if first_number > second_number:
    first_number, second_number = second_number, first_number
for num in range(first_number, second_number):
    numbers.append(num)
    if num % 3 == 0:
        numbers3.append(num)
print(numbers)
print(numbers3)

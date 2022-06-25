# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def gen_list(size=10, of=1000, to=1000000):
    import random
    list1 = []
    for _ in range(size):
        list1.append(random.randint(of, to))
    return list1


def palindrome(number):
    number = str(number)
    reversed_number = number[::-1]
    if number == reversed_number:
        return True
    return False


a = 1000
b = 500000
numbers = gen_list(10, a, b)
i = 0
for el in numbers:
    if palindrome(el):
        i += 1
print(numbers)
print(i)

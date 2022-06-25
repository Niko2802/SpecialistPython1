# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    number = str(number)
    reversed_number = number[::-1]
    if number == reversed_number:
        return True
    return False


print(palindrome(123321))

# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

def gen_list(size, of, to):
    import random
    list1 = []
    for _ in range(size):
        list1.append(random.randint(of, to))
    return list1


print(gen_list(10, -100, 100))

## "Логирование в файл"

### Задание

Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла

### Формат входных данных

Функция должна уметь записывать строки в файл.

### Формат выходных данных

Программа ничего не выводит в терминал, все сообщения записываются в указанный файл или в файл по умолчанию.

### Решение задачи

```python
def log(text, file="log.txt"):
    f = open(file, "a", encoding="utf-8")
    f.write(text + "\n")
    f.close()


log("hello world")  # дописывает "hello world" в конец файла log.txt
log("message", "log01.txt")  # дописывает "message" в конец файла log01.txt

```

---

### Подсказки

<details>
<summary>Подсказка-1</summary>
Т.к. вам нужно дописывать информацию, открывайте файл на "дозапись" используя ключ "a".

Предварительно изучите, как работает программа, пытаясь дописать информацию в файл, которого нет.
</details>
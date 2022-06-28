# Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла

def log(text, file="log.txt"):
    f = open(file, "r", encoding="utf-8")
    text_from_file = []
    for line in f:
        text_from_file.append(line.rstrip())
        print(text_from_file)
    f.close()
    f = open(file, "w", encoding="utf-8")
    for line in text_from_file:
        f.write(line + "\n")
    f.write(text + "\n")
    f.close()


log("hello world")  # дописывает "hello world" в конец файла log.txt
log("message", "log01.txt")  # дописывает "message" в конец файла log01.txt

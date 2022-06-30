## "Обработка списка фруктов"

### Задание

Дана ведомость расчета заработной платы [data/workers.txt](data/workers.txt).

Рассчитайте зарплату всех работников, зная что они получат полный оклад, если отработают норму часов. \
Если же они отработали меньше нормы, то их ЗП уменьшается пропорционально, \
а за каждый час переработки они получают удвоенную ЗП, пропорциональную норме. \
Кол-во часов, которые были отработаны, указаны в файле ["data/hours_of.txt](data/hours_of.txt)

### Формат входных данных

Дано два текстовых файла. Один с информацией о сотрудниках, второй с количеством отработанных часов.

Гарантируется, что каждый сотрудник имеет уникальную фамилию(однофамильцев нет).

### Формат выходных данных

Выведите зарплату сотрудников с учетом переработки и недоработки.

### Решение задачи

```python
with open("data/workers.txt", "r", encoding="utf-8") as f:
    for line in f:
        name_workers, surname_workers, salary_workers, job_workers, normal_hours_workers = line.strip().split()
        with open("data/hours_of.txt", "r", encoding="utf-8") as f_hours:
            for line_of in f_hours:
                name_hours_of, surname_hours_of, hours_hours_of = line_of.strip().split()
                if name_workers == name_hours_of and surname_workers == surname_hours_of and name_workers != "Имя":
                    if int(normal_hours_workers) < int(hours_hours_of):
                        salary_total = int(salary_workers) + (int(hours_hours_of) - int(normal_hours_workers)) * int(
                            salary_workers) / int(normal_hours_workers) * 2
                    else:
                        salary_total = int(hours_hours_of) * int(salary_workers) / int(normal_hours_workers)
                    print(f"{name_workers} {surname_workers} заработал {salary_total:.2f}")

```

---

# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    len_ticket_number = len(ticket_number)
    if len_ticket_number != 6:
        return False
    ticket_number_list = []
    for item in ticket_number:
        ticket_number_list.append(item)
    sum_begin = 0
    sum_end = 0
    sum_begin = int(ticket_number_list[0]) + int(ticket_number_list[1])
    sum_end = int(ticket_number_list[len_ticket_number - 1]) + int(ticket_number_list[len_ticket_number - 2])
    if sum_begin == sum_end:
        return True
    return False



# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(436752))

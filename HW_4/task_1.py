"""
Выведите список простых множителей натурального числа N.
Ввод: значение типа <int>
Вывод: значение типа <list>

Примеры:
20
[2, 2, 5]

38
[2, 19]
"""

num = int(input('Введите натуральное число: '))
result_list = []
digit = 2
while digit ** 2 <= num:
    if num % digit == 0:
        result_list.append(digit)
        num //= digit
    else:
        digit += 1
if num > 1:
    result_list.append(num)
print(result_list)

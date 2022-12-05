"""
Задайте список случайных чисел. Выведите список чисел, которые не повторяются в заданном списке.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>

Пример:
[1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
[2, 4, 6, 8]
"""

from random import randrange

size_list = int(input('Введите размер списка: '))
rand_list = [randrange(9) for i in range(size_list)]
result_list = []
print(rand_list)
for i in range(size_list):
    if rand_list.count(rand_list[i]) == 1:
        result_list.append(rand_list[i])
print(result_list)

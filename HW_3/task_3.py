"""
Задайте список из вещественных чисел, округленных до сотых.
Найдите разницу между максимальным и минимальным значением дробной части элементов.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <float>

Пример:
[1.1, 1.2, 3.1, 5, 10.01]
2.0
"""

import random
list_size = int(input('Введите размерз списка: '))
list_float_nums = [round(random.uniform(0, 20), 2) for i in range(list_size)]
tmp_list = [round(list_float_nums[i_tmp] - int(list_float_nums[i_tmp]), 2) for i_tmp in range(list_size)]
print(f'Рандомный список: {list_float_nums}')
print(max(tmp_list) - min(tmp_list))

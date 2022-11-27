"""
Задайте список из N элементов, заполненный целыми числами из промежутка [-N, N].
Найдите произведение элементов на индексах, хранящихся в файле indexes.txt (в одной строке один индекс).
Решение должно работать при любом натуральном N.

Ввод: значение типа <int>
Вывод: значение типа <int>
"""

# file_name = 'HW_2/indexes.txt'

# with open(file_name, 'w', encoding='utf-8') as file:

#     file.writelines()

import random

n = int(input('Укажите длину списка: '))
my_list = [random.randint(-n, n) for i in range(n)]
result = 1
for i in range(n):
    file_indexes = 'HW_2/indexes.txt'
    with open(file_indexes) as file_indexes:
        
            for line in file_indexes:
                x = int(line)
                if i == x:
                    result = my_list[i] * result
                    print(my_list[i], result)
                    print(x)
print(my_list, result)

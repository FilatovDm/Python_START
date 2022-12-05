"""
Задать натуральное число k.
Сформируйте многочлен (полином) степени k со случайными коэффициентами из промежутка от 0 до 100, включительно.
Многочлен вывести в консоль и записать в файл.

Ввод: значение типа <int>
Вывод: значение типа <str>, файл с одной строкой.

Пример:
2
2x^2 + 4x + 5 = 0
"""
from random import randrange
k = int(input('Введите значение k: '))
polynomial = str(randrange(100)) + ' = 0'

if k > 0:
    koef = randrange(100)
    if koef != 0: polynomial = f'{koef}x + ' + polynomial
    for i in range(2, k + 1):
        koef = randrange(100)
        if koef != 0:
            polynomial = f'{koef}x^{i} + ' + polynomial

print(polynomial)

with open('polynomial_1.txt', 'w') as file:
    file.write(polynomial)

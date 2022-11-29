"""
Задайте целое число N.
Составьте список чисел Фибоначчи размерность 2N + 1 для отрицательной и положительной части (Негафибоначчи).
https://ru.wikipedia.org/wiki/Негафибоначчи

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
8
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

n = int(input('Введите целое число N: '))
fib_list = [0] * (2 * n + 1)
fib_list[n + 1], fib_list[n - 1] = 1, 1
koef = -1
for i in range(n + 2, 2 * n + 1):
    fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
    fib_list[-i - 1] = fib_list[i] * koef
    koef *= -1
print(fib_list)

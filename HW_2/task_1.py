"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Ввод: значение типа <float>
Вывод: значение типа <int>

Примеры:
6782.0
23

0.56
11
"""
num = float(input('Введите число: '))
str_num = str(num)
sum = 0
for i in range(len(str_num)):
    if str_num[i].isdigit():
        sum += int(str_num[i])
print(sum)

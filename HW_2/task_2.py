"""
Напишите программу, которая принимает на вход натуральное число N и выдает список факториалов по основаниям от 1 до N

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
4
[1, 2, 6, 24]
"""
# Ниже закоменчен тоже рабочий код
# num = int(input('Введите натуральное число: '))
# count, fact_list = 2, [1]
# for i in range(num - 1):
#     fact_list.append(fact_list[i] * count)
#     count += 1
# print(fact_list)

num = int(input('Введите натуральное число: '))
fact_list = [1] * num
for i in range(1, num):
    fact_list[i] = fact_list[i - 1] * (i + 1)
print(fact_list)
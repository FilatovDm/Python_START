"""
Напишите программу, удаляющую из текста все слова, в которых присутствуют буквы «а», «б» и «в».

Ввод: значение типа <str>
Вывод: значение типа <str>
"""

stroke = 'азбука автобус автомобиль аптека библиотека'
words = 'абв'

result = ' '.join(filter(lambda x: not (words[0] in x and words[1] in x and words[2] in x), stroke.split()))
print(result)

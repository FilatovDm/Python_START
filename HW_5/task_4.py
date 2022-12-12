"""
Реализуйте RLE алгоритм шифрования строки: замените повторяющиеся символы строки на один символ и число его повторов.
На первом месте идет количество повторов, на втором сам символ.
Восстановите строку после шифрования.

Ввод: значения типа <str>, можно получить из файла.
Вывод: значение типа <str>, можно записать в файл.

Примеры:
ыыыыыррррр   аааааагггггггг
5ы5р3 6а8г
"""

input_line = input()
count = 1
new_line = ''

for i in range(1, len(input_line)):
    if input_line[i] == input_line[i - 1]:
        if count == 9:
            new_line += str(count) + input_line[i-1]
            count = 1
        count += 1
    else: 
        new_line += str(count) + input_line[i-1]
        count = 1
        continue

new_line += str(count)  + input_line[-1]      
print(new_line)

def decoding(code):
    decode = ''
    for i in range(0, len(code), 2):
        count2, symbol = code[i: i + 2]
        decode += symbol * int(count2)
    return decode
print(decoding(new_line))

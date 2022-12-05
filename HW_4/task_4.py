"""
Даны файлы, в каждом из которых находится запись многочлена.
Найти сумму многочленов из файлов, ввести в консоль и записать в файл.
Входными данными для этой задачи являются выходные данные их предыдущей.

Ввод: значения типа <str>, полученные из файлов.
Вывод: значение типа <str>, файл с одной строкой.

Примеры:
9x^5+7x^4+7x^3+9x^2+6x+17=0
3x^2+2x+1=0
9x^5+7x^4+7x^3+12x^2+8x+18=0
"""

with open('polynomial.txt', 'r', encoding='utf-8') as file:
    polynominal = file.read()
with open('polynomial_1.txt', 'r', encoding='utf-8') as file:
    polynominal_1 = file.read()

poly_list = polynominal.split(' + ')
poly_list[-1] = poly_list[-1].replace(' = 0', '')

poly_list_1 = polynominal_1.split(' + ')
poly_list_1[-1] = poly_list_1[-1].replace(' = 0', '')

if len(poly_list) > len(poly_list_1):
    max_poly_list = poly_list
else: max_poly_list = poly_list_1
poly_result = []

for i in range(1, max(len(poly_list), len(poly_list_1)) ):
    if poly_list[-i].find('x') < 0:
        poly_result.append(int(poly_list[-i]) + int(poly_list_1[-i]))
        continue
    poly_result.append(str(int(poly_list[-i][:poly_list[-i].find('x')]) 
                       + int(poly_list_1[-i][:poly_list_1[-i].find('x')])) 
                       + poly_list[-i][poly_list[-i].find('x'):])
poly_result.append(max_poly_list[0])    
poly_result = poly_result[::-1]

result = ' + '.join(map(str, poly_result)) + ' = 0'
print(result)
with open('result_poly.txt', 'w', encoding='utf-8') as file:
    file.write(result)

# # P.S.: Я понимаю, что данное решение не на 100% выполняет поставленные требования.
# Если какой-либо коэффициент при каком-либо "x" будет равен 0, то сложение многочленов будет не корректным,
# но мозгов у меня пока не хватило, чтобы сделать правильно.
# И вообще считаю, что я куда-то не в том направлении думаю при решении этой задачи

"""
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
По возможности реализуйте использования скобок, меняющих приоритет операций.

Ввод: значение типа <str>
Вывод: значение числового типа данных
"""


def find(exp, search_operand):
    ind_start, ind_finish, ind_operand = 0, 0, 0
    operands_full = ['*', '/', '+', '-']
    operands = ['*', '/', '+', '-']
    for op in search_operand:
        operands.remove(op)
    found = False
    for i, sym in enumerate(exp):
        if i == 0 and sym == '-':
            continue
        if not found and sym in operands:
            ind_start = i + 1
        elif found and sym in operands_full:
            ind_finish = i - 1
            return ind_start, ind_finish, ind_operand
        elif sym in search_operand:
            found = True
            ind_operand = i
            ind_finish = len(exp) - 1
    return ind_start, ind_finish, ind_operand

def calc(exp):
    if '*' in exp or '/' in exp:
        ind_s, ind_f, ind_o = find(exp, ['*', '/'])
        if exp[ind_o] == '*':
            exp = exp[:ind_s] + str(float(exp[ind_s: ind_o]) * float(exp[ind_o + 1: ind_f + 1])) + exp[ind_f + 1:]
            exp = calc(exp)
        elif exp[ind_o] == '/':
            exp = exp[:ind_s] + str(float(exp[ind_s: ind_o]) / float(exp[ind_o + 1: ind_f + 1])) + exp[ind_f + 1:]
            exp = calc(exp)
    if '+' in exp or '-' in exp:
        ind_s, ind_f, ind_o = find(exp, ['+', '-'])
        if exp[ind_o] == '+':
            exp = exp[:ind_s] + str(float(exp[ind_s: ind_o]) + float(exp[ind_o + 1: ind_f + 1])) + exp[ind_f + 1:]
            exp = calc(exp)
        elif exp[ind_o] == '-':
            exp = exp[:ind_s] + str(float(exp[ind_s: ind_o]) - float(exp[ind_o + 1: ind_f + 1])) + exp[ind_f + 1:]
            exp = calc(exp)
    return exp

if __name__ == '__main__':
    exp = '3*4/2'
    print(calc(exp))


# Ниже реализация из сети, решил оставить здесь для себя, вдруг потом пригодится.

# import re

# actions = {
#   "^": lambda x, y: str(float(x)**float(y)),
#   "*": lambda x, y: str(float(x) * float(y)),
#   "/": lambda x, y: str(float(x) / float(y)),
#   "+": lambda x, y: str(float(x) + float(y)),
#   "-": lambda x, y: str(float(x) - float(y))
# }
 
# priority_reg_exp = r"\((.+?)\)"
# action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"
 
#     while (match := re.search(priori
# def my_eval(expresion: str) -> str:ty_reg_exp, expresion)):
#         expresion: str = expresion.replace(match.group(0), my_eval(match.group(1))) 
#     for symbol, action in actions.items():
#         while (match := re.search(action_reg_exp.format(symbol), expresion)):
#             expresion: str = expresion.replace(match.group(0), action(*match.groups())) 
#     return expresion
  
# exp = "(1 + 4) * (5 * (10 - 2)) / 5"
# print(my_eval(exp), eval(exp))

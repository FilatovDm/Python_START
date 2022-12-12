"""
Реализуйте код игры.
Правила игры: на столе лежит N количество конфет. Играют два игрока, делая ход друг после друга.
Первый ход определяется жеребьёвкой, то есть случаен. За один ход можно забрать не более чем k конфет.
Не брать конфеты НЕЛЬЗЯ. Побеждает тот, кто сделал последний ход, то есть забрал со стола остатки конфет.
Он забирает также все конфеты оппонента.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего оппонента?

a) Добавьте игру против бота
b) Подумайте, как наделить бота простейшим "интеллектом"
"""

from random import randint

def input_dat(name, max_candy):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до {max_candy}: "))
    while x < 1 or x > max_candy:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, took, counter, value):
    print(f"Ходил {name}, он взял {took}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
N = int(input("Введите количество конфет на столе: "))
max_candy = int(input("Введите максимальное количество конфет, которое можно взять за одни ход: "))
flag = randint(0,2)
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while N > max_candy:
    if flag:
        took = input_dat(player1, max_candy)
        counter1 += took
        N -= took
        flag = False
        p_print(player1, took, counter1, N)
    else:
        took = input_dat(player2, max_candy)
        counter2 += took
        N -= took
        flag = True
        p_print(player2, took, counter2, N)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

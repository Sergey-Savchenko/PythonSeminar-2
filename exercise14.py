# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

numb = int(input('Введите Предельное число: '))
i = 2
stepen = 2
while i<=numb:
    print(i)
    i=2**stepen
    stepen+=1
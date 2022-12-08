# 3'. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import os
os.system('clear')
from random import randint as rnd

mass = [rnd(1, 10) for i in range(12)]
print(f'Исходный список: {mass}')
print(f'Список уникальный элементов: {list(set(mass))}')
mass = [i for i in mass if mass.count(i) == 1]
print(f'Список из неповторяющихся элементов: {mass}')

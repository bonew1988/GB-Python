# 3'. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import os
os.system('clear')
a = [1.1, 1.2, 3.1, 5, 10.01]
b = [round(i % 1, 2) for i in a if i % 1 != 0]
print(f'Исходный список: {a}')
print(f'Разницу между максимальным и минимальным значением дробной части {max(b)} - {min(b)}')

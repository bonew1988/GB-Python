# 1'. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import os
# os.system('clear')
# a = [1, 2, 3, 4, 5, 65, 48, 12, 39, 18, 969, 348]
# sum = 0
# print(f'Исходный список {a}')
# print(f'Элементы нa нечетных позициях: ', end='')
# for i in range(1, len(a), 2):
#     print(f'{a[i]} ', end='')
#     sum += a[i]
# print()
# print(f'Сумма выбранных элементов: {sum}')


import os
os.system('clear')
a = [1, 2, 3, 4, 5, 65, 48, 12, 39, 18, 969, 348]
b = sum([a[i] for i in range(1, len(a), 2)])
print(f'{a} --> {b}')

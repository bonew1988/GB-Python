# 1'. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

import os
os.system('clear')
a = str(input('Введите вещественное число: '))
num_sum = 0
for i in range(len((a))):
    if a[i] == '-' or a[i] == '.':
        continue
    else:
        num_sum += int(a[i])
print(num_sum)
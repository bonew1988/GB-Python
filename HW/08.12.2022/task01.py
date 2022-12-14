# 4'. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*

# - 45 -> 101101 не проходит условие')
# elif (a % 5 == 0)
# - 3 -> 11
# - 2 -> 10

# import os
# os.system('clear')
# num = int(input('Введите число: '))
# print(bin(num)[2::])

import os
os.system('clear')
num = lambda x: bin(int(x))
print(num(input('Введите число: '))[2::])

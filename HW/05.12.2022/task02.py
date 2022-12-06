# 2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [1,2,3]
# * 144 -> [2,3]

import os
os.system('clear')
a = int(input("Введите натуральное число: "))
i = 2 # первое простое число
lst = []
print(f'Простые множители числа {a}: ', end='')
while i <= a:
    if a % i == 0:
        lst.append(i)
        a //= i
        i = 2
    else:
        i += 1
lst1 = list(set(lst))
newlst = sorted(lst1)
print(newlst)

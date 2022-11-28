# 4'. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2
# Позиции: 0,1 -> 2

import os
os.system('clear')
from random import randint

def genlist(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list

n = int(input('Введите число N: '))
list1 = genlist(n)
print(list1)
x = open('file.txt','r')
result = list1[int(x.readline())]*list1[int(x.readline(2))]
print(result)
x.close()

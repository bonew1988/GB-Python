# 5'. Реализуйте алгоритм перемешивания списка.

import os
os.system('clear')
from random import randint
import random

n = int(randint(5 , 10))
list1 = []
for i in range(n):
    k = int(randint(10,15))
    list1.append(k)
print(f'Исходный список:{list1}')
random.shuffle(list1)
print(f'Перемешанный список:{list1}')
# Задача 2.

# На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))

# Ввод:
# house=дом car=машина men=человек tree=дерево
# Вывод:
# (('house', 'дом'), ('car', 'машина'), ('men', 'человек'), ('tree', 'дерево'))

# import os
# os.system('clear')

# str1 = 'house=дом car=машина men=человек tree=дерево'.split()
# print(str1)
# str2 = []
# str2 = tuple(map(lambda x: tuple(x.split('=')), str1))

# print(str2)

import os
os.system('clear')
str1 = ('house=дом car=машина men=человек tree=дерево'.split())
str2 = sum(list(map(lambda x: x.split('='), str1)), [])
num1 = str2[::2]
num2 = str2[1::2]
zipped_values = zip(num1, num2)
zipped_tuple = tuple(zipped_values)
print(zipped_tuple)

# 1'. Вычислить число Пи c заданной точностью d

# *Пример:* 

# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  

import os
os.system('clear')

from math import pi
a = str(input('Введите точность числа Pi в формате "0.001; 0.0001; и т.д": '))
b = a[2:len(a)]
print(round(pi, len(b)))

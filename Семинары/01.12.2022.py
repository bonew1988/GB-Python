# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

# mylist = input('Введите данные для списка: ').split()
# print(f'Максимальный элемент: {max(mylist)} ; Минимальный элемент: {min(mylist)}')


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения (D = b^2-4ac, x1 = (-b+/- sqtr(D))/a)
# 2) с помощью дополнительных библиотек Python(sympy, scipy)(Дополнительно)

# # import cmath

# a = float(input('Input A: '))
# b = float(input('Input B: '))
# c = float(input('Input C: '))

# d = (b**2) - (4*a*c)
# if d > 0:
#     x1 = (-b-cmath.sqrt(d))/(2*a)
#     x2 = (-b+cmath.sqrt(d))/(2*a)
#     print(x1, x2)
# elif d == 0:
#     x = -b / (2 * a)
#     print(x)
# else:
#     print('Корней нет')


# # второвй вариант решение через библиотеку
# # import sympy

# # x = sympy.Symbol('x')
# # a = input('Input eq:')
# # solution = sympy.solve(a, x)
# # print(solution)




# # 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# # Пример:
# # 4, 5 -> 20
# # 7,10 -> 70


# def nok(x, y):
#     if x > y:
#         max = x
#     else:
#         max = y
#     while(True):
#         if (max % x == 0) and (max % y == 0):
#             i = max
#             break
#         max += 1
#     return i
# num1 = int(input("Enter first digit: "))
# num2 = int(input("Enter second digit: "))
# print(nok(num1, num2))

# второй вариант решения

# import math
# n = 14
# m = 21

# print((n * m) // math.gcd(n , m))

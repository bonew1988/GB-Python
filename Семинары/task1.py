# Квадрат числа
# a = int(input())
# print(f'Квадрат числа: {a**2}')

# Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.

# a = int(input())
# b = int(input())
# if a == b**2 or a**2 == b:
#    print(f'Является')
# else:
#    print(f'Не является')

# Программа на вход 5 чисел и поиск максимального из них

# max = int(input())
# for i in range(4):
#     b = int(input())
#     if b > max:
#         max = b
# print(max)

# решение через список

# a = list(map(int, input().split()))
# print(max(a))

# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
#    
#    *Примеры:* 
#    
#    - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# a = int(input())
# for i in range(-a,a+1):
#    print(i, end=' ')


# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#    
#    *Примеры:*
#    
#    - 6,78 -> 7
#    - 5 -> нет
#    - 0,34 -> 3

a = float(input())
n = int(a*10 % 10)
if n == 0:
    print(f'НЕТ')
else:
    print(n)



# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
# a = int(input('Введите число: '))
#
# if (a % 30 == 0):
#     print(f'Число не проходит условие')
# elif (a % 5 == 0) and (a % 10 == 0):
#     print(f'Число проходит условие')
# elif (a % 15 == 0):
#     print(f'Число проходит условие')
# else:
#     print(f'Число не проходит условие')



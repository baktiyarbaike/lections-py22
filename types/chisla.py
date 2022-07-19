# Тип данных int()

# number = 5 # number -> переменная

#+ 
# a = 10
# b = 5
# result = a + b 
# print (result)
# print (a+100)

# a = 10 
# b = 60
# c = 100 
# d = 1000000
# e = 50
# print(a + b + c + d + e)

# / and // 
# 5 / 2 = 2.5 -> float ()
# 5 // 2 = 2 -> целочисленное деление

# num1 = 25
# num2 = 12
# print (num1 / num2)
# print (num1 // num2)

# % -> деление при котором мы получим остаток

# a = 5 
# b = 2
# result = a % b
# print (result)

# ** -> возведение в степень pow()
# 5 ** 4 = 625
# 5 ** 2 = 5 * 5 = 25
# print (2 ** 4)

# a = 5
# b = 3
# result = pow (a, 5)
# print(result)
# print (pow(a, b))
# print (pow(5, 2, 12))

# round() -> округление числа с плавающей точкой

# a = 5.724232
# result = round (a, 2)
# print(result)

# abs() -> абсолютною значение -> (-5) -> 5

# a = abs(-16)
# print(a)

# divmod (a, b) -> она выводит два числа первое число, это результат целочисленного деления (//) a на b. 
# Второе число это модульное деление (%) a на b.
 
# result = divmod (5, 2)
# print(result)

# from cmath import pi
# import math

# a = 5
# print(math.sqrt(a))

# chislo_pi = math.pi
# print(chislo_pi)

# input ножественное число
# оператор присваивания(=)
# a, b, c, = 1, 2, 5
# print(a)
# print(b)
# print(c)
# a, b, c = c, a, b
# print(a, b, c)

# from math import pi

# r = int (input ('Vvedite radius:'))
# result_P = 2 * r * pi
# result_S = pi * (r ** 2)
# print('Площадь окружности', round(result_S))
# print('Периметр окружности', round(result_P))

# num = 6
# num = 'string'
# print (num)
# print (type(num))

# str1 = 'Hello world!'
# num = 5
# print(str1 * num)

# num = 5
# str1 = '16'
# print(str1 + str(num))
# num2 = int(str1)
# print(type(num2))

# var = input('Vvedite:')
# print(var)
# print (type(var))

# num1 = int(input('Vvedite chislo:'))
# num2 = int(input('Vvedite stepen:'))

# print (num1 ** num2)
# print (pow(num1, num2))

# import random

# from random import randint
# name = input ('Vvedite svoe imya:')
# last_name = input ('Vvedite sviyu familiyu:')
# name = 'John'
# last_name = 'Snow'
# num = str(random.randint(111111, 999999))
#print (num)
# num = set(num)
# num = '' .join(num)
#print (num)
# result = name + last_name + (num)
# print (result)

# a = 1
# b = a
# print (id(a))
# print (id(b))
# print (id(1))
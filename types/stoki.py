"Hello World!"
'S vami Kani!'
"""
Hello World
My name is John Snow
"""
'''
Hello World
'''
# Строки в Python - набор последовательных символов которые мы используем 
# для хранения и представления текстовой инфы!

# Индексация в строке
# name = 'John'
#        # j = 0 = -4
#        # O = 1 = -3
#        # h = 2 = -2
#        # n = 3 = -1
# print(name)
# print(name[1])
# print(name[-1])

# str1 = 'birthday'
# print(str1[5],str1[6],str1[7])
# print(str1[0], str1[1],str1[2], str1[3],str1[4])

#Срезы по индексам
#[star: end: <step>]
# str1 = 'birthday'
# print(str1[5:8])
# print(str1[5:])

# print(str1[0:5])
# print(str1[:5])

# text = 'Hello world! My name is John! I\'m King of North!'
# print(text)
# print(text[:13])
# print(text[::5])
# print(text[::-1])

# Конкатенация строк

# a = 'Hello'
# b = 'World'
# c = ' '
# result = a + c + b
# print(result)

#Экранирование - при помощи которого можно вставлять символы в строку ,
#  которые сложно ввести с клавиатуры.

# \n -> перенос строки
# \t -> горизонтальная табуляция
# \v -> вертикальная табуляция
# \f -> перевод страницы
# \r -> возврат указателя
#len -> выводит длину строки

# name = 'John \nSnow'
# print(name)
# len(name)
# print(len(name))

#Форматирование строк
# 1. с помощью %
# 2. с использванием .format()
# 3. Интерполяция строки (f - строки)

#%
# name = input('Enter your name:')
# last_name = input('Enter your last name:')
# print ('Hello mr/mrs %s %s' %(name, last_name))

# .format
# name = input('Enter your name:')
# last_name = input('Enter your last name:')
# print ('Hello mr/mrs {} {}'.format(name, last_name))

#f = строки
a = input('Enter mr/mrs:')
name = input('Enter your name:')
last_name = input('Enter your last name:')
print(f'Hello {a} {last_name} {name}. Welcome to the parthy!')

print(dir(str))

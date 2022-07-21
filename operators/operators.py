#Логическое операторы 

#Операторы сравнения 
# <, >,  == (равно), <=, >=, !=(не равно)

# num1 = 18
# num2 = 15
# print(18>15)
# print(type(5))

# stroka1 = 'Hello'
# stroka2 = 'World'
# print(stroka1 < stroka2)
# print(ord('H'))
# print(ord('W'))
# print(len(stroka1) > len(stroka2))

# text = 'Hello world! My name is John!'
# for letter in text:
#     print(ord(letter))

# print(chr(1080))

#Условные операторы
# if
# elif
# else

# if <condition>:
#     <body if>
#     <body if> #сработает если в if придет True
# elif <condition>:
#     <body elif>
# elif<condition>:
#     <body elif>
# else:
#     <bоdy> #если во всех условиях пришло False

# string = input('Enter smt:')

# if string == 'Hello':
#     print('Hello stranger!')
# elif string =='John':
#     print('Welcome back John Snow!')
# elif string == 'Mercedez':
#     print('Mercedez Benz S class!')
# else:
#     print('Совпадений не найдено!')

# print('Код закончился!')

# email = input('Enter email:')
# password1 = input('Enter password:')
# password2 = input('Enter password confirmation:')

# if len(password1) < 8:
#     raise Exception('Too short password!')

# password1 != password2:
#     raise Exception('Password didn\'t match!')
# else:
#     print('Successfully signed Up!')


# age = input('Enter your age:')
# if age.isdigit():
#     age = int(age)
# else:
#     raise ValueError('Enter correct values!!')

# if age < 18:
#     print(f'Chuvak prihodi cherez {18 - age} goda/let!!!')
# else:
#     print('Vy prohodite po vozrastu!')

password = input('Enter your password:')
symbols = ['_', ',', '.', '%', '#', '@', '+', '-', '*', '(', ')']

falg = False
for element in symbols:
    if element in password:
        flag = True

if password.isalpha():
    raise Exception('ВЫ ввели только буквы, нужны еще цифры!')
elif password.isdigit():
    raise Exception ('ВЫ ввели только цифры, введите еще буквы')
elif not flag:
    raise Exception('Вы не ввели хотя бы один спец-символ в пароль!!(_,.()*...)')
else:
    print('Все окей вы ввели корректный пароль!')

    






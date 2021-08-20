# import keyword
# print(keyword.kwlist)

# equals to ==

# print(1 == 1)
# print(1 == 2)

# does not equals to !=
# print(1 != 2)
# print(10 != 11)

# print(1 != 1)
# print(10 != 10)

# greater than >
# print(1 > 2)
# print(1 > 1)

# print(1 > 0)
# print(1 > -1)

# less than <
# print(1 < 2)
# print(1< 1)

# print(1 < 0)
# print(1 < -1)

# greater than or equals to >=

# print(1 >= 1)
# print(2 >= 3)

# print(3 >= 3)

# less than or equals to >=

# print(1 <= 1)
# print(2 <= 3)

# print(10 <= 3)

# print(not True)
# print(not False)

# Strings

# a = '1'
# print(type(a))

# name = 'Raju Dhakal'
# profession = "Software Engineer"

# print(type(name), type(profession))

# my_fav_sentence = '''I am Raju Dhakal
# I am breaking line
# In this triple quotation.'''
# print(my_fav_sentence)

# Concatinate String

# name = 'Raju'
# last_name = 'Dhakal'

# final_word = name + ' ' + last_name
# print(final_word)

# Length  of String
# a = '  a '
# print(len(a))

# in/not in string

# a = 'Hello World'
# print('Hello' in a)

# username = 'raju'
# password = 'raju'
# print(username in password)

# UpperCase

# name = 'Raju Dhakal'
# sentence = '       i love to do coding.      '
# # print(name.upper())
# # print(name.lower())
# # print(sentence.capitalize())

# # print(name.replace('Raju', 'Mr.'))

# print(len(sentence.strip()))

# String Slicing
# name = 'Raju'
# print(name[0 : 3])
# print(name[ : 3])
# print(name[ : : 2])

# Imutatability
# i = 5
# print(id(i))
# i = 6
# print(id(i))

# a = 5
# b = 5
# print(id(a))
# print(id(b))
# print(a is b)

# Type Conversion
# i = 5

# print((float(i)))
# print(type(str(i)))

# print(int(1.0))
# print(int('1'))
# print(int(True))
# print(int(False))

# print(float(1))
# print(float(1.0))
# print(float('1'))
# print (float(True))
# print(float(False))

# print(str(1))
# print(str(1.0))
# print(str('1'))
# print (str(True))
# print(str(False))

# print(bool(0))
# print(bool(1))
# print(bool(0.001))

# print(bool(''))

# List and its uses

# first_student = 'Bimal'
# second_student = 'Sushant'
# third_student = 'Abhishek'
# fourth_student = 'Abishkar'

# students = ['Bimal', 'Sushant', 'Abhishek', 'Abishkar']
# empty_list = []
# my_empty_list = list()

# print(type(students))
# print(type(empty_list))
# print(type(my_empty_list))

# print(students[0])
# print(students[3])

# print(students[0 : 2])
# print(students[0 : 10 : 2])

# students[0] = 'Mr. Awesome'
# print(students)
# print(len(students))

# students = ['Bimal', 'Sushant', True, False, 1, 0.1]
# print(id(students[0]))

# students.append('Ram')
# print(id(students))

# a =[1, 2, 3, 4, 5.0, 6.0,  'I', 'am', 'awesome', True]

# del a[4]
# del a[0 : 3]
# print(a)
# print(a[-1])

# a =[1, 2, 3, 4, 5.0, 6.0,  'I', 'am', 'awesome', True]
# student_list = ['Umesh', 'Bimal', 'Urusha', 'Tshering', 'Abishkar', 'Aditi', 'Abhishek']
# add --------> append insert

# a.append('Hello Awesome Class')
# print(a)

# student_list.append('Ram')
# # print(student_list)

# student_list.insert(0, 'Barney Stinson')
# student_list.append('Ted')
# print(student_list)

# remove pop

# student_list.remove('Abishkar')
# student_list.remove('Abhishek')
# print(student_list)

# student_list.pop()
# print(student_list)

# student_list.pop(1)
# print(student_list)


# a =[1, 2, 3, 4, 5.0, 6.0,  'I', 'am', 'awesome', True]
# student_list = ['Umesh', 'Bimal', 'Urusha', 'Tshering', 'Abishkar', 'Aditi', 'Abhishek']

# student_list.clear()
# student_list.reverse()
# student_list.sort()

# student_list.sort(reverse=True)
# print(student_list)


# a = [1, 2, 3, 4, 5]
# b = a

# b[0] = 'Bro Code Academy'
# print(a)
#
# b = a.copy()
# b[0] = 'Bro Code Academy'
# print(a)
# print(b)

# a = [1, 2, 3, 4, 5]
# b = [7, 8, 9, 10]

# print(a + b)

# ---------------------------------- #

# TUPLE

# a = (1, 2, 3, 4, 5, 6, 7, 8)
# a = ('sun', 'mon', 'tue', 'wed', 'thur', 'fri', 'sat')
# print(type(a))
# print(a[0])

# b = tuple()
# c = ()
# b = (1, 2, 3)
# print(a + b)

# a = (10,)
# print(type(a))

# ------------------------------------#

# SETS

# a = {1, 2, 3, 4, 5, 6, 6, 6, 7, 7, 7, 7, 'Raju', 'Raju', True, True}
# print(a)

# a = {'raju', 'dhakal', 'aditi', 'sharma', 'tshering', 'adijit', 'Kami'}
# print(a)
# a = {1, 2, 3}
# b = {4, 5, 6}

# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(b.difference(a))


# append adds to the last position
# add adds to the random position
# a.add('Barney Stinson')

# a.remove('dhakal')
# a.discard('test')

# a.clear()

# print(a)

# account_type = ('current', 'saving')

# a = list(account_type)
# a.append('Bro Account')
# account_type = tuple(a)
# print(a)

# a = set()
# print(type(a))

# a = {}
# print(type(a))

# phone_number = {'Raju': 9846210933, 'Januka': 9814115986, 'Baba': 9862274333}
# print(phone_number['Raju'])
# print(phone_number.keys)

# phone_number['Mummy'] = 9846638475
# print(phone_number)

# name = input('Enter your Name: ')
# print(name)

# print('You are awesome ' + name)

# age = input('Enter your Age: ')

# print('You are ' + age + ' years old.')

# student_marks = {'umesh': 1, 'bimal': 100, 'simaran': 67, 'abishkar': 51, 'bijay': 0}

# student_name = input('Enter your name: ')

# print('Your marks is ' + str(student_marks[student_name]))

# name = None

# a = None
# b = None
# c = None
# d = None

# print(a is b is c is d)

#--------------------------#

# RANGE

# print(list(range(20)))
# print(list(range(10, 20)))

# print(list(range(5, 15, 2)))

# print(list(range(4, 21, 2)))

# print(list(range(3, 20, 2)))

# ----------------------------------- #
# if else statement

# if 10 > 6: 
#     print('This class is legendary')
#     print('This statement is True')
# elif 4 > 5:
#     print('Why silent guys')
# else:
#     print('Hello Guys')

# if 7 > 6:
#     if 6 > 5:
#         print('I am nested if')
#     elif 5 > 6:
#         print('I am nested elif')
#     else:
#         print('I am nested else')
#     print('Barney')
# elif 5 > 4:
#     print('Stinson')
# else:
#     print('Sheldon')

# if 7 > 6:
#     pass
# elif 5 > 4:
#     print('Stinson')
# else:
#     print('Sheldon')

# if 6 > 6:
#     print('I am awesome.')
# else:
#     print('Bro Code Academy is the best!')

# name = input('Enter your name:')
# if name.lower() == 'raju':
#     print(name + ' is awesome.')
# else:
#     print('This is not getting interactive')
# print('I am awesome') if 6 > 6 else print('Bro Code Academy is Awesome!')

# print(name + ' is awesome.') if name.lower() == 'raju' else print('This is not getting interactive')

# a = 5 if 5 > 4 else 6
# print(a)

# Logical operators

# is_passed = True
# is_topper = False

# if is_passed and is_topper:

# bought_pyaj = True
# bought_chicken = False

# if bought_pyaj and bought_chicken:
#     print('Yaayyy! Masu Bhat khana painey bhayo!')
# else:
#     print('Hait Ghiraula ko tarkari chyaa!')

# if bought_pyaj or bought_chicken:
#     print('Yaayyy! Masu Bhat khana painey bhayo!')
# else:
#     print('Hait Ghiraula ko tarkari chyaa!')

# first_num = input('Enter first number:')
# second_num = input('Enter second number:')

# if int(first_num) > int(second_num):
#     print(first_num + ' is greater than ' + second_num)
# elif int(first_num) < int(second_num):
#     print(second_num + ' is greater than ' + first_num)
# else:
#     print(first_num + ' and ' + second_num + ' are equal.')
    
# if 10 > 5 and 10 > 6 and 10 > 7 and 10 > 8 and 10 != 10:
#     print('Welcome to Bro Code Academy!')
# else:
#     print('Kya Bore Bhayo!!')

# name = 'Raju Dhakal'
# if 10 == 10 and name.lower() == 'raju dhakal' and name[0] == 'R':
#     print('This class is awesome')
# if name.lower() == 'raju dhakal' and name[0 : 3] == 'Raj' and 10 != 10:
#     print('This class is jhur')

# else:
#     print('Babaal cha hai ta!')

#---------------------------------#

# MODULO OPERATOR
# is used to get remainder

# print(3 % 2)
# print(4 % 2)
# print(5 % 2)
# print(7 % 2)

# num = int(input('Enter a number: '))
# if num % 2 == 0:
#     print('Even Number')
# elif num % 2 != 0:
#     print('Odd Number')

# ------------------------ #
# LOOPING: While and For

# print('Hello World')
# print('Hello World')
# print('Hello World')
# print('Hello World')
# print('Hello World')
# print('Hello World')
# print('Hello World')
# print('Hello World')
# print('Hello World')
# print('Hello World')
# print('Hello World')

# i = 0
# while i < 5:
#     print('Hello World!')
#     i = i + 2

# name_marks = {'umesh': 5, 'abiskar': 55, 'bishal': 99, 'ajit': 25, 'simran': 60}

# while True:
#     name = input('Enter your name: ')
#     # print('Your marks is ' + str(name_marks[name]))
#     marks = name_marks[name]

#     if marks > 60 and marks < 80:
#         print('You passed in First Division')
#     elif marks > 80 and marks < 90:
#         print('You passed with Distinction')
#     elif marks >= 90:
#         print('Yaay! PARTY 🎉')
#     else:
#         print('Dhobi chutai and Flying Chappal! 😭')

# -------------------------------- #

# FOR Loop

# string # list # tuple # set # dict --> iterables

# name = 'raju'

# for char in name:
#     print(char)

# name = 'Bro Code'

# for a in name:
#     print(a, end=',')

# students = ['rama', 'ram', 'shyam', 'ghanashyam', 'barney']

# for item in students:
#     # print(item)
#     print(item, end=',')

# name_marks = {'umesh': 100, 'ram': 20, 'shyam': 25, 'sita': 21, 'hari': 51}

# for key, value in name_marks.items():
#     print(key, value)

# for item in range (20):
#     print(item, end= ' ')

# even = []
# odd = []

# for num in range(2, 51):
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)
# print(even)
# print(odd)

# ------------------------- #

# BREAK / CONTINUE

# for name in ['umesh', 'barney', 'ted', 'lily', 'marshal']:
#     if name == 'shankar':
#         print('Lilly is present!')
#         break
# else:
#     print('Shankar is not present!')

# for name in ['umesh', 'barney', 'ted', 'lily', 'marshal']:
#     if name == 'lily':
#         print('Lilly is present!')
#         continue
#     else:
#         print(name)

name = 'Raju'
greeting = 'Good Morning'
salutations = 'Mr.'
age = 27
address = 'Pokhara'

#print(greeting + ' ' + salutations + ' ' + name + '. Your age is ' + str(age))

print(f'{greeting} {salutations} {name}. Your age is {age} ')

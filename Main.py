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

print(list(range(20)))
print(list(range(10, 20)))

print(list(range(5, 15, 2)))

print(list(range(4, 21, 2)))

print(list(range(3, 20, 2)))
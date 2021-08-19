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

students = ['Bimal', 'Sushant', True, False, 1, 0.1]
print(id(students[0]))

students.append('Ram')
print(id(students))
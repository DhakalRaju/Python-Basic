# OOP 
# Objects and Classes

# Class is blue print of an object. It defines how an object looks like.
# Object is an instance of a class.
# Class is a blueprint/template/modal of an object

# class Student:
#     def  __init__(self):
#         self.first_name = 'Raju'
#         self.last_name = 'Dhakal'
#         self.age = 28

# s = Student()
# a = Student()
# reference variable

# print(s.first_name)
# print(s.last_name)
# print(a.first_name)
# print(a.last_name)

# class Student:
#     def  __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         print('I am awesome')
#     def test():
#         print('Chari Jelaima')

# s = Student('Raju', 'Dhakal', 28)
# print(s.first_name)
# print(s.last_name)
# print(s.age)

# class Student:
#     def  __init__(self, f_name, l_name, user_age):
#         self.first_name = f_name
#         self.last_name = l_name
#         self.age = user_age
#         print(id(self))


# s = Student('Raju', 'Dhakal', 28)
# print(id(s))
# a = Student('Bro', 'Code', 0)
# print(id(a))
# s.first_name = 'Roshan'
# print(s.first_name)
# del s.first_name
# print(s.first_name)

# # Types of Variable

# class Student:
#     school_name = 'Bro Code Academy'
#     principal_name = 'Prof. Dr. Raju Dhakal'
    
#     def  __init__(self, f_name, l_name, user_age):
#         self.first_name = f_name
#         self.last_name = l_name
#         self.age = user_age
    
#     def get_first_name(self):
#         return self.first_name

#     @classmethod
#     def get_school_name(cls):
#         cls.principal_name

#     @staticmethod
#     def get_holiday_list():
#         print('Saturday bida cha masu bhat khana parcha')

# s = Student('Raju', 'Dhakal', 28)
# # print(Student.principal_name)
# # print(Student.school_name)
# # print(s.get_first_name)
# print(Student.get_school_name())
# Student.get_holiday_list()

class Student:
    school_name = 'Bro Code Academy'
    principal_name = 'Prof. Dr. Raju Dhakal'
    
    def  __init__(self, user_age):
        self.__age = user_age

    def set_age(self, user_age):
        if user_age < 0:
            self.__age = 0
        else:
            self.__age = user_age

    def get_age(self):
        return self.__age
    
s = Student(27)
# input_age = input('Enter user age: ')
# s.age = input_age
# print(s.age)
s.set_age(-30)
print(s.get__age())
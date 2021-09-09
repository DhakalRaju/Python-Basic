# class CloudFactoryWorker:
#     def __init__(self, name, l_name, project, employee_id):
#         self.first_name = name
#         self.last_name = l_name
#         self.project_name = project
#         self.id = employee_id

#     def calculate_salary(self, hours):
#         salary = hours * 20
#         return salary

# class CFWorker(CloudFactoryWorker):
#     pass


# class CoreTeam(CloudFactoryWorker):
#     pass

# CF1 = CFWorker('Raju', 'Dhakal', 'Expensify', 102563)
# print(CF1.first_name)


# POLYMORPHISM

class CloudFactoryWorker:
    def __init__(self, name, l_name, project, employee_id):
        self.first_name = name
        self.last_name = l_name
        self.project_name = project
        self.id = employee_id

    def calculate_salary(self):
        print('I am based class')

class CFWorker(CloudFactoryWorker):
    def calculate_salary(self):
        print('I am hourly bases worker')


class CoreTeam(CloudFactoryWorker):
    def calculate_salary(self):
        print('I am paid based on title.')


CF1 = CFWorker('Raju', 'Dhakal', 'Expensify', 102563)
CF2 = CoreTeam('Raju', 'Dhakal', 'Expensify', 102563)
CF1.calculate_salary()
CF2.calculate_salary()
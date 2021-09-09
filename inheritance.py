class CloudFactoryWorker:
    def __init__(self, name, l_name, project, employee_id):
        self.first_name = name
        self.last_name = l_name
        self.project_name = project
        self.id = employee_id

class CFWorker(CloudFactoryWorker):
    pass


class CoreTeam(CloudFactoryWorker):
    pass

CF1 = CFWorker('Raju', 'Dhakal', 'Expensify', 102563)
print(CF1.first_name)
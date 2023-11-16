from dz26.employee import Employee


class AdminEmp(Employee):
    def __init__(self, name):
        super().__init__(name)

    def print_name(self):
        return self.name

    def zp_all(self):
        return self.salary

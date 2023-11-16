from dz26.employee import Employee


class Sales(Employee):
    def __init__(self, name, count):
        super().__init__(name)
        self.count = count

    def print_name(self):
        return self.name

    def zp_all(self):
        return self.salary + (self.comis * self.count)

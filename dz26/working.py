from dz26.employee import Employee


class Working(Employee):
    def __init__(self, name, hour):
        super().__init__(name)
        self.hour = hour

    def print_name(self):
        return self.name

    def zp_all(self):
        return self.hour * self.cost_hour

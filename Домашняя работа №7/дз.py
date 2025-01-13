class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return (f"Сведенья о сотруднике:\n"
                f"\tИмя: {self.name}\n"
                f"\tid: {self.id}")


class Manager(Employee):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department

    def manage_project(self):
        ...


class Technician:
    def __init__(self, specialization):
        self.specialization = specialization

    def perform_maintenance(self):
        ...


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        super(Manager, self).__init__(name, id, department)
        super(Technician, self).__init__(specialization)
        self.subservient = set()

    def add_employee(self, employee: Employee):
        self.subservient.add(employee)

    def get_employee(self):
        print("Сведенья о сотрудниках:\n" + "".join(list(employee.get_info() for employee in self.subservient)))

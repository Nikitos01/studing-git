Employee = type('Employee', (object,), {
    '__init__': lambda self, name, id: (None if (setattr(self, 'name', name) or setattr(self, 'id', id)) else None),
    'get_info': lambda self: f"Сведения о сотруднике:\n\tИмя: {self.name}\n\tid: {self.id}\n"
})

Manager = type('Manager', (object,), {
    '__init__': lambda self, department: (None if setattr(self, 'department', department) else None),
    'manage_project': lambda self: "Управление проектом"
})

Technician = type('Technician', (object,), {
    '__init__': lambda self, specialization: (None if setattr(self, 'specialization', specialization) else None),
    'perform_maintenance': lambda self: "Выполнение технического обслуживания"
})

TechManager = type('TechManager', (Manager, Technician), {
    '__init__': lambda self, department, specialization: (None if (Manager.__init__(self, department),
                                                          Technician.__init__(self, specialization),
                                                          setattr(self, 'subservient', set())) else None),
    'add_employee': lambda self, employee: self.subservient.add(employee),
    'get_employee': lambda self: ("Сведенья о сотрудниках:\n" + \
                                  "".join(list(employee.get_info() for employee in self.subservient)))
})

emp1 = Employee("Иван Иванов", 101)
emp2 = Employee("Петр Петров", 102)

mgr = TechManager("IT", "Сетевой инженер")
mgr.add_employee(emp1)
mgr.add_employee(emp2)

print(emp1.get_info())
print(mgr.get_employee())



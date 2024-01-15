class Employee:
    rasieAmount = 1.04

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.'+last + '@email.com'

        def apply_raise(self):
            self.pay =int(self.pay * self.rasieAmount)


        def applay_raise(self):
            self.pay = int(self.pay * Employee.rasieAmount)


emp1 = Employee('Brian', 'Rye', 50000)
print(emp1.pay)


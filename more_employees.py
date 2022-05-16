from employee import Employee
from payroll import SalaryEmployee


class HourlyEmployee(Employee):
    def __init__(self, id, name, hour_rate, hours_worked):
        super().__init__(id, name)
        self.hour_rate = int(hour_rate)
        self.hours_worked = int(hours_worked)

    def ask_salary(self):
        try:
            self.hours_worked = int(input("Anna tehdyt tunnit:"))
        except:
            self.hours_worked = 0
        try:
            self.hour_rate = int(input("Anna tuntipalkka:"))
        except:
            self.hour_rate = 0

    def calculate_salary(self):
        return self.hour_rate * self.hours_worked


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, monthly_salary, comission):
        super().__init__(id, name, monthly_salary)
        self.commission = int(comission)

    def ask_salary(self):
        try:
            self.monthly_salary = int(input("Give salary: "))
        except:
            self.monthly_salary = 0
        try:
            self.commission = int(input("Give commission: "))
        except:
            self.commission = 0

    def calculate_salary(self):
        return super().calculate_salary() + self.commission

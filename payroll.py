from employee import Employee


class PayrollSystem:
    __employees = []

    def __init__(self, employees):
        self.__employees = employees

    def calculate_payroll(self):
        for i in self.__employees:
            print("Payroll\n==============")
            print("For person:", i.get_id(), "-", i.get_name())
            print("- Gets paid: ", i.calculate_salary(), "\n", sep='')


class SalaryEmployee (Employee):
    monthly_salary = 0

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.monthly_salary = salary

    def calculate_salary(self):
        return self.monthly_salary


def main():
    id = 0
    employees = []

    while True:
        id += 1
        name = input("Give the name of the employee: (0 to quit): ")
        if name == "0":
            break
        salary = int(input("Give the salary: "))
        e = SalaryEmployee(id, name, salary)
        employees.append(e)

    payroll = PayrollSystem(employees)
    payroll.calculate_payroll()


if __name__ == "__main__":
    main()

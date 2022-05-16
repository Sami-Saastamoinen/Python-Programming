from split_join import my_join, my_split
from payroll import SalaryEmployee


while True:
    print("(1) Add employees to the list\n(2) Write employees to the file\n(3) Read employees from the file\n(4) Print employees\n(0) Quit\n")
    selection = int(input("Select an action: "))
    if selection == 1:
        salary_employees = []
        name = " "
        id = 1
        while name != '0':
            name = str(input("Give the employee's name (0 to quit):"))
            if name != '0':
                try:
                    salary = int(input("Give the salary:"))
                except:
                    salary = 0
                salary_employees.append(SalaryEmployee(id, name, salary))
                id += 1

    elif selection == 2:
        file = open("salary_employee.csv", 'a')
        for employee in salary_employees:
            lst = [str(employee.id), employee.name,
                   str(employee.monthly_salary)]
            temp_str = my_join(lst, ',')
            temp_str += '\n'
            file.write(temp_str)
        file.close()
        print(len(salary_employees),
              " employee(s) added to file: salary_employee.csv")

    elif selection == 3:
        file = open("salary_employee.csv", 'r')
        for line in file:
            line = line.strip('\n')
            temp_lst = my_split(line, ',')
            salary_employees.append(SalaryEmployee(
                int(temp_lst[0]), temp_lst[1], int(temp_lst[2])))
        file.close()
        print(len(salary_employees),
              " employee(s) read from file: salary_employee.csv")

    elif selection == 4:
        for employee in salary_employees:
            print("Id:", employee.id, "Name:", employee.name,
                  "Salary:", employee.monthly_salary)

    elif selection == 0:
        print("Program closing, thank you.")
        break
    else:
        print("Invalid selection")

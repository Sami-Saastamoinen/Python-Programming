
class Employee:
    """"""
    id = 0
    name = ''

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name


def main():
    employees = []
    id = 0

    while True:
        id += 1
        name = input("Give the name of the employee: (0 to quit):")
        if name == "0":
            break
        e = Employee(id, name)
        employees.append(e)

    for i in employees:
        print("Id:", i.get_id(), "Name:", i.get_name())


if __name__ == "__main__":
    main()

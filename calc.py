import math


def ask_number():
    while 1:
        try:
            num = int(input("Insert a number: "))
            return num
        except Exception:
            print("Wrong input!")


choice = 0
num1 = ask_number()
num2 = ask_number()

while (choice != 8):
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(num1/num2)\n(6)cos(num1/num2)\n(7)Change numbers\n(8)Quit\nChosen numbers:", num1, num2)
    choice = int(input("Make a choice (1-8): "))
    if choice == 1:
        print("Answer is:", num1 + num2)
    elif choice == 2:
        print("Answer is:", num1 - num2)
    elif choice == 3:
        print("Answer is:", num1 * num2)
    elif choice == 4:
        print("Answer is:", num1 / num2)
    elif choice == 5:
        print("Answer is:", math.sin(num1/num2))
    elif choice == 6:
        print("Answer is:", math.cos(num1/num2))
    elif choice == 7:
        num1 = ask_number()
        num2 = ask_number()

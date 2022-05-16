prices = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
choice = 0
total = 0
print("Supermarket\n===========")
while True:
    choice = int(input("Choose a product (1-10) 0 to quit: "))
    if choice >= 1 and choice <= 10:
        print("Product:", choice, "Price:", prices[choice-1], sep='\t')
        total = total + prices[choice-1]
    elif choice == 0:
        print("Total:", total, sep='\t')
        while True:
            payment = int(input("Payment: "))
            if payment < total:
                print("Payment isn't enough")
            else:
                break
        print("Change:", (payment - total), sep='\t')
        break
    else:
        print("Wrong input")

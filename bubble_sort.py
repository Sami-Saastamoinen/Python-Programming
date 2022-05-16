def bubble_sort(lis):
    length = len(lis)
    for i in range(length):
        for j in range(length - i):
            a = lis[j]
            if a != lis[-1]:
                b = lis[j + 1]
                if a > b:
                    lis[j] = b
                    lis[j + 1] = a
    return lis


count = int(input("Give the amount of numbers to sort: "))
nums = []

for i in range(count):
    print("Give number at [", i, "]:")
    value = int(input())
    nums.append(value)

print("Sorted List in increasing order:", bubble_sort(nums))

import random

times = 5
print("Let's flip a coin", times, "times")
for i in range(times):
    coin = random.randint(0, 1)
    if coin == 1:
        print("Heads!")
    else:
        print("Tails!")

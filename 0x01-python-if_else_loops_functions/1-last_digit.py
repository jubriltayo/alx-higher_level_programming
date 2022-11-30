import random
number = random.randint(-10000, 10000)
if number < 0:
    lastd = number % -10
else:
    lastd = number % 10
if lastd > 5:
    print(f"Last digit of {number} is {lastd} and is greater than 5")
elif lastd < 6 and lastd != 0:
    print(f"Last digit of {number} is {lastd} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is 0 and is 0")

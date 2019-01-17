import random
import string

D4 = random.randint(1,4)
D6 = random.randint(1,6)
D10 = random.randint(0,9)

print("Types of Dice - D4, D6, D10")
my_input = raw_input("What Kind of Dice Are You Rolling?:")


if my_input == "D4":
    print(D4)
elif my_input =="D6":
    print(D6)
elif my_input =="D10":
	print(D10)
else:
	print("Invalid Input")
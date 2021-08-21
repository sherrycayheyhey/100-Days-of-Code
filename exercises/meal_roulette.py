# teach about the split function

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

loser = random.randint(1, len(names)-1)
print(names[loser] + " is going to buy the meal today!")

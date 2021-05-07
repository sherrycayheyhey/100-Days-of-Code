print("Welcome to the tip calculator.\n")

# get user input
bill = float(input("What is the bill total? $"))
tip = int(input("\nWhat percentage tip would you like to give? "))
people = int(input("\nHow many people are splitting the bill? "))

# calculate the tip and add it to the bill
bill += bill * (tip / 100)

# split the bill into number of people then round to two decimal places
total_per_person = round(bill / people, 2)

#format the string to have 2 places after the decimal to avoid situations like $12.8 which looks weird
print(f"Each person should pay $" + "{:.2f}".format(total_per_person))

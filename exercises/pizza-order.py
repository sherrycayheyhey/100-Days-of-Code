# could be soda, cakes, build a bear, etc.

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

price = 0;

if size == "S":
  price = 15;
elif size =="M":
  price = 20
elif size =="L":
  price = 25

if add_pepperoni == "Y":
  price += 2

if extra_cheese == "Y":
  price += 1

print(f"Your final bill is: ${price}.")

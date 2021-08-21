# give logic and then let the student figure out how to code

# it's a leap year if that year is evenly divisible by 4 
# **except** every year that is evenly divisible by 100 
# **unless** the year is also evenly divisible by 400

year = int(input("Which year do you want to check? "))

if year % 100 == 0:
  if year % 400 == 0:
    print("Leap year.")
  else: 
    print("Not leap year.")
elif year % 4 == 0:
  print("Leap year.")
else: 
  print("Not leap year.")

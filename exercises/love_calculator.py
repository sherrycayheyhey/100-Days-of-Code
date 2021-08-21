print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

coupleName = (name1 + name2).lower()

trueScore = 0
loveScore = 0

trueScore += coupleName.count("t")
trueScore += coupleName.count("r")
trueScore += coupleName.count("u")
trueScore += coupleName.count("e")

loveScore += coupleName.count("l")
loveScore += coupleName.count("o")
loveScore += coupleName.count("v")
loveScore += coupleName.count("e")

loveTotal = int(str(trueScore) + str(loveScore))

if loveTotal < 10 or loveScore > 90:
  print(f"Your score is {loveTotal}, you go together like coke and mentos.")
elif loveTotal > 40 and loveTotal < 50:
  print(f"Your score is {loveTotal}, you are alright together.")
else:
  print(f"Your score is {loveTotal}.")

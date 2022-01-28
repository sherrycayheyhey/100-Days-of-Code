import random
import art

# type chart

text = ["fire", "water", "grass"]
pic = [art.fire, art.water, art.grass]
computerType = random.randint(0, len(text) - 1)

print("You opponent chose " + text[computerType] + pic[computerType])

userType = input("Which pokemon type do you want to attack it with?  ")

if userType == "fire":
    userType = 0
elif userType == "water":
    userType = 1
elif userType == "grass":
    userType = 2

print("\nyou used " + text[userType] + pic[userType])

# nve nve se           l l w           0 -1 -2
# se  nve nve          w l l           1  0 -1
# nve se  nve          l w l           2  1  0

outcome = userType - computerType

if outcome == 1 or outcome == -2:
    print("that was super effective")
else:
    print("that was not very effective")

from termcolor import colored
import random

fire = colored('''
   )
  ) \\
 / ) (
 \(_)/ 
''', 'yellow')

electric = colored('''
    
         ,/
       ,'/
     ,' /
   .'  /_____,
 .'____    ,' 
      /  ,'
     / ,'
    /,'
   /'


''', 'yellow')

water = colored('''
     ,
     )\\
    /  \\
   '  # '
   ',  ,'
     `'
''', 'blue')

grass = colored('''
   ,   
  /|\  
 /\| \ 
|˙,|/ |
\ \|,˙/
 ˙,|,˙ 
   |  
''', 'green')

pic = [fire, water, grass]
text = ["fire", "water", "grass"]

computerType = random.randint(0, len(pic) - 1)

userType = input("computer used " + text[computerType] + pic[computerType] + "\nWhich pokemon type do you want to use?  ")

if userType == "fire":
  userType = 0
elif userType == "water":
  userType = 1
elif userType == "grass":
  userType = 2

print("\nyou used " + text[userType] + pic[userType])



#l, l, w     0, -1, -2
#w, l, l.     1, 0, -1
#l, w, l.     2, 1, 0

outcome = computerType - userType

if outcome == 0:
  print("you lose!")
elif outcome == -1:
  print("you lose!")
elif outcome == 1:
  print("you win!")
elif outcome == -2:
  print("you win!")
elif outcome == 2:
  print("you lose!")

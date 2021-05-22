from art import logo
from termcolor import colored, cprint

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cprint(logo, 'blue', 'on_white')

# get the user inputs
def user_inputs():
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(direction, text, shift)

# encode or decode the message
def caesar(direction, text, shift):
  # wrap for shifts larger than 26
  if shift > 26:
    shift = shift % 26

  secret_message = ""

  for letter in text:
    # get letter from alphabet and offset by the shift
    # add this new letter to the word
    if letter not in alphabet:
      # leave non-alpha chars alone
      secret_message += letter
    elif direction == 'encode':
      secret_message += alphabet[alphabet.index(letter) + shift]
    elif direction == 'decode':
      secret_message += alphabet[alphabet.index(letter) - shift]
    else:
      # the user typed something weird 
      return print("please try again, you dingdong!")

  # print the result
  print(f"The {direction}d text is {secret_message}\n")

  # continue?
  more_cipher()

# prompt the user to continue
def more_cipher():
  user_choice = input("Do you want to use the cipher again? ")
  if user_choice == 'yes':
    user_inputs()
  else:
    print('later, sucka!')

# start the program
user_inputs()

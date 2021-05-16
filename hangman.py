import random
from hangman_art import * #hangmen and logo
from hangman_words import word_list #list of words

# set up game state variables 
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

# check user guess against chosen word and decrement lives as necessary
while not end_of_game:
    
    guess = input("Guess a letter: ").lower()

    # letter already used
    if guess in display:
      print(f"you already used {guess}")

    # check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        # correct letter guessed
        if letter == guess:
            display[position] = letter

    # incorrect letter guessed
    if guess not in chosen_word:
        print(f"{guess} is not in the word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("LOSER!")

    # join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # check if all the letters of the word have been solved
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])

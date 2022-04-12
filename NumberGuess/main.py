from art import logo
import random
import sys

# list of pokemon names
pokemon = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle",
           "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto",
           "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew",
           "Sandslash", "Nidoran♀", "Nidorina", "Nidoqueen", "Nidoran♂", "Nidorino", "Nidoking", "Clefairy", "Clefable",
           "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume",
           "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck",
           "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra",
           "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool",
           "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite",
           "Magneton", "Farfetch’d", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster",
           "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode",
           "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing",
           "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu",
           "Starmie", "Mr.Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados",
           "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto",
           "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite",
           "Mewtwo", "Mew"]


# function to set the lives
def set_difficulty():
    """Prompt the user for difficulty level and assign appropriate number of lives"""
    difficulty = input("Choose a diffuculty mode; 'magikarp' or 'gyarados': ")
    if difficulty == "magikarp":
        print(
            "Ahh...I see that you're the type of trainer that likes to attack with splash. In that case, I'll give you 10 guesses.")
        lives = 10
        return lives
    elif difficulty == "gyarados":
        print("A more evolved trainer, I see. You may take up to 5 guesses.")
        lives = 5
        return lives
    else:
        sys.exit("ditto?!")


# function to check if the guess was correct
def check_guess(user_guess, guesses, oak_pick):
    """Checks oak's choice against user's guess. Returns the number of lives remaining"""
    if user_guess == oak_pick:
        # correct, print out the pokemon name
        print("correct!")
        print(f"I was thinking of that cute little {pokemon[oak_pick]}!")
        sys.exit()
    elif user_guess < oak_pick:
        # print out that the number is too low, guess again
        print("too low")

    elif user_guess > oak_pick:
        # print that the number is too high, guess again
        print("too high")

    return guesses - 1


# game function
def game():
    # print logo and welcome
    print(logo)
    print("Welcome to Guess My Pokemon! I'm your host: Professor Oak.")

    # make Oak's selection, set lives
    oaks_pick = random.randint(1, 151)
    #print(oaks_pick)
    lives = set_difficulty()
    print("I'm thinking of a Kanto pokemon...")

    # prompt for the first guess
    user_guess = int(input("which one do you think it is? "))
    lives = check_guess(user_guess, lives, oaks_pick)

    # continue to promt the user and check the answer
    # stop when correct answer or no lives
    while user_guess != oaks_pick:
        if lives == 0:
            print("you'll never be a Pokemon Master :(")
            return
        elif lives == 1:
            print(f"{lives} life remaining\n")
        else:
            print(f"{lives} lives remaining\n")

        user_guess = int(input("Guess again! "))
        lives = check_guess(user_guess, lives, oaks_pick)

# start the game
game()

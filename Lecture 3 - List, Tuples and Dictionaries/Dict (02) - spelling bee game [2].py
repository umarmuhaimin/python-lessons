WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ")

        # TODO: Check if guess in dictionary
        if guess == "GRAPHIC":
            WORDS.clear() # all of the keys_and_values from the dictionary are removed because guess == 7 letters == Wins the game.
            print("You've won!")
        elif guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good Job! You scored {points} points.")

    print("That's the game!")

main()

# 🔹 Explaination line by line 

# 👉 if guess == "GRAPHIC": WORDS.clear()
# → This means:
# • If the player types "GRAPHIC", the program removes all words from the dictionary using .clear().
# • This ends the game immediately, because while len(WORDS) > 0: will now be false.
# → Summary:
# • Typing "GRAPHIC" clears the dictionary and wins the game.
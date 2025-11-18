# 🔹 SPELLING BEE GAME 🔹

# 👉 In this python file, you need to :
# 1. Show a welcome message and the letters you can use.
# 2. While there are words left in the dictionary:
#    → Show how many words are left.
#    → Ask you to guess a word.
#    → If your guess is in the dictionary:
#       • Remove the word.
#       • Give you points and show your score.
# 3. When all words are guessed, print “That’s the game!” and finish.

########################################################################################################

# 🔹 dictionary = {"key": "value"}

WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5}
# WORDS = {"Word": "points"}

# "PAIR" is a key, and its value is 4.
# "HAIR" is a key, and its value is 4.
# "CHAIR" is a key, and its value is 5.

def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ")

        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good Job! You scored {points} points.")

    print("That's the game!")

main()

########################################################################################################

# 🔹 Explaination line by line :

# 👉 while len(WORDS) > 0 :
# → The game keeps running as long as there are words (keys) left in the dictionary.
# → Each time you guess a word correctly, it is removed from the dictionary.
# → When there are no more words left (len(WORDS) == 0), the loop ends and the game finishes.
# → In short, Keep playing and guessing until all words are gone, then the game ends.


# 👉 print(f"{len(WORDS)} words left!")
# → Show how many words you still need to guess.
# → if you use f"{}" string : you don't need to have a lot of comma and you can just have one quote, one at the beginning and another at the end. 
# → In between the f"{}" string : you can return any item from the container/dict , and you can also add text as an output to print.

# 👉 guess = input("Guess a word: ")
# → Ask the player to type a word.

# 👉 if guess in WORDS.keys():
# → Check if the guessed word is in the dictionary. 
# → It will only go through the keys and see if the guess word matches any of keys from the dict.

# 👉 points = WORDS.pop(guess)
# → If the guess is correct, remove the word from the dictionary and get its points.

# → When you guess a word, for example "CHAIR", the code does:
# → If guess is "CHAIR", then WORDS.pop("CHAIR"):
# → Removes "CHAIR" from the dictionary.
# → Returns its value, which is 5.
# → Value of 5 will be stored inside points variable.
# → So, points becomes 5.

# → Example:
# → Suppose you type CHAIR:
# → The program checks if "CHAIR" is in WORDS.
# → It removes "CHAIR" and gets the value 5.
# → It prints: Good Job! You scored 5 points.

# → .pop(key) will:
# → Remove the key (and its value) from the dictionary.
# → Return the value of that key.
# → So in your game, when you guess a word correctly, .pop(guess) removes that word from WORDS and gives you its points.

# → Summary:
# → The value "points" comes from the dictionary.
# → WORDS["CHAIR"] gives 5.
# → WORDS.pop("CHAIR") also gives 5 and removes "CHAIR" from the dictionary.


# 👉 print(f"Good Job! You scored {points} points.")
# → Tell the player they got it right and show their points.

########################################################################################################

# 👉 Process step by step : 

WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5}

# 1. Show welcome message and letters
# Output: 
# Welcome to Spelling Bee!
# Your letters are: A I P C R H G

# 2. Start the guessing loop
######################################################
# • First round:
# → Output: 
# 3 words left!
# → You type: PAIR
# → Program checks: Is "PAIR" in WORDS? Yes.
# → Removes "PAIR" from WORDS, gives you 4 points.
# → Output: 
# Good Job! You scored 4 points.
######################################################
# • Second round:
# → Output: 
# 2 words left!
# → You type: HAIR
# → Program checks: Is "HAIR" in WORDS? Yes.
# → Removes "HAIR" from WORDS, gives you 4 points.
# → Output:
# Good Job! You scored 4 points.
######################################################
# • Third round:
# → Output:
# 1 words left!
# → You type: CHAIR
# → Program checks: Is "CHAIR" in WORDS? Yes.
# → Removes "CHAIR" from WORDS, gives you 5 points.
# → Output:
# Good Job! You scored 5 points.
######################################################

# 3. End the game
# → Now WORDS is empty.
# → Output:
# That's the game!

# → Summary:
# • You guess "PAIR", "HAIR", and "CHAIR".
# • Each time, the word is removed and you get its points.
# • When all words are gone, the game ends.

##########################################################################

# ✅ What does this program do?
# → It’s a spelling game.
# → You get a set of letters: A I P C R H G.
# → The program has a dictionary called WORDS with words as keys and points as values.
# → You guess a word.
# → If your guess is in the dictionary, you get points and that word is removed from the list.
# → The game keeps going until there are no words left.













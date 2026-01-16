WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to Spelling Bee!")
    for word, points in WORDS.items():
  # for key, value in WORDS.items():
        print(f"{word} was worth {points} points.")

main()


# 🔹 Purpose of this file:

# → To show all the words in the dictionary and how many points each word is worth.
# → It’s not a game, just a way to display the contents of the WORDS dictionary.

# 👉 What are we trying to achieve?
# → Print each word and its points, so you can see what words are available and their scores.

# 👉 What is the use of .items()?
# → .items() lets you loop through both the key (word) and value (points) in the dictionary at the same time.
# → Example:
# → For WORDS = {"PAIR": 4, "HAIR": 4},
# → .items() gives you pairs like ("PAIR", 4) and ("HAIR", 4) printed/outputed all at the same time.

# 👉 In short:
# → .items() helps you get both the word and its points to print them together all at the same time.
# → .items() allows us to output all of the keys_and_values from the dictionary all at the same time, so you can print them together in a loop.
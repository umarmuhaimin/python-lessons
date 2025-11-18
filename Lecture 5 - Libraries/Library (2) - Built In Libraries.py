# 📚 Built-In Libraries You Must Know

#################################################################################

# 🔹 random Module / Library

random

# → Used for generating random numbers and making random selections.
# → Useful for randomness.

# ✅ Example :

# 👉 random.choice(sequence)
import random
print(random.choice(["cat", "dog", "bird"]))
# Output: Randomly prints either "cat", "dog", or "bird".


# 👉 random.randint(a, b)
# → Returns a random integer between a and b.

import random
print(random.randint(1, 6))
# Output: Returns a random integer between 1 and 6.


# 👉 random.shuffle(list)
# → Shuffles a list in-place.

import random
cards = ["A", "K", "Q"]
random.shuffle(cards)
print(cards)
# Output: Shuffles and prints the list of cards in random order.


# Shuffles a list of cards and prints the shuffled list horizontally.
import random
cards = ["Jack", "Nolan", "Ava"]
random.shuffle(cards)
print(cards)


# Shuffles a list of cards and prints them in random order item by item by line since arrangement matters.
import random
cards = ["Jack", "Nolan", "Ava"]
random.shuffle(cards)
for card in cards:
    print(card)

#################################################################################

# 🔹 statistics Module / library

statistics

# → Used for math / analytics.

# ✅ Example :

# 👉 statistics.mean(iterable)
import statistics
print(statistics.mean([80, 90, 100]))  
# Output: 90.0

# → Calculates the average of the numbers in the list.

# 👉 statistics.median(iterable)
import statistics
print(statistics.median([80, 90, 100, 95]))  
# Output: 92.5

# → Finds the median value in the list.

# 👉 statistics.mode(iterable)
import statistics
print(statistics.mode([80, 90, 100, 90, 95]))  
# Output: 90

# → Finds the most common value in the list.

#################################################################################


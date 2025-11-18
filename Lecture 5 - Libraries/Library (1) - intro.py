# 📚 CS50P – Lecture 4: Libraries 

# 1. What Are Libraries?
# → A library is a collection of pre-written code that you can import and use.
# → Helps you avoid reinventing the wheel.
# → Python comes with many built-in libraries (standard library).
# → You can also install third-party libraries using pip.

# 👉 Example: The built-in module / library random in Python.

import random

coin = random.choice(["heads", "tails"])
print(coin)

#################################################################################

# 2. Importing Module / Libraries

# 🔹 Import the entire module :
import random
coin = random.choice(["heads", "tails"])
print(coin)

# → Call functions with the module name: module.function()

# 👉 To include a whole module: import module_name (e.g., import random). 

import random

coin = random.choice(["heads", "tails"])
print(coin)
# Output: Randomly prints either "heads" or "tails".


# 🔹 Import only the function you need :
from random import choice
coin = choice(["heads", "tails"])

# → Cleaner if you're using only one or two functions.
# → This lets you call choice() directly without prefix random. 
# → Modules can offer many functions; importing only what you need can make your code cleaner and slightly faster.

# 👉 To import a specific function from a module: from module_name import function_name.

from random import choice
coin = choice(["heads", "tails"])
print(coin)


# 🔹 Import with alias
import random as r
print(r.randint(1, 10))

# → Shortens module name for easier access.

# 👉 To give a module an alias: import module_name as alias.
import random as r
print(r.randint(1, 10))
# Output: Randomly prints an integer between 1 and 10.

#################################################################################


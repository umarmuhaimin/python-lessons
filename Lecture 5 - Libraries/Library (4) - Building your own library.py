# 📚 Building Your Own Library (Custom Modules)

# ✅ Why this matters:
# → Organizes your code.
# → You can create reusable modules.
# → Lets you reuse functions across projects.

# 🔹 Importing libraries / modules / functions.

# 👉 sayings.py 
def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

# This is your custom library with two functions: hello() and goodbye().


# 👉 main.py
# import sayings

# sayings.hello("Alice")
# sayings.goodbye("Alice")

# Output:
# hello, Alice
# goodbye, Alice

# 🔹 Importing specific functions from a module.

# 👉 main.py
# from sayings import hello
hello("Bob")

# Output:
# hello, Bob

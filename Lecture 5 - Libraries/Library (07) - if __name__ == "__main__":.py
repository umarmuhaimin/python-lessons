# ❌ Wrong way of setting up a custom library that causes an error.

# sayings.py
def main():
    hello("World")
    goodbye("World")

def hello(name):
    print(f"hello", {name})

def goodbye(name):
    print(f"goodbye", {name})

main()

########################################################################################################################

#say.py
import sys
# from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])

# 👉 Output when run python3 says.py David:
# hello, world
# goodbye, world
# hello, David

# ❌ Explanation:
# → This custom library causes an error because when say.py is run directly, it calls main() which in turn calls hello() and goodbye() before they are defined. This results in a NameError.
# → To fix this, we can use the if __name__ == "__main__": construct to ensure that main() is only called when the script is run directly, not when it is imported as a module.

########################################################################################################################

# ✅ Correct way of setting up a custom library.

# sayings.py
def main():
    hello("World")
    goodbye("World")

def hello(name):
    print(f"hello", {name})

def goodbye(name):
    print(f"goodbye", {name})

if __name__ == "__main__": # Ensures that main() runs only when the script is executed directly from sayings.py and not when imported as a module.
    main()

########################################################################################################################

# say.py
import sys
# from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])

# 👉 Output when run python3 say.py David:
# hello, David

# ✅ Explanation:
# → By adding the if __name__ == "__main__": guard in sayings.py, we prevent main() from being called when sayings.py is imported as a module in say.py. This allows us to use the hello() function without any errors.
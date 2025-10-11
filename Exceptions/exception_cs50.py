# 🔹 Syntax error:
# A syntax error occurs when the code is not written in accordance with the rules of the programming language.

# 👉 Example:
# → print("Hello, world)
# • Solution:
print("Hello, world")

################################################################################################################

# 🔹 Improving programs with handling exceptions.

################################################################################################################

# 👉 Before improvement:

x = int(input("what's x?"))
print(f"x is{x}.")

# • Input: Output
# → 50: x is 50.
# → - 50: x is - 50.
# → cat: ValueError: invalid literal for int() with base 10: 'cat'

# 👉 After improvement:

try:
    x = int(input("what's x?"))
    print(f"x is {x}.")
except ValueError:
    print("x is not an integer.")

# • Input: Output
# → 50: x is 50.
# → - 50: x is - 50.
# → cat: x is not an integer.

################################################################################################################

# 👉 Before improvement:

try:
    x = int(input("what's x?"))       # This line may raise a ValueError. The value error is happening when the input is not an integer. The input does not copy from left to right so it will raise an error.
except ValueError:
    print("x is not an integer.")

print(f"x is {x}.")

# • Input: Output
# → 50: x is 50.
# → - 50: x is - 50.
# → cat: x is not an integer.

# 👉 After improvement:

# • Method 1:
while True:
    try:
        x = int(input("what's x?"))
        break
    except ValueError:
        print("x is not an integer.")
    else:
        print(f"x is {x}.")

# • Method 2:
while True:
    try:
        x = int(input("what's x?"))
    except ValueError:
        print("x is not an integer.")
    else:
        break

print(f"x is {x}.")

# • Method 3:
while True:
    try:
        x = int(input("what's x?"))
        break
    except ValueError:
        print("x is not an integer.")

print(f"x is {x}.")

# • Input: Output
# → 50: x is 50.
# → - 50: x is - 50.
# → cat: x is not an integer. (repeats until a valid integer is entered)

# • while loop explaination:
# → If the user inputs a valid integer, it succeeds, breaks the loop, and prints the value of x.
# → If the user inputs an invalid integer, it raises a ValueError, prints "x is not an integer.", and prompts for input again.
# → This continues until a valid integer is entered.

################################################################################################################

# 🔹 Creating a function.

# • Method 1:
def main():
    x = get_int()          # x is equivalent to the return value of get_int() function.
    print(f"x is {x}.")

def get_int():
    while True:
        try:
            x = int(input("what's x?"))
        except ValueError:
            print("x is not an integer.")
        else:
            break
    return x

main()

# • Input: Output
# → 50: x is 50.
# → - 50: x is - 50.
# → cat: x is not an integer. (repeats until a valid integer is entered)

# • Method 2:
def main():
    x = get_int()          # x is equivalent to the return value of get_int() function.
    print(f"x is {x}.")

def get_int():
    while True:
        try:
            x = int(input("what's x?"))
            return x
        except ValueError:
            print("x is not an integer.")
        
main()

# • Input: Output
# → 50: x is 50.
# → - 50: x is - 50.
# → cat: x is not an integer. (repeats until a valid integer is entered)

# • Method 3: {RETURN DIRECTLY}
def main():
    x = get_int()          # x is equivalent to the return value of get_int() function.
    print(f"x is {x}.")

def get_int():
    while True:
        try:
            return int(input("what's x?"))
        except ValueError:
            print("x is not an integer.")
        
main()

# • Input: Output
# → 50: x is 50.
# → - 50: x is - 50.
# → cat: x is not an integer. (repeats until a valid integer is entered)

################################################################################################################

# 🔹 Pass
# → The pass statement in Python means “do nothing.” Pass statement just tells Python to skip that part and move on.

def main():
    x = get_int()          # x is equivalent to the return value of get_int() function.
    print(f"x is {x}.")

def get_int():
    while True:
        try:
            return int(input("what's x?"))
        except ValueError:
            pass

main()

# • Input: Output
# → 50: x is 50.
# → - 50: x is - 50.
# → cat: (no output, just reprompts for input until a valid integer is entered)

# 👉 Here’s the simplest explanation for the pass statement in your code:

# → When you use pass in the except block, it means “do nothing” if there’s an error.
# → If you enter something that’s not an integer, the program ignores the error and just asks again.
# → No message is shown to the user; it just keeps looping until you enter a valid number.
# → In short:
# → pass is used here to quietly skip errors and keep asking for input until you type a valid integer.

################################################################################################################

# 🔹 Using a parameter (prompt) in a function.

def main():
    x = get_int("What's x?")          # This parameter of prompt is customizable. So you can change the question easily.
    print(f"x is {x}.")

def get_int(prompt):           # The parameter prompt is a variable that holds the value passed to the function when it is called.
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()

# • Input: Output
# → 50: x is 50.
# → - 50: x is - 50.
# → cat: (no output, just reprompts for input until a valid integer is entered)

# 👉 Here’s what you can conclude:

# • The program asks the user for a number using a custom prompt ("What's x?").
# • If the input is a valid integer, it prints the value.
# • If the input is not an integer, it does nothing (because of pass) and asks again.
# • The loop repeats until a valid integer is entered.
# • Using a parameter (prompt) makes the function flexible—you can change the question easily.
# • In short:
# • This code safely asks for an integer, ignores errors quietly, and uses a customizable prompt for input.

# 👉 Emphasis on the prompt parameter:

# • The prompt parameter lets you customize the question shown to the user when asking for input.
# • Instead of always asking "what's x?", you can pass any message you want.
# • This makes your function flexible and reusable for different questions.
    
# 👉 Example:
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

x = get_int("Enter your age: ")
y = get_int("How many apples? ")

# • Here, prompt is "Enter your age: " for one input and "How many apples? " for another.
# • The function uses whatever prompt you give it.

# 👉 In short:
# • The prompt parameter lets you easily change the input question, making your code more flexible and user-friendly.




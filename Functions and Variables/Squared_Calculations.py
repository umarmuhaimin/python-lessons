### In this python file, we will define a function that calculates the square of a number.

# Square Integers : 
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))
def square(n):
    return n * n
main()

# Explaination:
# 1. We define a function named `main` that prompts the user to input an integer.
# 2. The input is converted to an integer using `int()`.
# 3. We then call another function named `square`, passing the input integer as an argument.
# 4. The `square` function takes a number `n` and returns its square by multiplying `n` by itself.
# 5. Finally, the result is printed in the `main` function.
# 6. The `main` function is called to execute the program.


# Cubic Integers :
def main():
    x = int(input("What's x? "))
    print("x cubic is", cubic(x))
def cubic(n):
    return n * n * n
main()

# To the power of n calculations :
def main():
    x = int(input("What's x? "))
    print("x to the power of n is", power(x)) # where n is an integer defined by user.
def power(n): # if n = 4, then we set the program to return n ** 4.
    return n ** 4
main()

# alternative method using pow() function :
def main():
    x = int(input("What's x? "))
    print("x to the power of n is", power(x)) # where n is an integer defined by user.
def power(n):   # if n = 3, then we set the program to pow(n, 3).
    return pow(n, 3)
main()

# To the power of n calculations (Second method) :
def main():
    x = int(input("What's x? ")) # where x is the base defined by user.
    y = int(input("What's y? ")) # where y is the power defined by user.
    print(f"x to the power of y is {power(x, y)}")
def power(n, m):    # if n = base and m = power, then we set the program to return n ** m.
    return n ** m
main()

### Just a reminder, everytime you use f-strings method, always include curly braces {}. ###

# alternative method without f-string :
def main():
    x = int(input("What's x? ")) # where x is the base defined by user.
    y = int(input("What's y? ")) # where y is the power defined by user.
    print("x to the power of y is", power(x, y))
def power(n, m):    # if n = base and m = power, then we set the program to return n ** m.
    return n ** m
main()


# To create a function in Python :

# 1. Use the `def` keyword followed by the function name and parentheses.
# 2. Inside the parentheses, you can define parameters that the function will take.
# 3. Use a colon `:` to indicate the start of the function body.
# 4. Indent the function body to indicate that it belongs to the function.
# 5. Use the `return` statement to return a value from the function.

# Simplest way to create your own function :

# 1. def main ()
# 2. Introduce condition with function
# 3. Give definition to function
# 4. main()
    
### In this python file, we will learn about how to return a value that we input either from variables or functions ###

# Remember, every line of codes will be run by order from the top to the bottom.


# To return a value from a variable of a function, we can use "return" function to output the value.
def get_guess():
    guess = input("Enter a guess from 1 to 10? ")
    return guess
print(get_guess())

# We can have two variable with the same name but different use. This is because these two variables are inside of different scopes.
# Scope : The region of a program where a variable or name is visible and accessible. It dictates where a variable can be used and which parts of the code have access to it.
# Easy definition : Scope is a variable that is only available from inside the region it is created. It can only be used in the region/group of code where it is created.


# For example :
def get_guess():
    guess = input("Enter a guess from 1 to 10? ") # The variable guess here is only applicable for this function.
    return guess

def main():
    guess = get_guess() # The variable guess here is only applicable for this function.
    print(guess)
main()


# Integer example :
def get_guess():
    guess = int(input("Enter a guess:")) # The variable guess here is only applicable for this function.
    return guess

def main():
    guess = get_guess() # The variable guess here is only applicable for this function.
    if guess == 50:
        print("Correct")
    else:
        print("Incorrect")

main()

# The sign " : " means therefore.


# String example :
def get_guess():
    guess = str(input("Enter a guess:")) # The variable guess here is only applicable for this function.
    return guess

def main():
    guess = get_guess() # The variable guess here is only applicable for this function.
    if guess == "fifty":
        print("Correct")
    else:
        print("Incorrect")

main()
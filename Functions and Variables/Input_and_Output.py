# Lesson (1): Input and Output data from the user using input() and print() functions.

# The input() function takes input from the user as a string.
# The print() function outputs data from input to the console (terminal).
 
# Basic Example :
# Ask the user for their name and print a greeting message.
name = input("What's your name? ")
print("Hello,",name)

# General Notes :

# 1. The input() function always returns a string. If you need a different data type (like int or float), you must convert it using functions like int() or float().
# int = integer (a whole number, positive or negative, without decimals).
# float = a number that has a decimal place.
# int and float are data types.
# Example :
age = int(input("How old are you? "))  # Convert input to integer
height = float(input("What's your height in meters? "))  # Convert input to float
print("You are", age, "years old and", height, "meters tall.")

# Additional Notes : 
# You can concatenate strings using the + operator or separate them with commas in the print() function.
# Concatenante : link (things) together in a chain or series. Basically Linking the component of Hello and name together.
# Example :
name = input("What's your name? ")
print("Hello, " + name)  # Using concatenation
print("Hello,", name)     # Using comma separation


# 2. You can format strings using f-strings because it is more readable and easier to use. 
# f-strings allows you to embed expressions inside string literals, using curly braces {}. Therefore, no need to have many commas in the print() function.
# Example :
name = input("What's your name? ")
age = int(input("How old are you? "))
print(f"Hello, {name}. You are {age} years old.")


# 3. The print() function can take multiple arguments, which it separates by spaces by default.
# Example :
print("Hello,", name, "you are", age, "years old.")  # Multiple arguments


# 4. You can customize the separator and end character in the print() function using the sep and end parameters.
# Example :
print("Hello", name, sep=" - ", end="!\n")  # Custom separator and end character
# Output: Hello - [name]!
# sep=" - " is used to separate the words with " - " instead of the default space.
# end="!\n" is for ending the line with ! and moving to the next line.
# Note: \n is a newline character that moves the cursor to the next line. /n is used to create a new line in the output.


# 5. To get input without a prompt, you can call input() without any arguments.
# Example :
user_input = input()  # No prompt
print("You entered:", user_input)


# 6. To read multiple values from a single input line, you can use the split() method.
# split() method splits a string into a list where each word is a list item. The default separator is any whitespace.
# Example :
values = input("Enter multiple values separated by spaces: ").split()
print("You entered:", values)
# Output: If the user inputs "apple banana cherry", the output will be ['apple', 'banana', 'cherry'].


# 7. To read a single character input, you can use input() and then take the first character of the string.
# This is done by indexing the string with [0], which gives you the first character.
# Note: Indexing in Python starts at 0, so [0] refers to the first character.
# If the user inputs more than one character, only the first character will be considered.
# If the user inputs a word, only the first letter of that word will be considered.
# If the user set the index to [1], it will take the second character instead.
# To read the last character of the input, you can use negative indexing with [-1].
# Example :
char = input("Enter a character: ")[0]  # Take the first character
print("You entered:", char)

# 8. To remove whitespace from the beginning and end of the input, you can use the strip() method.
# Example :
user_input = input("Enter something with extra spaces: ").strip()
print("You entered:", user_input)
# Output: If the user inputs "   hello   ", the output will be "hello"
# Example (2) :
name = input("Enter your name: ")
name = name.strip()  # Remove leading/trailing whitespace
print("Hello, " + name + "!")

# 9. To capitalize the first letter of the input, you can use the capitalize() method.
# Example :
user_input = input("Enter something: ").capitalize()
print("You entered:", user_input)
# Output: If the user inputs "hello", the output will be "Hello"
# Example (2) :
name = input("Enter your name: ")
name = name.strip().capitalize()  # Remove leading/trailing whitespace and capitalize
print("Hello, " + name + "!")

# 10. To convert the input to lowercase or uppercase, you can use the lower() and upper() methods respectively.
# Example :
user_input = input("Enter something: ").lower()
print("You entered (lowercase):", user_input)
# Output: If the user inputs "HeLLo", the output will be "hello"
user_input = input("Enter something: ").upper()
print("You entered (uppercase):", user_input)
# Output: If the user inputs "HeLLo", the output will be "HELLO"
# Example (2) :
name = input("Enter your name: ")
name = name.strip().upper()  # Remove leading/trailing whitespace and convert to uppercase
print("HELLO, " + name + "!")

# 11. To capitilize the title of each word in the input, you can use the title() method.
# Example :
user_input = input("Enter something: ").title()
print("You entered (title case):", user_input)
# Output: If the user inputs "hello world", the output will be "Hello World"
# Example (2) :
name = input("Enter your name: ")
name = name.strip().title()  # Remove leading/trailing whitespace and convert to title case
print("Hello, " + name + "!")
# So basically, title() method capitalizes the first letter of each word in the string.

# 12. To split the user's full name into first and last names, you can use the split() method.
# Example :
full_name = input("Enter your full name: ").strip().title()
first_name, last_name = full_name.split()  # Split into first and last names
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
# Output: If the user inputs "john doe", the output will be "First Name: John" and "Last Name: Doe"
# So basically, we can use this method to display the first and last names separately.
# Note: This method assumes that the user will input exactly two names (first and last).
# If the user inputs more than two names, it will raise a ValueError.
# If the user inputs only one name, it will also raise a ValueError.

# To handle cases where the user might input more than two names, you can use {unpacking} with asterisk (*) to capture the remaining names.
# Example :
full_name = input("Enter your full name: ").strip().title()
names = full_name.split()  # Split into a list of names
first_name = names[0]  # First name is the first element
last_name = names[-1]  # Last name is the last element
middle_names = names[1:-1]  # Middle names are the elements in between
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Middle Names: {' '.join(middle_names) if middle_names else 'None'}")
# Output: If the user inputs "john michael doe", the output will be "First Name: John", "Last Name: Doe", and "Middle Names: Michael"
# If the user inputs "john doe", the output will be "First Name: John", "Last Name: Doe", and "Middle Names: None"
# The indexing of [1:-1] is used to get all elements from the second element to the second last element, which are the {middle names}.
# The join() method is used to join the middle names list into a single string with spaces in between.
# The if-else condition is used to check if there are any middle names.
# If there are no middle names, it will display "None" instead of an empty string

### These are some ways you can use to greet users ###

name = input("What's your name? ").strip().title()
print("Hello,", name)

name = input("What's your name? ").strip().title()
print("Hello, " + name)

name = input("What's your name? ").strip().title()
print("Hello, ", end="\n")
print(name)

name = input("What's your name? ").strip().title()
print("Hello, ",name, sep="Welcome back ")
# Output : Hello, Welcome back [name]

name = input("What's your name? ").strip().title()
print(f"hello, {name}")

full_name = input("Enter your full name: ").strip().title()
first_name, last_name = full_name.split()  # Split into first and last names
print(f"hello, {first_name}")


### Displaying quotes in strings ###

print("hello, \"friend\"")
print("hello, 'friend'")


### Define hello as a function instead of using print function ###

# A function is a block of code that performs a specific task.
# It is defined using the def keyword, followed by the function name and parentheses ().
# Functions can take parameters (inputs) and can return values (outputs).
# Functions help to organize code, make it reusable, and improve readability.

# In this case, we define a function called hello that takes one parameter (to) and prints a greeting message.
# This way, we can reuse the hello function to greet different users without repeating the print statement.
# This is especially useful if we want to greet multiple users or if the greeting logic becomes more complex in the future.

# We can use hello function to greet multiple users without repeating the print statement. 
# You can call the hello function multiple times with different names.

# All of these method starts from the top to the bottom.

# First method :
def hello(to):
    print("hello, " + to)
name = input("What's your name? ").strip().title()
hello(name)

# Explanation of the first method :
# In this method, we define the hello function that takes one parameter (to) and prints a greeting message.
# We then ask the user for their name using input() and store it in the variable name.
# Finally, we call the hello function with the user's name as an argument, greeting the user with their name.
# For example :
# hello(name) is the same as hello("Jason") if the user inputs "Jason".
# So basically, the argument (name) is passed to the parameter (to) in the hello function.
# Hence, hello(to) becomes hello("Jason") and prints "hello, Jason".
# Therefore, hello(to) will have the same value as hello(name) when the function is called. A function is called when there is an argument in the parentheses after the function name.


# Second method :
def hello(to="World"):
    print("hello,", to)
hello()
name = input("What's your name? ")
hello(name)

# Explanation of the second method :
# In this method, we define the hello function with a default parameter value of "World".
# This means that if we call the hello function without any arguments "just with hello() and without any parameters" , it will greet "World."

# If we provide an argument (like the user's name), it will greet that name instead.

# argument = a value that is passed to a function when it is called. For example, in hello(name), name is the argument. Argument is without def keyword.
# parameter = a variable that is defined in the function definition to accept the argument. For example, in def hello(to), to is the parameter. Parameter is with def keyword.
# In terms of priority, it will always prioritize the argument over the parameter.

# First, it will print "hello, World" because we called the hello() function without any arguments.
# Then, it will ask the user for their name using input().
# Finally, it will call the hello(name) function with the user's name as an argument, greeting the user with their name.

# With orders :
# 1. Hello, World because hello() is called without any arguments.
# 2. Then, it asks for the user's name.
# 3. (name) argument is passed to the (to) parameter in the hello function.
# 4. Hence, hello(to) becomes hello("Mike") and prints "hello, Mike" if the user inputs "Mike".
# Therefore, hello(to) will have the same value as hello(name) when the function is called.
# A function is called when there is an argument in the parentheses after the function name.


# Third method :
def main():
    name = input("What's your name? ")
    hello(name)
def hello(to="World"):
    print("hello,", to)
hello()
main()

# Since there is no print function on the first section, the process will start with the parameter (to) as it has an argument hello() which is empty, so it will take the default value "World" and print "hello, World".
# Then, the main function is called which will ask for the user's name and store it in the variable (name).
# Finally, the hello function is called with the argument (name) which contains the user's input.
# The argument (name) is passed to the parameter (to) in the hello function, and it prints "hello, [user's name]".
# For example, if the user inputs "Alice", it will print "hello, Alice".

# So the order of execution is:
# 1. hello() -> prints "hello, World". Only focus on the hello() section.
# 2. main() -> asks for user's name and stores it in (name). Only focus on the main() section which starts from def main(): to the end of main().
# 3. hello(name) -> prints "hello, [user's name]". (name) argument is passed to (to) parameter in the hello function. Therefore, it will print "hello, [user's name]".





























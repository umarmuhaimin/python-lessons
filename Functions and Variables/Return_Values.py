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


# Example of Side Effects, where you don't need a return function and a variable to identify greeting whether there is hello or not :
def greet(input):    # input is a parameter.
    if "hello" in input:
        print("hello, there")
    else:
        print("I'm not sure what you mean")

greet("hello, computer")


# Example of return value application using a return function and a variable is needed :
def greet(input):  # "input" in this line of code is a parameter.
    if "hello" in input:
        return "hello, there"
    else:
        return "I'm not sure what you mean"
    
greeting = greet("hello, computer")
print(greeting)

# You are not inputing anything as a user. The input is already fixed in the system which is "hello" keyword. If this keyword is identified, then the system will output "hello, there". 
# It's basically like a chatbox inside a fixed system to make sure all fixed data inputed is correct as set-up by the user.
# In order to change the fix input data, you need to change it in the {if statement} line of code.
# To check whether the input data is correct or acceptable by the system, you can do it by changing words/sentence at greeting = greet("your own word/sentence"). If there is "hello" keyword in this line of code, then the system will output "hello, there".


# The reason why we use return function is because we can modify the code at any time later on without altering/chaning the present code of program. This is much useful compared to print function which we might need to alter all of the codes to suite the function.
def greet(input):  # 
    if "hello" in input:
        return "hello, there"
    else:
        return "I'm not sure what you mean"
    
greeting = greet("hello, computer")
print("What's up my friend. " + greeting)

def greet(input):  # 
    if "hello" in input:
        return "hello, there"
    else:
        return "I'm not sure what you mean"
    
greeting = greet("hello, computer")
print(greeting + " David")

### This coding system will only take the keyword "hello" from the greet input to print the successful output. If greet input does not contain any "hello" keyword, then it will print the failure output ###

# Return Values : 
# - The value of a return value allows us to modify things throughout our code and use the output of some function later on. 
# - We can use return value throughout our code as we go off and build new programs / line of codes at the same time without altering the present codes.
# - We use return function in this method.


# Side Effects :
# - A side effect in Python is an immediate change that prevents new code from being displayed in the output.
# - In Python, side effects occur when a change happens right away, causing new code not to appear in the output.
# - Uses print function in this method.


# Intermediate example of Side Effects :
emoticon = "^.^"

def main():
    say("Is anyone there? ")
    emoticon = ":D" # When running the program, this emoticon will not be displayed because of side effects.
    say("Oh, hi!")

def say(phrase):
    print(phrase + " " + emoticon)

main()

# In order to make changes on the output inside or outside of a function without altering any line of codes, we can use global variable.
# Global variables = variable that is defined outside of any function or class, typically at the top level of a script or module. This means it has a "global scope," making it accessible from anywhere within that module, including inside functions. 

# Therefore, in order to overcome Side Effects, we can use global variable.
emoticon = "^.^"

def main():
    global emoticon # global variable: Any changes can be made at any time present or later on while coding.
    say("Is anyone there? ")
    emoticon = ":D"
    say("Oh, hi!")


def say(phrase):
    print(phrase + " " + emoticon)  # " " indicates space in between phrase and emoticon.
main() 

# phrase = say("Is anyone there? ") and say("Oh, hi!")
# emoticon =  "^.^" , if global variable is added to emoticon then the second emoticon = ":D" 
# If there is no global emoticon, then the ouput emoticon will output same "^.^" emoticon.

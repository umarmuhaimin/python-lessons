# Parity condition ("%"): We use this condition for calculation involves even or odd number.
# Even numbers are real number that can be divided by 2 and gives a remainder of 0 when it keeps divided by 2.
# In python, to identify even numbers : you can just divide the integer with 2 using parity condition ("%") and if it gives a remainder of 0 -> even number.

# Case (1) :
x = int(input("What's x?"))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")


# Case (2) : Creating Even and Odd function.
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even number")
    else:
        print("Odd Number")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()
    

# RECALL : Steps to create a function 
# 1. Introduce the main view of the function : introduce def main(): / def anything():
# 2. input user data using variable for any case.
# 3. Introduce the function name that has content behind it / function that we want to work with without giving out the full function purpose.
# 4. Print the outcome that you are looking for.
# 5. Now, define the purpose of the function.
# 6. Call main() to run the code.


# Case (3) : Creating Even and Odd function but simplified
def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
def is_even(n):
    return True if n % 2 == 0 else False
main()


# Case (4) : Creating Even and Odd function with the most simpified method / way. No need to use if and else condition to give purpose to even function.
def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
def is_even(n):
    return n % 2 == 0
main()


